# AIML Day 34 Notes

## 1. Hyperparameters

Hyperparameters are values that are set before training a machine learning model.

They control how the model learns.

Examples:

```text
Random Forest:
n_estimators
max_depth
min_samples_split
min_samples_leaf

LightGBM:
n_estimators
learning_rate
max_depth
reg_lambda
```

Hyperparameters are different from model parameters.

### Model Parameters

These are learned automatically during training.

Example:

A decision tree learns which feature and threshold should be used for splitting.

### Hyperparameters

These are selected before training.

Example:

```text
max_depth = 10
n_estimators = 100
```

---

# 2. Hyperparameter Tuning

Hyperparameter tuning means trying different hyperparameter values to find a combination that gives good model performance.

Example:

```text
max_depth = 5
max_depth = 10
max_depth = 15
```

The model is trained and evaluated using different values.

The combination giving the best validation performance is selected.

---

# 3. Manual Hyperparameter Tuning

In manual tuning, we choose parameter values ourselves.

Example:

```python
RandomForestRegressor(
    n_estimators=100,
    max_depth=10
)
```

This can become slow when many parameters need to be tested.

---

# 4. Optuna

Optuna is a hyperparameter optimization framework.

It automatically searches for good hyperparameter combinations.

Basic flow:

```text
Define objective function
        ↓
Define hyperparameter search space
        ↓
Optuna selects values
        ↓
Train model
        ↓
Evaluate model
        ↓
Return score
        ↓
Optuna tries another combination
        ↓
Best parameters are selected
```

Example:

```python
trial.suggest_int("n_estimators", 10, 500)
```

This tells Optuna to try integer values between 10 and 500.

Example:

```python
trial.suggest_float("learning_rate", 0.1, 0.8)
```

This allows Optuna to try floating-point values in that range.

---

# 5. Optuna Study

A study manages the optimization process.

Example:

```python
study = optuna.create_study(direction="minimize")
```

For MAE, we want a smaller value.

Therefore:

```text
direction = "minimize"
```

For metrics where higher is better, such as R², we would use:

```python
direction="maximize"
```

---

# 6. Objective Function

The objective function tells Optuna what to optimize.

Example:

```python
def objective(trial):

    params = {
        "n_estimators": trial.suggest_int("n_estimators", 10, 500)
    }

    model = RandomForestRegressor(**params)

    # train and evaluate

    return score
```

Optuna repeatedly calls this function with different parameter values.

---

# 7. Random Forest Hyperparameters

Important Random Forest hyperparameters:

### n_estimators

Number of trees in the forest.

Example:

```text
n_estimators = 100
```

means the forest contains 100 trees.

### max_depth

Maximum depth of each tree.

Example:

```text
max_depth = 10
```

limits the depth of each tree.

### min_samples_split

Minimum number of samples required to split an internal node.

### min_samples_leaf

Minimum number of samples required in a leaf node.

### max_features

Controls how many features are considered when searching for a split.

Examples:

```text
None
sqrt
log2
```

### max_samples

Controls the fraction of samples used when fitting each tree when applicable.

---

# 8. LightGBM

LightGBM is a gradient boosting framework based on decision trees.

It builds trees sequentially.

Each new tree attempts to improve the errors made by previous trees.

Example:

```python
LGBMRegressor()
```

Important hyperparameters include:

```text
n_estimators
learning_rate
max_depth
subsample
min_child_weight
min_split_gain
reg_lambda
```

---

# 9. n_estimators

Number of trees used by the model.

Example:

```python
n_estimators=100
```

More trees can improve learning, but may increase training time.

---

# 10. Learning Rate

The learning rate controls how much each new tree contributes to the final model.

Example:

```python
learning_rate=0.1
```

A smaller learning rate generally requires more trees.

---

# 11. MLflow

MLflow is used to track machine learning experiments.

It can store:

```text
Parameters
Metrics
Models
Artifacts
Experiment information
```

Example:

```python
mlflow.log_params(params)
```

Example:

```python
mlflow.log_metric("test_error", test_mae)
```

---

# 12. MLflow Run

An MLflow run represents one experiment execution.

Example:

```python
with mlflow.start_run():
    ...
```

Inside a run, we can log:

```text
parameters
metrics
models
artifacts
```

---

# 13. Nested MLflow Runs

When Optuna runs multiple trials, each trial can be recorded as a nested MLflow run.

Example:

```python
with mlflow.start_run(nested=True):
    ...
```

The parent run represents the complete optimization experiment.

The nested runs represent individual Optuna trials.

---

# 14. DagsHub

DagsHub can be used with MLflow for remote experiment tracking and machine learning project management.

Example:

```python
dagshub.init(
    repo_owner="margamacademy26-prog",
    repo_name="swiggy-time-predicition",
    mlflow=True
)
```

---

# 15. Feature Preprocessing

Before training, different types of features need different preprocessing methods.

Numerical columns:

```text
age
ratings
pickup_time_minutes
distance
```

Categorical columns:

```text
weather
type_of_order
type_of_vehicle
festival
city_type
is_weekend
order_time_of_day
traffic
distance_type
```

---

# 16. Min-Max Scaling

Min-Max Scaling transforms numerical values into a specified range, normally 0 to 1.

Example:

```python
MinMaxScaler()
```

Conceptually:

```text
scaled value =
(value - minimum) / (maximum - minimum)
```

Example:

If values are:

```text
10, 20, 30
```

then the minimum becomes approximately 0 and maximum becomes approximately 1.

---

# 17. One-Hot Encoding

One-Hot Encoding converts categorical values into separate binary columns.

Example:

```text
weather

Sunny
Rainy
Cloudy
```

can become separate columns such as:

```text
Rainy
Sunny
```

Using:

```python
OneHotEncoder(
    drop="first",
    handle_unknown="ignore"
)
```

`drop="first"` removes one category to avoid redundant columns.

`handle_unknown="ignore"` prevents errors when an unseen category appears during transformation.

---

# 18. Ordinal Encoding

Ordinal Encoding is useful when categories have a meaningful order.

Example:

```text
traffic

low
medium
high
jam
```

can be represented as:

```text
low      -> 0
medium   -> 1
high     -> 2
jam      -> 3
```

Another example:

```text
short
medium
long
very_long
```

can be represented as:

```text
short      -> 0
medium     -> 1
long       -> 2
very_long  -> 3
```

---

# 19. ColumnTransformer

ColumnTransformer allows different preprocessing operations to be applied to different columns.

Example:

```python
preprocessor = ColumnTransformer(
    transformers=[
        ("scale", MinMaxScaler(), num_cols),
        ("nominal_encode", OneHotEncoder(), nominal_cat_cols),
        ("ordinal_encode", OrdinalEncoder(), ordinal_cat_cols)
    ]
)
```

This means:

```text
Numerical columns
        ↓
MinMaxScaler

Nominal categorical columns
        ↓
OneHotEncoder

Ordinal categorical columns
        ↓
OrdinalEncoder
```

---

# 20. Pipeline

A Pipeline combines multiple preprocessing or modeling steps.

Example:

```python
processing_pipeline = Pipeline(
    steps=[
        ("preprocess", preprocessor)
    ]
)
```

This helps keep preprocessing organized and reproducible.

---

# 21. PowerTransformer

PowerTransformer transforms numerical data to make its distribution more suitable for modeling.

It was also used to transform the target variable:

```python
pt = PowerTransformer()
```

Training target:

```python
y_train_pt = pt.fit_transform(
    y_train.values.reshape(-1, 1)
)
```

---

# 22. TransformedTargetRegressor

TransformedTargetRegressor allows a model to train using a transformed target and automatically transform predictions back.

Example:

```python
model = TransformedTargetRegressor(
    regressor=rf,
    transformer=pt
)
```

This is useful when the target variable needs transformation.

---

# 23. Train-Test Split

The dataset is divided into training and testing data.

Example:

```python
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

Here:

```text
80% → training
20% → testing
```

---

# 24. Cross-Validation

Cross-validation evaluates the model using multiple training and validation splits.

Example:

```python
cross_val_score(
    model,
    X_train_trans,
    y_train,
    cv=5,
    scoring="neg_mean_absolute_error"
)
```

With:

```text
cv=5
```

the training data is divided into 5 folds.

The model is trained and validated multiple times.

---

# 25. Why Cross-Validation?

A single train-test split can sometimes give a misleading result.

Cross-validation provides multiple validation measurements.

Example:

```text
Fold 1 → MAE
Fold 2 → MAE
Fold 3 → MAE
Fold 4 → MAE
Fold 5 → MAE
```

The average score can then be used for comparison.

---

# 26. Negative Mean Absolute Error

Scikit-learn represents losses such as MAE as negative values when using `cross_val_score`.

Example:

```python
scoring="neg_mean_absolute_error"
```

If the returned mean is:

```text
-4.25
```

the actual MAE is:

```text
4.25
```

Therefore:

```python
mean_score = -cv_score.mean()
```

is used.

---

# 27. Mean Absolute Error

MAE measures the average absolute difference between actual and predicted values.

Formula:

```text
MAE = average(|actual - predicted|)
```

Example:

Actual:

```text
30
```

Predicted:

```text
35
```

Absolute error:

```text
|30 - 35| = 5
```

If the MAE is 4 minutes, predictions are off by about 4 minutes on average.

Lower MAE is better.

---

# 28. R² Score

R² measures how much variation in the target is explained by the model.

Example:

```python
r2_score(y_test, y_pred_test_org)
```

A value closer to 1 generally means the model explains more of the variation.

---

# 29. Complete Machine Learning Workflow

The complete workflow used today was:

```text
Load Dataset
      ↓
Remove Unnecessary Columns
      ↓
Handle Missing Values
      ↓
Separate X and y
      ↓
Train-Test Split
      ↓
Define Preprocessing
      ↓
Scale Numerical Features
      ↓
Encode Categorical Features
      ↓
Transform Target
      ↓
Train Model
      ↓
Define Optuna Search Space
      ↓
Run Cross-Validation
      ↓
Optimize Hyperparameters
      ↓
Select Best Parameters
      ↓
Train Final Model
      ↓
Generate Predictions
      ↓
Inverse Transform Predictions
      ↓
Calculate MAE and R²
      ↓
Log Results Using MLflow
```

---

# 30. Important Difference Between the Three Programs

### Program 1

LightGBM with Optuna + MLflow.

It searches for the best LightGBM hyperparameters.

### Program 2

Random Forest with Optuna + MLflow + DagsHub.

It searches for the best Random Forest hyperparameters.

### Program 3

LightGBM final model.

It uses already selected parameters instead of running Optuna again.

Example:

```python
lgbm_params = {
    "n_estimators": 145,
    "learning_rate": 0.16632111599858262,
    "max_depth": 17
}
```

This is useful when we already have the best parameters from a previous tuning experiment.
