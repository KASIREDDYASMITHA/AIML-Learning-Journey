
# Day 9 - Linear Regression
# Linear Regression from Scratch + sklearn

import numpy as np
from sklearn.linear_model import LinearRegression


# =========================================================
# Dataset
# =========================================================

X_train = np.array([3, 4, 5, 6, 7, 8])
y_train = np.array([19, 33, 47, 61, 75, 89])


# =========================================================
# 1. Closed Form Solution
# =========================================================

n = len(X_train)

sum_x = np.sum(X_train)
sum_y = np.sum(y_train)
sum_x2 = np.sum(X_train ** 2)
sum_xy = np.sum(X_train * y_train)

m = (
    n * sum_xy - sum_x * sum_y
) / (
    n * sum_x2 - sum_x ** 2
)

b = (sum_y - m * sum_x) / n

print("===== Closed Form Solution =====")
print("m =", m)
print("b =", b)
print("Equation: y =", m, "x +", b)


# =========================================================
# 2. Linear Regression From Scratch
# =========================================================

class ManaLR:

    def __init__(self):
        self.m = None
        self.b = None

    def fit(self, X_train, y_train):

        num = 0
        den = 0

        x_bar = X_train.mean()
        y_bar = y_train.mean()

        for i in range(X_train.shape[0]):

            num += (
                (X_train[i] - x_bar)
                * (y_train[i] - y_bar)
            )

            den += (
                (X_train[i] - x_bar) ** 2
            )

        self.m = num / den

        self.b = y_bar - (
            self.m * x_bar
        )

    def predict(self, X_test):

        return self.m * X_test + self.b


# =========================================================
# 3. Train ManaLR
# =========================================================

lr = ManaLR()

lr.fit(X_train, y_train)

print("\n===== ManaLR =====")
print("m =", lr.m)
print("b =", lr.b)


# =========================================================
# 4. Prediction
# =========================================================

X_test = np.array([9, 10])

predictions = lr.predict(X_test)

print("\n===== Predictions =====")
print("Input:", X_test)
print("Prediction:", predictions)


# =========================================================
# 5. sklearn Linear Regression
# =========================================================

sklearn_lr = LinearRegression()

sklearn_lr.fit(
    X_train.reshape(-1, 1),
    y_train
)

print("\n===== sklearn LinearRegression =====")
print("Coefficient:", sklearn_lr.coef_)
print("Intercept:", sklearn_lr.intercept_)


# =========================================================
# 6. Final Comparison
# =========================================================

print("\n===== Final Comparison =====")

print("Closed Form")
print("m =", m)
print("b =", b)

print("\nManaLR")
print("m =", lr.m)
print("b =", lr.b)

print("\nsklearn")
print("m =", sklearn_lr.coef_[0])
print("b =", sklearn_lr.intercept_)