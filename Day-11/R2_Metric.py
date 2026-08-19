
# Day 11 - R² (R-Squared) Metric
# AIML Learning Journey

# Actual target values
y_actual = [10, 20, 30, 40, 50]

# Model predictions
y_pred = [12, 22, 28, 42, 48]

# Mean of actual values
y_mean = sum(y_actual) / len(y_actual)

# SS_tot - Total Sum of Squares
ss_tot = sum((y - y_mean) ** 2 for y in y_actual)

# SS_res - Residual Sum of Squares
ss_res = sum((y - pred) ** 2 for y, pred in zip(y_actual, y_pred))

# R² calculation
r2 = 1 - (ss_res / ss_tot)

print("Actual Values:", y_actual)
print("Predicted Values:", y_pred)
print("Mean of y:", y_mean)
print("SS_tot:", ss_tot)
print("SS_res:", ss_res)
print("R² Score:", r2)