# Day 24 - End-to-End Machine Learning Workflow

## 1. Full Machine Learning Workflow

A complete Machine Learning project can be viewed as a pipeline:

1. Problem Framing
2. Feature Engineering
3. Data Cleaning and Exploration
4. Choosing Metrics and Building a Baseline
5. Model Training
6. Experiment Tracking
7. Model Quality and Deployment
8. CI/CD
9. Docker
10. Deployment, Storage and Scaling

The goal is to build a reliable system, not just train a model.

---

## 2. Problem Framing

Before building a model, clearly define:

- What problem are we solving?
- What are we predicting?
- What data is available?
- What will the prediction be used for?

### Example

A delivery company wants to predict how many minutes an order will take to arrive.

Input:

- Distance
- Traffic level
- Weather
- Vehicle type
- Order type
- Preparation time

Output:

- Predicted delivery time in minutes

Since delivery time is a continuous numerical value, this is a regression problem.

---

## 3. Feature Engineering

Features are the input variables used by the Machine Learning model.

Feature engineering means creating useful model inputs from raw data.

### Numerical Features

Examples:

- Distance
- Preparation time
- Traffic density
- Temperature

Numerical values can be directly used by many ML algorithms.

### Categorical Features

Examples:

- Vehicle type
- Weather condition
- Order type
- City

Categorical data may need encoding before it can be used by a model.

### Date and Time Features

Date/time information can be converted into useful features such as:

- Hour
- Day of week
- Month
- Weekend indicator

### Geospatial Features

Location information can be transformed into useful numerical features such as:

- Distance
- Latitude
- Longitude
- Area or zone

The real value is not always in the raw data. It can be in the features we create from it.

---

## 4. Data Cleaning

Poor-quality data can produce poor predictions.

Common data problems include:

- Missing values
- Duplicate records
- Incorrect values
- Inconsistent formats
- Outliers
- Wrong data types

Cleaning should happen before model training.

Example:

If delivery distance contains negative values, those records need to be investigated and corrected or removed.

---

## 5. Exploratory Data Analysis

Exploratory Data Analysis (EDA) helps us understand the dataset before modelling.

We can check:

- Dataset shape
- Data types
- Missing values
- Statistical summaries
- Distributions
- Relationships between features
- Outliers
- Correlations

EDA helps identify which features may be useful for the model.

---

## 6. Choosing the Metric

The evaluation metric should match the problem.

For regression problems, common metrics include:

### MAE - Mean Absolute Error

MAE measures the average absolute difference between actual and predicted values.

Example:

Actual delivery time = 40 minutes
Predicted delivery time = 35 minutes

Absolute error = 5 minutes

Lower MAE is better.

---

### MSE - Mean Squared Error

MSE calculates the average squared prediction error.

Large errors receive more penalty because the errors are squared.

Lower MSE is better.

---

### RMSE - Root Mean Squared Error

RMSE is the square root of MSE.

It is expressed in the same unit as the target.

For delivery time, RMSE is measured in minutes.

Lower RMSE is better.

---

### R² Score

R² indicates how much of the variation in the target is explained by the model.

A value closer to 1 generally indicates better explanatory performance.

---

## 7. Classification Metrics

Precision, recall, TP and FP are mainly used for classification problems.

### Precision

Precision answers:

"Of the observations predicted as positive, how many were actually positive?"

Precision = TP / (TP + FP)

### Recall

Recall answers:

"Of all actual positive observations, how many did the model correctly identify?"

Recall = TP / (TP + FN)

These metrics are not the primary metrics for predicting a continuous delivery time.

For delivery-time prediction, regression metrics such as MAE, RMSE and R² are more appropriate.

---

## 8. Train-Test Split

The dataset should be divided into training and testing data.

Training data is used to learn the model.

Testing data is used to evaluate how the model performs on unseen data.

Example:

80% -> Training data
20% -> Testing data

The exact split can depend on the dataset and problem.

---

## 9. Baseline Model

A baseline gives us a simple reference point.

Every more complicated model should provide useful improvement over the baseline.

For a delivery-time regression problem, a simple baseline can predict the average delivery time for every order.

Example:

Average delivery time = 35 minutes

Baseline prediction:

Order 1 -> 35 minutes
Order 2 -> 35 minutes
Order 3 -> 35 minutes

A trained model should perform better than this baseline according to the selected evaluation metric.

---

## 10. Model Training

After preparing the data, we train a Machine Learning model.

Example:

Linear Regression

Input:

Distance
Traffic
Preparation time

Output:

Predicted delivery time

The model learns relationships between input features and the target value.

---

## 11. Model Evaluation

After training, evaluate the model on unseen test data.

For regression we can calculate:

- MAE
- MSE
- RMSE
- R²

We should compare the trained model with the baseline.

The goal is not simply to use a sophisticated algorithm.

The model should provide measurable value.

---

## 12. Experiment Tracking

During ML development, we may train many models with different:

- Features
- Algorithms
- Hyperparameters
- Training datasets

MLflow can be used to track experiments.

It can help record:

- Parameters
- Metrics
- Model versions
- Experiment results

This makes experiments easier to compare and reproduce.

---

## 13. Model Registry

A model registry can be used to manage trained model versions.

Example:

Version 1 -> Initial model
Version 2 -> Improved features
Version 3 -> Improved model

The registry helps manage which model version is ready for deployment.

---

## 14. CI/CD for Machine Learning

CI means Continuous Integration.

CD means Continuous Delivery or Continuous Deployment.

The idea is to automatically test and deliver changes.

A simplified ML pipeline can be:

Code change
    ↓
Run tests
    ↓
Validate model
    ↓
Build application
    ↓
Deploy approved model

The purpose is to make deployment more reliable and repeatable.

---

## 15. Docker

Docker packages an application and its dependencies into a container.

The idea is:

"It works on my machine" should become "It works in the same environment everywhere."

Docker helps create a consistent environment for:

- Python version
- Libraries
- Application code
- Dependencies

This reduces environment-related problems.

---

## 16. Deployment

After a model has been trained and validated, it can be deployed so that applications can use it.

Example:

Customer order
    ↓
Application sends features
    ↓
ML model
    ↓
Predicted delivery time
    ↓
Customer sees estimated delivery time

---

## 17. Storage

A deployed ML system may need storage for:

- Training data
- Processed data
- Models
- Experiment results
- Logs

Different components may use different storage systems depending on the project.

---

## 18. Scaling

When the number of users or predictions increases, the ML system may need to scale.

Scaling can involve:

- More computing resources
- Multiple model-serving instances
- Load balancing
- Efficient storage
- Caching

Deployment, storage and scaling are separate responsibilities in a larger ML system.

---

## 19. Important Learning

A Machine Learning project is not only:

Data -> Model -> Prediction

A real ML system is closer to:

Problem
    ↓
Data
    ↓
Feature Engineering
    ↓
Cleaning & EDA
    ↓
Metric & Baseline
    ↓
Model Training
    ↓
Evaluation
    ↓
Experiment Tracking
    ↓
Deployment
    ↓
Monitoring
    ↓
Scaling

The model is only one part of the complete ML system.