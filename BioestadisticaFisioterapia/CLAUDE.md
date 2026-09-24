# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

**Project:** Bioestadística para Fisioterapia — Diapositivas Quarto
**Institution:** Dpto. Estadística e Investigación Operativa, Universidad de Granada
**Author:** Miguel Angel Luque-Fernández
**Course:** Grado en Fisioterapia

---

## Core Principles

- **Quarto is the source of truth** — `.qmd` files are authoritative; Beamer `.tex` files in the parent directory are the legacy source
- **Render to verify** — always `quarto render` the changed file and confirm clean output before reporting done
- **Spanish is the course language** — all slide text, labels, and callouts must be in Spanish
- **Clinical fisioterapia context** — every statistical concept needs a clinical/fisioterapia example or interpretation
- **R code must be runnable** — all `{r}` chunks must execute without errors inside the QMD

---

## Project Structure

```
qmd_slides/
├── _quarto.yml              # Website config (navbar, revealjs defaults, MathJax macros)
├── index.qmd                # Landing page (course overview, objectives, resources)
├── madrid-theme.scss        # Custom RevealJS theme (typography, callouts, layout)
├── logo.png                 # UGR logo
├── T01_Descriptiva.qmd      # Tema I: Descriptive statistics (48 slides)
├── T02_Probabilidad.qmd     # Tema II: Probability and random variables (65 slides)
├── T03_Estimacion_IC.qmd    # Tema III: Estimation and confidence intervals (33 slides)
├── T04_Test_Hipotesis.qmd   # Tema IV: Hypothesis testing
├── T05_ChiCuadrado.qmd      # Tema V: Categorical data — χ² tests
├── T06_RegresionCorr.qmd    # Tema VI: Regression and correlation
├── .claude/skills/          # Symlinked to parent project skills
└── _site/                   # Rendered output (GitHub Pages)
```

---

## Commands

**Important:** The Anaconda R (v3.3.1, `/Users/MALF/opt/anaconda3/bin/R`) has a broken dynamic library. Always prefix PATH to use `/usr/local/bin/R` (v4.6.0).

```bash
# Render a single topic (preview locally)
PATH="/usr/local/bin:$PATH" quarto render T01_Descriptiva.qmd

# Render all topics
quarto render

# Preview with live reload
quarto preview

# Render the full website
quarto render --to revealjs
```

Rendering is the primary verification step. No separate build tool or test suite exists — the rendered HTML is the artifact.

---

## YAML Header Conventions

Each `.qmd` file has its own YAML header overriding website defaults for that topic:
- `fig-width` and `fig-height` control R plot dimensions (typical: 8×5 or 9×6.5)
- `code-fold: true` collapses R code by default
- `code-overflow: wrap` or `scroll` for long lines
- `slide-number: c/t` shows current/total

Global defaults live in `_quarto.yml` (includes MathJax macros like `\E`, `\Var`, `\P`, `\indep`, `\SE`).

---

## Slide Authoring

### Slide separators
- `---` starts a new slide (standard Quarto/RevealJS)
- `##` for the slide title
- `# Title {.center}` for section divider slides

### Custom CSS classes (defined in `madrid-theme.scss`)

| Class | Effect | Use Case |
|-------|--------|----------|
| `.callout-note` | Blue left-border box | Key information, context |
| `.callout-tip` | Green left-border box | Recommendations, best practices |
| `.callout-warning` | Orange left-border box | Cautions, limitations |
| `.callout-important` | Red left-border box | Critical points, must-know |
| `.framed` | Bordered box with subtle gradient | Key formulas, definitions |
| `.def` | Dark left-border, light background | Formal definitions |
| `.exercise` | Dashed orange border, yellow bg | Clinical/practical exercises |
| `.connection` | Blue gradient left-border | Bridges between topics |
| `.small` | 70% font | Footnotes, references |
| `.columns` / `.column` | Two-column layout | Side-by-side content |
| `.incremental` | RevealJS fragment list | Bullet-by-bullet reveal |
| `.center` | Centered text (on section) | Section dividers |
| `{.smaller}` | 85% font (non-existent; use `.small`) | — |

### R code in slides

R chunks render to both code blocks and output. `execute: eval: true` is set project-wide. Plot dimensions are set per-topic in YAML. Use `#| fig-height: N` for per-chunk overrides.

R plotmath Unicode rendering is font-dependent. When using union/intersection symbols in R figures, use `intToUtf8(8746)` for ∪ and `intToUtf8(8745)` for ∩ with `par(family="Arial Unicode MS")`, and format titles via `bquote()`.

### Content patterns

Each topic follows a consistent structure:
1. Title slide with logo
2. Learning objectives (`Objetivos de Aprendizaje`)
3. Core content with `##`-headed slides
4. R code examples with clinical data
5. Bridge slide to the next topic (`.connection`)
6. Resumen (key takeaways)

---

## Git

The `_site/` directory is in `.gitignore`. Commits should contain only source files (`.qmd`, `.scss`, `.yml`). GitHub Pages serves from `_site/` via a separate deploy mechanism.
