# SuperLearner Tutorial for Epidemiologists and Biostatisticians

A hands-on tutorial on Super Learner, the cross-validated ensemble machine learning method by van der Laan, Polley and Hubbard (2007), written for epidemiologists, biostatisticians, and clinical researchers who want to move beyond single-model fitting.

The tutorial starts with a single penalised regression and builds up to a full 18-learner clinical prediction model with external validation, calibration plots, and a practical bridge to causal inference (TMLE).

## Live tutorial

Read the interactive version on GitHub Pages:  
https://migariane.github.io/SL-Tutorial/SuperLearner_Tutorial.html

Also available as:
- PDF (printable): `SuperLearner_Tutorial.pdf`
- Quarto source: `SuperLearner_Tutorial.qmd`

## Keywords

Super Learner, ensemble learning, cross-validation, machine learning, epidemiology, biostatistics, clinical prediction, TMLE, targeted learning, R, SuperLearner package

## What the tutorial covers

| Section | Description |
|---------|-------------|
| Introduction | What SL is, why it matters for epi/biostat, the 6-stage algorithm |
| Installation & Setup | Core and wrapper packages, exploring built-in learners |
| Simulated Epidemiological Data | Known-truth binary outcome with interactions and non-linearity |
| Basic Super Learner | Single learner to full ensemble with benchmark |
| Predictions and Performance | `predict()` mechanics, ROC curves, AUC with honest interpretation |
| Cross-Validated SL | `CV.SuperLearner()` for valid performance estimates, weight stability |
| Hyperparameter Tuning | Manual wrappers and `create.Learner()` grids (RF, XGBoost) |
| Feature Screening | Correlation and LASSO screens, NCI-60 learner x screener matrix |
| Meta-Learning Methods | NNLS vs NNloglik vs AUC optimisation |
| Parallel Computing | Multicore, `mcSuperLearner`, snow clusters |
| Custom Learner Wrappers | GBM, MARS/earth, robust LASSO screener from scratch |
| Full Clinical Application | 1000-patient CVD cohort, 9 covariates, 18 learners, test AUC and calibration |
| Regression and Dose-Response | Continuous outcomes, non-linear exposure-response curves |
| Comparison: SL vs caret | Internal CV vs external test, five concrete SL advantages |
| Best Practices | Six-point checklist for epidemiologists |
| Bridge to TMLE | Nuisance parameter estimation for causal inference |

## Author and affiliation

Miguel Angel Luque Fernandez  
Full Professor of Biostatistics  
Department of Statistics and Operations Research  
University of Granada, Spain  

Personal website: https://migariane.github.io  
Email: mluquefe@ugr.es  
GitHub: https://github.com/migariane

## License

This work is licensed under a Creative Commons Attribution 4.0 International License (CC BY 4.0). You are free to share and adapt this material for any purpose, even commercially, provided you give appropriate credit.

© 2026 Miguel Angel Luque-Fernandez

## Acknowledgments

- Super Learner methodology: van der Laan, Polley and Hubbard (2007)
- R package SuperLearner: Eric Polley, Erin LeDell, Chris Kennedy, Mark van der Laan
- Tutorial inspired by the NCI-60 genomics applications (Polley et al., 2012)
- Built with Quarto for reproducible multi-format output

## Citation

If you use this tutorial in your work, please cite:

```bibtex
@misc{luquefernandez2026superlearnertutorial,
  author       = {Miguel Angel Luque-Fernandez},
  title        = {SuperLearner Tutorial for Epidemiologists and Biostatisticians},
  year         = {2026},
  url          = {https://migariane.github.io/SL-Tutorial/SuperLearner_Tutorial.html},
  note         = {CC BY 4.0}
}
```

Last updated: August 2026