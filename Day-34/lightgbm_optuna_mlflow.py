import numpy as np
import pandas as pd
import mlflow
import optuna

from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer, TransformedTargetRegressor
from sklearn.preprocessing import (
    OneHotEncoder,
    MinMaxScaler,
    PowerTransformer,
    OrdinalEncoder
)
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import r2_score, mean_absolute_error

from lightgbm import LGBMRegressor


# --------------------------------------------------
# 1. Load Dataset
# --------------------------------------------------

df = pd.read_csv("swiggy_cleaned.csv")


# --------------------------------------------------
# 2. Drop unnecessary columns
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

df.drop(
    columns=columns_to_drop,
    inplace=True,
    errors="ignore"
)


# --------------------------------------------------
# 3. Remove missing values
# --------------------------------------------------

df = df.dropna()


# --------------------------------------------------
# 4. Separate features and target
# --------------------------------------------------

X = df.drop(columns="time_taken")
y = df["time_taken"]


# --------------------------------------------------
# 5. Train-Test Split
# --------------------------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# --------------------------------------------------
# 6. Target Transformation
# --------------------------------------------------

pt = PowerTransformer()

y_train_pt = pt.fit_transform(
    y_train.values.reshape(-1, 1)
)

y_test_pt = pt.transform(
    y_test.values.reshape(-1, 1)
)


# --------------------------------------------------
# 7. Feature Categories
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
# 8. Preprocessor
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
# 9. Processing Pipeline
# --------------------------------------------------

processing_pipeline = Pipeline(
    steps=[
        ("preprocess", preprocessor)
    ]
)


# --------------------------------------------------
# 10. Transform Features
# --------------------------------------------------

X_train_trans = processing_pipeline.fit_transform(
    X_train
)

X_test_trans = processing_pipeline.transform(
    X_test
)


# --------------------------------------------------
# 11. Initialize MLflow Experiment
# --------------------------------------------------

mlflow.set_experiment(
    "Exp 4 - LGBM HP Tuning"
)


# --------------------------------------------------
# 12. Optuna Objective Function
# --------------------------------------------------

def objective(trial):

    with mlflow.start_run(nested=True):

        params = {

            "n_estimators": trial.suggest_int(
                "n_estimators",
                10,
                200
            ),

            "max_depth": trial.suggest_int(
                "max_depth",
                1,
                40
            ),

            "learning_rate": trial.suggest_float(
                "learning_rate",
                0.1,
                0.8
            ),

            "subsample": trial.suggest_float(
                "subsample",
                0.5,
                1.0
            ),

            "min_child_weight": trial.suggest_int(
                "min_child_weight",
                5,
                20
            ),

            "min_split_gain": trial.suggest_float(
                "min_split_gain",
                0,
                10
            ),

            "reg_lambda": trial.suggest_float(
                "reg_lambda",
                0,
                100
            ),

            "random_state": 42,
            "n_jobs": -1
        }


        # Log parameters
        mlflow.log_params(params)


        # Create LightGBM model
        lgbm = LGBMRegressor(
            **params
        )


        # Target transformation
        model = TransformedTargetRegressor(
            regressor=lgbm,
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


        # Log metric
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

with mlflow.start_run(
    run_name="best_model"
):

    study.optimize(
        objective,
        n_trials=50,
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
    # 15. Train Final Tuned Model
    # --------------------------------------------------

    best_lgbm = LGBMRegressor(
        **study.best_params
    )

    best_lgbm.fit(
        X_train_trans,
        y_train_pt.ravel()
    )


    # --------------------------------------------------
    # 16. Predictions
    # --------------------------------------------------

    y_pred_train = best_lgbm.predict(
        X_train_trans
    )

    y_pred_test = best_lgbm.predict(
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
    # 18. Cross Validation
    # --------------------------------------------------

    model = TransformedTargetRegressor(
        regressor=best_lgbm,
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
    # 21. Log Model
    # --------------------------------------------------

    mlflow.sklearn.log_model(
        best_lgbm,
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


# --------------------------------------------------
# 23. Final LightGBM Example
# --------------------------------------------------

# These parameters came from a previous tuning experiment.
# They can be used when you do not want to run Optuna again.

final_lgbm_params = {
    "n_estimators": 145,
    "learning_rate": 0.16632111599858262,
    "max_depth": 17
}

final_lgbm = LGBMRegressor(
    **final_lgbm_params
)

final_lgbm.fit(
    X_train_trans,
    y_train_pt.ravel()
)


# Predictions
final_train_pred = final_lgbm.predict(
    X_train_trans
)

final_test_pred = final_lgbm.predict(
    X_test_trans
)


# Inverse transform
final_train_pred_org = pt.inverse_transform(
    final_train_pred.reshape(-1, 1)
)

final_test_pred_org = pt.inverse_transform(
    final_test_pred.reshape(-1, 1)
)


# Final evaluation
print("\nFinal LightGBM Model")

print(
    f"Train MAE: "
    f"{mean_absolute_error(y_train, final_train_pred_org):.2f} minutes"
)

print(
    f"Test MAE: "
    f"{mean_absolute_error(y_test, final_test_pred_org):.2f} minutes"
)