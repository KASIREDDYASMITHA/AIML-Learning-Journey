# Day 32 - ML Experimentation and Production Pipelines

## 1. Missing Value Indicator

A missing value is not always meaningless.

There are two common approaches:

### Approach 1: Drop the row

Advantages:

- Simple
- No need to guess the missing value

Disadvantages:

- Data is lost
- Can introduce selection bias

### Approach 2: Fill the missing value

Advantages:

- Keeps the row
- Preserves the dataset size

Disadvantage:

- The model may not know that the original value was missing

### Missing Value Indicator

An indicator column preserves the information that a value was missing.

Example:

```text
weather    weather_was_missing
Sunny      0
Sunny      1
Stormy     0
Sunny      1
```

`0` means the value was available.

`1` means the original value was missing.

In Scikit-learn:

```python
SimpleImputer(
    strategy="most_frequent",
    add_indicator=True
)
```

The faculty example showed that dropping rows produced a lower test MAE than the indicator approach for that particular dataset. This is an experimental result, not a universal rule.

---

# 2. Feature Scaling

Different numerical features can have very different ranges.

Example:

```text
Age       = 25
Distance  = 2000
```

A large numerical range can dominate some models even when the feature is not actually more important.

Scaling puts numerical features onto a comparable scale.

## Min-Max Scaling

Min-Max Scaling converts values into a range between 0 and 1.

Formula:

```text
x_scaled = (x - min) / (max - min)
```

Example:

```text
Age:
25 -> 0.22
45 -> 0.84

Distance:
2 km  -> 0.10
18 km -> 0.90
```

### Important

Scale numerical columns.

Do not apply numerical scaling directly to categorical columns such as:

```text
weather
traffic
city
```

Categorical features need encoding.

---

# 3. Hyperparameter Tuning

Hyperparameters are model settings that are selected before training.

The model does not learn these values automatically from the training data.

Examples for Random Forest:

```text
n_estimators
max_depth
```

Different hyperparameter values can produce different model performance.

---

# 4. Grid Search

Grid Search tests every predefined combination.

Example:

```text
n_estimators    max_depth

50              5
50              10
50              20

100             5
100             10
100             20

200             5
200             10
200             20
```

Advantage:

- Exhaustive search over the specified grid

Disadvantage:

- Number of combinations can become extremely large

---

# 5. Random Search

Random Search selects a random subset of possible parameter combinations.

Advantage:

- Cheaper than testing every combination

Disadvantage:

- May miss good parameter combinations

---

# 6. Bayesian / Smart Search

Smart search uses results from previous trials to decide where to search next.

Instead of blindly testing combinations, it learns where good configurations are likely to exist.

Optuna uses this type of efficient search strategy.

---

# 7. Optuna

Optuna is a Python framework for automated hyperparameter optimization.

## Important Terms

### Study

A complete hyperparameter optimization session.

### Trial

One attempt using one particular set of hyperparameters.

### Objective Function

A function that:

1. Receives hyperparameter suggestions
2. Builds the model
3. Trains the model
4. Calculates a score
5. Returns the score

Example:

```python
def objective(trial):
    n_estimators = trial.suggest_int("n_estimators", 10, 500)
    max_depth = trial.suggest_int("max_depth", 1, 30)
```

### Direction

Determines whether the objective should be minimized or maximized.

For MAE:

```python
direction="minimize"
```

because lower MAE is better.

### Best Parameters

```python
study.best_params
```

### Best Score

```python
study.best_value
```

---

# 8. Ensemble Methods

Ensemble learning combines multiple models.

The reason for using an ensemble is that different models can make different mistakes.

Combining them can produce a more stable prediction.

---

# 9. Bagging

Bagging means:

```text
Same model type
       +
Different samples
       ↓
Multiple models
       ↓
Combine predictions
```

Random Forest is an example of bagging.

Example:

```text
Tree 1 = 32 minutes
Tree 2 = 24 minutes
Tree 3 = 27 minutes

Average = 27.7 minutes
```

---

# 10. Stacking

Stacking combines different types of models.

Example:

```text
Input Data
    ↓
Random Forest ────┐
                  ↓
               Meta Model
                  ↓
             Final Prediction
                  ↑
LightGBM ─────────┘
```

The base models produce predictions.

A meta-model learns how to combine those predictions.

Example:

```text
RF prediction  = 28
LGBM prediction = 33

Final:
0.4 × 28 + 0.6 × 33
= 31
```

A common meta-model can be Linear Regression.

---

# 11. Cross Validation in Stacking

Example:

```python
StackingRegressor(
    estimators=[
        ("rf", best_rf),
        ("lgbm", best_lgbm)
    ],
    final_estimator=LinearRegression(),
    cv=5
)
```

`cv=5` means 5-fold cross-validation is used.

This helps prevent the meta-model from simply learning predictions produced from data already seen during training.

---

# 12. MLflow

MLflow is used for tracking Machine Learning experiments.

When many experiments are performed, it becomes difficult to manually remember:

- Which parameters were used
- What score was obtained
- Which model was saved

MLflow acts like an experiment logbook.

---

# 13. What to Log in MLflow

## Parameters

Example:

```text
n_estimators = 479
max_depth = 17
```

## Metrics

Example:

```text
test_mae = 3.083
```

## Artifacts

Examples:

- Trained model
- Saved model file
- Other experiment files

---

# 14. MLflow Model Registry

MLflow Model Registry can be used to manage model versions.

A simplified flow is:

```text
Experiment
    ↓
Model Registered
    ↓
Staging
    ↓
Validation / Tests
    ↓
Production
    ↓
Live Application
```

The idea is to have a controlled process before a model reaches production.

---

# 15. Complete Pipeline

The complete workflow learned today is:

```text
Raw Data
   ↓
Missing Value Handling
   ↓
Feature Scaling
   ↓
Hyperparameter Tuning
   ↓
Best Models
   ↓
Ensemble / Stacking
   ↓
MLflow Experiment Tracking
   ↓
Model Registry
   ↓
Production
```

