#!/usr/bin/env python3
"""
generate_videos.py — Genera videos MP4 (~5 min) para los 6 temas de
Bioestadística para Fisioterapia.

Pipeline:
  1. Lee cada TXT de notebooklm_txt/ y extrae contenido clave de TODO el tema
  2. Genera slides PNG con Pillow (título, secciones, bullets, cierre)
  3. Genera audio con macOS `say` (voz Monica, español)
  4. Une slides + audio con ffmpeg → MP4 (1080p)
"""

import os
import re
import subprocess
import textwrap
from pathlib import Path

# ─── CONFIG ───────────────────────────────────────────────────────────
BASE_DIR = Path("/Users/MALF/Library/CloudStorage/Dropbox/UGR/CLAUDE/my-project/Slides/TemasTeoriaFisioterapia/qmd_slides")
TXT_DIR = BASE_DIR / "notebooklm_txt"
OUT_DIR = BASE_DIR / "videos"

W, H = 1280, 720
FPS = 24
BG_COLOR = (15, 25, 45)
ACCENT = (52, 152, 219)
GOLD = (241, 196, 15)
WHITE = (255, 255, 255)
LIGHT_GRAY = (189, 195, 199)
DARK_BG = (10, 18, 35)
SECTION_BG = (20, 40, 70)
TTS_VOICE = "Monica"
TTS_RATE = 175  # words per minute for natural educational pace
TARGET_WORDS = 600  # ~4 min speech + slide padding ≈ 5 min total

TOPICS = [
    ("T01", "Bioestadistica_Fisioterapia", "Estadística Descriptiva"),
    ("T02", "Bioestadistica_Fisioterapia", "Probabilidad y Variables Aleatorias"),
    ("T03", "Bioestadistica_Fisioterapia", "Teoría de la Estimación e Intervalos de Confianza"),
    ("T04", "Bioestadistica_Fisioterapia", "Contraste de Hipótesis"),
    ("T05", "Bioestadistica_Fisioterapia", "Análisis de Datos Cualitativos — Chi-Cuadrado"),
    ("T06", "Bioestadistica_Fisioterapia", "Regresión y Correlación"),
]


# ─── HELPERS ──────────────────────────────────────────────────────────

def clean_line(s: str) -> str:
    """Remove markdown, LaTeX, and formatting from a line."""
    s = re.sub(r'\$\$[^$]+\$\$', '', s)       # display math
    s = re.sub(r'\$[^$]+\$', '', s)           # inline math
    s = re.sub(r'\*\*(.+?)\*\*', r'\1', s)    # bold
    s = re.sub(r'\*(.+?)\*', r'\1', s)        # italic
    s = re.sub(r'`[^`]+`', '', s)             # code
    s = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', s)  # links
    s = re.sub(r'!\[[^\]]*\]\([^)]+\)', '', s)     # images
    s = re.sub(r'^\s*[-*+]\s+', '', s)        # list markers
    s = re.sub(r'^\s*\d+\.\s+', '', s)        # numbered lists
    s = re.sub(r'\[@[^\]]+\]', '', s)          # citations
    s = re.sub(r'\{[^}]+\}', '', s)            # curly brace formatting
    s = re.sub(r'\s+', ' ', s)                 # normalize whitespace
    return s.strip()


def is_meta_line(s: str) -> bool:
    """Check if line is metadata/header (author, license, etc.)."""
    meta_patterns = [
        r'^Miguel Angel', r'^CC BY', r'^Dpto\.?\s', r'^Universidad de',
        r'^maluque\.', r'^migariane\.', r'^\*\*Grado en',
        r'^Grado en Fisioterapia', r'^\*\*CC BY',
        r'^Bioestadística para', r'^\*\*Bioestadística',
    ]
    return any(re.match(p, s) for p in meta_patterns)


def is_reference_line(s: str) -> bool:
    """Check if line is a reference or reference section."""
    ref_patterns = [
        r'^\[@', r'^Altman', r'^Rosner', r'^Tukey', r'^Stevens',
        r'^Femia', r'^Luque-Fernandez', r'^Luque-Fernández',
        r'^Fisher', r'^Pearson', r'^Student', r'^Wilcoxon', r'^Mann',
        r'^Spearman', r'^Kruskal', r'^Galton', r'^Neyman',
        r'^\.reference-box', r'^Referencia', r'^\*\*Referencia',
        r'^Pepe', r'^\d+\.\s',  # numbered list after references
    ]
    # Also skip headings that are references
    if re.match(r'^#+\s*Referencia', s):
        return True
    return any(re.match(p, s) for p in ref_patterns)


def is_table_or_code(s: str) -> bool:
    """Check if line is a table row or code block."""
    return bool(re.match(r'^\|.*\|$', s)) or s.startswith('```') or '---' in s


# ─── STEP 1: Smart narration extraction ────────────────────────────────

def extract_narration(text: str, target_words: int = TARGET_WORDS) -> str:
    """
    Extract a coherent narration covering the ENTIRE topic.
    Strategy: split into sections by ## headings, then sample proportionally
    from each section based on its size.
    """
    lines = text.split('\n')

    # Parse into sections: [(heading, [lines])]
    sections = []
    current_heading = "Inicio"
    current_lines = []

    for line in lines:
        s = line.strip()
        if not s:
            continue

        # Detect section heading
        if s.startswith('## '):
            if current_lines:
                sections.append((current_heading, current_lines))
            current_heading = s[3:].strip()
            current_lines = []
        elif s.startswith('# ') and len(sections) == 0:
            # Main title — capture for title slide
            if current_lines:
                sections.append((current_heading, current_lines))
            current_heading = s[2:].strip()
            current_lines = []
        else:
            current_lines.append(s)

    if current_lines:
        sections.append((current_heading, current_lines))

    # Filter: remove meta lines, tables, references from each section
    clean_sections = []
    for heading, sec_lines in sections:
        cleaned = []
        for line in sec_lines:
            if is_meta_line(line) or is_reference_line(line) or is_table_or_code(line):
                continue
            cl = clean_line(line)
            if cl and len(cl) > 10:
                cleaned.append(cl)
        if cleaned:
            clean_sections.append((heading, cleaned))

    # Calculate words per section
    section_words = [(h, lines, sum(len(l.split()) for l in lines))
                     for h, lines in clean_sections]
    total_words = sum(sw[2] for sw in section_words)

    if total_words == 0:
        return ""

    # Allocate target words proportionally, with minimum per section
    narration_parts = []
    words_used = 0

    for heading, lines, sw in section_words:
        # Proportional allocation
        alloc = int(target_words * (sw / total_words))
        alloc = max(alloc, 15)  # minimum 15 words per section

        # Take lines until we reach allocation
        section_text = []
        wc = 0
        for line in lines:
            lw = len(line.split())
            if wc + lw > alloc:
                remaining = alloc - wc
                if remaining > 3:
                    section_text.append(' '.join(line.split()[:remaining]))
                break
            section_text.append(line)
            wc += lw

        if section_text:
            # Add heading as spoken transition
            narration_parts.append(f"{heading}.")
            narration_parts.append(' '.join(section_text))
            words_used += wc + len(heading.split())

    return '\n\n'.join(narration_parts)


# ─── STEP 2: Slide generation ──────────────────────────────────────────

def get_font(size: int):
    """Load a font at given size, fall back to default."""
    from PIL import ImageFont
    try:
        return ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", size)
    except Exception:
        return ImageFont.load_default()


def create_title_slide(topic_num: str, title: str, out_path: Path):
    """Title card slide."""
    from PIL import Image, ImageDraw

    img = Image.new("RGB", (W, H), BG_COLOR)
    draw = ImageDraw.Draw(img)

    ftitle = get_font(68)
    fsub = get_font(40)
    fsmall = get_font(28)

    # Gold accent bars
    draw.rectangle([(0, 0), (W, 6)], fill=GOLD)
    draw.rectangle([(0, H - 6), (W, H)], fill=GOLD)

    # Topic number
    label = f"TEMA {topic_num[1:]}"
    draw.text((100, 120), label, fill=GOLD, font=fsub)

    # Title
    lines = textwrap.wrap(title, width=32)
    y = 300
    for line in lines:
        draw.text((100, y), line, fill=WHITE, font=ftitle)
        y += 90

    # Course + author
    draw.text((100, H - 220), "Bioestadística para la Decisión Clínica", fill=LIGHT_GRAY, font=fsmall)
    draw.text((100, H - 170), "Miguel Angel Luque-Fernández · Universidad de Granada", fill=LIGHT_GRAY, font=fsmall)
    draw.text((100, H - 120), "Grado en Fisioterapia", fill=LIGHT_GRAY, font=fsmall)

    # Blue accent vertical bar
    draw.rectangle([(52, 120), (64, H - 80)], fill=ACCENT)

    img.save(out_path, "PNG")


def create_section_slide(heading: str, slide_num: int, out_path: Path):
    """Section divider slide."""
    from PIL import Image, ImageDraw

    img = Image.new("RGB", (W, H), SECTION_BG)
    draw = ImageDraw.Draw(img)

    ftitle = get_font(52)
    fnum = get_font(24)

    draw.rectangle([(0, 0), (W, 4)], fill=GOLD)
    draw.rectangle([(0, H - 4), (W, H)], fill=GOLD)

    draw.text((W - 80, 30), str(slide_num), fill=LIGHT_GRAY, font=fnum)

    lines = textwrap.wrap(heading, width=40)
    y = H // 2 - (len(lines) * 35)
    for line in lines:
        draw.text((120, y), line, fill=WHITE, font=ftitle)
        y += 70

    draw.rectangle([(80, H // 2 - 50), (92, H // 2 + 50)], fill=GOLD)

    img.save(out_path, "PNG")


def create_bullet_slide(bullets: list[str], slide_num: int, out_path: Path):
    """Bullet-point content slide."""
    from PIL import Image, ImageDraw

    img = Image.new("RGB", (W, H), DARK_BG)
    draw = ImageDraw.Draw(img)

    fbullet = get_font(38)
    fnum = get_font(24)

    # Left accent bar
    draw.rectangle([(0, 0), (10, H)], fill=ACCENT)
    # Bottom accent line
    draw.rectangle([(0, H - 4), (W, H)], fill=GOLD)

    draw.text((W - 80, 30), str(slide_num), fill=LIGHT_GRAY, font=fnum)

    y = 100
    for bullet in bullets:
        bullet = bullet.strip()
        if not bullet:
            continue

        # Gold bullet marker
        draw.rectangle([(50, y + 12), (64, y + 26)], fill=GOLD)

        wrapped = textwrap.wrap(bullet, width=58)
        for line in wrapped:
            draw.text((85, y), line, fill=WHITE, font=fbullet)
            y += 50

        y += 16  # extra spacing between bullets

        if y > H - 120:
            break

    img.save(out_path, "PNG")


def create_closing_slide(topic_num: str, title: str, out_path: Path):
    """Closing/end slide."""
    from PIL import Image, ImageDraw

    img = Image.new("RGB", (W, H), BG_COLOR)
    draw = ImageDraw.Draw(img)

    fend = get_font(56)
    fsub = get_font(36)

    draw.rectangle([(0, 0), (W, 6)], fill=GOLD)
    draw.rectangle([(0, H - 6), (W, H)], fill=GOLD)

    draw.text((100, 300), f"Tema {topic_num[1:]}:", fill=GOLD, font=fsub)
    lines = textwrap.wrap(title, width=35)
    y = 380
    for line in lines:
        draw.text((100, y), line, fill=WHITE, font=fend)
        y += 80

    end_text = "— Fin del Tema —"
    f_end = get_font(42)
    draw.text((100, H - 250), end_text, fill=GOLD, font=f_end)

    draw.rectangle([(52, 300), (64, H - 80)], fill=ACCENT)

    img.save(out_path, "PNG")


def generate_slides(topic_num: str, title: str, narration: str, slide_dir: Path):
    """
    Convert narration to slides: title → section dividers → bullet content → closing.
    Returns [(path, duration_seconds)].
    """
    from PIL import Image

    slide_dir.mkdir(parents=True, exist_ok=True)
    slides = []

    # 1) Title slide (4s, no narration yet)
    tp = slide_dir / "00_title.png"
    create_title_slide(topic_num, title, tp)
    slides.append((str(tp), 4.0))

    # 2) Parse narration into sections (delimited by double newlines = new heading)
    blocks = narration.split('\n\n')
    slide_num = 1
    words_per_slide = 70  # ~30 seconds per slide at 150 wpm
    chars_per_bullet = 130
    current_bullets = []
    current_words = 0

    for block in blocks:
        block = block.strip()
        if not block:
            continue

        # Detect section heading (ends with period, relatively short)
        is_heading = (len(block) < 80 and block.endswith('.') and
                      not any(c in block for c in [',', ';', '(', ')']) and
                      len(block.split()) < 10)

        if is_heading:
            # Flush current bullets
            if current_bullets:
                sp = slide_dir / f"{slide_num:02d}.png"
                create_bullet_slide(current_bullets, slide_num, sp)
                dur = max((current_words / 150) * 60, 5.0)
                slides.append((str(sp), dur))
                slide_num += 1

            # Section divider
            sp = slide_dir / f"{slide_num:02d}_section.png"
            create_section_slide(block.rstrip('.'), slide_num, sp)
            slides.append((str(sp), 3.0))
            slide_num += 1
            current_bullets = []
            current_words = 0
            continue

        # Content block — split into bullet-sized chunks
        chunks = textwrap.wrap(block, width=chars_per_bullet)
        for chunk in chunks:
            cw = len(chunk.split())
            if current_words + cw > words_per_slide and current_bullets:
                sp = slide_dir / f"{slide_num:02d}.png"
                create_bullet_slide(current_bullets, slide_num, sp)
                dur = max((current_words / 150) * 60, 5.0)
                slides.append((str(sp), dur))
                slide_num += 1
                current_bullets = []
                current_words = 0
            current_bullets.append(chunk)
            current_words += cw

    # Flush remaining
    if current_bullets:
        sp = slide_dir / f"{slide_num:02d}.png"
        create_bullet_slide(current_bullets, slide_num, sp)
        dur = max((current_words / 150) * 60, 5.0)
        slides.append((str(sp), dur))

    # 3) Closing slide
    cp = slide_dir / "99_close.png"
    create_closing_slide(topic_num, title, cp)
    slides.append((str(cp), 4.0))

    return slides


# ─── STEP 3: TTS audio ─────────────────────────────────────────────────

def generate_audio(narration_text: str, audio_path: Path) -> float:
    """Generate AIFF audio with macOS `say`. Returns duration in seconds."""
    txt_path = audio_path.with_suffix(".txt")
    txt_path.write_text(narration_text)

    subprocess.run(
        ["say", "-v", TTS_VOICE, "-r", str(TTS_RATE),
         "-o", str(audio_path.with_suffix("")), "-f", str(txt_path)],
        check=True, capture_output=True
    )

    result = subprocess.run(
        ["afinfo", str(audio_path.with_suffix(".aiff"))],
        capture_output=True, text=True
    )
    duration = 0.0
    for line in result.stdout.split("\n"):
        if "estimated duration" in line:
            duration = float(line.split(":")[1].strip().split()[0])
            break

    txt_path.unlink(missing_ok=True)
    return duration


# ─── STEP 4: ffmpeg assembly ───────────────────────────────────────────

def combine_to_video(slides: list, audio_path: Path, output_path: Path):
    """Combine slide PNGs + AIFF audio → MP4 using a single ffmpeg concat."""
    if not slides:
        return

    temp_dir = output_path.parent / "temp"
    temp_dir.mkdir(exist_ok=True)

    # Build a concat file that references images directly with duration
    concat_file = temp_dir / "input.txt"
    with open(concat_file, "w") as f:
        for slide_path, duration in slides:
            f.write(f"file '{slide_path}'\n")
            f.write(f"duration {duration}\n")
        # Last image needs to be repeated for concat to work properly
        f.write(f"file '{slides[-1][0]}'\n")

    # Single ffmpeg call: concat images → video, mux with audio, done
    subprocess.run([
        "ffmpeg", "-y",
        "-f", "concat", "-safe", "0", "-i", str(concat_file),
        "-i", str(audio_path.with_suffix(".aiff")),
        "-vf", f"scale={W}:{H}:force_original_aspect_ratio=decrease,"
               f"pad={W}:{H}:(ow-iw)/2:(oh-ih)/2,format=yuv420p,fps={FPS}",
        "-c:v", "libx264", "-preset", "ultrafast", "-crf", "28",
        "-pix_fmt", "yuv420p",
        "-c:a", "aac", "-b:a", "128k",
        "-shortest", "-movflags", "+faststart",
        str(output_path)
    ], check=True, capture_output=True)

    import shutil
    shutil.rmtree(temp_dir)


# ─── MAIN ──────────────────────────────────────────────────────────────

def main():
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    for topic_num, filename, title in TOPICS:
        print(f"\n{'='*60}")
        print(f"  {topic_num}: {title}")
        print(f"{'='*60}")

        txt_path = TXT_DIR / f"{topic_num}_{filename}.txt"
        if not txt_path.exists():
            print(f"  ERROR: no encontrado {txt_path}")
            continue

        text = txt_path.read_text(encoding="utf-8")
        print(f"  TXT: {len(text):,} caracteres")

        # Extract narration
        narration = extract_narration(text)
        wc = len(narration.split())
        print(f"  Guion: {wc} palabras (~{wc/150:.1f} min)")

        if wc < 50:
            print(f"  ERROR: guion demasiado corto, saltando")
            continue

        # Generate slides
        slide_dir = OUT_DIR / f"{topic_num}_slides"
        slides = generate_slides(topic_num, title, narration, slide_dir)
        print(f"  Slides: {len(slides)}")

        # Generate audio
        audio_path = OUT_DIR / f"{topic_num}_audio"
        duration = generate_audio(narration, audio_path)
        print(f"  Audio: {duration:.1f}s")

        # Combine
        safe_title = re.sub(r'[^a-zA-Z0-9áéíóúÁÉÍÓÚñÑü\s-]', '', title).replace(' ', '_')
        video_path = OUT_DIR / f"{topic_num}_{safe_title}.mp4"
        combine_to_video(slides, audio_path, video_path)
        mb = video_path.stat().st_size / (1024 * 1024)
        print(f"  Video: {video_path.name} ({mb:.1f} MB)")

        # Cleanup
        audio_path.with_suffix(".aiff").unlink(missing_ok=True)
        audio_path.with_suffix(".txt").unlink(missing_ok=True)

    print(f"\n{'='*60}")
    print(f"  Completado. Videos en: {OUT_DIR}")
    print(f"{'='*60}")


if __name__ == "__main__":
    main()
