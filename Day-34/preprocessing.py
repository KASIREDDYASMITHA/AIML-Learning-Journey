import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, MinMaxScaler, OrdinalEncoder


# Load dataset
df = pd.read_csv("swiggy_cleaned.csv")


# Columns that are not required for model training
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


# Remove missing values
df = df.dropna()


# Separate features and target
X = df.drop(columns="time_taken")
y = df["time_taken"]


# Numerical columns
num_cols = [
    "age",
    "ratings",
    "pickup_time_minutes",
    "distance"
]


# Nominal categorical columns
nominal_cat_cols = [
    "weather",
    "type_of_order",
    "type_of_vehicle",
    "festival",
    "city_type",
    "is_weekend",
    "order_time_of_day"
]


# Ordinal categorical columns
ordinal_cat_cols = [
    "traffic",
    "distance_type"
]


# Define category ordering
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


# Create preprocessing transformer
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


# Create preprocessing pipeline
processing_pipeline = Pipeline(
    steps=[
        ("preprocess", preprocessor)
    ]
)


print("Dataset shape:", df.shape)
print("Feature columns:", X.columns.tolist())
print("Preprocessing pipeline created successfully.")