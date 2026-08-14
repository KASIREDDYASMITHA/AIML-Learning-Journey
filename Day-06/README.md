# Day 6 - Linear Regression: Finding the Best Line Mathematically

## Overview

Day 6 focuses on understanding how Linear Regression mathematically finds the best-fitting line by minimizing the total squared error.

The session moves from intuition to a mathematical approach using loss, derivatives, partial derivatives, and the closed-form solution.

---

## Topics Covered

* Linear Regression
* Equation of a straight line
* Slope (`m`) and intercept (`b`)
* Prediction
* Error and squared error
* Total squared loss
* Minimizing loss
* Varying the intercept while fixing the slope
* Varying the slope while fixing the intercept
* U-shaped loss curve
* Derivative and minimum point
* Partial derivatives
* Loss as a function of `m` and `b`
* Closed-form solution
* Normal equations
* Verification of the solution

---

## Linear Regression Equation

The equation of a straight line is:

```text
y = mx + b
```

Where:

* `m` = slope
* `b` = intercept
* `x` = input
* `y` = actual output

Prediction:

```text
ŷ = mx + b
```

---

## Loss Function

The total squared loss is:

```text
L(m, b) = Σ [yᵢ - (mxᵢ + b)]²
```

The objective is to find the values of `m` and `b` that minimize this loss.

---

## Mathematical Optimization

At the minimum of the loss:

```text
∂L / ∂m = 0
∂L / ∂b = 0
```

Solving these equations gives the closed-form solution for the slope and intercept.

### Slope

```text
m = [nΣxy - (Σx)(Σy)] / [nΣx² - (Σx)²]
```

### Intercept

```text
b = [Σy - mΣx] / n
```

---

## Example Dataset

```text
x = [1, 2, 3, 4, 5]

y = [7, 9, 11, 13, 15]
```

The calculated values are:

```text
m = 2
b = 5
```

Therefore, the best line is:

```text
y = 2x + 5
```

---

## Key Learning

The important idea from this session is that the best Linear Regression line is not selected by guessing.

We define a loss function and mathematically minimize it.

The overall process is:

```text
Data
  ↓
Prediction
  ↓
Error
  ↓
Squared Error
  ↓
Total Loss
  ↓
Find Minimum
  ↓
Derivatives / Partial Derivatives
  ↓
Closed-Form Solution
  ↓
Best m and b
```

---

## Files in This Folder

* `notes.md` - Detailed notes from Day 6
* `README.md` - Overview, concepts, formulas, and key learning from Day 6
