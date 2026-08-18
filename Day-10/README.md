# Day 10 – Multiple Linear Regression & Model Evaluation

## 📚 Topics Covered

Today I learned:

* Multiple Linear Regression
* Multiple input features
* Multiple Linear Regression equation
* Interpretation of coefficients
* Normal Equation
* Gradient Descent
* Regression Model Evaluation
* Mean Absolute Error (MAE)
* Mean Squared Error (MSE)
* Root Mean Squared Error (RMSE)

## 🧠 Learning Summary

### Multiple Linear Regression

Multiple Linear Regression is used when multiple input features are used to predict an output.

The equation is:

`ŷ = m₁x₁ + m₂x₂ + m₃x₃ + ... + mₙxₙ + b`

Each input feature has its own coefficient.

### Normal Equation

The Normal Equation provides a closed-form solution for finding the optimal coefficients:

`β = (XᵀX)⁻¹Xᵀy`

However, matrix inversion can become computationally expensive for large datasets with many features.

### Gradient Descent

Gradient Descent is an iterative approach used to reduce the loss and find suitable model parameters.

The process is:

1. Start with an initial guess.
2. Measure the prediction error.
3. Adjust the coefficients.
4. Repeat until convergence.

## 📊 Regression Metrics

### MAE

Measures the average absolute error.

`MAE = (1/n) Σ |yᵢ − ŷᵢ|`

### MSE

Measures the average squared error and penalizes large errors more heavily.

`MSE = (1/n) Σ (yᵢ − ŷᵢ)²`

### RMSE

RMSE is the square root of MSE and brings the metric back to the original output unit.

`RMSE = √[(1/n) Σ (yᵢ − ŷᵢ)²]`

## 💻 Practical Implementation

Today I implemented Linear Regression using:

* Python
* NumPy
* Pandas
* Scikit-learn

I practiced:

* Loading a CSV dataset
* Selecting input and target columns
* Splitting data into training and testing sets
* Creating a Linear Regression model
* Training the model
* Finding the coefficient
* Finding the intercept

## 🎯 Day 10 Outcome

Today I understood how regression can work with multiple features and how regression models can be evaluated using MAE, MSE, and RMSE.

**Day 10 of my AI/ML Learning Journey 🚀**
