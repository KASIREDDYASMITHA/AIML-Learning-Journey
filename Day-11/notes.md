# AIML Learning Journey – Day 11
# R² (R-Squared) – Regression Evaluation Metric

---

## 1. Today's Topic

Today I learned about R² (R-Squared), a regression evaluation metric.

### Topics Covered

- The hidden problem with MAE, MSE, and RMSE
- Baseline model
- Why the baseline model is important
- R² score
- R² intuition
- R² formula
- SS_res – Residual Sum of Squares
- SS_tot – Total Sum of Squares
- Interpretation of R² values
- Why R² is scale-independent

---

# 2. The Hidden Problem with MAE, MSE, and RMSE

MAE, MSE, and RMSE are commonly used metrics for evaluating regression models.

However, they have a hidden problem:

> MAE, MSE, and RMSE are tied to the scale of the data.

This means that the same error value can have completely different meanings depending on the problem.

---

## Example 1: House Price Prediction

Suppose we are predicting house prices.

The model has:

```text
RMSE = 5 lakhs