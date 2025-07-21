# Final Project: Student Performance Analyzer (SPA)

## Objective

This project aims to analyze student exam performance based on various factors like gender, parental education, lunch type, and test preparation. Students will apply Python and Machine Learning techniques to:

- Explore and visualize the data
- Predict whether a student will pass or fail
- Discover patterns among students using clustering

---
## Dataset

**Dataset Name**: StudentsPerformance.csv  
**Location**: This file is already included in the `project_folder/` directory of this repository.  

Just load it directly using pandas:

import pandas as pd
df = pd.read_csv('project_folder/StudentsPerformance.csv')


### Columns Overview:

| Column                     | Description                                |
|----------------------------|--------------------------------------------|
| gender                    | Male or Female                              |
| race/ethnicity            | Group A, B, C, D, or E                      |
| parental level of education | Parent's highest education level         |
| lunch                     | Standard or Free/Reduced lunch              |
| test preparation course   | Completed or None                           |
| math score                | Math exam score (0-100)                     |
| reading score             | Reading exam score (0-100)                  |
| writing score             | Writing exam score (0-100)                  |

---

## Project Tasks

### 1. Data Preprocessing

- Load dataset using Pandas
- Check for missing or duplicate values
- Convert categorical columns using Label Encoding or OneHot Encoding

### 2. Exploratory Data Analysis (EDA)

- Plot score distributions using histograms
- Compare average scores by gender, lunch type, and test preparation status
- Create a correlation heatmap
- Use boxplots and bar plots for insights

### 3. Feature Engineering

- Create a new column `average_score`
- Create a new column `result`:
  - "Pass" if average score ≥ 50
  - "Fail" if average score < 50

- Convert result to binary labels for machine learning (1 = Pass, 0 = Fail)

---

## Machine Learning Models

### A. Classification

Use the following models to predict `Pass` or `Fail`:

1. Logistic Regression
2. K-Nearest Neighbors (KNN)

**Evaluation Metrics**:
- Accuracy Score
- Confusion Matrix
- Precision, Recall, F1-score

### B. Clustering

Use K-Means Clustering to group students based on performance patterns:
- Cluster by math score, reading score, and writing score
- Visualize clusters using 2D plots

---

## Bonus Analysis

- Analyze effect of test preparation on average scores
- Compare average scores across different lunch types and parental education levels

---


## Learning Outcomes

By completing this project, you will learn:
- Full end-to-end machine learning workflow
- Data cleaning, feature engineering, and visualization
- Classification and clustering algorithms
- Evaluation and interpretation of ML models
