"""
AIML Day 53: Regression with Keras
Predicting house prices (a continuous numerical target).

"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_absolute_error, r2_score

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense


# ---------------------------------------------------------
# 1. Create a synthetic house-price dataset (600 rows)
# ---------------------------------------------------------
np.random.seed(42)

number_of_houses = 600

df = pd.DataFrame({
    "sqft": np.random.randint(800, 4001, number_of_houses),
    "bedrooms": np.random.randint(1, 7, number_of_houses),
    "age_years": np.random.randint(0, 41, number_of_houses),
    "distance_km": np.round(np.random.uniform(1, 25, number_of_houses), 1),
    "location_score": np.random.randint(1, 11, number_of_houses)
})

# Create a practice target using the five features and random noise.
noise = np.random.normal(0, 18000, number_of_houses)

df["price"] = (
    50000
    + df["sqft"] * 180
    + df["bedrooms"] * 12000
    - df["age_years"] * 1500
    - df["distance_km"] * 3500
    + df["location_score"] * 12000
    + noise
)

df["price"] = df["price"].clip(lower=50000).round(2)

print("First five rows of the dataset:")
print(df.head())
print("\nDataset shape:", df.shape)


# ---------------------------------------------------------
# 2. Separate input features (X) and target (y)
# ---------------------------------------------------------
X = df.drop(columns=["price"])
y = df["price"].values


# ---------------------------------------------------------
# 3. Split data into training and testing sets
# ---------------------------------------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# ---------------------------------------------------------
# 4. Scale input features
# ---------------------------------------------------------
scaler = StandardScaler()

X_train_trf = scaler.fit_transform(X_train)
X_test_trf = scaler.transform(X_test)


# ---------------------------------------------------------
# 5. Scale the target values
# ---------------------------------------------------------
y_scaler = StandardScaler()

y_train_trf = y_scaler.fit_transform(
    y_train.reshape(-1, 1)
).flatten()

y_test_trf = y_scaler.transform(
    y_test.reshape(-1, 1)
).flatten()
