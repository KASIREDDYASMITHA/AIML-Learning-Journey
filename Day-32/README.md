# AIML Learning Journey - Day 32

### Main Topics

1. Missing Value Indicator
2. Feature Scaling
3. Hyperparameter Tuning
4. Optuna
5. Ensemble Methods
6. Stacking
7. MLflow

---

## 1. Missing Value Indicator

Missing values can contain useful information.

Instead of only replacing missing values, we can create an additional indicator column that tells the model whether the original value was missing.

Example:

```text
weather    weather_was_missing
Sunny      0
Sunny      1
Stormy     0
Sunny      1
```

---

## 2. Feature Scaling

Feature scaling brings numerical features to a similar range.

I learned Min-Max Scaling, which converts values approximately into the range 0 to 1.

Example:

```text
Age       -> scaled Age
25        -> 0.22
45        -> 0.84
```

Scaling is especially important for models that depend on distances or gradient-based optimization.

---

## 3. Hyperparameter Tuning

Hyperparameters are settings that are selected before model training.

Examples:

- `n_estimators`
- `max_depth`

I learned three major search strategies:

- Grid Search
- Random Search
- Bayesian / Smart Search

---

## 4. Optuna

Optuna is a Python framework used for efficient hyperparameter optimization.

Important terms:

- Study
- Trial
- Objective Function
- Search Space
- `trial.suggest_int()`
- `trial.suggest_float()`
- `trial.suggest_categorical()`
- `study.best_params`
- `study.best_value`

Optuna uses previous trial results to intelligently select the next parameters to test.

---

## 5. Ensemble Methods

Ensemble learning combines multiple models to improve stability and prediction quality.

### Bagging

Bagging trains multiple models using different samples of the data and combines their predictions.

Random Forest is an example of bagging.

### Stacking

Stacking combines different model types.

The predictions from base models are given to a meta-model, which learns how to combine them.

---

## 6. MLflow

MLflow helps track Machine Learning experiments.

Three important things can be logged:

- Parameters
- Metrics
- Artifacts / Models

Example:

```text
Parameters:
n_estimators = 479
max_depth = 17

Metric:
test_mae = 3.083
```

MLflow can also be used with a Model Registry to manage model versions and promotion toward production.
