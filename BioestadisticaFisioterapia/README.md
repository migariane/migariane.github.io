# Bioestadística para Fisioterapia

**Material docente interactivo — Grado en Fisioterapia, Universidad de Granada**

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
[![Quarto](https://img.shields.io/badge/Quarto-RevealJS-39729E.svg)](https://quarto.org)
[![R](https://img.shields.io/badge/R-BioEstatR-276DC3.svg)](https://migariane.github.io/BioEstatR)
[![Libro](https://img.shields.io/badge/Libro-Matem%C3%A1ticaEstad%C3%ADsticaMedicinaR-green.svg)](https://migariane.github.io/MatematicaEstadisticaMedicinaR)

Presentaciones interactivas en **Quarto RevealJS** que cubren el temario completo de Bioestadística para el Grado en Fisioterapia de la Universidad de Granada. Cada tema combina fundamentos matemáticos, aplicación clínica en fisioterapia, ejemplos numéricos paso a paso, y práctica guiada con **R + [BioEstatR](https://migariane.github.io/BioEstatR)**.

---

## Temario

| # | Tema | Contenido |
|:-:|------|-----------|
| **01** | Estadística Descriptiva (Parte I) | Tipos de datos, tablas de frecuencia, organización y resumen de datos, visualización |
| **01** | Estadística Descriptiva (Parte II) | Medidas de posición, dispersión, forma, diagramas de caja, aplicación práctica |
| **02** | Probabilidad y VA (Parte I) | Axiomas de Kolmogorov, Bayes, VPP/VPN, variables aleatorias discretas y continuas |
| **02** | Probabilidad y VA (Parte II) | Distribuciones Normal, Binomial, Poisson, t-Student, χ², F, TCL, aproximaciones |
| **03** | Estimación e Intervalos de Confianza | TCL, error estándar, IC para media y proporción, tamaño muestral |
| **04** | Contraste de Hipótesis (Parte I) | NHST, error tipo I/II, normalidad, tests para una media y una proporción |
| **04** | Contraste de Hipótesis (Parte II) | Tests para dos muestras, tests no paramétricos, McNemar, potencia, d de Cohen |
| **05** | Datos Cualitativos — χ² | Tablas de contingencia, OR, RR, DR, NNT, test exacto de Fisher, Mantel-Haenszel |
| **06** | Regresión y Correlación | Pearson y Spearman, regresión lineal simple (MCO), R², diagnóstico de residuos, cuarteto de Anscombe |

---

## Estructura del proyecto

```
├── _quarto.yml              # Configuración del sitio web
├── index.qmd                # Página de inicio
├── madrid-theme.scss        # Tema visual personalizado
├── T01_I_Descriptiva.qmd     # Tema I — Parte I
├── T01_II_Descriptiva.qmd    # Tema I — Parte II
├── T02_I_Probabilidad.qmd    # Tema II — Parte I
├── T02_II_Probabilidad.qmd   # Tema II — Parte II
├── T03_Estimacion_IC.qmd     # Tema III
├── T04_I_Test_Hipotesis.qmd  # Tema IV — Parte I
├── T04_II_Test_Hipotesis.qmd # Tema IV — Parte II
├── T05_ChiCuadrado.qmd       # Tema V
├── T06_RegresionCorr.qmd     # Tema VI
├── references.bib           # Bibliografía (BibTeX)
└── pdf-macros.tex           # Macros LaTeX para PDF
```

---

## Renderizado

```bash
# Renderizar el sitio completo (RevealJS)
quarto render

# Renderizar un tema específico a PDF
quarto render T01_Descriptiva.qmd --to pdf

# Previsualizar
quarto preview
```

---

## Licencia

[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) © 2026 Miguel Angel Luque-Fernández

Las diapositivas son de uso libre para fines docentes. El código R incluido es reproducible con el paquete [BioEstatR](https://migariane.github.io/BioEstatR).

---

## Autor

**Miguel Angel Luque-Fernández**  
Profesor Titular, Dpto. de Estadística e Investigación Operativa  
Universidad de Granada  
[mluquefe@ugr.es](mailto:mluquefe@ugr.es) · [migariane.github.io](https://migariane.github.io)
