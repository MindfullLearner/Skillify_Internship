# Task 03 — Real-World Dataset Analysis System

## Project Overview

This project focuses on analyzing a real-world retail sales dataset using Python, Pandas, and NumPy.

The **Sample Superstore Dataset** was used to explore sales, profit, customer segments, product categories, geographical regions, and discount patterns.

The main objective was to perform exploratory data analysis (EDA), identify meaningful patterns, and extract business insights from the dataset.

## Objectives

- Load and explore a real-world CSV dataset.
- Understand dataset structure and data types.
- Perform data quality checks.
- Apply filtering and sorting operations.
- Calculate basic statistical measures.
- Analyze sales and profit across different categories and regions.
- Investigate discount levels and their relationship with profitability.
- Identify meaningful business findings using data analysis.

## Dataset Information

- **Dataset Name:** Sample Superstore
- **Source:** [Kaggle — Sample Superstore Dataset](https://www.kaggle.com/datasets/vivek468/superstore-dataset-final)
- **File Name:** `Sample_Superstore.csv`
- **Total Records:** 9,994
- **Total Columns:** 21
- **Time Period:** 2014–2017
- **File Format:** CSV

### Important Dataset Columns

| Column | Description |
|---|---|
| Order Date | Date when the order was placed |
| Ship Date | Date when the order was shipped |
| Segment | Customer segment |
| Region | Geographical sales region |
| Category | Product category |
| Sub-Category | Specific product sub-category |
| Sales | Sales amount |
| Quantity | Number of units |
| Discount | Discount applied |
| Profit | Profit or loss amount |

## Technologies and Libraries

- **Python** — Programming language
- **Pandas** — Data manipulation and DataFrame operations
- **NumPy** — Numerical calculations
- **Google Colab / Jupyter Notebook** — Development environment

## Analysis Performed

The following operations were performed during the project:

1. **Data Exploration:** Examined dataset structure using `head()`, `shape`, `columns`, `info()`, and `describe()`.

2. **Data Quality Checks:** Checked missing values and duplicate records.

3. **Filtering:** Identified high-sales records and loss-making transactions.

4. **Sorting:** Identified records with the highest sales and highest profits.

5. **Statistical Analysis:** Calculated mean, median, standard deviation, and average quantity.

6. **Category-wise Analysis:** Compared total sales and profit across product categories.

7. **Region-wise Analysis:** Evaluated business performance across geographical regions.

8. **Sub-Category Analysis:** Identified the most profitable and loss-making product sub-categories.

9. **Discount Analysis:** Examined average and total profit across different discount levels.

10. **Customer Segment Analysis:** Compared sales and profitability across customer segments.

11. **Year-wise Analysis:** Examined yearly sales, profit, and record counts from 2014 to 2017.

12. **Correlation Analysis:** Investigated the linear relationship between sales and profit.

## Key Findings

- The Technology category generated the highest total sales (836,154.03) and profit (145,454.95).
- The West region recorded the highest total sales (725,457.82) and profit (108,418.45).
- Copiers generated the highest sub-category profit (55,617.82).
- Tables recorded the largest total loss (-17,725.48).
- The Consumer segment generated the highest total sales and profit.
- Home Office recorded the highest average profit per record (33.82).
- The year 2017 recorded the highest total sales and profit.
- Higher discount levels showed an association with lower profitability.
- Sales and profit had a moderate positive correlation of approximately 0.48.

## Data Quality Results

| Check | Result |
|---|---:|
| Total Records | 9,994 |
| Total Columns | 21 |
| Missing Values | 0 |
| Exact Duplicate Rows | 0 |

## Project Structure

```text
Task-03-Sales-Data-Analysis/
│
├── Task_03_Sales_Data_Analysis.ipynb
├── Sample_Superstore.csv
├── README.md
```

## How to Run the Project

1. Download or clone this project repository.
2. Install Python if running locally.
3. Install the required libraries:

```bash
pip install pandas numpy
```

4. Open the notebook using Jupyter Notebook or Google Colab.
5. Upload `Sample_Superstore.csv` to the working environment.
6. Update the CSV file path if necessary.
7. Run the notebook cells sequentially to reproduce the analysis.

## Project Deliverables

- Jupyter Notebook containing Python code, calculations, and analysis outputs.
- Screenshots demonstrating the completed analysis.
- Final report documenting methodology, results, and key findings.

## Learning Outcomes

Through this project, I gained practical experience in:

- Working with real-world CSV datasets.
- Using Pandas DataFrames for data manipulation.
- Applying NumPy for numerical calculations.
- Performing exploratory data analysis.
- Filtering, sorting, and grouping data.
- Calculating descriptive statistics and correlation.
- Identifying patterns and extracting meaningful business insights.

---

**Internship:** Skillify — Artificial Intelligence
**Task:** 03 — Real-World Dataset Analysis System
