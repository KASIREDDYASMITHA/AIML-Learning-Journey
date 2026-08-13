# Day 5 — Linear Regression

## AIML Learning Journey

Today I learned the fundamentals of **Linear Regression** and how a machine learning model finds the best line for making predictions.

---

# 1. What is Linear Regression?

Linear Regression is a supervised machine learning algorithm used to predict a continuous numerical output.

The basic idea is:

- We have input data `x`
- We have an output/target `y`
- We try to find a relationship between `x` and `y`
- We represent that relationship using a straight line
- The goal is to find the line that makes the smallest possible prediction error

The basic equation is:

y = mx + b

Where:

- `y` = predicted output
- `x` = input feature
- `m` = slope
- `b` = intercept

The prediction is often written as:

ŷ = mx + b

Here, `ŷ` means the predicted value of `y`.

---

# 2. Understanding the Pattern

Consider the following data:

| x | y |
|---|---|
| 1 | 7 |
| 2 | 9 |
| 3 | 11 |
| 4 | 13 |
| 5 | 15 |

The pattern is:

y = 2x + 5

For every increase of 1 in `x`, `y` increases by 2.

Therefore:

- Slope `m = 2`
- Intercept `b = 5`

For example:

When x = 1:

y = 2(1) + 5 = 7

When x = 5:

y = 2(5) + 5 = 15

This is a clean example where the relationship can be described perfectly by a straight line.

---

# 3. Slope

The slope tells us how much the predicted output changes when the input increases by one unit.

In:

y = 2x + 5

the slope is:

m = 2

This means:

For every 1-unit increase in `x`, the predicted `y` increases by 2.

### Example 1

If:

y = 3x + 4

then:

m = 3

So when `x` increases by 1, predicted `y` increases by 3.

### Example 2

If:

y = -2x + 10

then:

m = -2

So when `x` increases by 1, predicted `y` decreases by 2.

---

# 4. Intercept

The intercept is the predicted value of `y` when:

x = 0

In:

y = 2x + 5

when x = 0:

y = 5

Therefore:

b = 5

The intercept shifts the entire line upward or downward.

### Example 1

y = 3x + 7

Intercept = 7

### Example 2

y = 5x - 2

Intercept = -2

---

# 5. Real-World Data Has Noise

Real-world data is usually not perfectly clean.

Measurements can contain errors and different variables can interact with each other.

Example noisy dataset:

| x | y |
|---|---|
| 1 | 8 |
| 2 | 10 |
| 3 | 14 |
| 4 | 12 |
| 5 | 17 |
| 6 | 16 |
| 7 | 20 |

There is still a general pattern:

As `x` increases, `y` tends to increase.

However, there is no perfect line that passes through every point.

This is called **noise**.

The important idea is:

> Real-world machine learning data is usually messy, so the model tries to find the best approximation rather than an exact rule.

---

# 6. Prediction

A linear regression model uses:

ŷ = mx + b

to produce a prediction.

Suppose the line is:

y = 2x + 3

For:

x = 3

the predicted value is:

ŷ = 2(3) + 3
ŷ = 9

If the actual value is:

y = 14

then the prediction is 9 while the actual value is 14.

---

# 7. Error

The error represents the difference between the actual value and the predicted value.

Error = Actual - Predicted

Using the previous example:

Actual = 14
Predicted = 9

Error = 14 - 9
Error = +5

The model undershot the actual value by 5 units.

Every data point can have its own prediction error.

---

# 8. Why We Cannot Simply Add Errors

Suppose some errors are positive and some are negative.

If we simply add them:

+5 + (-5) = 0

This might make the model look perfect even though the individual predictions are wrong.

Therefore, raw error is not a reliable overall measure of model quality.

Positive and negative errors can cancel each other.

---

# 9. Squared Error

To avoid positive and negative errors cancelling each other, we square each error.

Squared Error = Error²

For example:

Error = +5

Squared Error:

5² = 25

For:

Error = -5

Squared Error:

(-5)² = 25

After squaring, all errors become non-negative.

Squaring also gives greater importance to larger errors.

---

# 10. Total Squared Error

To evaluate an entire line, we calculate the squared error for every data point and add them together.

Total Squared Error:

TSE = Σ(Actual - Predicted)²

A lower Total Squared Error means the line is a better fit to the data.

---

# 11. Comparing Two Models

Consider the noisy dataset.

## Model A

Equation:

y = 2x + 3

The total squared error is:

70

## Model B

Equation:

y = 4x - 2

The total squared error is:

145

Therefore:

Model A is better because:

70 < 145

The model with the lower total squared error is the better-fitting model.

---

# 12. Comparing Three Candidate Lines

For the same noisy dataset:

| Line | Equation | Total Loss |
|---|---|---:|
| Line 1 | y = x + 5 | 196 |
| Line 2 | y = 2x + 3 | 70 |
| Line 3 | y = 2.5x + 2 | 49 |

The best line among these three is:

y = 2.5x + 2

because it has the lowest total squared error:

49

Important:

The best line does not have to produce zero error.

It only needs to produce the **minimum loss** among the candidate lines.

---

# 13. Loss

Loss is a measure of how wrong the model's predictions are.

For linear regression in today's lesson, we used Total Squared Error as the loss.

Conceptually:

- Smaller loss → better predictions
- Larger loss → worse predictions

The goal of linear regression is to find the line with the lowest possible loss.

---

# 14. Important Difference: Error vs Loss

### Error

Error is calculated for an individual prediction.

Error = Actual - Predicted

Example:

Actual = 14
Predicted = 9

Error = 14 - 9 = 5

### Loss

Loss measures the overall error across the dataset.

For today's linear regression lesson:

Loss = Total Squared Error

Therefore:

**Error → individual prediction**

**Loss → overall model performance**

---

# 15. Linear Regression as Finding the Best Line

Every straight line can be defined using two numbers:

- `m` = slope
- `b` = intercept

The equation is:

ŷ = mx + b

Different values of `m` and `b` produce different lines.

Linear Regression tries to find the values of `m` and `b` that minimize the total squared error.

Therefore:

Goal:

Find `m` and `b` such that:

Total Squared Error is minimum.

---

# 16. Core Intuition of Linear Regression

The complete idea can be understood as:

Input data
→ Find a pattern
→ Choose a line
→ Make predictions
→ Compare predictions with actual values
→ Calculate errors
→ Square the errors
→ Add the squared errors
→ Calculate loss
→ Find the line with minimum loss

---

# 17. Mathematical Representation

The linear regression prediction equation is:

ŷ = mx + b

Where:

`ŷ` = predicted output

`x` = input

`m` = slope

`b` = intercept

The error for one data point is:

Error = y - ŷ

The squared error is:

Squared Error = (y - ŷ)²

The total squared error is:

TSE = Σ(y - ŷ)²

The goal is:

Minimize TSE.

---

# 18. Key Understanding

Linear Regression is not about finding a line that perfectly passes through every data point.

Real-world data contains noise.

Instead, Linear Regression finds the line that is **least wrong overall** according to the chosen loss function.



# 19. What I Learned Today

- Linear Regression is used for predicting continuous numerical values.
- A linear model can be represented as `ŷ = mx + b`.
- `m` represents the slope.
- `b` represents the intercept.
- The slope determines how much the prediction changes when `x` changes.
- The intercept is the predicted value when `x = 0`.
- Real-world data contains noise.
- Predictions will usually not be exactly equal to actual values.
- Error measures the difference between actual and predicted values.
- Raw errors cannot simply be added because positive and negative errors can cancel.
- Squaring errors removes negative signs.
- Squaring also penalizes larger errors more strongly.
- Total Squared Error can be used to compare different lines.
- Lower loss means a better-fitting line.
- Linear Regression searches for the values of `m` and `b` that minimize the loss.
- The best model does not necessarily have zero error; it has the minimum error/loss for the data.

