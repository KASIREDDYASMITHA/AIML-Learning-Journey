import numpy as np
import pandas as pd
import dagshub
import mlflow
import optuna

from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer, TransformedTargetRegressor
from sklearn.preprocessing import OneHotEncoder, MinMaxScaler, PowerTransformer, OrdinalEncoder
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_absolute_error


# --------------------------------------------------
# 1. Initialize DagsHub and MLflow
# --------------------------------------------------

dagshub.init(
    repo_owner="margamacademy26-prog",
    repo_name="swiggy-time-predicition",
    mlflow=True
)

mlflow.set_experiment("Exp 3 - RF HP Tuning")


# --------------------------------------------------
# 2. Load Dataset
# --------------------------------------------------

df = pd.read_csv("swiggy_cleaned.csv")


# --------------------------------------------------
# 3. Drop unnecessary columns
# --------------------------------------------------

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

df.drop(columns=columns_to_drop, inplace=True, errors="ignore")


# --------------------------------------------------
# 4. Remove missing values
# --------------------------------------------------

df = df.dropna()


# --------------------------------------------------
# 5. Separate features and target
# --------------------------------------------------

X = df.drop(columns="time_taken")
y = df["time_taken"]


# --------------------------------------------------
# 6. Train-Test Split
# --------------------------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# --------------------------------------------------
# 7. Target Transformation
# --------------------------------------------------

pt = PowerTransformer()

y_train_pt = pt.fit_transform(
    y_train.values.reshape(-1, 1)
)

y_test_pt = pt.transform(
    y_test.values.reshape(-1, 1)
)


# --------------------------------------------------
# 8. Define Feature Categories
# --------------------------------------------------

num_cols = [
    "age",
    "ratings",
    "pickup_time_minutes",
    "distance"
]

nominal_cat_cols = [
    "weather",
    "type_of_order",
    "type_of_vehicle",
    "festival",
    "city_type",
    "is_weekend",
    "order_time_of_day"
]

ordinal_cat_cols = [
    "traffic",
    "distance_type"
]


traffic_order = [
    "low",
    "medium",
    "high",
    "jam"
]

distance_type_order = [
    "short",
    "medium",
    "long",
    "very_long"
]


# --------------------------------------------------
# 9. Build Preprocessor
# --------------------------------------------------

preprocessor = ColumnTransformer(
    transformers=[
        (
            "scale",
            MinMaxScaler(),
            num_cols
        ),

        (
            "nominal_encode",
            OneHotEncoder(
                drop="first",
                handle_unknown="ignore",
                sparse_output=False
            ),
            nominal_cat_cols
        ),

        (
            "ordinal_encode",
            OrdinalEncoder(
                categories=[
                    traffic_order,
                    distance_type_order
                ],
                encoded_missing_value=-999,
                handle_unknown="use_encoded_value",
                unknown_value=-1
            ),
            ordinal_cat_cols
        )
    ],

    remainder="passthrough",
    n_jobs=-1,
    verbose_feature_names_out=False
)


# --------------------------------------------------
# 10. Preprocessing Pipeline
# --------------------------------------------------

processing_pipeline = Pipeline(
    steps=[
        ("preprocess", preprocessor)
    ]
)


# --------------------------------------------------
# 11. Transform Features
# --------------------------------------------------

X_train_trans = processing_pipeline.fit_transform(X_train)
X_test_trans = processing_pipeline.transform(X_test)


# --------------------------------------------------
# 12. Optuna Objective Function
# --------------------------------------------------

def objective(trial):

    with mlflow.start_run(nested=True):

        params = {
            "n_estimators": trial.suggest_int(
                "n_estimators", 10, 500
            ),

            "max_depth": trial.suggest_int(
                "max_depth", 1, 30
            ),

            "max_features": trial.suggest_categorical(
                "max_features",
                [None, "sqrt", "log2"]
            ),

            "min_samples_split": trial.suggest_int(
                "min_samples_split", 2, 10
            ),

            "min_samples_leaf": trial.suggest_int(
                "min_samples_leaf", 1, 10
            ),

            "max_samples": trial.suggest_float(
                "max_samples", 0.5, 1
            ),

            "random_state": 42,
            "n_jobs": -1
        }


        # Log parameters
        mlflow.log_params(params)


        # Create Random Forest
        rf = RandomForestRegressor(**params)


        # Apply target transformation
        model = TransformedTargetRegressor(
            regressor=rf,
            transformer=pt
        )


        # Cross-validation
        cv_score = cross_val_score(
            model,
            X_train_trans,
            y_train,
            cv=5,
            scoring="neg_mean_absolute_error",
            n_jobs=-1
        )


        mean_score = -cv_score.mean()


        # Log CV score
        mlflow.log_metric(
            "cross_val_error",
            mean_score
        )


        return mean_score


# --------------------------------------------------
# 13. Create Optuna Study
# --------------------------------------------------

study = optuna.create_study(
    direction="minimize"
)


# --------------------------------------------------
# 14. Run Optimization
# --------------------------------------------------

with mlflow.start_run(run_name="best_model"):

    study.optimize(
        objective,
        n_trials=20,
        n_jobs=-1,
        show_progress_bar=True
    )


    # Log best parameters
    mlflow.log_params(
        study.best_params
    )

    mlflow.log_metric(
        "best_score",
        study.best_value
    )


    # --------------------------------------------------
    # 15. Train Final Model
    # --------------------------------------------------

    best_rf = RandomForestRegressor(
        **study.best_params
    )

    best_rf.fit(
        X_train_trans,
        y_train_pt.ravel()
    )


    # --------------------------------------------------
    # 16. Predictions
    # --------------------------------------------------

    y_pred_train = best_rf.predict(
        X_train_trans
    )

    y_pred_test = best_rf.predict(
        X_test_trans
    )


    # --------------------------------------------------
    # 17. Inverse Transform Predictions
    # --------------------------------------------------

    y_pred_train_org = pt.inverse_transform(
        y_pred_train.reshape(-1, 1)
    )

    y_pred_test_org = pt.inverse_transform(
        y_pred_test.reshape(-1, 1)
    )


    # --------------------------------------------------
    # 18. Cross Validation of Best Model
    # --------------------------------------------------

    model = TransformedTargetRegressor(
        regressor=best_rf,
        transformer=pt
    )

    scores = cross_val_score(
        model,
        X_train_trans,
        y_train,
        scoring="neg_mean_absolute_error",
        cv=5,
        n_jobs=-1
    )


    cv_mae = -scores.mean()


    # --------------------------------------------------
    # 19. Calculate Metrics
    # --------------------------------------------------

    train_mae = mean_absolute_error(
        y_train,
        y_pred_train_org
    )

    test_mae = mean_absolute_error(
        y_test,
        y_pred_test_org
    )

    train_r2 = r2_score(
        y_train,
        y_pred_train_org
    )

    test_r2 = r2_score(
        y_test,
        y_pred_test_org
    )


    # --------------------------------------------------
    # 20. Log Metrics
    # --------------------------------------------------

    mlflow.log_metric(
        "training_error",
        train_mae
    )

    mlflow.log_metric(
        "test_error",
        test_mae
    )

    mlflow.log_metric(
        "training_r2",
        train_r2
    )

    mlflow.log_metric(
        "test_r2",
        test_r2
    )

    mlflow.log_metric(
        "cross_val",
        cv_mae
    )


    # --------------------------------------------------
    # 21. Save Model
    # --------------------------------------------------

    mlflow.sklearn.log_model(
        best_rf,
        artifact_path="model"
    )


    # --------------------------------------------------
    # 22. Print Results
    # --------------------------------------------------

    print("\nBest Parameters:")
    print(study.best_params)

    print(
        f"\nBest CV MAE: "
        f"{study.best_value:.4f}"
    )

    print(
        f"Train MAE: "
        f"{train_mae:.4f}"
    )

    print(
        f"Test MAE: "
        f"{test_mae:.4f}"
    )

    print(
        f"Train R2: "
        f"{train_r2:.4f}"
    )

    print(
        f"Test R2: "
        f"{test_r2:.4f}"
    )

    print(
        f"Cross Validation MAE: "
        f"{cv_mae:.4f}"
    )


print("\nExecution completed successfully!")