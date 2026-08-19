# AIML Learning Journey – Day 11

## Topic: R² (R-Squared) Metric

Today I learned about the R² (R-Squared) metric used for evaluating regression models.

### Topics Covered

- Limitations of MAE, MSE, and RMSE
- Baseline model
- Mean-based prediction
- R² intuition
- R² formula
- SS_res (Residual Sum of Squares)
- SS_tot (Total Sum of Squares)
- Interpretation of R² values
- Why R² is scale-independent

---

## 1. Problem with MAE, MSE, and RMSE

MAE, MSE, and RMSE depend on the scale and units of the target variable.

For example:

- House price prediction:
  - RMSE = 5 lakhs
- Age prediction:
  - RMSE = 5 years

Although both models have RMSE = 5, we cannot directly say that they perform equally well.

The reason is that RMSE depends on the scale of the target variable.

---

## 2. Baseline Model

A baseline model is the simplest possible regression model.

It completely ignores the input features and predicts the mean of the target variable for every data point.

For example, if:

```text
Mean of y = 30