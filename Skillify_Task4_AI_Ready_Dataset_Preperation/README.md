# Task 4: AI-Ready Dataset Preparation

## Project Overview

This project focuses on preparing a real-world dataset for Machine Learning by performing essential data preprocessing and cleaning operations.

The **Titanic dataset** was selected for this task. The objective was to transform raw data into a clean, structured, and machine-learning-ready format by handling missing values, investigating duplicate records, analyzing outliers, encoding categorical features, scaling numerical features, and creating visualizations.

## Objectives

- Explore and understand the dataset.
- Identify and handle missing values.
- Detect and investigate duplicate records.
- Detect and analyze numerical outliers.
- Apply transformations to reduce data skewness.
- Encode categorical variables into numerical representations.
- Scale numerical features.
- Create visualizations to understand data distributions and patterns.
- Export the processed dataset into CSV files.

## Technologies and Libraries

- **Python** — Programming language
- **Pandas** — Data manipulation and analysis
- **NumPy** — Numerical operations
- **Matplotlib** — Data visualization
- **Seaborn** — Statistical visualization
- **Scikit-learn** — Data preprocessing, feature scaling, and train-test splitting
- **Jupyter Notebook** — Development environment

## Dataset Information

**Dataset:** Titanic Dataset  
**Source:** Seaborn built-in dataset

- Original rows: 891
- Original columns: 15
- Selected columns: 8 (including the target variable)
- Target variable: `survived`

The target variable indicates whether a passenger survived:
- `0` — Did not survive
- `1` — Survived

## Data Preprocessing Steps

### 1. Data Exploration

The dataset was explored to understand its structure, column names, data types, statistical summaries, and missing values.

### 2. Missing Value Handling

Missing values were identified in the following columns:

- `age`
- `embarked`
- `deck`
- `embark_town`

Only the selected features were retained for preprocessing. Missing values were handled using:

- Median imputation for `age`.
- Mode imputation for `embarked`.

Redundant and unnecessary columns were excluded from the selected dataset.

### 3. Duplicate Investigation

Duplicate records were identified and investigated.

A total of 107 duplicate occurrences were detected. However, they were not automatically removed because the dataset does not provide a unique passenger identifier to confirm whether identical records represent accidental duplication or different passengers with similar information.

### 4. Outlier Detection and Treatment

The Interquartile Range (IQR) method was used to identify potential outliers in numerical features.

Outliers were investigated rather than blindly removed because some extreme values may represent legitimate passenger information.

The `fare` feature showed strong right skewness. A logarithmic transformation using `np.log1p()` was applied to reduce its skewness.

### 5. Categorical Encoding

Categorical features were converted into numerical representations using One-Hot Encoding.

Features encoded:
- `pclass`
- `sex`
- `embarked`

### 6. Numerical Feature Scaling

StandardScaler was applied to numerical features:

- `age`
- `sibsp`
- `parch`
- `fare_log`

The scaler was fitted on the training data and then used to transform the testing data to avoid data leakage.

### 7. Train-Test Split

The dataset was divided into:

- Training data: 80% (712 records)
- Testing data: 20% (179 records)

Stratified splitting was used to maintain the target variable's class distribution.

### 8. Data Visualization

The following visualizations were created:

1. **Survival Distribution:** A count plot showing the number of passengers who survived and did not survive.
2. **Age vs Survival:** A box plot comparing passenger age distributions according to survival status.
3. **Fare Distribution:** A histogram comparing fare distribution before and after logarithmic transformation.

## Final Dataset

The processed dataset contains:

- 891 records
- 12 input features
- 1 target variable
- 13 columns in total

The categorical features have been encoded, numerical features have been scaled, and missing values have been handled.

## Project Structure

```text
Task-4-AI-Ready-Dataset-Preparation/
│
├── Task_4_AI_Ready_Dataset_Preparation.ipynb
│
├── train.csv
├── test.csv
├── titanic_ml_ready.csv
│
├── README.md
│
└── visualizations/
    ├── survival_distribution.png
    ├── age_vs_survival.png
    └── fare_distribution.png
```

*Note: Adjust the notebook and visualization filenames in this structure to match your actual files.*

## How to Run the Project

1. Clone or download this repository.
2. Install the required libraries:

```bash
pip install pandas numpy matplotlib seaborn scikit-learn jupyter
```

3. Open the project folder.
4. Launch Jupyter Notebook:

```bash
jupyter notebook
```

5. Open the project notebook and run the cells sequentially.

## Output Files

| File | Description |
|---|---|
| `train.csv` | Processed training dataset |
| `test.csv` | Processed testing dataset |
| `titanic_ml_ready.csv` | Complete processed dataset |

## Key Learnings

Through this project, I gained practical experience in:

- Understanding and exploring real-world datasets.
- Handling missing and duplicate records.
- Detecting and interpreting outliers.
- Applying logarithmic transformations to skewed data.
- Converting categorical data into numerical features.
- Scaling numerical features using StandardScaler.
- Splitting datasets into training and testing sets.
- Understanding data leakage and why preprocessing should be fitted on training data.
- Creating visualizations for exploratory data analysis.
- Exporting structured datasets for Machine Learning workflows.

## Conclusion

This project demonstrates the importance of data preprocessing before building Machine Learning models. Raw datasets often contain missing values, inconsistent formats, categorical variables, and unusual distributions.

By applying appropriate preprocessing techniques, the Titanic dataset was transformed into a structured format suitable for further Machine Learning experimentation.

**Internship:** Skillify — Artificial Intelligence
**Task:** Task 4 — AI-Ready Dataset Preparation
