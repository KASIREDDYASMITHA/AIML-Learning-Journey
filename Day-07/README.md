# AIML Learning Journey — Day 7


**Linear Regression — Finding the Best Line Mathematically**

Day 7 focused on understanding how to mathematically find the best-fit line in Linear Regression instead of relying on intuition or visual guessing.

The session moved from the idea of a best line to the mathematical derivation using **loss, derivatives, partial derivatives, and the closed-form solution**.

---

## 🧠 What I Learned

### 1. Linear Regression Equation

The prediction equation is:

```text
ŷ = mx + b
```

Where:

* `ŷ` = predicted value
* `m` = slope
* `x` = input
* `b` = intercept

---

### 2. Loss Function

The total squared error is:

```text
L(m,b) = Σ [yᵢ - (mxᵢ + b)]²
```

The objective of Linear Regression is to find the values of `m` and `b` that minimize this loss.

---

### 3. U-Shaped Loss Curve

When one parameter is fixed and the other is varied, the loss decreases, reaches a minimum, and then increases.

At the minimum point:

```text
Derivative = 0
```

This gives us the mathematical condition for finding the minimum loss.

---

### 4. Partial Derivatives

Because loss depends on both `m` and `b`, we use two partial derivatives:

```text
∂L/∂m = 0

∂L/∂b = 0
```

Solving these equations gives the exact values of the slope and intercept.

---

### 5. Closed-Form Solution

The normal equations give:

**Slope:**

```text
m = [nΣxy - (Σx)(Σy)]
    ------------------
    [nΣx² - (Σx)²]
```

**Intercept:**

```text
b = (Σy - mΣx) / n
```

The intercept can also be written as:

```text
b = ȳ - mx̄
```


## 📊 Example Covered

Dataset:

|  x |  y |
| -: | -: |
|  1 |  7 |
|  2 |  9 |
|  3 | 11 |
|  4 | 13 |
|  5 | 15 |

Calculated values:

```text
n = 5
Σx = 15
Σy = 55
Σx² = 55
Σxy = 185
```

Using the closed-form formula:

```text
m = 2
```

Then:

```text
b = 5
```

Therefore, the best-fit line is:

```text
ŷ = 2x + 5
```

This exactly matches the line identified earlier through intuition.

---

## 🔑 Key Concepts

* Linear Regression
* Best-fit line
* Slope `m`
* Intercept `b`
* Prediction `ŷ`
* Loss function
* Squared error
* Minimization
* Derivative
* Partial derivative
* Chain rule
* U-shaped loss curve
* Normal equations
* Closed-form solution

---

