# Day 6 - Linear Regression: Finding the Best Line Mathematically

## Topic

Linear Regression - Finding the Best Line Mathematically

---

## 1. What is Linear Regression?

Linear Regression tries to find the best straight line that represents the relationship between input `x` and output `y`.

The equation of a straight line is:

y = mx + b

Where:

- `m` = slope
- `b` = intercept
- `x` = input
- `y` = actual output
- `ŷ` = predicted output

The goal is to find the values of `m` and `b` that give the best possible fit to the data.

---

## 2. Perfect Dataset

Consider the following dataset:

| x | y |
|---|---|
| 1 | 7 |
| 2 | 9 |
| 3 | 11 |
| 4 | 13 |
| 5 | 15 |

Looking at the pattern:

- Every time `x` increases by 1, `y` increases by 2.
- Therefore, the slope `m = 2`.
- When `x = 0`, `y = 5`.
- Therefore, the intercept `b = 5`.

So the line is:

y = 2x + 5

Here:

m = 2
b = 5

---

## 3. Why Do We Need a Mathematical Method?

For a perfect dataset, we can find the line by observing the pattern.

But real-world datasets are usually noisy.

A line may not pass exactly through every data point.

Therefore, intuition alone is not enough.

We need a method that can mathematically find the line that gives the minimum error.

The answer starts with the concept of:

**Loss**

---

## 4. Loss

Loss measures how far the predictions made by our line are from the actual values.

For each data point:

Prediction:

ŷ = mx + b

Error:

y - ŷ

Squared error:

(y - ŷ)²

Total loss is the sum of the squared errors for all data points.

The loss function is:

L(m, b) = Σ [yᵢ - (mxᵢ + b)]²

Where:

- `yᵢ` = actual value
- `mxᵢ + b` = predicted value
- `(yᵢ - (mxᵢ + b))²` = squared error for one data point
- `n` = number of data points

The best line is the line that minimizes the total squared loss.

---

## 5. Comparing Different Lines

For the perfect dataset:

| Line | Total Loss |
|---|---:|
| y = 2x + 5 | 0 |
| y = 3x + 1 | 35 |

The line:

y = 2x + 5

has zero total loss because it passes through every data point exactly.

Therefore, it is the best line for this dataset.

However, with noisy real-world data, the best line usually has some non-zero loss.

---

# 6. Fix the Slope and Vary the Intercept

First, fix:

m = 1

Then change the value of `b`.

The different lines have different losses:

| b | Total Loss |
|---:|---:|
| 2 | 190 |
| 4 | 90 |
| 6 | 30 |
| 8 | 10 |
| 10 | 30 |

The lowest loss is:

b = 8

with:

Loss = 10

### Observation

For a fixed slope:

- As `b` changes, the loss changes.
- Loss first decreases.
- Loss reaches a minimum.
- Loss then increases again.

Therefore, there is a particular value of `b` that gives the minimum loss for the fixed slope.

---

# 7. Fix the Intercept and Vary the Slope

Now fix:

b = 2

Then change the value of `m`.

| m | Total Loss |
|---:|---:|
| 0 | 445 |
| 1 | 190 |
| 2 | 45 |
| 3 | 10 |
| 4 | 85 |

The lowest loss is:

m = 3

with:

Loss = 10

### Observation

For a fixed intercept:

- As `m` changes, the loss changes.
- Loss decreases.
- Loss reaches a minimum.
- Loss increases again.

Therefore, there is a particular value of `m` that gives the minimum loss for the fixed intercept.

---

# 8. Loss Curve

When we plot:

- `m` on the x-axis
- `Loss` on the y-axis

the loss forms a U-shaped curve.

Example:

| m | Loss |
|---:|---:|
| 0 | 445 |
| 1 | 190 |
| 2 | 45 |
| 3 | 10 |
| 4 | 85 |

The curve has a clear bottom.

The bottom represents the minimum loss.

Therefore:

**Best value of the parameter = value where the loss reaches its minimum.**

---

# 9. What Happens at the Minimum?

The slope of the loss curve changes as we move along the curve.

### Left side of minimum

Slope < 0

The loss is decreasing.

### At the minimum

Slope = 0

The loss has reached its lowest point.

### Right side of minimum

Slope > 0

The loss is increasing.

Therefore:

**At the minimum, the slope of the loss curve is zero.**

This gives us the mathematical condition for finding the best parameters.

---

# 10. Derivative

The slope of a curve at a particular point is represented mathematically by its derivative.

Derivative tells us the rate of change.

In this problem:

d(Loss) / dm

represents the slope of the loss curve with respect to `m`.

To find the minimum:

1. Differentiate the loss.
2. Set the derivative equal to zero.
3. Solve for the parameter.

Therefore:

d(Loss) / dm = 0

This converts the idea of finding the lowest point into an algebraic procedure.

---

# 11. Loss Depends on Both m and b

The loss does not depend only on `m`.

It depends on both:

- `m` = slope
- `b` = intercept

Therefore:

L = f(m, b)

Changing either `m` or `b` changes the loss.

When both parameters are considered together, the loss becomes a surface rather than just a curve.

The loss surface can be visualized like a bowl-shaped valley.

Our goal is to find the exact bottom of this surface.

---

# 12. Partial Derivatives

Because the loss depends on two variables, we use partial derivatives.

### Partial derivative with respect to m

∂L / ∂m

Here:

- `m` is treated as the variable.
- `b` is treated as fixed.

### Partial derivative with respect to b

∂L / ∂b

Here:

- `b` is treated as the variable.
- `m` is treated as fixed.

At the minimum:

∂L / ∂m = 0

and

∂L / ∂b = 0

We therefore have two equations and two unknowns:

- `m`
- `b`

Solving these equations gives the exact values of the slope and intercept.

---

# 13. Formal Loss Function

The total squared loss is:

L(m, b) = Σ [yᵢ - (mxᵢ + b)]²

For each data point:

Actual value:

yᵢ

Predicted value:

ŷᵢ = mxᵢ + b

Error:

yᵢ - ŷᵢ

Squared error:

(yᵢ - ŷᵢ)²

Total loss:

Σ (yᵢ - (mxᵢ + b))²

This is the quantity that we minimize.

---

# 14. Closed Form Solution

Setting both partial derivatives to zero:

∂L / ∂m = 0

∂L / ∂b = 0

Solving these equations gives the closed form solution, also called the normal equations.

## Slope Formula

m = [nΣxy - (Σx)(Σy)] / [nΣx² - (Σx)²]

## Intercept Formula

b = [Σy - mΣx] / n

These formulas allow us to directly calculate the exact values of `m` and `b`.

No iterative search is required for this solution.

---

# 15. Verify the Formula with the Dataset

Dataset:

| x | y | x² | xy |
|---:|---:|---:|---:|
| 1 | 7 | 1 | 7 |
| 2 | 9 | 4 | 18 |
| 3 | 11 | 9 | 33 |
| 4 | 13 | 16 | 52 |
| 5 | 15 | 25 | 75 |
| **Σ = 15** | **Σ = 55** | **Σ = 55** | **Σ = 185** |

Number of data points:

n = 5

---

## Calculate m

Formula:

m = [nΣxy - (Σx)(Σy)] / [nΣx² - (Σx)²]

Substitute the values:

m = [5 × 185 - 15 × 55] / [5 × 55 - 15²]

m = [925 - 825] / [275 - 225]

m = 100 / 50

m = 2

Therefore:

m = 2

---

## Calculate b

Formula:

b = [Σy - mΣx] / n

Substitute:

b = [55 - 2 × 15] / 5

b = [55 - 30] / 5

b = 25 / 5

b = 5

Therefore:

b = 5

---

# 16. Final Best Line

We obtained:

m = 2

b = 5

Therefore:

y = 2x + 5

This is exactly the same line that we found earlier by intuition.

The closed form mathematical solution confirms why that line is the best line for the given perfect dataset.

---

# 17. Key Observations

### Observation 1: Loss measures fit

The best line minimizes the total squared error.

### Observation 2: Loss changes with m and b

Changing either the slope or intercept changes the total loss.

### Observation 3: Loss has a minimum

When one parameter is varied while the other is fixed, the loss forms a U-shaped curve.

### Observation 4: Minimum means zero slope

At the bottom of the loss curve:

slope = 0

### Observation 5: Two parameters require two partial derivatives

Because loss depends on both `m` and `b`:

∂L / ∂m = 0

∂L / ∂b = 0

### Observation 6: Closed form gives the exact answer

Solving the equations gives:

m = 2

b = 5

Therefore:

y = 2x + 5

---

# 18. Important Formulas

### Line Equation

y = mx + b

### Prediction

ŷ = mx + b

### Error

y - ŷ

### Squared Error

(y - ŷ)²

### Total Squared Loss

L(m, b) = Σ [yᵢ - (mxᵢ + b)]²

### Minimum Condition

∂L / ∂m = 0

∂L / ∂b = 0

### Slope

m = [nΣxy - (Σx)(Σy)] / [nΣx² - (Σx)²]

### Intercept

b = [Σy - mΣx] / n

---

# 19. Day 6 Summary

Today I learned how Linear Regression can find the best line mathematically instead of relying only on intuition.

The main flow is:

Data
→ Prediction
→ Error
→ Squared Error
→ Total Loss
→ Minimize Loss
→ Derivatives
→ Partial Derivatives
→ Set them to Zero
→ Solve for m and b
→ Closed Form Solution

For the example dataset:

x = [1, 2, 3, 4, 5]

y = [7, 9, 11, 13, 15]

the exact solution is:

m = 2

b = 5

Best line:

y = 2x + 5