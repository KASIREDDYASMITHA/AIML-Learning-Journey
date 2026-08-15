# Day 7 — Linear Regression: Finding the Best Line Mathematically

## 1. Topic Covered

 how to mathematically find the **best-fit line in Linear Regression**.

The main idea was:

> Find the values of slope `m` and intercept `b` that minimize the total squared error (loss).

Instead of guessing the line, we use **derivatives and partial derivatives** to find the exact minimum of the loss function.

---

# 2. Recall: Linear Regression Line

The equation of a straight line is:

```text
y = mx + b
```

Where:

* `x` = input/independent variable
* `y` = actual output/dependent variable
* `m` = slope of the line
* `b` = y-intercept

For prediction, we write:

```text
ŷ = mx + b
```

Where:

* `ŷ` = predicted value
* `m` = slope
* `x` = input
* `b` = intercept

---

# 3. Perfect Dataset Example

Consider the following dataset:

| x | y  |
| - | -- |
| 1 | 7  |
| 2 | 9  |
| 3 | 11 |
| 4 | 13 |
| 5 | 15 |

Looking at the data:

```text
x increases by 1
y increases by 2
```

Therefore:

```text
m = 2
```

At:

```text
x = 0
```

the value of `y` would be:

```text
y = 5
```

Therefore:

```text
b = 5
```

So the line is:

```text
y = 2x + 5
```

Thus:

```text
m = 2
b = 5
```

---

# 4. Prediction Using the Line

For the line:

```text
ŷ = 2x + 5
```

the predictions are:

| x | Actual y | Predicted ŷ |
| - | -------: | ----------: |
| 1 |        7 |           7 |
| 2 |        9 |           9 |
| 3 |       11 |          11 |
| 4 |       13 |          13 |
| 5 |       15 |          15 |

Every prediction exactly matches the actual value.

Therefore, the total squared error is:

```text
0
```

---

# 5. Comparing With Another Line

Consider another line:

```text
y = 3x + 1
```

For the same dataset, this line does not pass through every point.

Its total squared error is:

```text
35
```

While our line:

```text
y = 2x + 5
```

has:

```text
Total Loss = 0
```

Therefore, the line `y = 2x + 5` is better for this perfect dataset.

However, real-world datasets are usually noisy, so intuition alone cannot reliably find the best line.

We need a mathematical method.

---

# 6. What Makes a Line the Best?

A line is considered the best line when it minimizes the total error between:

```text
Actual value
```

and

```text
Predicted value
```

The loss function measures how far the predictions are from the actual values.

The goal is:

```text
Minimize Loss
```

---

# 7. Loss Function

For each data point:

```text
Prediction = mxᵢ + b
```

The error is:

```text
yᵢ - (mxᵢ + b)
```

The squared error is:

```text
(yᵢ - (mxᵢ + b))²
```

For all `n` data points, the total loss is:

```text
L(m,b) = Σ [yᵢ - (mxᵢ + b)]²
         i=1 to n
```

Equivalent form:

```text
L = Σ (ŷᵢ - yᵢ)²
```

where:

```text
ŷᵢ = mxᵢ + b
```

The objective is:

```text
Find m and b that minimize L.
```

---

# 8. Why Do We Minimize Squared Error?

We use the squared difference:

```text
(actual - predicted)²
```

because squaring makes the error positive and gives a mathematical function that can be differentiated.

The total loss is therefore:

```text
L = Σ (ŷᵢ - yᵢ)²
```

---

# 9. Fix the Slope and Vary the Intercept

Suppose:

```text
m = 1
```

is fixed.

Now change the value of `b`.

|  b | Total Loss |
| -: | ---------: |
|  2 |        190 |
|  4 |         90 |
|  6 |         30 |
|  8 |         10 |
| 10 |         30 |

The loss decreases:

```text
190 → 90 → 30 → 10
```

and then increases:

```text
10 → 30
```

Therefore, there is a minimum.

For this example:

```text
b = 8
```

gives the lowest loss.

---

# 10. Fix the Intercept and Vary the Slope

Now suppose:

```text
b = 2
```

is fixed.

Change the value of `m`.

|  m | Total Loss |
| -: | ---------: |
|  0 |        445 |
|  1 |        190 |
|  2 |         45 |
|  3 |         10 |
|  4 |         85 |

Again, the loss decreases and then increases.

The lowest loss occurs at:

```text
m = 3
```

for this fixed value of `b`.

---

# 11. U-Shaped Loss Curve

When we vary one parameter while keeping the other fixed, the loss forms a **U-shaped curve**.

Example:

```text
Loss
 ^
 |        *
 |      *   *
 |    *       *
 |  *           *
 | *      ↓      *
 +--------------------> m
          minimum
```

The important observation is:

```text
Loss decreases
      ↓
reaches minimum
      ↓
Loss increases
```

At the bottom of the U-shaped curve, the slope is:

```text
0
```

Therefore:

```text
Derivative = 0
```

at the minimum.

---

# 12. Derivative

The derivative represents the slope or rate of change of a function.

In this problem:

```text
d(Loss)/dm
```

represents how the loss changes when `m` changes.

At the minimum:

```text
dL/dm = 0
```

Therefore, to find the minimum:

1. Differentiate the loss.
2. Set the derivative equal to zero.
3. Solve for the unknown parameter.

---

# 13. Loss Depends on Both m and b

The loss does not depend only on `m`.

It depends on both:

```text
m
b
```

Therefore:

```text
L = L(m,b)
```

Changing either `m` or `b` changes the loss.

Instead of a simple curve, the loss can be viewed as a **surface** in three dimensions.

The minimum is the exact point where the loss is lowest.

---

# 14. Partial Derivatives

Since there are two unknown parameters:

```text
m
b
```

we need two partial derivatives.

### Partial derivative with respect to m

When calculating:

```text
∂L/∂m
```

we treat `b` as a constant and differentiate with respect to `m`.

At the minimum:

```text
∂L/∂m = 0
```

### Partial derivative with respect to b

When calculating:

```text
∂L/∂b
```

we treat `m` as a constant and differentiate with respect to `b`.

At the minimum:

```text
∂L/∂b = 0
```

Therefore, the two conditions are:

```text
∂L/∂m = 0

∂L/∂b = 0
```

These two equations can be solved to find:

```text
m
b
```

---

# 15. Important Differentiation Rules

Some differentiation rules used in the derivation are:

## Power Rule

```text
d(xⁿ)/dx = n xⁿ⁻¹
```

Example:

```text
d(x²)/dx = 2x
```

Another example:

```text
d(x³)/dx = 3x²
```

## Constant Rule

If a value is constant with respect to the variable:

```text
d(c)/dx = 0
```

For example, when differentiating with respect to `b`, `m` is treated as a constant.

---

# 16. Chain Rule

The derivation also uses the chain rule.

General form:

```text
d(f(g(x)))/dx
=
df/dg × dg/dx
```

For a squared expression:

```text
d(u²)/dx = 2u × du/dx
```

This is important because the loss contains:

```text
[yᵢ - (mxᵢ + b)]²
```

---

# 17. Deriving the Partial Derivative with Respect to b

Start with the loss:

```text
L = Σ [yᵢ - (mxᵢ + b)]²
```

For minimum loss:

```text
∂L/∂b = 0
```

Therefore:

```text
∂/∂b Σ [yᵢ - (mxᵢ + b)]² = 0
```

Move the derivative inside the summation:

```text
Σ ∂/∂b [yᵢ - mxᵢ - b]² = 0
```

Using the chain rule:

```text
Σ 2(yᵢ - mxᵢ - b)
   × ∂(yᵢ - mxᵢ - b)/∂b = 0
```

Since:

```text
∂(yᵢ - mxᵢ - b)/∂b = -1
```

we get:

```text
Σ 2(yᵢ - mxᵢ - b)(-1) = 0
```

Therefore:

```text
-2 Σ(yᵢ - mxᵢ - b) = 0
```

Divide by `-2`:

```text
Σ(yᵢ - mxᵢ - b) = 0
```

---

# 18. Expanding the Summation

We have:

```text
Σ(yᵢ - mxᵢ - b) = 0
```

Separate the summation:

```text
Σyᵢ - Σmxᵢ - Σb = 0
```

Since `m` is constant:

```text
Σmxᵢ = mΣxᵢ
```

Therefore:

```text
Σyᵢ - mΣxᵢ - Σb = 0
```

Since `b` is constant and there are `n` observations:

```text
Σb = nb
```

So:

```text
Σyᵢ - mΣxᵢ - nb = 0
```

Rearranging:

```text
Σyᵢ - mΣxᵢ = nb
```

Divide by `n`:

```text
Σyᵢ/n - mΣxᵢ/n = b
```

Therefore:

```text
b = Σyᵢ/n - mΣxᵢ/n
```

Using the mean notation:

```text
ȳ = Σyᵢ/n

x̄ = Σxᵢ/n
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

# 19. Meaning of the Intercept Formula

The formula:

```text
b = ȳ - mx̄
```

shows that once the slope `m` is known, the intercept `b` can be calculated using the mean of `x` and the mean of `y`.

Where:

```text
x̄ = mean of x

ȳ = mean of y
```

Therefore:

```text
b = mean(y) - m × mean(x)
```

---

# 20. Normal Equations / Closed-Form Solution

Setting both partial derivatives to zero gives the **normal equations**.

The closed-form solution gives explicit formulas for `m` and `b`.

### Slope

```text
m =
[nΣxy - (Σx)(Σy)]
------------------
[nΣx² - (Σx)²]
```

### Intercept

```text
b =
Σy - mΣx
---------
n
```

Equivalent form:

```text
b = ȳ - mx̄
```

These formulas allow us to calculate the exact best-fit line without repeatedly guessing values.

---

# 21. Verification Using the Perfect Dataset

Dataset:

| x | y  |
| - | -- |
| 1 | 7  |
| 2 | 9  |
| 3 | 11 |
| 4 | 13 |
| 5 | 15 |

We calculate:

|          x |          y |         x² |          xy |
| ---------: | ---------: | ---------: | ----------: |
|          1 |          7 |          1 |           7 |
|          2 |          9 |          4 |          18 |
|          3 |         11 |          9 |          33 |
|          4 |         13 |         16 |          52 |
|          5 |         15 |         25 |          75 |
| **Σ = 15** | **Σ = 55** | **Σ = 55** | **Σ = 185** |

Number of observations:

```text
n = 5
```

Therefore:

```text
Σx = 15

Σy = 55

Σx² = 55

Σxy = 185
```

---

# 22. Calculate the Slope

Use:

```text
m =
[nΣxy - (Σx)(Σy)]
------------------
[nΣx² - (Σx)²]
```

Substitute the values:

```text
m =
[5 × 185 - 15 × 55]
--------------------
[5 × 55 - 15²]
```

Calculate:

```text
m =
[925 - 825]
-----------
[275 - 225]
```

Therefore:

```text
m = 100/50
```

So:

```text
m = 2
```

---

# 23. Calculate the Intercept

Use:

```text
b = (Σy - mΣx)/n
```

Substitute:

```text
b = (55 - 2 × 15)/5
```

Calculate:

```text
b = (55 - 30)/5
```

```text
b = 25/5
```

Therefore:

```text
b = 5
```

---

# 24. Final Regression Equation

We obtained:

```text
m = 2

b = 5
```

Therefore:

```text
ŷ = 2x + 5
```

This is exactly the same line that we found earlier using intuition.

The mathematical derivation confirms that:

```text
Best-fit line = ŷ = 2x + 5
```

for this perfect dataset.

---

# 25. Why the Closed-Form Solution Is Important

The closed-form solution gives the exact values of:

```text
m
b
```

directly from the dataset.

It does not require guessing different lines.

The process is:

```text
Dataset
   ↓
Define Loss
   ↓
Differentiate
   ↓
Calculate Partial Derivatives
   ↓
Set Partial Derivatives = 0
   ↓
Solve the Equations
   ↓
Find m and b
   ↓
Get the Best-Fit Line
```

---

# 26. Key Concepts Learned Today

### 1. Linear Regression Equation

```text
ŷ = mx + b
```

### 2. Loss Function

```text
L = Σ [yᵢ - (mxᵢ + b)]²
```

### 3. Goal

```text
Minimize Loss
```

### 4. Minimum Condition

At the minimum:

```text
Derivative = 0
```

### 5. Two Unknown Parameters

Because the loss depends on both `m` and `b`:

```text
∂L/∂m = 0

∂L/∂b = 0
```

### 6. Intercept Formula

```text
b = ȳ - mx̄
```

### 7. Slope Formula

```text
m =
[nΣxy - (Σx)(Σy)]
------------------
[nΣx² - (Σx)²]
```

### 8. Final Example

For the dataset:

```text
(1,7)
(2,9)
(3,11)
(4,13)
(5,15)
```

we get:

```text
m = 2
b = 5
```

Therefore:

```text
ŷ = 2x + 5
```

---

