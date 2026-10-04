# Day 35 - Swiggy Time Prediction

## Topic

Today I learned about **Swiggy Time Prediction**, which is a supervised Machine Learning regression problem.

The main objective is to predict the food delivery time based on different input features.

Example:

Input:
- Distance
- Weather
- Traffic
- Delivery information

Output:

Predicted Delivery Time = 35 minutes


# 1. Machine Learning Project Workflow

The general Machine Learning workflow is:

Dataset
↓
Data Exploration
↓
Data Cleaning
↓
EDA
↓
Feature Preparation
↓
Train/Test Split
↓
Model Training
↓
Model Evaluation
↓
Model Selection
↓
Hyperparameter Tuning
↓
Final Model
↓
Model Saving
↓
Deployment


# 2. Data Exploration

Data exploration means understanding the dataset before building the Machine Learning model.

We check:

- Number of rows
- Number of columns
- Column names
- Data types
- Missing values
- Duplicate values
- Unique values
- Statistical summary
- Target column
- Relationships between features

## Pandas

```python
import pandas as pd

df = pd.read_csv("swiggy.csv")

print(df.head())
print(df.shape)
print(df.columns)
print(df.info())
print(df.describe())
print(df.isnull().sum())
print(df.nunique())
```


# 3. Data Cleaning

Raw datasets may contain different problems.

Common problems are:

- Missing values
- Incorrect data types
- Duplicate rows
- Incorrect values
- Outliers
- Inconsistent categories
- Invalid values

Data cleaning prepares the dataset for Machine Learning.


# 4. Handling Null Values

Null values are missing values.

Two common approaches are:

1. Drop
2. Impute


## 4.1 Dropping Null Values

Rows containing missing values can be removed.

```python
df = df.dropna()
```

Advantages:

- Simple
- Fast

Disadvantage:

If many rows contain missing values, dropping them can result in significant data loss.

Example 1:

If a dataset has 100000 rows and only 100 missing rows, dropping them may be acceptable.

Example 2:

If a dataset has 100000 rows and 40000 missing rows, dropping them would result in huge data loss.


# 5. Imputation

Instead of deleting missing values, we can replace them.

For numerical columns, median can be used:

```python
df["column"] = df["column"].fillna(
    df["column"].median()
)
```

For categorical columns, mode can be used:

```python
df["column"] = df["column"].fillna(
    df["column"].mode()[0]
)
```


# 6. Data Types

Common data types include:

- int
- float
- object
- string
- boolean
- datetime

Check data types:

```python
print(df.dtypes)
```

Machine Learning models generally require input data to be converted into suitable numerical formats.


# 7. Value Correction

Datasets can contain incorrect or inconsistent values.

Example:

```text
Hyderabad
hyderabad
HYDERABAD
```

These represent the same city but are written differently.

They can be standardized:

```python
df["city"] = df["city"].str.lower().str.strip()
```

Another example:

```text
30 min
30 minutes
30
```

These values may need to be converted into a consistent format.


# 8. Duplicate Values

Duplicate rows can affect Machine Learning training.

Check duplicates:

```python
print(df.duplicated().sum())
```

Remove duplicates:

```python
df = df.drop_duplicates()
```


# 9. EDA

EDA stands for:

**Exploratory Data Analysis**

EDA is used to understand:

- Data distribution
- Patterns
- Relationships
- Outliers
- Trends
- Feature behavior

Three important types of analysis are:

1. Univariate Analysis
2. Bivariate Analysis
3. Multivariate Analysis


# 10. Univariate Analysis

Univariate analysis studies one variable at a time.

Example:

Analyzing delivery time:

```python
print(df["Time_taken(min)"].describe())
```

We can use:

- Histogram
- Box plot
- Bar chart

Questions we can answer:

- What is the average delivery time?
- What is the minimum delivery time?
- What is the maximum delivery time?
- Are there outliers?
- What is the distribution?


# 11. Bivariate Analysis

Bivariate analysis studies the relationship between two variables.

Example 1:

Distance vs Delivery Time

Example 2:

Weather vs Delivery Time

A scatter plot or other suitable visualization can be used to understand relationships between two variables.


# 12. Multivariate Analysis

Multivariate analysis studies relationships between multiple variables.

Example:

Distance
+
Weather
+
Traffic
+
Vehicle Condition
+
Delivery Person Information

may collectively affect:

Delivery Time

Correlation analysis can be used:

```python
print(df.corr(numeric_only=True))
```


# 13. Hypothesis Testing

Hypothesis testing is a statistical method used to determine whether there is sufficient evidence for a relationship or difference.

There are two main hypotheses:

## Null Hypothesis - H0

The null hypothesis generally states that there is no significant effect or difference.

## Alternative Hypothesis - H1

The alternative hypothesis states that there is a significant effect or difference.


## Example 1

Question:

Does weather affect delivery time?

H0:

Weather has no significant effect on delivery time.

H1:

Weather has a significant effect on delivery time.


## Example 2

Question:

Does distance affect delivery time?

H0:

Distance has no significant relationship with delivery time.

H1:

Distance has a significant relationship with delivery time.


# 14. P-Value

The p-value is used in hypothesis testing.

A commonly used significance level is:

α = 0.05

General interpretation:

If:

p-value < 0.05

Reject H0.

If:

p-value >= 0.05

Fail to reject H0.

The exact statistical test depends on the problem and data.


# 15. Regression

Regression is used when the target/output is numerical.

In this project:

Input Features
↓
Regression Model
↓
Delivery Time

Example:

Distance = 5 km
Weather = Clear
Traffic = High

The model might predict:

35 minutes


# 16. LGBM Regressor

LGBM stands for:

**Light Gradient Boosting Machine**

It is a gradient boosting algorithm based on decision trees.

It is commonly used for tabular Machine Learning problems.

Advantages:

- Fast
- Efficient
- Good performance
- Handles nonlinear relationships
- Suitable for large datasets

Basic example:

```python
from lightgbm import LGBMRegressor

model = LGBMRegressor()

model.fit(
    X_train,
    y_train
)

predictions = model.predict(
    X_test
)
```


# 17. Random Forest Regressor

Random Forest is an ensemble Machine Learning algorithm.

It creates multiple decision trees and combines their predictions.

For regression, predictions from multiple trees are aggregated to produce the final prediction.

Basic example:

```python
from sklearn.ensemble import RandomForestRegressor

model = RandomForestRegressor()

model.fit(
    X_train,
    y_train
)

predictions = model.predict(
    X_test
)
```


# 18. LGBM vs Random Forest

Both models can be useful for tabular regression problems.

## LGBM

Advantages:

- Fast
- Efficient
- Strong performance on tabular data
- Many tuning parameters

## Random Forest

Advantages:

- Easy to understand
- Robust
- Handles nonlinear relationships
- Usually requires less preprocessing

The best model should be selected based on evaluation results.

We should not assume that one model is always better.


# 19. Model Evaluation

Important regression metrics are:

1. MAE
2. MSE
3. RMSE
4. R²


# 20. MAE

MAE stands for:

**Mean Absolute Error**

It represents the average absolute difference between actual and predicted values.

Example:

Actual = 30

Predicted = 32

Error:

|30 - 32| = 2

Lower MAE is generally better.


# 21. MSE

MSE stands for:

**Mean Squared Error**

It calculates the average squared error.

Large errors receive more penalty because the errors are squared.

Formula:

MSE = Average((Actual - Predicted)²)

Lower MSE is better.


# 22. RMSE

RMSE stands for:

**Root Mean Squared Error**

Formula:

RMSE = √MSE

RMSE is in the same unit as the target.

If delivery time is measured in minutes, RMSE is also measured in minutes.

Lower RMSE is better.


# 23. R²

R² represents how well the model explains the variation in the target.

Generally:

Higher R² = Better

However, model selection should not depend only on R².


# 24. Stacking Regressor

Stacking is an ensemble learning technique.

It combines multiple base models and uses another model called a:

**Meta Model**

to make the final prediction.

## Stacking Architecture

Input Data
↓
LGBM
↓
Prediction

Input Data
↓
Random Forest
↓
Prediction

LGBM Prediction + Random Forest Prediction
↓
Meta Model
↓
Final Prediction


# 25. Base Models

The models used as the first-level models are called:

**Base Models**

For this project:

Base Model 1 = LGBM Regressor

Base Model 2 = Random Forest Regressor


# 26. Meta Model

The model that learns from the predictions of the base models is called the:

**Meta Model**

Example:

LGBM prediction = 37

Random Forest prediction = 32

↓
Meta Model
↓
Final prediction = 34

The meta-model learns how to combine the base-model predictions.

It is not necessarily just calculating the average.


# 27. Stacking Regressor Example

```python
from sklearn.ensemble import (
    RandomForestRegressor,
    StackingRegressor
)

from lightgbm import LGBMRegressor


lgbm = LGBMRegressor()

rf = RandomForestRegressor()


estimators = [
    ("lgbm", lgbm),
    ("rf", rf)
]


stacking_model = StackingRegressor(
    estimators=estimators,
    final_estimator=RandomForestRegressor()
)


stacking_model.fit(
    X_train,
    y_train
)


predictions = stacking_model.predict(
    X_test
)
```


# 28. Why Stacking?

Different models can learn different patterns from the same data.

For example:

LGBM may capture certain nonlinear relationships very well.

Random Forest may capture other patterns.

Stacking allows another model to learn how to combine their predictions.


# 29. Optuna

Optuna is a hyperparameter optimization framework.

It is used to search for good hyperparameter values.

Instead of manually testing many combinations, Optuna automatically tries different configurations.

## Optuna Workflow

Define Objective
↓
Optuna Suggests Parameters
↓
Train Model
↓
Evaluate Model
↓
Return Score
↓
Optuna Tries Another Configuration
↓
Best Parameters


# 30. Hyperparameters

Hyperparameters are settings that control how a Machine Learning model is trained.

For Random Forest:

- n_estimators
- max_depth
- min_samples_split
- min_samples_leaf

For LGBM:

- n_estimators
- learning_rate
- num_leaves
- max_depth


# 31. Optuna Example

```python
import optuna

from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error


def objective(trial):

    n_estimators = trial.suggest_int(
        "n_estimators",
        50,
        300
    )

    max_depth = trial.suggest_int(
        "max_depth",
        3,
        20
    )

    model = RandomForestRegressor(
        n_estimators=n_estimators,
        max_depth=max_depth,
        random_state=42
    )

    model.fit(
        X_train,
        y_train
    )

    predictions = model.predict(
        X_test
    )

    rmse = mean_squared_error(
        y_test,
        predictions
    ) ** 0.5

    return rmse


study = optuna.create_study(
    direction="minimize"
)

study.optimize(
    objective,
    n_trials=20
)

print(study.best_params)
print(study.best_value)
```

For RMSE:

Lower RMSE = Better


# 32. Important Understanding About Optuna

Optuna does not automatically choose any Machine Learning model from nothing.

We define:

- Model
- Objective function
- Hyperparameter search space
- Evaluation metric

Optuna then searches for good hyperparameter configurations.


# 33. Model Selection

Suppose we train:

- LGBM
- Random Forest
- Stacking Regressor

We evaluate them using:

- MAE
- MSE
- RMSE
- R²

Example:

Model | RMSE

LGBM = 37

Random Forest = 32

Stacking = 33

In this example, Random Forest has the lowest RMSE.

Therefore, based on RMSE:

Random Forest = Best

But the final model should be selected based on appropriate evaluation metrics and project requirements.


# 34. Model Saving

After selecting the final model, it can be saved.

One common method is using Joblib.

```python
import joblib

joblib.dump(
    model,
    "swiggy_time_model.pkl"
)
```

The saved model can later be loaded:

```python
model = joblib.load(
    "swiggy_time_model.pkl"
)
```

This avoids retraining the model every time it is used.


# 35. Deployment

Deployment means making a trained Machine Learning model available for real-world use.

Basic flow:

Training
↓
Trained Model
↓
Save Model
↓
Backend API
↓
User/Application
↓
Prediction


# 36. FastAPI

FastAPI is a Python framework used for building APIs.

A trained Machine Learning model can be exposed through a FastAPI endpoint.

Example endpoint:

POST /predict

The client sends input data.

The API sends the input to the trained model.

The model returns the prediction.


# 37. FastAPI Prediction Flow

Client
↓
Input Features
↓
FastAPI
↓
Trained Model
↓
Prediction
↓
JSON Response

Example request:

```json
{
    "distance": 5,
    "rating": 4.5
}
```

Example response:

```json
{
    "predicted_time": 34.2
}
```

The actual input fields must match the features used during model training.


# 38. FastAPI Example

```python
from fastapi import FastAPI
from pydantic import BaseModel
import joblib


app = FastAPI(
    title="Swiggy Time Prediction API"
)


model = joblib.load(
    "swiggy_time_model.pkl"
)


class PredictionInput(BaseModel):

    distance: float
    rating: float


@app.get("/")
def home():

    return {
        "message": "Swiggy Time Prediction API is running"
    }


@app.post("/predict")
def predict(data: PredictionInput):

    input_data = [[
        data.distance,
        data.rating
    ]]

    prediction = model.predict(
        input_data
    )

    return {
        "predicted_time": float(
            prediction[0]
        )
    }
```

Important:

The fields distance and rating are only examples.

In a real project, the API input must match the exact features expected by the trained model and its preprocessing pipeline.


# 39. DVC

DVC stands for:

**Data Version Control**

DVC is used for versioning large datasets and Machine Learning artifacts.

Git is mainly used for:

- Source Code
- README
- Configuration
- Small Project Files

DVC can be used for:

- Large Dataset
- Large Model
- Machine Learning Artifacts


# 40. Problem With Large Model Files in Git

Suppose:

model.pkl = 1 GB

If the model is committed directly to Git, the repository becomes very large.

If the model is updated many times, repository history can also become large.

This is inefficient.


# 41. DVC Solution

DVC tracks large files and connects them with remote storage.

Conceptually:

Git Repository
↓
model.pkl.dvc
↓
DVC Storage
↓
Actual Model

DVC stores tracking metadata while the actual large artifact can be stored remotely.


# 42. DVC Remote Storage

DVC can use remote storage such as:

- AWS S3
- Azure Blob Storage
- Google Cloud Storage

Example:

Local Machine
↓
DVC
↓
AWS S3
↓
Large Dataset / Model


# 43. Basic DVC Commands

Initialize DVC:

```bash
dvc init
```

Track a dataset:

```bash
dvc add data/swiggy.csv
```

Add DVC metadata to Git:

```bash
git add data/swiggy.csv.dvc data/.gitignore
```

Commit:

```bash
git commit -m "Track Swiggy dataset with DVC"
```


# 44. AWS S3

AWS S3 stands for:

**Amazon Simple Storage Service**

S3 is an object storage service provided by AWS.

It can store:

- Datasets
- Model files
- Machine Learning artifacts
- Large files

Architecture:

Machine Learning Project
↓
DVC
↓
AWS S3
↓
Large Dataset / Model


# 45. Git vs DVC

## Git

Used mainly for:

- Python files
- README files
- Notes
- Configuration
- Source code
- Small files

## DVC

Used mainly for:

- Large datasets
- Large model files
- ML artifacts
- Data versions


# 46. Complete Project Architecture

Swiggy Dataset
↓
Data Exploration
↓
Data Cleaning
↓
EDA
↓
Feature Preparation
↓
LGBM + Random Forest
↓
Base Model Predictions
↓
Meta Model
↓
Stacking Regressor
↓
Optuna Optimization
↓
Best Model
↓
Save Model
↓
DVC
↓
AWS S3
↓
FastAPI
↓
API Endpoint
↓
Prediction


# 47. Complete Machine Learning Lifecycle

Raw Data
↓
Data Exploration
↓
Data Cleaning
↓
EDA
↓
Feature Engineering
↓
Train/Test Split
↓
Train Multiple Models
↓
Evaluate Models
↓
Select Base Models
↓
Stacking
↓
Meta Model
↓
Hyperparameter Tuning
↓
Best Model
↓
Save Model
↓
DVC
↓
FastAPI
↓
Deployment


# 48. Complete Python Program - Swiggy Regression

```python
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split

from sklearn.ensemble import (
    RandomForestRegressor,
    StackingRegressor
)

from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)

from lightgbm import LGBMRegressor


# Load dataset
df = pd.read_csv("swiggy.csv")


# Display dataset
print(df.head())
print(df.shape)
print(df.info())
print(df.isnull().sum())


# Remove duplicate rows
df = df.drop_duplicates()


# Target column
TARGET_COLUMN = "Time_taken(min)"


# Remove rows where target is missing
df = df.dropna(
    subset=[TARGET_COLUMN]
)


# Separate input and target
X = df.drop(
    columns=[TARGET_COLUMN]
)

y = df[TARGET_COLUMN]


# Convert categorical columns into numerical columns
X = pd.get_dummies(
    X,
    drop_first=True
)


# Fill remaining missing numerical values
X = X.fillna(
    X.median(numeric_only=True)
)


# Train/test split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)


# LGBM model
lgbm = LGBMRegressor(
    n_estimators=200,
    learning_rate=0.05,
    random_state=42
)

lgbm.fit(
    X_train,
    y_train
)

lgbm_prediction = lgbm.predict(
    X_test
)


# Random Forest
rf = RandomForestRegressor(
    n_estimators=200,
    random_state=42,
    n_jobs=-1
)

rf.fit(
    X_train,
    y_train
)

rf_prediction = rf.predict(
    X_test
)


# LGBM Evaluation
print("\nLGBM Results")

print(
    "MAE:",
    mean_absolute_error(
        y_test,
        lgbm_prediction
    )
)

print(
    "RMSE:",
    np.sqrt(
        mean_squared_error(
            y_test,
            lgbm_prediction
        )
    )
)

print(
    "R2:",
    r2_score(
        y_test,
        lgbm_prediction
    )
)


# Random Forest Evaluation
print("\nRandom Forest Results")

print(
    "MAE:",
    mean_absolute_error(
        y_test,
        rf_prediction
    )
)

print(
    "RMSE:",
    np.sqrt(
        mean_squared_error(
            y_test,
            rf_prediction
        )
    )
)

print(
    "R2:",
    r2_score(
        y_test,
        rf_prediction
    )
)


# Stacking model
estimators = [

    (
        "lgbm",
        LGBMRegressor(
            n_estimators=150,
            learning_rate=0.05,
            random_state=42
        )
    ),

    (
        "rf",
        RandomForestRegressor(
            n_estimators=150,
            random_state=42,
            n_jobs=-1
        )
    )
]


stacking_model = StackingRegressor(

    estimators=estimators,

    final_estimator=RandomForestRegressor(
        n_estimators=100,
        random_state=42
    )
)


stacking_model.fit(
    X_train,
    y_train
)


stacking_prediction = stacking_model.predict(
    X_test
)


# Stacking Evaluation
print("\nStacking Results")

print(
    "MAE:",
    mean_absolute_error(
        y_test,
        stacking_prediction
    )
)

print(
    "RMSE:",
    np.sqrt(
        mean_squared_error(
            y_test,
            stacking_prediction
        )
    )
)

print(
    "R2:",
    r2_score(
        y_test,
        stacking_prediction
    )
)


print("\nProgram completed.")
```


# 49. Key Learnings of Day 35

Today I learned:

1. Data Exploration
2. Data Cleaning
3. Handling Null Values
4. Value Correction
5. Duplicate Removal
6. Univariate Analysis
7. Bivariate Analysis
8. Multivariate Analysis
9. Hypothesis Testing
10. Regression
11. LGBM Regressor
12. Random Forest Regressor
13. Model Evaluation
14. MAE
15. MSE
16. RMSE
17. R²
18. Stacking Regressor
19. Base Models
20. Meta Model
21. Optuna
22. Hyperparameter Tuning
23. Model Selection
24. Model Saving
25. FastAPI
26. DVC
27. AWS S3
28. Model Deployment


# 50. Important Interview Questions

## What is Regression?

Regression is a supervised Machine Learning technique used to predict continuous numerical values.


## What is LGBM?

LGBM is a gradient boosting framework based on decision trees and is commonly used for efficient tabular Machine Learning.


## What is Random Forest?

Random Forest is an ensemble algorithm that combines predictions from multiple decision trees.


## What is Stacking?

Stacking is an ensemble technique where predictions from multiple base models are given to a meta-model to produce the final prediction.


## What is a Base Model?

A base model is a first-level model that produces predictions used by the meta-model.


## What is a Meta Model?

A meta-model learns from the predictions generated by the base models and produces the final prediction.


## What is Optuna?

Optuna is a hyperparameter optimization framework that automatically searches for good hyperparameter configurations.


## What is FastAPI?

FastAPI is a Python framework used to build APIs and can be used to expose a trained Machine Learning model for prediction.


## What is DVC?

DVC stands for Data Version Control and is used to version and manage large datasets and Machine Learning artifacts.


## What is AWS S3?

AWS S3 is an object storage service that can be used to store datasets, models, and other large Machine Learning artifacts.


# Day 35 Final Summary

Today I learned how to build an end-to-end Machine Learning regression workflow using a Swiggy delivery-time prediction problem.

The complete workflow is:

Data Exploration
↓
Data Cleaning
↓
EDA
↓
Feature Preparation
↓
Model Training
↓
Model Evaluation
↓
Model Selection
↓
Stacking
↓
Hyperparameter Tuning
↓
Best Model
↓
Model Saving
↓
DVC
↓
FastAPI
↓
Deployment

Main Models:

- LGBM Regressor
- Random Forest Regressor
- Stacking Regressor

Optimization:

- Optuna
- Hyperparameter Tuning

Evaluation Metrics:

- MAE
- MSE
- RMSE
- R²

Deployment:

- FastAPI

Machine Learning Artifact / Data Versioning:

- DVC

Cloud Storage:

- AWS S3


# Day 35 Completed

Topic: Swiggy Time Prediction

Problem Type: Supervised Machine Learning - Regression

Main Models:
- LGBM Regressor
- Random Forest Regressor
- Stacking Regressor

Optimization:
- Optuna
- Hyperparameter Tuning

Evaluation:
- MAE
- MSE
- RMSE
- R²

Deployment:
- FastAPI

Version Control / ML Artifacts:
- DVC

Cloud Storage:
- AWS S3