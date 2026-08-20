# AIML Learning - Day 12

## Topic: R² and Adjusted R²

Today I learned about **R² (R-squared)** and **Adjusted R²**, two important evaluation metrics used in regression problems.

## Topics Covered

* Limitations of MAE, MSE, and RMSE when comparing different problems
* Baseline model
* R² (R-squared)
* R² formula
* Interpretation of R²
* Comparing regression models using R²
* Scale independence of R²
* Strengths and weaknesses of R²
* Why R² increases when additional features are added
* Degrees of freedom
* Adjusted R²
* Adjusted R² formula
* Complexity penalty in Adjusted R²
* Comparing R² and Adjusted R²
* Strengths and weaknesses of Adjusted R²
* Choosing the appropriate regression metric

## Key Learnings

### R²

R² measures how much of the variation in the target variable is explained by the regression model.

Formula:

**R² = 1 - (SS_res / SS_tot)**

Where:

* `SS_res` = Sum of Squared Residuals
* `SS_tot` = Total Sum of Squares

### Interpretation of R²

* **R² = 1** → Perfect model
* **R² = 0** → Model is no better than predicting the mean
* **R² < 0** → Model performs worse than the baseline model
* **R² = 0.90** → Model explains 90% of the variation in the target variable

### Adjusted R²

Adjusted R² improves upon R² by adding a penalty for unnecessary features.

Formula:

**Adjusted R² = 1 - ((1 - R²) × (n - 1) / (n - p - 1))**

Where:

* `n` = Number of data points
* `p` = Number of input features
* `R²` = Regular R² score

### Main Difference

**R²** generally increases when more features are added, even if those features are not useful.

**Adjusted R²** considers the number of features and penalizes the model when an added feature does not improve the model sufficiently.

## Metrics Summary

| Metric      | Main Purpose                                                       |
| ----------- | ------------------------------------------------------------------ |
| MAE         | Measures average absolute error                                    |
| MSE         | Measures average squared error and strongly penalizes large errors |
| RMSE        | Measures error in the same units as the target                     |
| R²          | Measures the fraction of variation explained by the model          |
| Adjusted R² | Measures explained variation while penalizing unnecessary features |

## Practical Takeaway

* Use **RMSE** when you want an error measure in the same units as the target.
* Use **R²** for a quick understanding of how much variation the model explains.
* Use **Adjusted R²** when comparing models with different numbers of features.
* A useful feature should improve the model enough to justify the additional complexity.

## Learning Outcome

By the end of Day 12, I understood how **R² evaluates regression performance** and how **Adjusted R² provides a fairer evaluation when models contain different numbers of features**.


