# AIML Learning Journey - Day 34

## Topic

Hyperparameter Tuning, Optuna, MLflow and Regression Model Optimization

## What I Learned

Today I learned how to improve regression models by tuning their hyperparameters.

The main topics covered were:

* Hyperparameters
* Hyperparameter tuning
* Optuna
* MLflow
* Experiment tracking
* Cross-validation
* Random Forest Regression
* LightGBM Regression
* Feature preprocessing
* One-Hot Encoding
* Ordinal Encoding
* Min-Max Scaling
* Power Transformation
* TransformedTargetRegressor
* MAE
* R² Score
* Train and test evaluation

## Dataset

The Swiggy delivery-time dataset was used.

Target column:

```text
time_taken
```

Some unnecessary columns such as rider ID, latitude/longitude, dates and city-related columns were removed before training.

## Models

Two regression models were studied:

1. Random Forest Regressor
2. LightGBM Regressor

## Hyperparameter Tuning

Optuna was used to automatically search for better hyperparameter combinations.

For Random Forest, parameters such as:

* n_estimators
* max_depth
* max_features
* min_samples_split
* min_samples_leaf
* max_samples

were tuned.

For LightGBM, parameters such as:

* n_estimators
* max_depth
* learning_rate
* subsample
* min_child_weight
* min_split_gain
* reg_lambda

were tuned.

## Experiment Tracking

MLflow was used to track:

* Hyperparameters
* Cross-validation error
* Training error
* Test error
* Training R²
* Test R²
* Best trial results
* Trained model

DagsHub was also used with MLflow for experiment tracking.

## Evaluation Metrics

### Mean Absolute Error

MAE measures the average absolute difference between actual and predicted values.

Lower MAE is better.

### R² Score

R² measures how much of the variation in the target variable is explained by the model.

A value closer to 1 generally indicates better fit.

## Main Learning

Instead of manually trying different model parameters, Optuna can search through a defined parameter space and identify a parameter combination that gives a better validation score.

MLflow helps record and compare these experiments.

## Day 34 Summary

Today I learned how preprocessing, target transformation, hyperparameter optimization, cross-validation and experiment tracking can be combined to build and evaluate regression models systematically.
