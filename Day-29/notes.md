# Day 29 - Exploratory Data Analysis (EDA)

## 1. Introduction to EDA

Exploratory Data Analysis (EDA) is the process of
analyzing and understanding a dataset before applying
machine learning algorithms.

EDA helps us understand the structure, patterns,
relationships, and problems in the dataset.

### Objectives of EDA

1. Understand the dataset.
2. Identify numerical and categorical columns.
3. Find missing values.
4. Detect duplicate records.
5. Understand the distribution of data.
6. Identify relationships between features.
7. Detect outliers.
8. Select relevant features.
9. Prepare data for machine learning.

## 2. Steps in EDA

The important steps involved in EDA are:

1. Data Understanding
2. Data Cleaning
3. Feature Selection
4. Missing Value Imputation
5. Numerical Data Analysis
6. Categorical Data Analysis
7. Data Visualization
8. Hypothesis Formation

## 3. Data Understanding

Data understanding is the first step in EDA.

It involves inspecting the dataset to understand
its structure, size, columns, and data types.

### Important Pandas Functions

#### 1. head()

Displays the first five rows of a dataset.

    df.head()

#### 2. tail()

Displays the last five rows of a dataset.

    df.tail()

#### 3. shape

Returns the number of rows and columns.

    df.shape

#### 4. info()

Displays information about the dataset, including
column names, data types, and non-null values.

    df.info()

#### 5. describe()

Provides statistical information about numerical
columns, such as mean, standard deviation,
minimum, maximum, and quartiles.

    df.describe()

#### 6. isnull()

Checks for missing values in the dataset.

    df.isnull().sum()

#### 7. duplicated()

Checks for duplicate rows.

    df.duplicated().sum()

## 4. Data Types

Before performing data analysis, we need to
identify the data types of the columns.

Data can be classified into two main categories:

1. Numerical Data
2. Categorical Data

### 4.1 Numerical Data

Numerical data consists of values that represent
numbers and can be used for mathematical operations.

Examples:
- Age
- Salary
- Temperature
- Height
- Weight
- Marks

Numerical data can be divided into two types.

#### A. Discrete Data

Discrete data consists of countable values.

Examples:
- Number of students
- Number of employees
- Number of products

#### B. Continuous Data

Continuous data can take any value within a range.

Examples:
- Height
- Weight
- Temperature
- Distance

### 4.2 Categorical Data

Categorical data represents labels, groups,
or categories.

Examples:
- Gender
- Department
- City
- Education
- Product Category

Categorical data can be divided into two types.

#### A. Nominal Data

Nominal data consists of categories that do not
have a specific order.

Examples:
- Gender
- City
- Blood Group
- Department

#### B. Ordinal Data

Ordinal data consists of categories that have
a meaningful order.

Examples:
- Low, Medium, High
- Poor, Average, Good
- Beginner, Intermediate, Advanced

## 5. Identifying Numerical and Categorical Columns

We can use Pandas to identify numerical and
categorical columns automatically.

### Numerical Columns

    numerical_cols = df.select_dtypes(
        include=["number"]
    ).columns

### Categorical Columns

    categorical_cols = df.select_dtypes(
        include=["object", "category"]
    ).columns

### Number of Columns

    len(numerical_cols)

    len(categorical_cols)

The number of numerical and categorical columns
depends on the dataset.

Note: Boolean columns and datetime columns may
require separate handling.

## 6. Feature Selection

Feature selection is the process of selecting
relevant features from a dataset for machine
learning.

A feature is an input variable used by a
machine learning model to make predictions.

### Advantages of Feature Selection

1. Reduces unnecessary features.
2. Reduces model complexity.
3. Can improve model performance.
4. Reduces training time.
5. Helps avoid irrelevant information.

### Common Feature Selection Methods

1. Filter Methods
2. Wrapper Methods
3. Embedded Methods

Examples:
- Correlation
- Chi-square test
- Recursive Feature Elimination
- Lasso Regression

Feature selection should be based on the problem
and the relationship between the features and
the target variable.

## 7. Missing Values

Missing values are values that are not available
in a dataset.

In Pandas, missing values are commonly represented
by NaN or None.

### Causes of Missing Values

1. Data entry errors
2. Incomplete surveys
3. Data collection problems
4. Sensor failures
5. Missing information

### Identifying Missing Values

    df.isnull().sum()

This returns the number of missing values
in each column.

### Handling Missing Values

There are different ways to handle missing values.

1. Remove rows containing missing values.
2. Remove columns containing too many missing values.
3. Replace missing numerical values with the mean.
4. Replace missing numerical values with the median.
5. Replace missing categorical values with the mode.

## 8. Imputation

Imputation is the process of replacing missing
values with estimated or appropriate values.

### Numerical Imputation

Numerical missing values can be replaced using
mean or median.

#### Mean Imputation

Mean is the average of all available values.

    df["Age"].fillna(df["Age"].mean())

Mean imputation is generally suitable when
the numerical data has no extreme outliers.

#### Median Imputation

Median is the middle value of the sorted data.

    df["Age"].fillna(df["Age"].median())

Median imputation is useful when the data
contains outliers or is skewed.

### Categorical Imputation

Categorical missing values can be replaced
using the mode.

Mode is the most frequently occurring value.

    df["City"].fillna(df["City"].mode()[0])

The appropriate imputation method depends
on the dataset and the problem.

## 9. Numerical Data Analysis

Numerical data analysis is used to understand
the distribution and statistical properties
of numerical features.

### Important Statistical Measures

#### Mean

The average of all values.

    df["Age"].mean()

#### Median

The middle value of the sorted data.

    df["Age"].median()

#### Mode

The most frequently occurring value.

    df["Age"].mode()

#### Minimum

The smallest value in a column.

    df["Age"].min()

#### Maximum

The largest value in a column.

    df["Age"].max()

#### Standard Deviation

Measures how spread out the values are
from the mean.

    df["Age"].std()

### Describe Function

The describe() function provides a summary
of numerical columns.

    df.describe()

It returns:
- Count
- Mean
- Standard deviation
- Minimum
- 25th percentile
- 50th percentile
- 75th percentile
- Maximum

## 10. Categorical Data Analysis

Categorical data analysis is used to understand
the distribution and frequency of categories.

### Unique Values

The unique() function returns the distinct
values in a column.

    df["Department"].unique()

### Number of Unique Values

The nunique() function returns the number
of distinct values.

    df["Department"].nunique()

### Value Counts

The value_counts() function returns the
frequency of each category.

    df["Department"].value_counts()

These functions help us understand the
distribution of categorical features.

## 11. Data Visualization

Data visualization represents data using
graphs and charts.

It helps identify patterns, trends,
distributions, and outliers.

Common visualization techniques include:

1. Histogram
2. Bar Chart
3. Box Plot
4. Scatter Plot
5. Heatmap

### Histogram

A histogram is used to visualize the
distribution of numerical data.

It divides numerical values into intervals
called bins and displays the frequency
of values in each interval.

A histogram helps us understand:
- Data distribution
- Concentration of values
- Skewness
- Possible outliers

Example using Matplotlib:

    import matplotlib.pyplot as plt

    df["Age"].hist(bins=10)

    plt.xlabel("Age")
    plt.ylabel("Frequency")
    plt.title("Age Distribution")
    plt.show()

## 12. Hypothesis

A hypothesis is a statement or assumption
that can be tested using data.

In data analysis, hypotheses help us
investigate possible relationships between
variables.

Example 1:
Students who study for more hours may
score higher marks.

Example 2:
Employees with more experience may
receive higher salaries.

A hypothesis should be tested using
appropriate statistical methods and data.
