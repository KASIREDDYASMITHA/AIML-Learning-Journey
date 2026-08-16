# Day 8 - Linear Regression: Finding the Best Line Mathematically

## Topic

**Linear Regression — Finding the Best-Fit Line Mathematically**

Today's class focused on understanding how Linear Regression finds the best line using:

* Loss Function
* Total Squared Error
* Slope (`m`)
* Intercept (`b`)
* Loss Minimization
* U-shaped Loss Curve
* Derivative
* Chain Rule
* Partial Derivatives
* Closed-Form Solution
* Normal Equations
* Mathematical Verification

---

# 1. Recall: The Perfect Dataset

Consider the following dataset:

|  x |  y |
| -: | -: |
|  1 |  7 |
|  2 |  9 |
|  3 | 11 |
|  4 | 13 |
|  5 | 15 |

We can observe that `y` increases by `2` whenever `x` increases by `1`.

Therefore, the slope is:

```text
m = 2
```

At `x = 0`, the value of `y` would be:

```text
y = 5
```

Therefore, the intercept is:

```text
b = 5
```

So the line is:

```text
y = 2x + 5
```

The goal of today's class was to understand how we can arrive at this answer mathematically instead of simply observing the pattern.

---

# 2. Linear Regression Equation

The equation of a straight line is:

```text
ŷ = mx + b
```

where:

```text
ŷ = predicted value
m = slope
x = input value
b = intercept
```

For multiple observations:

```text
ŷᵢ = mxᵢ + b
```

The objective of Linear Regression is to find the values of `m` and `b` that give the best possible predictions.

---

# 3. What Does "Best Line" Mean?

The best line is the line that minimizes the difference between the actual values and predicted values.

For one data point:

```text
Actual value = yᵢ
Predicted value = mxᵢ + b
```

Therefore, the error is:

```text
Error = yᵢ - (mxᵢ + b)
```

If we simply add errors, positive and negative errors could cancel each other.

Therefore, we square the errors.

The squared error for one data point is:

```text
[yᵢ - (mxᵢ + b)]²
```

The best line is the line that minimizes the total squared error across all observations.

---

# 4. Loss Function

The total loss is:

```text
L = Σ [yᵢ - (mxᵢ + b)]²
```

More formally:

```text
L(m, b) = Σᵢ₌₁ⁿ [yᵢ - (mxᵢ + b)]²
```

where:

```text
L = total loss
yᵢ = actual value
xᵢ = input value
mxᵢ + b = predicted value
n = number of observations
```

The objective is:

```text
Minimize L(m, b)
```

In simple terms:

> Find the values of `m` and `b` that produce the smallest possible total squared error.

---

# 5. Comparing Lines Using Loss

For our perfect dataset, consider the line:

```text
y = 2x + 5
```

This line passes through every data point exactly.

Therefore:

```text
Total Loss = 0
```

Now consider another line:

```text
y = 3x + 1
```

This line does not pass through all the points.

Its total squared error is:

```text
Total Loss = 35
```

Therefore:

```text
y = 2x + 5
```

is better because:

```text
0 < 35
```

The smaller the loss, the better the fit.

---

# 6. Why Intuition Is Not Enough

For the perfect dataset, it is easy to identify the line visually.

But real-world datasets are usually:

* noisy
* inconsistent
* imperfect
* large
* difficult to analyze visually

There may not be a line that passes exactly through every data point.

Therefore, we need a mathematical method that can find the best line even when the data is messy.

The answer begins with the loss function.

---

# 7. Changing the Intercept

Suppose the slope is fixed.

We change only the intercept `b`.

For example:

|  b | Total Loss |
| -: | ---------: |
|  2 |        190 |
|  4 |         90 |
|  6 |         30 |
|  8 |         10 |
| 10 |         30 |

We can see that the loss:

```text
decreases → reaches minimum → increases
```

The lowest loss occurs at:

```text
b = 8
```

for the fixed slope used in this example.

This produces a U-shaped loss curve.

---

# 8. Changing the Slope

Now suppose the intercept is fixed.

We change only the slope `m`.

Example:

|  m | Total Loss |
| -: | ---------: |
|  0 |        445 |
|  1 |        190 |
|  2 |         45 |
|  3 |         10 |
|  4 |         85 |

Again, the loss:

```text
decreases → reaches minimum → increases
```

The lowest loss occurs at:

```text
m = 3
```

for the fixed intercept used in this example.

---

# 9. U-Shaped Loss Curve

When we plot loss against a parameter such as `m`, the curve has a U-shaped structure.

```text
Loss
 ^
 |
 |\
 | \
 |  \
 |   \
 |    \__
 |       \__
 |          \__
 |             /
 |            /
 +--------------------> m
             ^
           Minimum
```

There is a clear minimum.

At the minimum point, the loss stops decreasing and starts increasing.

---

# 10. What Does the Minimum Mean?

At the bottom of a U-shaped curve:

```text
Slope = 0
```

On the left side:

```text
Slope < 0
```

At the minimum:

```text
Slope = 0
```

On the right side:

```text
Slope > 0
```

Therefore, the mathematical condition for the minimum is:

```text
Derivative = 0
```

This is the key mathematical idea used to derive the best-fit line.

---

# 11. Derivative

The derivative measures the slope or rate of change of a function.

Therefore:

```text
Derivative = Rate of Change
```

For the loss function:

```text
dL/dm
```

represents how the loss changes when `m` changes.

At the minimum:

```text
dL/dm = 0
```

Therefore, to find the minimum:

1. Differentiate the loss.
2. Set the derivative equal to zero.
3. Solve for the parameter.

---

# 12. Loss Depends on Two Parameters

The Linear Regression loss depends on both:

```text
m
```

and:

```text
b
```

Therefore:

```text
L = L(m, b)
```

We cannot optimize only one parameter.

We need to find the minimum with respect to both `m` and `b`.

This means we need two partial derivatives.

---

# 13. Partial Derivatives

A partial derivative measures how a function changes with respect to one variable while treating the other variables as constants.

For `m`:

```text
∂L/∂m
```

means:

> Differentiate the loss with respect to `m` while treating `b` as constant.

For `b`:

```text
∂L/∂b
```

means:

> Differentiate the loss with respect to `b` while treating `m` as constant.

At the minimum:

```text
∂L/∂m = 0
```

and:

```text
∂L/∂b = 0
```

Therefore, we have:

```text
2 equations
2 unknowns
```

The two unknowns are:

```text
m
b
```

Solving these equations gives the exact best-fit line.

---

# 14. Formal Loss Function

The loss function is:

```text
L(m, b) = Σᵢ₌₁ⁿ [yᵢ - (mxᵢ + b)]²
```

For each observation:

```text
Actual value = yᵢ
```

```text
Predicted value = mxᵢ + b
```

Therefore:

```text
Error = yᵢ - (mxᵢ + b)
```

and:

```text
Squared Error = [yᵢ - (mxᵢ + b)]²
```

The total loss is:

```text
L = Σ [yᵢ - (mxᵢ + b)]²
```

This is the quantity that we want to minimize.

---

# 15. Finding the Intercept First

We start with:

```text
L = Σ [yᵢ - mxᵢ - b]²
```

Take the partial derivative with respect to `b`:

```text
∂L/∂b = 0
```

Using the chain rule:

```text
d(u²)/du = 2u
```

we obtain:

```text
∂L/∂b = Σ 2[yᵢ - mxᵢ - b](-1)
```

Set it equal to zero:

```text
Σ 2[yᵢ - mxᵢ - b](-1) = 0
```

Ignoring the constant factor `-2`:

```text
Σ [yᵢ - mxᵢ - b] = 0
```

Expand:

```text
Σyᵢ - mΣxᵢ - Σb = 0
```

Since `b` is the same for every observation:

```text
Σb = nb
```

Therefore:

```text
Σyᵢ - mΣxᵢ - nb = 0
```

Rearrange:

```text
nb = Σyᵢ - mΣxᵢ
```

Therefore:

```text
b = [Σyᵢ - mΣxᵢ] / n
```

So:

```text
b = (Σy - mΣx) / n
```

Using the means:

```text
x̄ = Σx / n
```

and:

```text
ȳ = Σy / n
```

we get:

```text
b = ȳ - mx̄
```

Therefore, the intercept formula is:

```text
b = ȳ - mx̄
```

---

# 16. Substitute the Intercept into the Loss Function

We now know:

```text
b = ȳ - mx̄
```

The loss function is:

```text
L = Σ [yᵢ - mxᵢ - b]²
```

Substitute:

```text
b = ȳ - mx̄
```

Therefore:

```text
L = Σ [yᵢ - mxᵢ - (ȳ - mx̄)]²
```

Simplify:

```text
L = Σ [yᵢ - mxᵢ - ȳ + mx̄]²
```

Group the terms:

```text
L = Σ [(yᵢ - ȳ) - m(xᵢ - x̄)]²
```

This form is useful for deriving the slope.

---

# 17. Differentiate with Respect to m

We now calculate:

```text
∂L/∂m = 0
```

We have:

```text
L = Σ [(yᵢ - ȳ) - m(xᵢ - x̄)]²
```

Using the chain rule:

```text
d(u²)/dx = 2u · du/dx
```

Therefore:

```text
∂L/∂m
=
Σ 2[(yᵢ - ȳ) - m(xᵢ - x̄)]
   · [-(xᵢ - x̄)]
```

Set equal to zero:

```text
Σ 2[(yᵢ - ȳ) - m(xᵢ - x̄)]
   [-(xᵢ - x̄)]
= 0
```

The constant factor can be removed:

```text
Σ [(yᵢ - ȳ) - m(xᵢ - x̄)]
   (xᵢ - x̄)
= 0
```

---

# 18. Expand the Equation

Expand:

```text
Σ (yᵢ - ȳ)(xᵢ - x̄)
-
mΣ (xᵢ - x̄)(xᵢ - x̄)
= 0
```

Since:

```text
(xᵢ - x̄)(xᵢ - x̄)
=
(xᵢ - x̄)²
```

we get:

```text
Σ (yᵢ - ȳ)(xᵢ - x̄)
-
mΣ (xᵢ - x̄)²
= 0
```

Move the second term to the other side:

```text
Σ (yᵢ - ȳ)(xᵢ - x̄)
=
mΣ (xᵢ - x̄)²
```

Therefore:

```text
m =
Σ (yᵢ - ȳ)(xᵢ - x̄)
--------------------------------
Σ (xᵢ - x̄)²
```

This is one of the important formulas for the slope.

---

# 19. Slope Formula

The slope can therefore be calculated as:

```text
m =
Σ (yᵢ - ȳ)(xᵢ - x̄)
---------------------
Σ (xᵢ - x̄)²
```

This formula uses deviations from the means.

An equivalent closed-form formula is:

```text
m =
[nΣxy - (Σx)(Σy)]
-------------------
[nΣx² - (Σx)²]
```

Both forms calculate the same optimal slope.

---

# 20. Closed-Form Solution

The mathematical solution for Linear Regression is:

### Slope

```text
m =
[nΣxy - (Σx)(Σy)]
-------------------
[nΣx² - (Σx)²]
```

### Intercept

```text
b =
[Σy - mΣx]
-----------
n
```

or:

```text
b = ȳ - mx̄
```

These formulas give the optimal values directly.

This is called a:

```text
Closed-Form Solution
```

because we do not need to repeatedly guess values of `m` and `b`.

---

# 21. Normal Equations

Setting the two partial derivatives to zero gives:

```text
∂L/∂m = 0
```

and:

```text
∂L/∂b = 0
```

Solving these equations gives the Normal Equations / closed-form solution for Linear Regression.

The final parameters are:

```text
m = optimal slope
b = optimal intercept
```

---

# 22. Verify the Formula with the Dataset

Consider:

|  x |  y | x² | xy |
| -: | -: | -: | -: |
|  1 |  7 |  1 |  7 |
|  2 |  9 |  4 | 18 |
|  3 | 11 |  9 | 33 |
|  4 | 13 | 16 | 52 |
|  5 | 15 | 25 | 75 |

Calculate the sums:

```text
Σx = 15
```

```text
Σy = 55
```

```text
Σx² = 55
```

```text
Σxy = 185
```

Number of observations:

```text
n = 5
```

---

# 23. Calculate m

Use:

```text
m =
[nΣxy - (Σx)(Σy)]
-------------------
[nΣx² - (Σx)²]
```

Substitute:

```text
m =
[5(185) - (15)(55)]
--------------------
[5(55) - (15)²]
```

Calculate the numerator:

```text
5 × 185 = 925
```

```text
15 × 55 = 825
```

Therefore:

```text
Numerator = 925 - 825
          = 100
```

Calculate the denominator:

```text
5 × 55 = 275
```

```text
15² = 225
```

Therefore:

```text
Denominator = 275 - 225
            = 50
```

Therefore:

```text
m = 100 / 50
```

So:

```text
m = 2
```

---

# 24. Calculate b

Use:

```text
b = [Σy - mΣx] / n
```

Substitute:

```text
b = [55 - 2(15)] / 5
```

Calculate:

```text
2 × 15 = 30
```

Therefore:

```text
b = (55 - 30) / 5
```

```text
b = 25 / 5
```

Therefore:

```text
b = 5
```

---

# 25. Final Line

We obtained:

```text
m = 2
```

and:

```text
b = 5
```

The Linear Regression equation is:

```text
ŷ = mx + b
```

Therefore:

```text
ŷ = 2x + 5
```

This is exactly the line that we identified earlier by observing the dataset.

---

# 26. Verify the Predictions

For:

```text
x = 1
```

the prediction is:

```text
ŷ = 2(1) + 5
```

```text
ŷ = 7
```

Actual value:

```text
y = 7
```

---

For:

```text
x = 2
```

```text
ŷ = 2(2) + 5
```

```text
ŷ = 9
```

Actual value:

```text
y = 9
```

---

For:

```text
x = 3
```

```text
ŷ = 2(3) + 5
```

```text
ŷ = 11
```

Actual value:

```text
y = 11
```

---

For:

```text
x = 4
```

```text
ŷ = 2(4) + 5
```

```text
ŷ = 13
```

Actual value:

```text
y = 13
```

---

For:

```text
x = 5
```

```text
ŷ = 2(5) + 5
```

```text
ŷ = 15
```

Actual value:

```text
y = 15
```

Every prediction exactly matches the actual value.

Therefore:

```text
Total Squared Error = 0
```

---

# 27. Complete Mathematical Flow

The entire derivation can be summarized as:

```text
Linear Regression
       ↓
ŷ = mx + b
       ↓
Calculate Prediction Error
       ↓
Error = yᵢ - (mxᵢ + b)
       ↓
Square the Error
       ↓
[yᵢ - (mxᵢ + b)]²
       ↓
Sum all Squared Errors
       ↓
L = Σ[yᵢ - (mxᵢ + b)]²
       ↓
Minimize Loss
       ↓
∂L/∂m = 0
and
∂L/∂b = 0
       ↓
Solve the Two Equations
       ↓
Find m and b
       ↓
Construct the Best-Fit Line
```

---

# 28. Important Formulas

## Linear Regression Equation

```text
ŷ = mx + b
```

## Loss Function

```text
L = Σ[yᵢ - (mxᵢ + b)]²
```

## Intercept

```text
b = ȳ - mx̄
```

or:

```text
b = [Σy - mΣx] / n
```

## Slope

```text
m =
Σ(yᵢ - ȳ)(xᵢ - x̄)
-------------------
Σ(xᵢ - x̄)²
```

Equivalent form:

```text
m =
[nΣxy - (Σx)(Σy)]
-------------------
[nΣx² - (Σx)²]
```

## Minimum Condition

```text
∂L/∂m = 0
```

```text
∂L/∂b = 0
```

---

# 29. Important Concepts Learned

## 1. Loss

Loss measures how well the line fits the data.

Example:

```text
Loss = 0
```

means every prediction is exactly correct for the dataset.

Example:

```text
Loss = 35
```

means the line has a larger total squared error.

---

## 2. Minimum

The best line corresponds to the minimum loss.

At the minimum:

```text
Derivative = 0
```

---

## 3. Derivative

Derivative measures the rate of change or slope of a function.

For the loss curve:

```text
dL/dm
```

measures how loss changes as `m` changes.

---

## 4. Partial Derivative

Because loss depends on both `m` and `b`, we use partial derivatives:

```text
∂L/∂m
```

and:

```text
∂L/∂b
```

---

## 5. Chain Rule

When differentiating a squared expression such as:

```text
u²
```

we use:

```text
d(u²)/dx = 2u · du/dx
```

This is required when differentiating the Linear Regression loss function.

---

## 6. Closed-Form Solution

The closed-form solution gives the optimal `m` and `b` directly.

It avoids guessing the parameters repeatedly.

---

# 30. Important Terminology

| Term                 | Meaning                                                               |
| -------------------- | --------------------------------------------------------------------- |
| Linear Regression    | A method for modeling a relationship using a linear equation          |
| Slope (`m`)          | Determines the direction and steepness of the line                    |
| Intercept (`b`)      | Value of the line when `x = 0`                                        |
| Prediction (`ŷ`)     | Value predicted by the model                                          |
| Error                | Difference between actual and predicted value                         |
| Squared Error        | Error multiplied by itself                                            |
| Loss                 | Sum of squared errors                                                 |
| Derivative           | Measures rate of change                                               |
| Partial Derivative   | Derivative with respect to one variable while holding others constant |
| Minimum              | Point where the loss is lowest                                        |
| Chain Rule           | Rule used to differentiate composite functions                        |
| Closed-Form Solution | Direct mathematical solution for model parameters                     |
| Normal Equations     | Equations obtained from setting partial derivatives to zero           |

---

# 31. Key Takeaways

1. Linear Regression uses the equation:

```text
ŷ = mx + b
```

2. The quality of the line is measured using total squared error:

```text
L = Σ[yᵢ - (mxᵢ + b)]²
```

3. The best line is the line with minimum loss.

4. A minimum occurs where the derivative is zero.

5. Since the loss depends on both `m` and `b`, we use two partial derivatives:

```text
∂L/∂m = 0
```

```text
∂L/∂b = 0
```

6. Solving these equations gives the closed-form solution.

7. The slope is:

```text
m =
[nΣxy - (Σx)(Σy)]
-------------------
[nΣx² - (Σx)²]
```

8. The intercept is:

```text
b = ȳ - mx̄
```

9. For today's dataset:

```text
X = [1, 2, 3, 4, 5]
Y = [7, 9, 11, 13, 15]
```

we obtained:

```text
m = 2
b = 5
```

10. Therefore, the final Linear Regression line is:

```text
ŷ = 2x + 5
```

11. For this perfect dataset:

```text
Total Squared Error = 0
```

---

# 32. Final Understanding

The important idea from today's class is not simply memorizing:

```text
m = 2
b = 5
```

The important idea is understanding **why** these values are obtained.

The reasoning is:

```text
We need the best line
        ↓
Best means minimum loss
        ↓
Loss is total squared error
        ↓
Loss depends on m and b
        ↓
Minimum occurs where derivatives are zero
        ↓
Use partial derivatives
        ↓
∂L/∂m = 0
∂L/∂b = 0
        ↓
Solve the equations
        ↓
Obtain m and b
        ↓
Construct the best-fit line
```

For the example:

```text
m = 2
b = 5
```

Therefore:

```text
ŷ = 2x + 5
```

The mathematical derivation confirms the result that was initially identified through intuition.

