# Day 12 - R² and Adjusted R²

## 1. Introduction

In regression, we need evaluation metrics to understand how well our model performs.

Previously, I learned about:

* MAE (Mean Absolute Error)
* MSE (Mean Squared Error)
* RMSE (Root Mean Squared Error)

Today, we learned:

* R² (R-squared)
* Adjusted R²
* Baseline model
* Degrees of freedom
* Model complexity and feature selection

---

## 2. The Hidden Problem with MAE, MSE, and RMSE

MAE, MSE, and RMSE depend on the scale and units of the target variable.

For example:

### House Price Prediction

RMSE = 5 lakhs

### Age Prediction

RMSE = 5 years

Both models have RMSE = 5, but we cannot directly say that both models are equally good.

The reason is that the target variables have different scales and units.

Therefore, RMSE alone is not enough to compare model performance across completely different problems.

---

## 3. Baseline Model

A baseline model is the simplest possible regression model.

It ignores all input features and always predicts the mean of the target variable.

For example:

```text
Actual y:
10, 20, 30, 40, 50

Mean:
30
```

The baseline model predicts:

```text
30, 30, 30, 30, 30
```

The baseline model uses no information from the input features.

A useful regression model should perform better than this baseline.

---

## 4. R² (R-squared)

R² is a regression evaluation metric that tells us how much of the variation in the target variable is explained by the model.

R² compares our model with the baseline model.

It is also called the **coefficient of determination**.

### Formula

```text
R² = 1 - (SS_res / SS_tot)
```

Where:

```text
SS_res = Σ(yᵢ - ŷᵢ)²
```

```text
SS_tot = Σ(yᵢ - ȳ)²
```

Where:

* `yᵢ` = Actual value
* `ŷᵢ` = Predicted value
* `ȳ` = Mean of actual target values

### SS_res

SS_res represents the error remaining in the model.

```text
SS_res = Sum of squared residuals
```

### SS_tot

SS_tot represents the error of the baseline mean model.

```text
SS_tot = Total sum of squares
```

---

## 5. Interpretation of R²

### R² = 1

Perfect model.

```text
SS_res = 0
```

The model explains all the variation in the target.

### R² = 0

The model is no better than predicting the mean.

```text
SS_res = SS_tot
```

### R² < 0

The model performs worse than the baseline model.

### Example

```text
R² = 0.90
```

This means the model explains approximately **90% of the variation** in the target variable.

---

## 6. Why R² Is Scale Independent

R² is a pure number and has no units.

```text
R² = 1 - (SS_res / SS_tot)
```

SS_res and SS_tot have the same units, so the units cancel during division.

This makes R² useful for comparing regression performance across problems with different units and scales.

Example:

```text
House Price Prediction
RMSE = 5 lakhs
R² = 0.95

Age Prediction
RMSE = 5 years
R² = 0.40
```

Although both problems have RMSE = 5, their R² values clearly show different model performance.

---

## 7. Example: Calculating R²

Consider:

```text
Actual y:
10, 20, 30, 40, 50

Mean:
30

SS_tot = 1000
```

### Model A

Predictions:

```text
12, 22, 28, 42, 48
```

```text
SS_res = 20
```

Calculate:

```text
R² = 1 - (20 / 1000)

R² = 1 - 0.02

R² = 0.98
```

Therefore:

```text
R² = 0.98
```

Model A explains **98% of the variation** in the target.

### Model B

Predictions:

```text
10, 20, 30, 40, 50
```

For the example used in the notes:

```text
SS_res = 100
```

Therefore:

```text
R² = 1 - (100 / 1000)

R² = 1 - 0.10

R² = 0.90
```

Therefore:

```text
R² = 0.90
```

Model B explains **90% of the variation** in the target.

### Comparison

```text
Model A → R² = 0.98
Model B → R² = 0.90
```

Therefore, Model A is better according to R².

---

## 8. R² Comparison with Other Metrics

| Metric | Model A | Model B | Winner  |
| ------ | ------: | ------: | ------- |
| MAE    |     2.0 |     2.0 | Tie     |
| MSE    |     4.0 |    20.0 | Model A |
| RMSE   |     2.0 |    4.47 | Model A |
| R²     |    0.98 |    0.90 | Model A |

R² confirms what MSE and RMSE already indicate in this example.

---

## 9. R² Strengths

### 1. Scale Independent

R² can be compared across problems with different units and magnitudes.

### 2. Easy to Interpret

For example:

```text
R² = 0.90
```

means the model explains 90% of the variation in the target variable.

### 3. Universally Reported

R² is commonly reported for regression problems.

---

## 10. R² Weaknesses

The main problem with R² is that it generally increases when more features are added.

This can happen even when the added features are useless.

R² does not include a complexity penalty.

Therefore, adding junk or random features can create a false sense of improvement.

---

## 11. Example: R² with a Useless Feature

Suppose we have two house price models.

### Model 1

Feature:

```text
Size
```

```text
R² = 0.90
```

### Model 2

Features:

```text
Size
Random Noise
```

```text
R² = 0.92
```

The random noise feature contains no useful information.

However:

```text
R² increased from 0.90 → 0.92
```

This does not necessarily mean the model genuinely improved.

R² cannot distinguish between useful and useless features.

Therefore, we need a metric that considers model complexity.

---

## 12. Degrees of Freedom

Degrees of freedom represent the amount of flexibility available to the model relative to the amount of data and number of features.

Formula:

```text
Degrees of Freedom = n - p - 1
```

Where:

* `n` = Number of data points
* `p` = Number of input features

As the number of features increases, the available degrees of freedom decrease.

Each additional input feature gives the model another lever to fit the data.

A model can use this additional flexibility to fit noise, even if the new feature contains no useful signal.

A model that achieves good performance with fewer useful features is generally more trustworthy.

---

## 13. Adjusted R²

Adjusted R² is a modified version of R² that considers the number of input features.

It adds a penalty for unnecessary model complexity.

### Formula

```text
Adjusted R² = 1 - ((1 - R²) × (n - 1) / (n - p - 1))
```

Where:

* `n` = Number of data points
* `p` = Number of input features
* `R²` = Regular R² score

---

## 14. How the Adjusted R² Penalty Works

When a new feature is added:

### Useful Feature

If the new feature improves the model sufficiently:

```text
Adjusted R² increases
```

### Useless Feature

If the new feature does not improve the model sufficiently:

```text
Adjusted R² decreases
```

Therefore, every new feature must justify its existence.

Adjusted R² penalizes the model when it uses additional degrees of freedom without gaining enough explanatory power.

---

## 15. Example: Adjusted R²

Consider:

```text
Model 1:
Features = Size
R² = 0.90
Adjusted R² = 0.867
```

```text
Model 2:
Features = Size + Random Noise
R² = 0.92
Adjusted R² = 0.840
```

For Model 2:

```text
n = 5
p = 2
R² = 0.92
```

Formula:

```text
Adjusted R²
= 1 - ((1 - 0.92) × (5 - 1) / (5 - 2 - 1))
```

Step 1:

```text
= 1 - (0.08 × 4 / 2)
```

Step 2:

```text
= 1 - 0.16
```

Step 3:

```text
= 0.840
```

Therefore:

```text
Adjusted R² = 0.840
```

Here:

```text
R²:
0.90 → 0.92
```

But:

```text
Adjusted R²:
0.867 → 0.840
```

R² suggests an improvement, but Adjusted R² shows that the additional random noise feature made the model worse after considering complexity.

---

## 16. R² vs Adjusted R²

| R²                                          | Adjusted R²                                                     |
| ------------------------------------------- | --------------------------------------------------------------- |
| Measures variation explained by the model   | Measures variation explained while considering model complexity |
| Generally increases when features are added | Can increase or decrease when features are added                |
| Does not penalize unnecessary features      | Penalizes unnecessary features                                  |
| Useful for quick evaluation                 | Useful when comparing models with different feature counts      |
| Can give a false sense of improvement       | Gives a fairer comparison                                       |

---

## 17. Adjusted R² Strengths

### 1. Penalizes Complexity

Adding useless features is penalized instead of automatically being rewarded.

### 2. Fairer Model Comparison

It is more useful when comparing models with different numbers of features.

### 3. Helps with Feature Selection

It helps determine whether adding a feature is worth the additional complexity.

---

## 18. Adjusted R² Weaknesses

### 1. Less Intuitive

The formula is more complicated than regular R².

### 2. Still Manipulable

Many moderately useful features can still increase the score together.

### 3. Regression Only

Adjusted R² is used for regression problems.

---

## 19. All Five Regression Metrics

| Metric      | What It Measures                | Unit           | Best Used When                                      |
| ----------- | ------------------------------- | -------------- | --------------------------------------------------- |
| MAE         | Average absolute error          | Same as output | Errors are roughly equal in importance              |
| MSE         | Average squared error           | Squared output | Large errors must be penalized heavily              |
| RMSE        | Root of MSE                     | Same as output | You want MSE sensitivity with readable units        |
| R²          | Fraction of variation explained | None           | Comparing models across different problems          |
| Adjusted R² | R² with complexity penalty      | None           | Comparing models with different numbers of features |

---

## 20. Practical Usage

### MAE

Use MAE when errors are roughly equal in importance and you want the average absolute error.

### MSE

Use MSE when large errors should be penalized heavily.

### RMSE

Use RMSE when you want sensitivity to large errors while keeping the result in the same units as the target.

### R²

Use R² for a quick understanding of how much variation in the target is explained by the model.

### Adjusted R²

Use Adjusted R² when comparing models with different numbers of features.

---

## 21. Practical Recommendation

For regression problems:

```text
RMSE + R²
```

can provide a useful overall picture.

When comparing models with different numbers of features, also consider:

```text
Adjusted R²
```

RMSE tells us about prediction error in the target's units.

R² tells us how much variation is explained.

Adjusted R² additionally considers model complexity.

---

# 22. Key Takeaways

* MAE, MSE, and RMSE are tied to the scale of the target variable.
* The baseline model predicts the mean every time.
* A regression model should ideally perform better than the baseline.
* R² measures how much variation in the target variable is explained by the model.
* R² is scale independent.
* R² = 1 represents a perfect model.
* R² = 0 means the model is no better than predicting the mean.
* R² < 0 means the model performs worse than the baseline.
* R² generally increases when features are added.
* R² does not penalize unnecessary features.
* Degrees of freedom decrease as the number of features increases.
* Adjusted R² considers the number of input features.
* Adjusted R² penalizes unnecessary features.
* A useful feature can increase Adjusted R².
* A useless feature can decrease Adjusted R².
* Adjusted R² is useful when comparing models with different numbers of features.

---

# 23. Final Summary

## R²

```text
R² = 1 - (SS_res / SS_tot)
```

R² tells us how much variation in the target variable is explained by the model.

```text
R² = 1       → Perfect model
R² = 0       → Same as baseline
R² < 0       → Worse than baseline
```

## Adjusted R²

```text
Adjusted R²
= 1 - ((1 - R²) × (n - 1) / (n - p - 1))
```

Adjusted R² considers both:

1. Model performance
2. Number of input features

Therefore:

```text
R² → Quick regression evaluation

Adjusted R² → Fairer comparison when feature counts differ
```

**Main Learning:**

R² tells us how well the model explains the variation in the target, while Adjusted R² additionally checks whether the improvement is justified by the number of features used.
