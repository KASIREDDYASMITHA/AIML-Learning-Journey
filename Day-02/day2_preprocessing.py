# Day 2 - Machine Learning
# Topic: Data Loading, EDA, Feature Selection,
# Train-Test Split and Feature Scaling

# Install required packages in Google Colab if needed:
# !pip install pandas numpy matplotlib scikit-learn joblib


# --------------------------------------------------
# 1. Import Libraries
# --------------------------------------------------

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


# --------------------------------------------------
# 2. Load the Dataset
# --------------------------------------------------

df = pd.read_csv("late_to_office_dataset.csv")

print("First 5 rows:")
print(df.head())


# --------------------------------------------------
# 3. Explore the Dataset
# --------------------------------------------------

print("\nShape of Dataset:")
print(df.shape)

print("\nDataset Information:")
print(df.info())

print("\nStatistical Description:")
print(df.describe())

print("\nMissing Values:")
print(df.isnull().sum())


# --------------------------------------------------
# 4. Visualize the Data
# --------------------------------------------------

plt.figure(figsize=(8, 6))

plt.scatter(
    df["distance_km"],
    df["time_left_minutes"]
)

plt.xlabel("Distance (km)")
plt.ylabel("Time Left (minutes)")
plt.title("Distance vs Time Left")

plt.show()


# --------------------------------------------------
# 5. Feature Selection
# --------------------------------------------------

# X = Input features
X = df[["distance_km", "time_left_minutes"]]

# y = Output / Target
y = df["will_be_late"]

print("\nInput Features (X):")
print(X.head())

print("\nTarget (y):")
print(y.head())


# --------------------------------------------------
# 6. Train-Test Split
# --------------------------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("\nTraining Data:")
print(X_train.shape)

print("\nTesting Data:")
print(X_test.shape)


# --------------------------------------------------
# 7. Feature Scaling
# --------------------------------------------------

scaler = StandardScaler()

# Fit and transform only the training data
X_train_scaled = scaler.fit_transform(X_train)

# Only transform the test data
X_test_scaled = scaler.transform(X_test)


# --------------------------------------------------
# 8. Display Scaled Data
# --------------------------------------------------

print("\nScaled Training Data:")
print(X_train_scaled[:5])

print("\nScaled Testing Data:")
print(X_test_scaled[:5])


# --------------------------------------------------
# Today's Learning Completed
# --------------------------------------------------

print("\nDay 2 completed up to Feature Scaling.")