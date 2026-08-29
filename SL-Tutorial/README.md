# SuperLearner Tutorial for Epidemiologists & Biostatisticians

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
[![GitHub Pages](https://img.shields.io/badge/GitHub_Pages-Live-brightgreen)](https://migariane.github.io/SL-Tutorial/SuperLearner_Tutorial.html)
[![Quarto](https://img.shields.io/badge/Built_with-Quarto-blue)](https://quarto.org/)

## 📖 Overview

A comprehensive, hands-on tutorial on **Super Learner (SL)** — the cross-validated ensemble machine learning method by van der Laan, Polley & Hubbard (2007) — written specifically for epidemiologists, biostatisticians, and clinical researchers.

This tutorial takes you from a single penalised regression to a full 18-learner clinical prediction model with external validation, calibration plots, and a bridge to causal inference (TMLE).

## 🔗 Live Tutorial

**👉 [Read the interactive HTML version on GitHub Pages](https://migariane.github.io/SL-Tutorial/SuperLearner_Tutorial.html)**

Also available as:
- [PDF (printable)](SuperLearner_Tutorial.pdf)
- [Quarto source (.qmd)](SuperLearner_Tutorial.qmd)

## 🎯 Keywords

`Super Learner` · `ensemble learning` · `cross-validation` · `machine learning` · `epidemiology` · `biostatistics` · `clinical prediction` · `TMLE` · `targeted learning` · `R` · `SuperLearner package`

## 📚 Tutorial Contents

| Section | Description |
|---------|-------------|
| **Introduction** | What SL is, why it matters for epi/biostat, the 6-stage algorithm |
| **Installation & Setup** | Core + wrapper packages, exploring built-in learners |
| **Simulated Epidemiological Data** | Known-truth binary outcome with interactions & non-linearity |
| **Basic Super Learner** | Single learner → two learners → full ensemble with benchmark |
| **Predictions & Performance** | `predict()` mechanics, ROC curves, AUC with honest interpretation |
| **Cross-Validated SL** | `CV.SuperLearner()` for valid performance estimates, weight stability |
| **Hyperparameter Tuning** | Manual wrappers + `create.Learner()` grids (RF, XGBoost) |
| **Feature Screening** | Correlation & LASSO screens, NCI-60 learner×screener matrix |
| **Meta-Learning Methods** | NNLS vs NNloglik vs AUC optimisation |
| **Parallel Computing** | Multicore, `mcSuperLearner`, snow clusters |
| **Custom Learner Wrappers** | GBM, MARS/earth, robust LASSO screener from scratch |
| **Full Clinical Application** | 1000-patient CVD cohort, 9 covariates, 18 learners, test AUC + calibration |
| **Regression & Dose-Response** | Continuous outcomes, non-linear exposure-response curves |
| **Comparison: SL vs caret** | Internal CV vs external test, 5 concrete SL advantages |
| **Best Practices** | 6-point checklist for epidemiologists |
| **Bridge to TMLE** | Nuisance parameter estimation for causal inference |

## 👤 Authorship & Affiliation

**Miguel Ángel Luque-Fernández**  
*Senior Researcher in Epidemiology & Biostatistics*  
[🌐 Personal Website](https://migariane.github.io) · [📧 Email](mailto:mluquefe@ugr.es) · [🐙 GitHub](https://github.com/migariane) · [🔬 ORCID](https://orcid.org/0000-0002-9385-3261) · [📖 Google Scholar](https://scholar.google.com/citations?user=MALF)

**Department of Statistics & Operations Research**  
**University of Granada (UGR), Spain**  
[🏛️ Department Website](https://departamentoest.ugr.es/)

## 📄 License

This work is licensed under a **Creative Commons Attribution 4.0 International License (CC BY 4.0)**.  
You are free to share and adapt this material for any purpose, even commercially, provided you give appropriate credit.

```
© 2026 Miguel Ángel Luque-Fernández
```

## 🙏 Acknowledgments

- Super Learner methodology: van der Laan, Polley & Hubbard (2007)
- R package `SuperLearner`: Eric Polley, Erin LeDell, Chris Kennedy, Mark van der Laan
- Tutorial inspired by the NCI-60 genomics applications (Polley et al., 2012)
- Built with [Quarto](https://quarto.org/) for reproducible multi-format output

## 📥 Citation

If you use this tutorial in your work, please cite:

```bibtex
@misc{luquefernandez2026superlearnertutorial,
  author       = {Miguel Ángel Luque-Fernández},
  title        = {SuperLearner Tutorial for Epidemiologists and Biostatisticians},
  year         = {2026},
  url          = {https://migariane.github.io/SL-Tutorial/SuperLearner_Tutorial.html},
  note         = {CC BY 4.0}
}
```

---

*Last updated: August 2026*