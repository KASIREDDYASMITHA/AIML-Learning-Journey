# AIML Day 30 - Model Training

## 1. Introduction to Model Training

Model training is the process of teaching a Machine Learning
model to identify patterns from a dataset.

The model learns relationships between input features and
the target variable.

After training, the model can make predictions on new data.

### Objective

The main objective of Day 30 is to implement a baseline
Machine Learning model.

We can start with Linear Regression and evaluate its
performance.

---

## 2. Baseline Model

A baseline model is a simple model used as a starting point
for evaluating Machine Learning performance.

It helps us understand how well a more advanced model
needs to perform.

A baseline model provides a reference for comparison.

### Example 1

We can use Linear Regression as a baseline model to
predict delivery time.

### Example 2

We can compare Linear Regression with Decision Tree
Regression to understand whether a more complex model
improves prediction accuracy.

---

## 3. Linear Regression

Linear Regression is a supervised Machine Learning
algorithm used to predict continuous numerical values.

It identifies the relationship between independent
variables and a dependent variable.

### Formula

y = mx + c

Where:

- y = Predicted output
- m = Slope
- x = Input feature
- c = Intercept

For multiple features:

y = b0 + b1x1 + b2x2 + ... + bnxn

Where:

- y = Predicted value
- b0 = Intercept
- b1, b2, ... bn = Model coefficients
- x1, x2, ... xn = Input features

### Examples

1. Predicting delivery time based on distance.
2. Predicting house prices based on area and number
   of bedrooms.

---

## 4. Dataset Preparation

Before training a Machine Learning model, we need
to prepare the dataset.

Dataset preparation includes:

1. Loading the dataset
2. Understanding the dataset
3. Checking missing values
4. Removing duplicate records
5. Dropping unnecessary columns
6. Separating features and target
7. Splitting the dataset

---

## 5. Loading the Dataset

Pandas is used to load and manipulate datasets.

Example:

    import pandas as pd

    df = pd.read_csv("delivery_data.csv")

    print(df.head())

The head() method displays the first five rows
of the dataset by default.

Other useful methods:

    print(df.shape)
    print(df.info())
    print(df.describe())
    print(df.isnull().sum())

---

## 6. Handling Missing Values

Missing values are values that are not available
in a dataset.

Missing values can affect model training.

There are two common approaches.

### Approach 1: Dropping Missing Values

We can remove rows or columns containing missing values.

Example:

    df = df.dropna()

This removes rows containing at least one missing value.

To remove columns containing missing values:

    df = df.dropna(axis=1)

Dropping data may reduce the size of the dataset.

It should be used carefully.

### Approach 2: Imputing Missing Values

Imputation means replacing missing values with
estimated or suitable values.

For numerical columns, we can use:

- Mean
- Median

For categorical columns, we can use:

- Most frequent value

Example:

    from sklearn.impute import SimpleImputer

    imputer = SimpleImputer(strategy="median")

The median is useful when numerical data contains
outliers.

The most frequent value can be used for categorical
features.

Imputation should be fitted on training data only
to prevent data leakage.

---

## 7. Dropping Unnecessary Columns

Some columns may not be useful for model training.

Examples:

- Unique IDs
- Unnecessary index columns
- Columns unrelated to the target

These columns can be removed.

Example:

    df = df.drop(columns=["ID"])

We should not remove a column without understanding
its purpose.

---

## 8. Removing Duplicate Records

Duplicate records are repeated rows in a dataset.

They may affect model training and evaluation.

To check duplicate records:

    print(df.duplicated().sum())

To remove duplicate records:

    df = df.drop_duplicates()

Removing duplicates can help prevent repeated
observations from unnecessarily influencing the model.

---

## 9. Features and Target

Features are the input variables used by a model.

The target is the variable that the model predicts.

Example:

Suppose we want to predict delivery time.

Features:
- Distance
- Weather
- Traffic
- Vehicle condition

Target:
- Delivery time

In Python:

    X = df.drop(columns=["Time_taken"])

    y = df["Time_taken"]

Here:

- X contains input features.
- y contains the target variable.

The target column name must match the dataset.

---

## 10. Numerical and Categorical Features

Features are commonly divided into two categories.

### Numerical Features

Numerical features contain numerical values.

Examples:

- Distance
- Temperature
- Age
- Delivery time

### Categorical Features

Categorical features represent groups or categories.

Examples:

- Weather
- Traffic
- City type
- Vehicle condition
- Order type

Categorical features usually need to be converted
into numerical representations before model training.

---

## 11. Train-Test Split

Train-test splitting divides a dataset into two parts.

### Training Data

Training data is used to train the Machine Learning model.

### Testing Data

Testing data is used to evaluate the trained model
on data it has not seen during training.

Example:

    from sklearn.model_selection import train_test_split

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )

Here:

- 80% of the data is used for training.
- 20% of the data is used for testing.
- random_state=42 makes the split reproducible.

---

## 12. Categorical Encoding

Categorical encoding converts categorical values
into numerical values.

### One-Hot Encoding

One-Hot Encoding creates separate binary columns
for categories.

Example:

Weather:

Sunny
Rainy
Cloudy

After encoding:

Weather_Sunny
Weather_Rainy
Weather_Cloudy

Each column contains 0 or 1.

One-Hot Encoding can be implemented using:

    from sklearn.preprocessing import OneHotEncoder

It is useful for nominal categorical features.

### Ordinal Encoding

Ordinal Encoding assigns numerical values to
categories that have a meaningful order.

Example:

Low = 0
Medium = 1
High = 2

Ordinal Encoding should be used only when
the categories have a meaningful order.

---

## 13. Model Training

After preparing the dataset, we train the model.

Example:

    from sklearn.linear_model import LinearRegression

    model = LinearRegression()

    model.fit(X_train, y_train)

The fit() method trains the model using
the training data.

---

## 14. Model Prediction

After training, we can make predictions using
the predict() method.

Example:

    y_pred = model.predict(X_test)

The model generates predicted values for
the test dataset.

---

## 15. Model Evaluation

Model evaluation helps us understand how well
the model performs.

For regression problems, common evaluation
metrics include:

### Mean Absolute Error (MAE)

MAE measures the average absolute difference
between actual and predicted values.

Lower MAE indicates smaller average errors.

### Mean Squared Error (MSE)

MSE calculates the average squared difference
between actual and predicted values.

Large errors receive greater penalties.

### Root Mean Squared Error (RMSE)

RMSE is the square root of MSE.

It is expressed in the same unit as the target.

### R-squared (R2)

R2 measures how much of the variation in
the target is explained by the model.

A higher R2 generally indicates a better fit.

However, R2 should not be interpreted alone.

---

## 16. Model Evaluation in Python

Example:

    from sklearn.metrics import (
        mean_absolute_error,
        mean_squared_error,
        r2_score
    )

    mae = mean_absolute_error(y_test, y_pred)

    mse = mean_squared_error(y_test, y_pred)

    rmse = mse ** 0.5

    r2 = r2_score(y_test, y_pred)

    print("MAE:", mae)
    print("MSE:", mse)
    print("RMSE:", rmse)
    print("R2:", r2)

---

## 17. Ensemble Learning

Ensemble learning combines predictions from
multiple models to improve performance.

Instead of relying on a single model, an
ensemble uses multiple models.

Examples:

1. Random Forest
2. Gradient Boosting

A Random Forest combines multiple decision trees.

Ensemble methods can improve predictive
performance, but they are not guaranteed
to outperform every baseline model.

---

# Part 2: ANOVA Hypothesis Testing

## 18. Introduction to ANOVA

ANOVA stands for Analysis of Variance.

It is a statistical method used to compare
the means of three or more groups.

It can help us determine whether a numerical
variable differs across categorical groups.

Example:

We can use ANOVA to investigate whether
average delivery time differs across
different weather conditions.

---

## 19. Hypothesis Testing

Hypothesis testing is a statistical method
used to evaluate a claim about a population.

It involves two hypotheses.

### Null Hypothesis (H0)

The null hypothesis states that there is
no statistically significant difference
between the group means.

### Alternative Hypothesis (H1)

The alternative hypothesis states that
at least one group mean is different.

---

## 20. One-Way ANOVA

One-way ANOVA examines whether a numerical
variable differs across groups of one
categorical variable.

Examples:

1. Does weather affect delivery time?
2. Does vehicle condition affect delivery time?

The categorical variable defines the groups.

The numerical variable is the measurement
whose means are compared.

---

## 21. ANOVA P-Value

The p-value helps us evaluate the evidence
against the null hypothesis.

A commonly used significance level is 0.05.

If p-value < 0.05:

Reject the null hypothesis.

There is statistically significant evidence
that not all group means are equal.

If p-value >= 0.05:

Fail to reject the null hypothesis.

There is insufficient statistical evidence
to conclude that the group means differ.

A p-value does not measure the size or
practical importance of an effect.

---

## 22. ANOVA Test in Python

Example:

    from scipy.stats import f_oneway

    group1 = [20, 25, 30]
    group2 = [35, 40, 45]
    group3 = [50, 55, 60]

    f_stat, p_value = f_oneway(
        group1,
        group2,
        group3
    )

    print("F-statistic:", f_stat)
    print("P-value:", p_value)

---

## 23. Delivery-Time Analysis

The homework involves investigating whether
different factors are associated with
delivery time.

Possible categorical variables:

- Weather
- Traffic
- Vehicle condition
- Type of order
- City type

Numerical variable:

- Delivery time

Examples of research questions:

1. Does weather affect delivery time?
2. Does traffic affect delivery time?
3. Does vehicle condition affect delivery time?
4. Does order type affect delivery time?
5. Does city type affect delivery time?

ANOVA can test differences in average
delivery time between the groups.

However, a significant ANOVA result does
not establish that a factor causes a
change in delivery time.

---

## 24. Important Points

1. Always inspect the dataset before training.
2. Check missing values and duplicates.
3. Remove only genuinely unnecessary columns.
4. Separate features and target correctly.
5. Split the dataset before fitting preprocessing
   steps to avoid data leakage.
6. Encode categorical features appropriately.
7. Train the baseline model.
8. Evaluate predictions using suitable metrics.
9. Use ANOVA to compare group means.
10. Interpret p-values carefully.
