# Machine Learning (From Scratch)

This repository contains a simple implementation of **Linear Regression from scratch** and a small workflow to use a salary dataset.

## What’s inside

- **Simple Linear Regression (from scratch)**: `SimpleLinearRegression`
  - Computes the best-fit **slope** and **intercept** using the closed-form least squares solution.
  - Provides:
    - `fit(X, y)`
    - `predict(X)`
    - `score(X, y)` (R²)
- **Dataset**: `datasets/Salary_dataset.csv`
- **Dataset download helper**: `utils/Dataset_Download_Script.py`
- **Notebook demo**: `algorithms/Regression/LinearRegression/simple_linear_regression_from_scratch.ipynb`

## Project structure

```text
.
├── main.py
├── pyproject.toml
├── datasets/
│   └── Salary_dataset.csv
├── algorithms/
│   └── Regression/
│       └── LinearRegression/
│           └── simple_linear_regression_from_scratch.ipynb
└── utils/
    └── Dataset_Download_Script.py
```

## Requirements

This project targets **Python 3.12+**.

Key dependencies from `pyproject.toml`:

- `numpy`
- `pandas`
- `matplotlib`
- `scikit-learn` (used in the notebook; from-scratch model is independent)
- `kagglehub` (dataset download utility)

## Setup

From the repo root:

1. Create a virtual environment (optional but recommended).
2. Install dependencies using your preferred tool (e.g., `uv`, since `uv.lock` is present).

Example (if you use `uv`):

```bash
uv sync
```

## Run / Demo

The main demo is in the notebook:

- `algorithms/Regression/LinearRegression/simple_linear_regression_from_scratch.ipynb`

### What the notebook does

1. Loads `datasets/Salary_dataset.csv` with pandas.
2. Uses `YearsExperience` as input feature `X` and `Salary` as target `y`.
3. Trains `SimpleLinearRegression`.
4. Prints:
   - learned `slope`
   - learned `intercept`
   - R² score
5. Predicts salary for new experience values.
6. Plots the regression line over the actual data.

## Dataset

### Local dataset path

- CSV: `datasets/Salary_dataset.csv`

The notebook expects it to be available at that path.

### Downloading (optional)

You can download the dataset using:

- `utils/Dataset_Download_Script.py`

This script uses `kagglehub` to download the dataset and then copies files into the **Datasets** directory.

> Note: the script currently uses a hardcoded destination:
> `D:\\Machine_Learning\\Datasets`
>
> If your Windows path differs, edit `destination` in the script.

## Notes / Model behavior

The from-scratch model fits a single-feature linear relationship:

\[\text{Salary} \approx m \cdot \text{YearsExperience} + b\]

Where:
- `m` = slope
- `b` = intercept

`score(X, y)` returns **R²**:

\[R^2 = 1 - \frac{\sum (y - \hat{y})^2}{\sum (y - \bar{y})^2}\]

## License

Add your license information here (e.g., MIT, Apache-2.0). 

