import numpy as np
import pandas as pd
import dagshub
import mlflow
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer, KNNImputer
from sklearn.preprocessing import OneHotEncoder, MinMaxScaler, OrdinalEncoder, PowerTransformer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn import set_config

# --- 1. Initialize DagsHub & MLflow ---
dagshub.init(repo_owner='margamacademy26-prog', repo_name='swiggy-time-predicition', mlflow=True)
set_config(transform_output="pandas")
mlflow.set_experiment("Exp 1 - Keep Vs Drop Missing Values")

# --- 2. Load and Prepare Original Data ---
df = pd.read_csv('swiggy_cleaned.csv')

columns_to_drop = [
    'rider_id',
    'restaurant_latitude',
    'restaurant_longitude',
    'delivery_latitude',
    'delivery_longitude',
    'order_date',
    "order_time_hour",
    "order_day",
    "city_name",
    "order_day_of_week",
    "order_month"
]
df.drop(columns=columns_to_drop, inplace=True)

# Column groupings for preprocessing
num_cols = ["age", "ratings", "pickup_time_minutes", "distance"]
nominal_cat_cols = [
    'weather', 'type_of_order', 'type_of_vehicle', 'festival',
    'city_type', 'is_weekend', 'order_time_of_day'
]
ordinal_cat_cols = ["traffic", "distance_type"]

traffic_order = ["low", "medium", "high", "jam"]
distance_type_order = ["short", "medium", "long", "very_long"]


# =====================================================================
# EXPERIMENT 1: DROP MISSING VALUES
# =====================================================================
print("Running Experiment 1: Drop Missing Values...")
temp_df_drop = df.copy().dropna()

X_drop = temp_df_drop.drop(columns='time_taken')
y_drop = temp_df_drop['time_taken']

X_train_drop, X_test_drop, y_train_drop, y_test_drop = train_test_split(
    X_drop, y_drop, test_size=0.2, random_state=42
)

# Power transform the target
pt_drop = PowerTransformer()
y_train_pt_drop = pt_drop.fit_transform(y_train_drop.values.reshape(-1, 1))
y_test_pt_drop = pt_drop.transform(y_test_drop.values.reshape(-1, 1))

# Simple Preprocessor without Imputation (as there are no NaNs left)
preprocessor_drop = ColumnTransformer(transformers=[
    ("scale", MinMaxScaler(), num_cols),
    ("nominal_encode", OneHotEncoder(drop="first", handle_unknown="ignore", sparse_output=False), nominal_cat_cols),
    ("ordinal_encode", OrdinalEncoder(categories=[traffic_order, distance_type_order]), ordinal_cat_cols)
], remainder="passthrough", n_jobs=-1, force_int_remainder_cols=False, verbose_feature_names_out=False)

preprocessor_drop.set_output(transform="pandas")
X_train_trans_drop = preprocessor_drop.fit_transform(X_train_drop)
X_test_trans_drop = preprocessor_drop.transform(X_test_drop)

# Fit Regressor
rf_drop = RandomForestRegressor(random_state=42)
rf_drop.fit(X_train_trans_drop, y_train_pt_drop.ravel())

# Evaluate and Log to MLflow
y_pred_train_drop = rf_drop.predict(X_train_trans_drop)
y_pred_test_drop = rf_drop.predict(X_test_trans_drop)

y_pred_train_org_drop = pt_drop.inverse_transform(y_pred_train_drop.reshape(-1, 1))
y_pred_test_org_drop = pt_drop.inverse_transform(y_pred_test_drop.reshape(-1, 1))

train_mae_drop = mean_absolute_error(y_train_drop, y_pred_train_org_drop)
test_mae_drop = mean_absolute_error(y_test_drop, y_pred_test_org_drop)
train_r2_drop = r2_score(y_train_drop, y_pred_train_org_drop)
test_r2_drop = r2_score(y_test_drop, y_pred_test_org_drop)

print(f"[Drop] Train Error: {train_mae_drop:.2f} min, R2: {train_r2_drop:.2f}")
print(f"[Drop] Test Error: {test_mae_drop:.2f} min, R2: {test_r2_drop:.2f}")

with mlflow.start_run(run_name="Drop Missing Values"):
    mlflow.log_param("experiment_type", "Drop Missing Values")
    mlflow.log_params(rf_drop.get_params())
    mlflow.log_metric("training_error", train_mae_drop)
    mlflow.log_metric("test_error", test_mae_drop)
    mlflow.log_metric("training_r2", train_r2_drop)
    mlflow.log_metric("test_r2", test_r2_drop)


# =====================================================================
# EXPERIMENT 2: IMPUTE MISSING VALUES
# =====================================================================
print("\nRunning Experiment 2: Impute Missing Values...")
temp_df_imp = df.copy()

X_imp = temp_df_imp.drop(columns='time_taken')
y_imp = temp_df_imp['time_taken']

X_train_imp, X_test_imp, y_train_imp, y_test_imp = train_test_split(
    X_imp, y_imp, test_size=0.2, random_state=42
)

# Power transform the target
pt_imp = PowerTransformer()
y_train_pt_imp = pt_imp.fit_transform(y_train_imp.values.reshape(-1, 1))
y_test_pt_imp = pt_imp.transform(y_test_imp.values.reshape(-1, 1))

# Imputation strategy
features_to_fill_mode = ['multiple_deliveries', 'festival', 'city_type']
features_to_fill_missing = [col for col in nominal_cat_cols if col not in features_to_fill_mode]

simple_imputer = ColumnTransformer(transformers=[
    ("mode_imputer", SimpleImputer(strategy="most_frequent"), features_to_fill_mode),
    ("missing_imputer", SimpleImputer(strategy="constant", fill_value="missing"), features_to_fill_missing)
], remainder="passthrough", n_jobs=-1, force_int_remainder_cols=False, verbose_feature_names_out=False)

preprocessor_imp = ColumnTransformer(transformers=[
    ("scale", MinMaxScaler(), num_cols),
    ("nominal_encode", OneHotEncoder(drop="first", handle_unknown="ignore", sparse_output=False), nominal_cat_cols),
    ("ordinal_encode", OrdinalEncoder(categories=[traffic_order, distance_type_order],
                                      encoded_missing_value=-999,
                                      handle_unknown="use_encoded_value",
                                      unknown_value=-1), ordinal_cat_cols)
], remainder="passthrough", n_jobs=-1, force_int_remainder_cols=False, verbose_feature_names_out=False)

knn_imputer = KNNImputer(n_neighbors=5)

processing_pipeline = Pipeline(steps=[
    ("simple_imputer", simple_imputer),
    ("preprocess", preprocessor_imp),
    ("knn_imputer", knn_imputer)
])

rf_imp = RandomForestRegressor(random_state=42)

model_pipe = Pipeline(steps=[
    ("preprocessing", processing_pipeline),
    ("model", rf_imp)
])

# Train model pipeline
model_pipe.fit(X_train_imp, y_train_pt_imp.ravel())

# Evaluate and Log to MLflow
y_pred_train_imp = model_pipe.predict(X_train_imp)
y_pred_test_imp = model_pipe.predict(X_test_imp)

y_pred_train_org_imp = pt_imp.inverse_transform(y_pred_train_imp.reshape(-1, 1))
y_pred_test_org_imp = pt_imp.inverse_transform(y_pred_test_imp.reshape(-1, 1))

train_mae_imp = mean_absolute_error(y_train_imp, y_pred_train_org_imp)
test_mae_imp = mean_absolute_error(y_test_imp, y_pred_test_org_imp)
train_r2_imp = r2_score(y_train_imp, y_pred_train_org_imp)
test_r2_imp = r2_score(y_test_imp, y_pred_test_org_imp)

print(f"[Impute] Train Error: {train_mae_imp:.2f} min, R2: {train_r2_imp:.2f}")
print(f"[Impute] Test Error: {test_mae_imp:.2f} min, R2: {test_r2_imp:.2f}")

with mlflow.start_run(run_name="Impute Missing Values"):
    mlflow.log_param("experiment_type", "Impute Missing Values")
    mlflow.log_params(rf_imp.get_params())
    mlflow.log_metric("training_error", train_mae_imp)
    mlflow.log_metric("test_error", test_mae_imp)
    mlflow.log_metric("training_r2", train_r2_imp)
    mlflow.log_metric("test_r2", test_r2_imp)
