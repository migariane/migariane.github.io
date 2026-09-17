# migariane.github.io

Personal academic website of **Miguel Angel Luque-Fernandez** — open-access tutorials, R packages, Stata programs, and Shiny apps for epidemiology, biostatistics, and causal inference.

**Live site:** <https://migariane.github.io/>

## About this website

This repository hosts the source files for my personal academic website, published as a static site with GitHub Pages from the `master` branch. The site collects teaching materials and software I have developed or use in courses and workshops, covering:

- **Conformal statistical inference** — marginal coverage, split conformal prediction, conformal quantile regression, full conformal, and Jackknife+.
- **Causal inference & TMLE** — potential outcomes, DAGs, G-computation, propensity scores, doubly robust AIPW, and targeted maximum likelihood estimation, in both R and Stata.
- **Survival analysis** — Kaplan–Meier estimation, Cox models, net survival, and flexible parametric (Royston–Parmar) models.
- **Machine learning** — cross-validation, SuperLearner ensembles, and metalearners for heterogeneous treatment effects.
- **Interactive Shiny apps** — teaching apps on the Central Limit Theorem, confidence intervals, collider bias, parametric survival distributions, and more.
- **Software packages** — the `eltmle`, `cvAUROC`, and `cmatch` Stata modules and the `BioEstatR` R package.
- **Books** — *Computational Causal Inference for Applied Researchers*, *Matemática Estadística con R*, and *Bioestadística Aplicada*.

The published site is static HTML, CSS, and JavaScript. The tutorials were rendered from R Markdown and Quarto notebooks.

## Repository structure

| Path | Purpose |
|------|---------|
| `index.html` | Landing page linking to all tutorials, packages, and apps. |
| `css/`, `stylesheets/`, `javascripts/`, `js/`, `fonts/` | Styles, fonts, and scripts for the static site. |
| `Figures/`, `images/` | Logos and figures used by the site and tutorials. |
| `*.html`, `*.Rmd`, `*.qmd` | Rendered tutorials and their sources. |
| `CATE/`, `SL-Tutorial/`, `test/`, `references/` | Supporting material for individual tutorials. |
| `sitemap.xml`, `robots.txt`, `404.html` | SEO and site plumbing. |

## Local preview

No build step is required to preview the site. Serve the repository root with any static file server, for example:

```bash
python3 -m http.server 8000
# then open http://localhost:8000/
```

## Contributing

Corrections, fixes, and improvements are welcome. Please open a pull request or file an issue at <https://github.com/migariane/migariane.github.io/issues>.

## Citation

If you use these materials in your own teaching or research, please cite the website:

```bibtex
@misc{luquefernandez_website,
  author = {Luque-Fernandez, Miguel Angel},
  title  = {Miguel Angel Luque-Fernandez | Tutorials and Software},
  year   = {2026},
  url    = {https://migariane.github.io/}
}
```

## Contact

- Email: [mluquefe@ugr.es](mailto:mluquefe@ugr.es)
- GitHub: [@migariane](https://github.com/migariane)
- Google Scholar: [profile](https://scholar.google.com/citations?user=lA11XToAAAAJ&hl=en)
- ORCID: [0000-0001-6683-5164](https://orcid.org/0000-0001-6683-5164)

## License

Released under the [MIT License](LICENSE). © 2026 Miguel Angel Luque-Fernandez.
