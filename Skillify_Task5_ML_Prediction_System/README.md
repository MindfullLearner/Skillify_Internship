# Titanic Survival Prediction System

## Project Overview

The Titanic Survival Prediction System is a Machine Learning classification project developed to predict whether a passenger survived the Titanic disaster based on passenger information.

The project demonstrates a complete Machine Learning workflow, starting from raw dataset exploration and preprocessing to model training, prediction, evaluation, and model saving.

The main objective was to build and compare different classification algorithms while implementing a proper preprocessing pipeline to prevent data leakage.

## Objectives

- Select and explore a suitable dataset.
- Identify relevant features and the target variable.
- Handle missing values and categorical data.
- Perform a train-test split before preprocessing.
- Build a preprocessing pipeline using Scikit-learn.
- Train multiple Machine Learning models.
- Generate predictions on unseen data.
- Evaluate and compare model performance.
- Apply hyperparameter tuning.
- Save and reload the trained model.

## Dataset

**Dataset:** Titanic Dataset (Seaborn)

- Total Records: 891
- Total Original Features: 15
- Selected Input Features: 7
- Target Variable: `survived`

### Selected Features

| Feature | Description |
|---|---|
| pclass | Passenger class |
| sex | Passenger gender |
| age | Passenger age |
| sibsp | Number of siblings/spouses aboard |
| parch | Number of parents/children aboard |
| fare | Passenger ticket fare |
| embarked | Port of embarkation |

**Target Variable:** `survived`

- 0 = Did Not Survive
- 1 = Survived

## Technologies and Libraries

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Joblib
- Google Colab

## Machine Learning Workflow

### 1. Exploratory Data Analysis (EDA)

Explored the dataset, examined missing values, analyzed survival distribution, and created visualizations.

### 2. Feature and Target Selection

Selected seven relevant features and used `survived` as the target variable.

### 3. Train-Test Split

Divided the dataset into:

- Training Data: 80% (712 records)
- Testing Data: 20% (179 records)

Used stratified splitting to maintain the survival class distribution.

### 4. Data Preprocessing

Implemented Scikit-learn pipelines to prevent data leakage.

**Numerical Preprocessing:**
- Missing values handled using median imputation.
- Features scaled using StandardScaler.

**Categorical Preprocessing:**
- Missing values handled using most-frequent imputation.
- Categories encoded using OneHotEncoder.

Used ColumnTransformer to combine numerical and categorical preprocessing.

All preprocessing transformations were fitted using training data only.

### 5. Model Training

Trained two classification algorithms:

- Logistic Regression
- Decision Tree Classifier

### 6. Model Evaluation

Evaluated model performance using:

- Accuracy
- Precision
- Recall
- F1-score
- Classification Report
- Confusion Matrix

### 7. Hyperparameter Tuning

Used GridSearchCV with 5-fold cross-validation to optimize Decision Tree parameters based on F1-score.

The search evaluated 45 parameter combinations.

### 8. Model Saving

Saved the complete Logistic Regression preprocessing and prediction pipeline using Joblib.

Also tested the saved model by loading it again and verifying that its predictions and accuracy matched the original model.

## Model Performance

The following results were obtained on the same testing dataset of 179 records.

| Evaluation Metric | Logistic Regression | Decision Tree | Tuned Decision Tree |
|---|---:|---:|---:|
| Accuracy | 80.45% | 81.56% | 79.33% |
| Precision | 79.31% | 79.03% | 75.81% |
| Recall | 66.67% | 71.01% | 68.12% |
| F1-score | 72.44% | 74.81% | 71.76% |

### Selected Model

Logistic Regression was selected as the primary saved model because it demonstrated a smaller difference between training accuracy (80.76%) and testing accuracy (80.45%).

Although the original Decision Tree achieved slightly higher testing accuracy and F1-score, its training accuracy was considerably higher (98.31%), indicating potential overfitting.

Therefore, Logistic Regression was preferred for its more consistent generalization performance.

## Project Files

- `Task_5_Titanic_ML_Prediction_System.ipynb` — Complete Machine Learning workflow and evaluation.
- `titanic_survival_model.pkl` — Saved Logistic Regression pipeline.
- `README.md` — Project documentation.

## Conclusion

This project demonstrated the complete development of a Machine Learning classification system using the Titanic dataset.

Three model configurations were evaluated: Logistic Regression, Decision Tree, and a tuned Decision Tree.

The results showed that the original Decision Tree achieved the highest testing accuracy of 81.56%, while Logistic Regression demonstrated more consistent training and testing performance.

The project also demonstrated the importance of proper preprocessing, avoiding data leakage, model comparison, hyperparameter tuning, and model persistence.

Overall, this project provided practical experience in developing and evaluating Machine Learning prediction systems using Python and Scikit-learn.

## Author

**Nayab Maryam**

Machine Learning & Generative AI Intern

Skillify Internship
