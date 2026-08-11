import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix


# ==========================================================
# 1. LOAD DATASET
# ==========================================================

df = pd.read_csv("data/late_to_office_dataset.csv")

print("First 5 rows:")
print(df.head())

print("\nShape:")
print(df.shape)

print("\nMissing values:")
print(df.isnull().sum())


# ==========================================================
# 2. FEATURE SELECTION
# ==========================================================

X = df[["distance_km", "time_left_minutes"]]
y = df["will_be_late"]


# ==========================================================
# 3. TRAIN-TEST SPLIT
# ==========================================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# ==========================================================
# 4. FEATURE SCALING
# ==========================================================

scaler = StandardScaler()

# Fit the scaler only on training data
X_train_scaled = scaler.fit_transform(X_train)

# Use the same scaler for test data
X_test_scaled = scaler.transform(X_test)


# ==========================================================
# 5. LOGISTIC REGRESSION
# ==========================================================

lr = LogisticRegression()

lr.fit(
    X_train_scaled,
    y_train
)


# ==========================================================
# 6. DECISION TREE
# ==========================================================

dt = DecisionTreeClassifier(
    random_state=42
)

dt.fit(
    X_train_scaled,
    y_train
)


# ==========================================================
# 7. PREDICTIONS
# ==========================================================

lr_predictions = lr.predict(
    X_test_scaled
)

dt_predictions = dt.predict(
    X_test_scaled
)


print("\nLogistic Regression Predictions:")
print(lr_predictions)


# ==========================================================
# 8. ACCURACY
# ==========================================================

lr_accuracy = accuracy_score(
    y_test,
    lr_predictions
)

dt_accuracy = accuracy_score(
    y_test,
    dt_predictions
)

print(
    "\nThe accuracy of Logistic Regression is:",
    lr_accuracy
)

print(
    "The accuracy of Decision Tree is:",
    dt_accuracy
)


# ==========================================================
# 9. CONFUSION MATRIX
# ==========================================================

lr_cm = confusion_matrix(
    y_test,
    lr_predictions
)

dt_cm = confusion_matrix(
    y_test,
    dt_predictions
)

print("\nLogistic Regression Confusion Matrix:")
print(lr_cm)

print("\nDecision Tree Confusion Matrix:")
print(dt_cm)


# ==========================================================
# 10. DECISION BOUNDARY
# ==========================================================

x_min = df["distance_km"].min() - 1
x_max = df["distance_km"].max() + 1

y_min = df["time_left_minutes"].min() - 1
y_max = df["time_left_minutes"].max() + 1


xx, yy = np.meshgrid(
    np.linspace(
        x_min,
        x_max,
        300
    ),
    np.linspace(
        y_min,
        y_max,
        300
    )
)


grid = pd.DataFrame({
    "distance_km": xx.ravel(),
    "time_left_minutes": yy.ravel()
})


grid_scaled = scaler.transform(
    grid
)


# Logistic Regression decision boundary
Z = lr.predict(
    grid_scaled
).reshape(
    xx.shape
)


plt.figure(
    figsize=(9, 6)
)


plt.contourf(
    xx,
    yy,
    Z,
    alpha=0.3,
    cmap="RdYlGn_r"
)


colors = df["will_be_late"].map({
    0: "green",
    1: "red"
})


plt.scatter(
    df["distance_km"],
    df["time_left_minutes"],
    c=colors,
    alpha=0.6,
    edgecolors="k",
    linewidths=0.3
)


plt.xlabel(
    "Distance from Home (km)"
)

plt.ylabel(
    "Time Left Before Late (minutes)"
)

plt.title(
    "Decision Boundary - Will You Be Late?"
)


from matplotlib.patches import Patch


legend_elements = [
    Patch(
        facecolor="green",
        alpha=0.6,
        label="On Time (0)"
    ),
    Patch(
        facecolor="red",
        alpha=0.6,
        label="Late (1)"
    )
]


plt.legend(
    handles=legend_elements
)


plt.savefig(
    "decision_boundary.png",
    dpi=150,
    bbox_inches="tight"
)


plt.show()


# ==========================================================
# 11. SAVE MODEL
# ==========================================================

joblib.dump(
    lr,
    "late_to_office_model.pkl"
)

joblib.dump(
    scaler,
    "late_to_office_scaler.pkl"
)


print(
    "\nModel saved as: late_to_office_model.pkl"
)

print(
    "Scaler saved as: late_to_office_scaler.pkl"
)


# ==========================================================
# 12. PREDICTION ON NEW DATA
# ==========================================================

# Example:
# 15 km away and only 20 minutes left

sample = pd.DataFrame({
    "distance_km": [15],
    "time_left_minutes": [20]
})


sample_scaled = scaler.transform(
    sample
)


prediction = lr.predict(
    sample_scaled
)


probability = lr.predict_proba(
    sample_scaled
)


print("\nNew Data Prediction:")

print(
    "Prediction:",
    "Late"
    if prediction[0] == 1
    else "On Time"
)


print(
    "Probability - On Time: {:.2f}, Late: {:.2f}".format(
        probability[0][0],
        probability[0][1]
    )
)