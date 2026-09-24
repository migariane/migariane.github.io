# CLAUDE.md

This file provides guidance to Claude Code when working with code in this repository.

**Project:** migariane.github.io — personal statistical learning site
**Author:** Miguel Angel Luque-Fernandez
**Upstream tutorials repo:** https://migariane.github.io/index.html
**Deploy:** GitHub Pages (built from Quarto/Rmd/HTML sources in this folder)

---

## Project Structure

```
migariane.github.io/           # The published site itself (mixed sources)
├── index.html                 # Landing page (tutorial list)
├── *.qmd / *.Rmd              # Tutorial sources (Quarto renders to .html here)
├── *.html                     # Rendered tutorial outputs (some hand-built, some Quarto)
├── BioestadisticaFisioterapia/  # Course where QUARTO is source of truth (own CLAUDE.md)
├── SL-Tutorial/               # SuperLearner tutorial (own README)
├── references/                # bibliography.bib + isme.csl
├── css/ fonts/ js/ images/ Figures/  # Site assets
├── theme-template.scss, ugr-theme.scss
└── robots.txt, sitemap.xml, params.json, 404.html
```

## Tutorial Topics (index.html)

1. Cross-validation (2. ML) 3. Causal Inference 4. Survival Analysis
5. TMLE 6. Shiny web apps 7. Plotly/ggplot (gapminder) 8. Stata (eltmle, cvauroc, cmatch)

Notable tutorials rendered here: `TMLE`, `CrossValidation.nb.Rmd`, `ConformalPrediction_Tutorial_ES.qmd`, `Maths_TMLE-IF`, `CATE`, `Tutorial-SVA-ULB`.

## Key Commands

```bash
# Render a single tutorial source back to HTML
quarto render Tutorial-TMLE.qmd     # (adjust to the file being edited)

# Pre-render check for a .nb.Rmd
Rscript -e "rmarkdown::render('CrossValidation.nb.Rmd')"
```

## Development Notes

- **Mixed heritage:** some `.html` files are generated from `.qmd`/`.Rmd` sources, others are hand-committed. When editing, prefer the source file and re-render; only hand-edit `.html` when no source exists.
- **Sub-projects with their own rules.** `BioestadisticaFisioterapia/` — Quarto is authoritative (Beamer legacy); Spanish; always re-render to verify. `SL-Tutorial/` — see its README.
- Contact for contributions: miguel-angel.luque at lshtm.ac.uk / @WATZILEI.