# Day 10 – Multiple Linear Regression & Model Evaluation

## 📌 Topics Covered

Today I continued my Machine Learning learning journey and studied **Multiple Linear Regression** and **Regression Model Evaluation**.

The main topics covered were:

* Why a single input feature is sometimes not enough
* Multiple Linear Regression
* Multiple Linear Regression equation
* Interpretation of coefficients
* Normal Equation / Closed Form Solution
* Gradient Descent
* Why model evaluation is important
* Mean Absolute Error (MAE)
* Mean Squared Error (MSE)
* Root Mean Squared Error (RMSE)
* Comparing regression models using evaluation metrics

---

## 🧠 What I Learned

### 1. Multiple Linear Regression

Real-world datasets usually contain multiple input features that can influence the target value.

For example, when predicting house prices, factors such as:

* House size
* Number of bedrooms
* Age of the building
* Distance from school
* Neighbourhood quality

can all affect the price.

Multiple Linear Regression allows us to use multiple input features together.

### Equation

ŷ = m₁x₁ + m₂x₂ + m₃x₃ + ... + mₙxₙ + b

Where:

* `ŷ` = predicted output
* `x₁, x₂, ..., xₙ` = input features
* `m₁, m₂, ..., mₙ` = coefficients
* `b` = intercept

Each feature has its own coefficient.

---

## 📊 Understanding Coefficients

Each coefficient represents the effect of one feature on the predicted output while keeping the other features constant.

For example:

* A positive coefficient means the output tends to increase as the feature increases.
* A negative coefficient means the output tends to decrease as the feature increases.
* The magnitude of the coefficient represents the strength of the feature's effect in the model.

---

## 🧮 Normal Equation

Multiple Linear Regression also has a closed-form solution called the **Normal Equation**.

β = (XᵀX)⁻¹Xᵀy

Where:

* `X` = matrix containing the input data
* `y` = vector containing the actual outputs
* `β` = coefficient vector

The Normal Equation can directly calculate the optimal coefficients.

However, matrix inversion can become computationally expensive for datasets with many features.

---

## ⚙️ Gradient Descent

Gradient Descent is an iterative optimization technique used to find suitable model parameters by reducing the loss.

The basic process is:

1. Start with an initial guess for the coefficients.
2. Calculate the prediction error.
3. Calculate the loss.
4. Adjust the coefficients in the direction that reduces the loss.
5. Repeat the process until the model converges.

Gradient Descent is an important optimization technique used throughout Machine Learning.

---

# 📈 Regression Model Evaluation

After training a regression model, we need to measure how well it performs.

Instead of relying on intuition, we use numerical evaluation metrics.

The main regression metrics I learned today are:

* MAE
* MSE
* RMSE

---

## 1. Mean Absolute Error (MAE)

MAE measures the average absolute difference between actual and predicted values.

### Formula

MAE = (1/n) Σ |yᵢ − ŷᵢ|

### Key Points

* Easy to understand.
* Uses the same unit as the target variable.
* Treats all errors equally.
* Less affected by individual large errors compared with MSE and RMSE.

---

## 2. Mean Squared Error (MSE)

MSE calculates the average of the squared errors.

### Formula

MSE = (1/n) Σ (yᵢ − ŷᵢ)²

Because the errors are squared, large errors receive much more penalty.

For example:

* Error of `2` → squared error = `4`
* Error of `10` → squared error = `100`

Therefore, MSE is highly sensitive to large errors and outliers.

---

## 3. Root Mean Squared Error (RMSE)

RMSE is the square root of MSE.

### Formula

RMSE = √[(1/n) Σ (yᵢ − ŷᵢ)²]

Taking the square root brings the metric back to the same unit as the target variable.

RMSE combines:

* The interpretability of being in the original unit.
* The ability to penalize large errors.

---

## 📊 MAE vs MSE vs RMSE

| Metric | Main Idea              | Large Error Penalty | Same Unit as Output |
| ------ | ---------------------- | ------------------- | ------------------- |
| MAE    | Average absolute error | Low                 | Yes                 |
| MSE    | Average squared error  | High                | No                  |
| RMSE   | Square root of MSE     | High                | Yes                 |

A lower value generally indicates better regression performance.

---

## 🔍 Important Observation

Suppose two models have:

* Model A: MAE = 2.0
* Model B: MAE = 2.0

MAE alone may consider both models equally good.

However, if Model B contains one very large error, MSE and RMSE will increase significantly because they penalize large errors more heavily.

Therefore, looking at multiple evaluation metrics gives a better understanding of model performance.

---

# 💻 Practical Work

I also implemented Linear Regression using Python and Scikit-learn.

### Libraries Used

* NumPy
* Pandas
* Scikit-learn

### Main Steps

1. Import the required libraries.
2. Load the dataset using Pandas.
3. Separate input feature `X` and target variable `y`.
4. Split the dataset into training and testing sets.
5. Create a `LinearRegression` model.
6. Train the model using the training data.
7. Access the model coefficient.
8. Access the model intercept.

---

## 🛠️ Technologies Used

* Python
* NumPy
* Pandas
* Scikit-learn
* Jupyter Notebook / Google Colab

---

## 🎯 Day 10 Learning Outcome

By the end of Day 10, I learned how regression can be extended from a single input feature to multiple features and how regression models can be evaluated using numerical metrics.

I also understood the differences between **MAE, MSE, and RMSE**, and why choosing the right evaluation metric is important when measuring model performance.

---

## 📚 Key Takeaways

* Real-world datasets usually contain multiple features.
* Multiple Linear Regression uses multiple input features to predict an output.
* Every feature has its own coefficient.
* The Normal Equation provides a closed-form solution.
* Gradient Descent provides an iterative approach to optimization.
* Model performance should be measured using numerical metrics.
* MAE is simple and interpretable.
* MSE strongly penalizes large errors.
* RMSE is in the same unit as the target and still penalizes large errors.
* Comparing multiple metrics provides a better picture of model performance.
