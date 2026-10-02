# AIML LEARNING JOURNEY - DAY 33

## Missing Values, Imputation, Preprocessing Pipeline, MLflow and DagsHub


# 1. TODAY'S TOPICS

Today I learned:

- Missing Values
- Checking Missing Values
- `isna()`
- `isna().sum()`
- Dropping Missing Values using `dropna()`
- Imputation
- SimpleImputer
- Mean Imputation
- Median Imputation
- Most Frequent / Mode Imputation
- Constant Imputation
- KNNImputer
- Numerical Missing Values
- Categorical Missing Values
- Nominal Categorical Variables
- Ordinal Categorical Variables
- OneHotEncoder
- OrdinalEncoder
- MinMaxScaler
- ColumnTransformer
- Pipeline
- Train-Test Split
- Preprocessing Pipeline
- Overfitting
- PowerTransformer
- RandomForestRegressor
- MAE
- R² Score
- MLflow
- DagsHub
- Experiment Tracking
- Comparing Drop vs Impute Missing Values

---

# 2. MISSING VALUES

Missing values are values that are not available, not recorded, or lost from a dataset.

Missing values can appear as:

- NaN
- None
- NULL

Example:

    Age    Salary
    22     30000
    25     NaN
    30     45000
    NaN    50000

Here, `NaN` represents a missing value.

---

# 3. WHY DO MISSING VALUES OCCUR?

Missing values can occur because:

- User did not provide the information.
- Data was not collected.
- There was an error during data collection.
- The value was not applicable.
- Data was lost during processing.
- Data was collected from different sources with incomplete information.

Example 1:

A customer may not provide their age.

Example 2:

A delivery record may not contain weather information.

---

# 4. WHY DO WE NEED TO HANDLE MISSING VALUES?

Many Machine Learning algorithms cannot directly work with missing values.

Therefore, missing values usually need to be handled before training the model.

There are two major approaches:

1. Drop missing values
2. Impute missing values

Flow:

    Missing Values
          |
    ----------------
    |              |
    Drop          Impute
    |              |
    dropna()   SimpleImputer
               KNNImputer

---

# 5. CHECKING MISSING VALUES

Pandas provides `isna()` to identify missing values.

    df.isna()

It returns:

- `True` when the value is missing.
- `False` when the value is present.

Example:

    Age
    22       False
    25       True
    30       False

---

# 6. COUNT MISSING VALUES IN EACH COLUMN

We can use:

    df.isna().sum()

Example:

    print(df.isna().sum())

Possible output:

    age                    10
    ratings                 5
    weather                20
    traffic                 8
    distance                0

This tells us how many missing values are present in each column.

---

# 7. FIND TOTAL MISSING VALUES

We can calculate the total number of missing values in the complete dataset:

    df.isna().sum().sum()

Explanation:

    df.isna()
        ↓
    Finds missing values

    sum()
        ↓
    Counts missing values in each column

    sum()
        ↓
    Calculates total missing values

---

# 8. MISSING VALUE PERCENTAGE

We can calculate the percentage of missing values in each column:

    (df.isna().sum() / len(df)) * 100

Example:

    age          2.5%
    ratings      1.2%
    weather      4.8%
    distance     0.0%

This helps us understand how much data is missing from each column.

---

# 9. HANDLING MISSING VALUES

There are two major approaches:

    1. Drop Missing Values
    2. Impute Missing Values

---

# 10. DROPPING MISSING VALUES

We can remove rows containing missing values using:

    df.dropna()

Example:

    df = df.dropna()

This removes rows containing missing values.

---

# 11. EXAMPLE OF DROPPING MISSING VALUES

Before:

    Age    Salary
    22     30000
    25     NaN
    30     45000
    35     NaN

After:

    Age    Salary
    22     30000
    30     45000

Rows containing missing values are removed.

---

# 12. ADVANTAGES OF DROPPING MISSING VALUES

Advantages:

- Simple to implement.
- No estimated values are introduced.
- Dataset becomes complete.

Example:

    df = df.dropna()

---

# 13. DISADVANTAGES OF DROPPING MISSING VALUES

The main disadvantage is data loss.

Example:

    Original rows = 10,000
    Rows with missing values = 2,000
    Remaining rows = 8,000

We lose 2,000 observations.

Therefore, we should not blindly use `dropna()`.

---

# 14. IMPUTATION

Imputation means replacing missing values with suitable values instead of deleting the row.

Example:

Before:

    Age
    22
    25
    NaN
    30

After:

    Age
    22
    25
    26
    30

The missing value has been replaced with an estimated value.

---

# 15. SIMPLEIMPUTER

`SimpleImputer` is provided by Scikit-learn.

Import:

    from sklearn.impute import SimpleImputer

Basic syntax:

    SimpleImputer(strategy="mean")

---

# 16. MEAN IMPUTATION

Mean imputation replaces missing numerical values with the mean of the available values.

Example:

    10
    20
    NaN
    30

Mean:

    (10 + 20 + 30) / 3 = 20

After imputation:

    10
    20
    20
    30

Code:

    imputer = SimpleImputer(strategy="mean")

Mean imputation can be used for numerical data when the mean is an appropriate representation of the feature.

---

# 17. MEDIAN IMPUTATION

Median imputation replaces missing values with the median.

Code:

    imputer = SimpleImputer(strategy="median")

Example:

    10
    20
    30
    40
    NaN

Median:

    30

After imputation:

    10
    20
    30
    40
    30

Median can be useful when numerical data contains outliers because the median is less affected by extreme values than the mean.

---

# 18. MODE / MOST FREQUENT IMPUTATION

For categorical variables, the most frequent value can be used.

Code:

    SimpleImputer(strategy="most_frequent")

Example:

    Weather
    Sunny
    Rainy
    Sunny
    NaN
    Sunny

Most frequent value:

    Sunny

After imputation:

    Weather
    Sunny
    Rainy
    Sunny
    Sunny
    Sunny

---

# 19. CONSTANT IMPUTATION

We can replace missing values with a fixed value.

Example:

    SimpleImputer(
        strategy="constant",
        fill_value="missing"
    )

Before:

    Weather
    Sunny
    NaN
    Rainy

After:

    Weather
    Sunny
    missing
    Rainy

This preserves the information that the original value was missing.

---

# 20. CHOOSING AN IMPUTATION STRATEGY

Different columns can use different strategies.

Numerical columns:

- Mean
- Median
- KNN

Categorical columns:

- Most Frequent
- Constant

The correct strategy depends on:

- Dataset
- Feature distribution
- Amount of missing data
- Type of feature
- Model performance
- Domain requirements

---

# 21. KNN IMPUTER

KNN stands for:

    K - Nearest Neighbors

`KNNImputer` estimates missing values using nearby observations.

Import:

    from sklearn.impute import KNNImputer

Example:

    knn_imputer = KNNImputer(n_neighbors=5)

Here:

    n_neighbors = 5

means the algorithm considers 5 nearest observations when estimating missing values.

---

# 22. HOW KNN IMPUTATION WORKS

Suppose one observation has a missing value.

KNN looks for similar observations based on available feature values.

The nearby observations are then used to estimate the missing value.

Flow:

    Missing Observation
            ↓
    Find Similar Observations
            ↓
    Find K Nearest Neighbors
            ↓
    Use Neighbor Information
            ↓
    Estimate Missing Value

---

# 23. IMPORTANT POINT ABOUT KNN IMPUTER

KNN-based imputation works with numerical representations.

Categorical features generally need to be appropriately encoded before applying techniques that require numerical values.

In today's faculty program, categorical variables are processed before `KNNImputer`.

---

# 24. CATEGORICAL VARIABLES

Categorical variables contain categories rather than continuous numerical values.

Examples:

    Weather:
    Sunny
    Rainy
    Cloudy

    Vehicle:
    Bike
    Scooter
    Car

    Traffic:
    Low
    Medium
    High
    Jam

---

# 25. NOMINAL AND ORDINAL VARIABLES

Categorical variables can be divided into:

    1. Nominal
    2. Ordinal

## NOMINAL VARIABLES

There is no natural order.

Example:

    Weather:
    Sunny
    Rainy
    Cloudy

Another example:

    Type of Vehicle:
    Bike
    Car
    Scooter

## ORDINAL VARIABLES

There is a meaningful order.

Example:

    Traffic:
    Low
    Medium
    High
    Jam

Another example:

    Distance:
    Short
    Medium
    Long
    Very Long

---

# 26. ONEHOTENCODER

One-Hot Encoding can be used for nominal categorical variables.

Import:

    from sklearn.preprocessing import OneHotEncoder

Example:

    OneHotEncoder(
        drop="first",
        handle_unknown="ignore",
        sparse_output=False
    )

It converts categories into separate binary/numerical columns.

Example:

    Weather

    Sunny
    Rainy
    Cloudy

can be converted into separate binary columns.

---

# 27. ORDINALENCODER

`OrdinalEncoder` can be used for ordinal categorical variables.

Import:

    from sklearn.preprocessing import OrdinalEncoder

Example:

    OrdinalEncoder(
        categories=[
            ["low", "medium", "high", "jam"]
        ]
    )

This allows us to specify the order of categories.

---

# 28. MINMAXSCALER

Numerical features can have different ranges.

Example:

    Age:
    18 - 60

    Distance:
    1 - 50

    Pickup Time:
    5 - 60

Scaling can bring numerical features into a comparable range.

Import:

    from sklearn.preprocessing import MinMaxScaler

Example:

    MinMaxScaler()

---

# 29. COLUMNTRANSFORMER

Different columns may require different preprocessing.

For example:

    Numerical Columns
          ↓
       Scaling

    Categorical Columns
          ↓
       Encoding

`ColumnTransformer` allows us to apply different transformations to different groups of columns.

Import:

    from sklearn.compose import ColumnTransformer

Example:

    preprocessor = ColumnTransformer(
        transformers=[
            (
                "numeric",
                MinMaxScaler(),
                numerical_columns
            ),
            (
                "categorical",
                OneHotEncoder(),
                categorical_columns
            )
        ]
    )

---

# 30. PIPELINE

A Pipeline combines multiple Machine Learning preprocessing and model steps into a sequence.

Import:

    from sklearn.pipeline import Pipeline

Example:

    pipeline = Pipeline(
        steps=[
            (
                "imputer",
                SimpleImputer(strategy="median")
            ),
            (
                "scaler",
                MinMaxScaler()
            )
        ]
    )

The data passes through the steps in order.

---

# 31. PIPELINE FLOW

A typical Machine Learning pipeline:

    Raw Data
        ↓
    Missing Value Handling
        ↓
    Encoding
        ↓
    Scaling
        ↓
    Model
        ↓
    Prediction

---

# 32. NUMERICAL PIPELINE

Example:

    numeric_pipeline = Pipeline(
        steps=[
            (
                "imputer",
                SimpleImputer(strategy="median")
            ),
            (
                "scaler",
                MinMaxScaler()
            )
        ]
    )

Flow:

    Numerical Data
          ↓
    Median Imputation
          ↓
    MinMax Scaling

---

# 33. CATEGORICAL PIPELINE

Example:

    categorical_pipeline = Pipeline(
        steps=[
            (
                "imputer",
                SimpleImputer(strategy="most_frequent")
            ),
            (
                "encoder",
                OneHotEncoder(handle_unknown="ignore")
            )
        ]
    )

Flow:

    Categorical Data
          ↓
    Most Frequent Imputation
          ↓
    One-Hot Encoding

---

# 34. COMBINING PIPELINES

Numerical and categorical pipelines can be combined using `ColumnTransformer`.

Example:

    preprocessor = ColumnTransformer(
        transformers=[
            (
                "numeric",
                numeric_pipeline,
                numeric_columns
            ),
            (
                "categorical",
                categorical_pipeline,
                categorical_columns
            )
        ]
    )

---

# 35. COMPLETE PROCESSING FLOW

                         Raw Dataset
                              ↓
                      Identify Columns
                              ↓
                 ┌────────────┴────────────┐
                 ↓                         ↓
            Numerical                 Categorical
                 ↓                         ↓
            Imputation                Imputation
                 ↓                         ↓
              Scaling                  Encoding
                 └────────────┬────────────┘
                              ↓
                     Processed Dataset
                              ↓
                            Model
                              ↓
                         Prediction

---

# 36. TRAIN AND TEST DATASET

A dataset is commonly divided into:

    Training Data
    Testing Data

Training data is used to train the model.

Testing data is used to evaluate the model on unseen data.

Example:

    from sklearn.model_selection import train_test_split

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )

Here:

    80% → Training Data
    20% → Testing Data

---

# 37. IMPORTANT RULE ABOUT PREPROCESSING

Preprocessing should be learned from the training data and then applied to the test data.

Correct approach:

    imputer.fit(X_train)

    X_train = imputer.transform(X_train)

    X_test = imputer.transform(X_test)

We should not independently calculate preprocessing values using the test dataset.

A Pipeline helps maintain this workflow correctly.

---

# 38. DATA LEAKAGE

Data leakage occurs when information from outside the training data improperly influences the model during training.

Example:

If we calculate the mean for imputation using both training and test data before splitting, information from the test set has entered the training process.

Correct approach:

    Split Data
        ↓
    Fit preprocessing on Training Data
        ↓
    Transform Training Data
        ↓
    Transform Test Data

Using a Pipeline helps prevent this type of preprocessing mistake.

---

# 39. OVERFITTING

Overfitting occurs when a model performs very well on training data but performs significantly worse on unseen test data.

Example 1:

    Train R² = 0.99
    Test R²  = 0.60

Example 2:

    Train MAE = 2 minutes
    Test MAE  = 10 minutes

A large difference between training and testing performance can indicate overfitting.

---

# 40. TRAIN VS TEST PERFORMANCE

For a regression model:

## MAE

Lower MAE generally indicates smaller prediction errors.

Example:

    Train MAE = 3
    Test MAE  = 5

## R²

Higher R² generally indicates that the model explains more variation in the target.

Example:

    Train R² = 0.90
    Test R²  = 0.82

---

# 41. DO NOT JUDGE OVERFITTING FROM ONE NUMBER

We should not say that a model is overfitting simply because the test score is low.

We should compare:

    Training Performance
            vs
    Testing Performance

A large difference between training and test performance is important evidence of possible overfitting.

Other problems such as:

- Poor data quality
- Distribution differences
- Preprocessing issues
- Underfitting

can also result in poor test performance.

---

# 42. POWERTRANSFORMER

In today's Swiggy delivery-time experiment, `PowerTransformer` was used on the target variable.

Import:

    from sklearn.preprocessing import PowerTransformer

Example:

    pt = PowerTransformer()

    y_train_transformed = pt.fit_transform(
        y_train.values.reshape(-1, 1)
    )

After prediction, the transformed values can be converted back:

    y_pred_original = pt.inverse_transform(
        y_pred.reshape(-1, 1)
    )

---

# 43. RANDOMFORESTREGRESSOR

The model used in today's experiment is:

    RandomForestRegressor()

Import:

    from sklearn.ensemble import RandomForestRegressor

Random Forest is an ensemble Machine Learning algorithm that combines multiple decision trees.

It can be used for regression problems.

---

# 44. MEAN ABSOLUTE ERROR

MAE stands for Mean Absolute Error.

It measures the average absolute difference between actual and predicted values.

Import:

    from sklearn.metrics import mean_absolute_error

Example:

    mae = mean_absolute_error(
        y_test,
        y_pred
    )

Lower MAE generally indicates smaller prediction errors.

For delivery time:

    MAE = 5

means the predictions are off by about 5 minutes on average in absolute terms.

---

# 45. R² SCORE

R² is a regression evaluation metric.

Import:

    from sklearn.metrics import r2_score

Example:

    r2 = r2_score(
        y_test,
        y_pred
    )

Higher R² generally indicates that the model explains more variation in the target, although interpretation depends on the dataset and problem.

---

# 46. TODAY'S MAIN EXPERIMENT

Today we compared two approaches for handling missing values:

    Experiment 1
    Drop Missing Values

    Experiment 2
    Impute Missing Values

The purpose is to compare how these approaches affect Machine Learning model performance.

---

# 47. EXPERIMENT 1 - DROP MISSING VALUES

First, a copy of the dataset is created:

    temp_df_drop = df.copy()

Then rows containing missing values are removed:

    temp_df_drop = df.copy().dropna()

Features and target are separated:

    X_drop = temp_df_drop.drop(
        columns="time_taken"
    )

    y_drop = temp_df_drop["time_taken"]

Then the data is divided into training and testing sets.

---

# 48. EXPERIMENT 1 FLOW

    Original Dataset
           ↓
    Remove Unwanted Columns
           ↓
    Drop Missing Rows
           ↓
    Train/Test Split
           ↓
    Power Transform Target
           ↓
    Scale Numerical Columns
           ↓
    Encode Categorical Columns
           ↓
    Random Forest
           ↓
    Prediction
           ↓
    MAE + R²
           ↓
    MLflow

---

# 49. EXPERIMENT 2 - IMPUTE MISSING VALUES

In Experiment 2, rows containing missing values are not removed.

Instead, missing values are handled through imputation.

The process uses:

    SimpleImputer
          +
    Preprocessing
          +
    KNNImputer
          +
    Random Forest

---

# 50. SIMPLE IMPUTATION IN EXPERIMENT 2

Some categorical columns use the most frequent value:

    SimpleImputer(
        strategy="most_frequent"
    )

Other categorical columns use a constant:

    SimpleImputer(
        strategy="constant",
        fill_value="missing"
    )

---

# 51. KNN IMPUTATION IN EXPERIMENT 2

The experiment also uses:

    KNNImputer(
        n_neighbors=5
    )

This estimates missing values using information from nearby observations in the processed numerical feature space.

---

# 52. PROCESSING PIPELINE USED IN EXPERIMENT 2

The processing pipeline is:

    processing_pipeline = Pipeline(
        steps=[
            (
                "simple_imputer",
                simple_imputer
            ),
            (
                "preprocess",
                preprocessor_imp
            ),
            (
                "knn_imputer",
                knn_imputer
            )
        ]
    )

The data passes through multiple processing stages.

---

# 53. COMPLETE MODEL PIPELINE

The processing pipeline is combined with the Random Forest model:

    model_pipe = Pipeline(
        steps=[
            (
                "preprocessing",
                processing_pipeline
            ),
            (
                "model",
                rf_imp
            )
        ]
    )

Complete flow:

    Input Data
         ↓
    Simple Imputer
         ↓
    Preprocessing
         ↓
    KNN Imputer
         ↓
    Random Forest
         ↓
    Prediction

---

# 54. WHY USE A PIPELINE?

Advantages of using a Pipeline:

1. Organizes preprocessing steps.
2. Keeps preprocessing and model steps together.
3. Reduces preprocessing mistakes.
4. Applies the same transformations consistently.
5. Makes training and prediction easier.
6. Helps avoid data leakage when preprocessing is properly fitted within the training workflow.

Example:

    model_pipe.fit(
        X_train,
        y_train
    )

Then:

    model_pipe.predict(
        X_test
    )

---

# 55. MLFLOW

MLflow is used for Machine Learning experiment tracking.

It can record:

- Parameters
- Metrics
- Experiment runs
- Model information

Import:

    import mlflow

Set an experiment:

    mlflow.set_experiment(
        "Exp 1 - Keep Vs Drop Missing Values"
    )

---

# 56. MLFLOW RUN

An MLflow run can be created using:

    with mlflow.start_run():
        ...

Example:

    with mlflow.start_run(
        run_name="Drop Missing Values"
    ):

        mlflow.log_param(
            "experiment_type",
            "Drop Missing Values"
        )

        mlflow.log_metric(
            "test_error",
            test_mae
        )

---

# 57. PARAMETERS VS METRICS

## PARAMETERS

Parameters are settings used by the model.

Examples:

- n_estimators
- max_depth
- random_state

They can be logged using:

    mlflow.log_param()

## METRICS

Metrics measure model performance.

Examples:

- MAE
- R²

They can be logged using:

    mlflow.log_metric()

---

# 58. DAGSHUB

DagsHub can be integrated with MLflow for Machine Learning project and experiment tracking.

Example:

    import dagshub

    dagshub.init(
        repo_owner="margamacademy26-prog",
        repo_name="swiggy-time-predicition",
        mlflow=True
    )

This connects the experiment tracking workflow with the DagsHub repository.

---

# 59. COMPARING THE TWO EXPERIMENTS

The purpose of the experiment is to compare:

    Drop Missing Values
            VS
    Impute Missing Values

We can compare:

    Training MAE
    Testing MAE
    Training R²
    Testing R²

Example:

                 DROP        IMPUTE

    Train MAE     ...          ...
    Test MAE      ...          ...

    Train R²      ...          ...
    Test R²       ...          ...

The actual values depend on the dataset and model run.

---

# 60. IMPORTANT LEARNING FROM THE EXPERIMENT

## DROPPING MISSING VALUES

    Simple
       ↓
    But may lose useful data

## IMPUTATION

    Preserves rows
       ↓
    But introduces estimated values

The choice should depend on:

- Amount of missing data
- Type of feature
- Feature distribution
- Importance of feature
- Dataset size
- Model performance
- Domain requirements

---

# 61. SWIGGY DATASET COLUMNS USED

The faculty program uses the following numerical columns:

    num_cols = [
        "age",
        "ratings",
        "pickup_time_minutes",
        "distance"
    ]

Nominal categorical columns:

    nominal_cat_cols = [
        "weather",
        "type_of_order",
        "type_of_vehicle",
        "festival",
        "city_type",
        "is_weekend",
        "order_time_of_day"
    ]

Ordinal categorical columns:

    ordinal_cat_cols = [
        "traffic",
        "distance_type"
    ]

Traffic order:

    traffic_order = [
        "low",
        "medium",
        "high",
        "jam"
    ]

Distance type order:

    distance_type_order = [
        "short",
        "medium",
        "long",
        "very_long"
    ]

---

# 62. COLUMNS REMOVED IN THE EXPERIMENT

The faculty program removes these columns:

    columns_to_drop = [
        "rider_id",
        "restaurant_latitude",
        "restaurant_longitude",
        "delivery_latitude",
        "delivery_longitude",
        "order_date",
        "order_time_hour",
        "order_day",
        "city_name",
        "order_day_of_week",
        "order_month"
    ]

These columns were removed before the main preprocessing and modeling experiment.

---

# 63. IMPORTANT PYTHON IMPORTS

    import numpy as np
    import pandas as pd

    import dagshub
    import mlflow

    from sklearn.pipeline import Pipeline
    from sklearn.compose import ColumnTransformer

    from sklearn.impute import SimpleImputer
    from sklearn.impute import KNNImputer

    from sklearn.preprocessing import (
        OneHotEncoder,
        MinMaxScaler,
        OrdinalEncoder,
        PowerTransformer
    )

    from sklearn.model_selection import train_test_split

    from sklearn.ensemble import RandomForestRegressor

    from sklearn.metrics import (
        mean_absolute_error,
        r2_score
    )

---

# 64. IMPORTANT SYNTAX TO REMEMBER

## Check missing values

    df.isna().sum()

## Total missing values

    df.isna().sum().sum()

## Drop missing rows

    df.dropna()

## Mean imputation

    SimpleImputer(
        strategy="mean"
    )

## Median imputation

    SimpleImputer(
        strategy="median"
    )

## Mode / Most Frequent imputation

    SimpleImputer(
        strategy="most_frequent"
    )

## Constant imputation

    SimpleImputer(
        strategy="constant",
        fill_value="missing"
    )

## KNN imputation

    KNNImputer(
        n_neighbors=5
    )

## Pipeline

    Pipeline(
        steps=[
            ("step1", transformer1),
            ("step2", transformer2)
        ]
    )

## ColumnTransformer

    ColumnTransformer(
        transformers=[
            (
                "name",
                transformer,
                columns
            )
        ]
    )

---

# 65. FACULTY PROGRAM - MAIN CONCEPT

The complete faculty experiment follows this general structure:

    Load Dataset
          ↓
    Remove Unwanted Columns
          ↓
    Identify Numerical Columns
          ↓
    Identify Nominal Columns
          ↓
    Identify Ordinal Columns
          ↓
    Experiment 1
    Drop Missing Values
          ↓
    Preprocess Data
          ↓
    Train Random Forest
          ↓
    Evaluate Model
          ↓
    Log Results to MLflow
          ↓
    Experiment 2
    Impute Missing Values
          ↓
    Build Processing Pipeline
          ↓
    KNN Imputation
          ↓
    Train Random Forest
          ↓
    Evaluate Model
          ↓
    Log Results to MLflow
          ↓
    Compare Experiments

---

# 66. INTERVIEW QUESTIONS

## Q1. What are missing values?

Missing values are values that are unavailable or not recorded in a dataset.

## Q2. How do you check missing values in Pandas?

    df.isna().sum()

## Q3. How do you find the total number of missing values?

    df.isna().sum().sum()

## Q4. How do you remove rows containing missing values?

    df.dropna()

## Q5. What is imputation?

Imputation is the process of replacing missing values with suitable values.

## Q6. What is SimpleImputer?

`SimpleImputer` is a Scikit-learn transformer used to replace missing values using strategies such as mean, median, most frequent, or constant.

## Q7. When can mode imputation be used?

Mode or most-frequent imputation can be used for categorical variables.

## Q8. What is KNNImputer?

KNNImputer estimates missing values using information from nearby observations.

## Q9. What is a Pipeline?

A Pipeline combines multiple preprocessing and/or model steps into a sequential workflow.

## Q10. What is ColumnTransformer?

ColumnTransformer allows different transformations to be applied to different groups of columns.

## Q11. What is overfitting?

Overfitting occurs when a model performs very well on training data but performs significantly worse on unseen data.

## Q12. What is MAE?

Mean Absolute Error measures the average absolute difference between actual and predicted values.

## Q13. What is R²?

R² is a regression metric that indicates how much variation in the target is explained by the model.

## Q14. Why do we compare train and test performance?

To understand how well the model generalizes to unseen data and to identify possible overfitting.

## Q15. Why not always use `dropna()`?

Because dropping rows can result in significant data loss.

## Q16. Why use MLflow?

MLflow helps track and compare Machine Learning experiments, parameters, and metrics.

## Q17. What is the difference between nominal and ordinal data?

Nominal data has categories without a natural order, while ordinal data has categories with a meaningful order.

## Q18. Why is OneHotEncoder used?

OneHotEncoder converts categorical values into numerical binary features and is commonly used for nominal categorical variables.

## Q19. Why is OrdinalEncoder used?

OrdinalEncoder converts ordered categorical values into numerical representations while allowing the category order to be specified.

## Q20. Why do we use a Pipeline?

A Pipeline combines preprocessing and model steps into one workflow and helps ensure consistent transformations between training and prediction.

---

# 67. DAY 33 QUICK REVISION

                    Missing Values
                          ↓
                   isna().sum()
                          ↓
                Understand Missing Data
                          ↓
                Choose Handling Method
                          ↓
             ┌────────────┴────────────┐
             ↓                         ↓
           Drop                     Impute
             ↓                         ↓
          dropna()              SimpleImputer
                                KNNImputer
             ↓                         ↓
             └────────────┬────────────┘
                          ↓
                    Preprocessing
                          ↓
                  ColumnTransformer
                          ↓
                       Pipeline
                          ↓
                        Model
                          ↓
                     Prediction
                          ↓
                    MAE and R²
                          ↓
                 Train vs Test Check
                          ↓
                  MLflow / DagsHub

---

# 68. FINAL SUMMARY

Today I learned how to identify and handle missing values in Machine Learning datasets.

The two major approaches are:

    Drop
    Impute

I learned how to:

    Check missing values
            ↓
    Choose a handling strategy
            ↓
    Apply dropping or imputation
            ↓
    Preprocess numerical features
            ↓
    Preprocess categorical features
            ↓
    Build a Pipeline
            ↓
    Train a Random Forest model
            ↓
    Evaluate using MAE and R²
            ↓
    Compare train and test performance
            ↓
    Identify possible overfitting
            ↓
    Track experiments using MLflow/DagsHub

The main practical experiment was:

    Experiment 1
    Drop Missing Values

    Experiment 2
    Impute Missing Values

The goal was to understand how different missing-value handling strategies can affect Machine Learning model performance.

---

# 69  KEYWORDS

    Missing Values
    NaN
    isna()
    isna().sum()
    dropna()
    Imputation
    SimpleImputer
    Mean
    Median
    Mode
    Most Frequent
    Constant
    KNNImputer
    KNN
    Nominal
    Ordinal
    OneHotEncoder
    OrdinalEncoder
    MinMaxScaler
    ColumnTransformer
    Pipeline
    Train-Test Split
    Data Leakage
    Overfitting
    PowerTransformer
    RandomForestRegressor
    MAE
    R²
    MLflow
    DagsHub
    Experiment Tracking
    Drop Missing Values
    Impute Missing Values
