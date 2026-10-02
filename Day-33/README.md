# Day 33 - Missing Values and Processing Pipeline

## Topics Covered

Today I learned about handling missing values in Machine Learning and building a preprocessing pipeline.

### Main Topics

- Missing values
- Checking null values using `isna().sum()`
- Dropping rows containing missing values
- Imputing missing values
- Simple Imputer
- KNN Imputer
- Mode imputation for categorical variables
- Processing Pipeline
- Train and test performance
- Overfitting
- MLflow experiment tracking
- DagsHub integration
- Comparing Drop vs Impute approaches

## What I Learned

Missing values are common in real-world datasets. Before training a Machine Learning model, missing values need to be handled properly.

Two common approaches are:

1. Drop rows containing missing values.
2. Impute missing values with suitable values.

For categorical columns, the most frequent value (mode) can be used.

For numerical columns, techniques such as KNN Imputer can be used.

I also learned how to combine multiple preprocessing steps using a Pipeline.

## Experiments

### Experiment 1 - Drop Missing Values

Rows containing missing values are removed using:

```python
df.dropna()