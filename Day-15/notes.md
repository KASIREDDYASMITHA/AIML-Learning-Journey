# Day 15 - KNN and Introduction to Decision Trees


# 1. KNN - Honest Assessment

K-Nearest Neighbors (KNN) is a simple and transparent distance-based machine learning algorithm.

## Strengths of KNN

### 1. Simple to Understand

The logic is completely transparent.

For a prediction:

* Calculate distances between the new data point and training points.
* Find the nearest neighbors.
* Use their classes to make the prediction.

### 2. No Training Time

KNN does not build a complicated model during training.

It essentially memorizes the training data.

The actual distance calculations happen when a prediction is required.

### 3. Naturally Handles Multiclass Problems

KNN can naturally handle multiple classes without modification.

For example:

* Class A
* Class B
* Class C

The nearest neighbors can vote among multiple classes.

### 4. Non-Parametric

KNN is non-parametric.

It makes no assumptions about the shape or distribution of the data.

---

# 2. Weaknesses of KNN

## 1. Slow at Inference

Every prediction requires calculating the distance to training points.

Therefore, prediction can become slow when the dataset is large.

The problem is mainly during **inference/prediction**, not during training.

---

## 2. Sensitive to Irrelevant Features

KNN uses the features while calculating distance.

If an irrelevant feature is included, it can affect the distance calculation and therefore affect the prediction.

Example:

```text
Age
Salary
Favorite Color
```

If Favorite Color has nothing to do with whether a customer buys a product, including it in the distance calculation can hurt the prediction.

---

## 3. Sensitive to Feature Scale

KNN is sensitive to the scale of features.

Features with large numerical magnitudes can dominate the distance calculation.

Example:

```text
Age = 30
Salary = 50000
```

Salary has a much larger numerical magnitude than Age.

Therefore, feature scaling such as normalization may be required.

---

## 4. Curse of Dimensionality

As the number of features increases, KNN performance can degrade.

When dimensionality becomes high:

* Distance calculations become more difficult.
* Data points become harder to distinguish.
* Nearest-neighbor relationships become less useful.
* Performance can decrease.

---

## KNN Overall

KNN is:

* Simple
* Transparent
* A useful baseline
* A good teaching algorithm

But for:

* Large datasets
* High-dimensional datasets

we may need smarter algorithms.

---

# 3. Challenge - Classify a Customer

Consider the following dataset:

| Age |  Salary | Bought? |
| --: | ------: | ------- |
|  22 | ₹25,000 | No      |
|  28 | ₹32,000 | No      |
|  26 | ₹40,000 | No      |
|  31 | ₹48,000 | No      |
|  35 | ₹58,000 | Yes     |
|  38 | ₹62,000 | Yes     |
|  42 | ₹75,000 | Yes     |
|  45 | ₹85,000 | Yes     |

Suppose a new customer is:

```text
Age = 36
Salary = ₹61,000
```

Question:

```text
Will this customer buy?
```

Instead of using a formula or algorithm initially, we can look at the data and create a simple rule.

Looking at the pattern, customers older than approximately 32 appear to have `Bought = Yes`.

---

# 4. From Instinct to If-Else Rules

A simple classification rule can be written as:

```python
if Age > 32:
    Bought = "Yes"
else:
    Bought = "No"
```

This is a complete working classifier.

Every new data point can be passed through this rule and receive a label.

There is:

* No complicated formula
* No complex model required
* Just a condition and a conclusion

This is classification using an **if-else rule**.

---

# 5. Same Logic, New Shape

The same if-else logic can be represented as a tree:

```text
              Age > 32?
              /       \
            No         Yes
            |           |
      Bought = No   Bought = Yes
```

The code and the diagram represent the same decision logic.

This structure is called a:

# Decision Tree

---

# 6. What is a Decision Tree?

A Decision Tree is a **flowchart of questions**.

Each question splits the data into smaller and more predictable groups.

At the end of each path is a prediction.

Basic idea:

```text
Question
   ↓
Split
   ↓
Smaller groups
   ↓
More predictable groups
   ↓
Prediction
```

Decision Trees are widely used because their decision-making process is interpretable.

The basic process that we performed manually is what the Decision Tree algorithm performs automatically.

---

# 7. Decision Tree Terminology

## Root Node

The **root node** is the first question or first split in the tree.

Example:

```text
Age > 32?
```

If Age is selected as the first feature, this becomes the root node.

---

## Split

A **split** divides the data into smaller groups.

Example:

```text
Age > 32
```

creates two groups:

```text
Age <= 32
Age > 32
```

---

## Internal Node

An **internal node** represents another question or decision inside the tree.

Example:

```text
Salary > 50000?
```

---

## Leaf Node

A **leaf node** is the endpoint of a path and contains the final prediction.

Example:

```text
Bought = Yes
```

or:

```text
Bought = No
```

---

# 8. Basic Structure of a Decision Tree

```text
                    Root Node
                  /           \
                Split         Split
                /               \
       Internal Node       Internal Node
            |                    |
       Leaf Node             Leaf Node
       Prediction             Prediction
```

Remember:

```text
Root Node   → First question
Split       → Divides data
Internal Node → Further question
Leaf Node   → Final prediction
```

---

# 9. Two Fundamental Questions in Decision Trees

Decision Trees raise two fundamental questions.

## Question 1 - Which Column?

Suppose we have:

```text
Age
Salary
City
Color
```

Which column should the tree use first?

Which feature should become the root?

And after that:

Which feature should be selected at the next level?

The algorithm must decide which column creates the most useful groups.

---

## Question 2 - Which Threshold?

For numerical columns, choosing the column is not enough.

Suppose the selected column is:

```text
Age
```

We still need to determine:

```text
Age > ?
```

Possible thresholds could be:

```text
Age > 25
Age > 30
Age > 32
Age > 35
Age > 40
```

The algorithm must search for the best threshold.

The important question is:

```text
Best according to what measure?
```

That leads to the concept of **purity and entropy**.

---

# 10. Categorical Columns

Categorical columns contain categories.

Examples:

```text
Color
City
Gender
```

For categorical columns, splitting can be intuitive.

For example:

```text
              Color?
             /   |   \
           Red Blue Green
```

There can be a branch for each category.

---

# 11. Numerical Columns

Numerical columns contain numerical values.

Examples:

```text
Age
Salary
Experience
```

For numerical columns, the algorithm must search for a suitable threshold.

Example:

```text
Age > 32?
```

The algorithm considers possible thresholds and searches for the threshold that produces the best split.

---

# 12. Reflecting on the Instinct

When we selected Age as the first column, the decision was not random.

We looked at the data and selected the column that made prediction easier.

The question becomes:

```text
What makes one split easier than another?
```

The answer is:

# Purity

---

# 13. Principle of Easiness

The goal at every Decision Tree node is to choose the split that creates the:

* Purest groups
* Most predictable child groups

The principle is:

```text
Better split
     ↓
More pure groups
     ↓
Easier prediction
```

But we need a mathematical way to measure how pure or mixed a group is.

That mathematical measure is:

# Entropy

---

# 14. What is Entropy?

Entropy is a mathematical measure of:

* Disorder
* Uncertainty
* How mixed or pure a group is

A group containing only one class is completely pure.

A group containing multiple classes is more mixed.

---

# 15. Pure Group

Consider:

```text
10 Yes
0 No
```

Every observation belongs to the same class.

Therefore:

```text
Entropy = 0
```

There is zero uncertainty.

The prediction is completely certain.

---

# 16. Mixed Group

Consider:

```text
5 Yes
5 No
```

The group is equally divided between two classes.

There is maximum uncertainty.

For binary classification:

```text
Entropy = 1
```

This is maximum entropy.

---

# 17. Entropy and Prediction Difficulty

The relationship is:

```text
Low Entropy
     ↓
Low uncertainty
     ↓
Easy to predict
```

and:

```text
High Entropy
     ↓
High uncertainty
     ↓
Hard to predict
```

Therefore:

```text
Low entropy = good / easier-to-predict group

High entropy = bad / harder-to-predict group
```

The Decision Tree tries to create groups with lower entropy.

---

# 18. Entropy Scale

For binary classification:

```text
Entropy = 0
```

means:

```text
Completely pure
```

and:

```text
Entropy = 1
```

means:

```text
Maximum disorder
```

Therefore:

```text
0 ≤ Entropy ≤ 1
```

for binary classification.

Everything between 0 and 1 represents different levels of class mixture.

---

# 19. Entropy Formula

The entropy formula is:

```text
H = -Σ pᵢ log₂(pᵢ)
```

Where:

```text
H   = Entropy

pᵢ  = Probability / proportion of class i

Σ   = Sum over all classes

log₂ = Logarithm with base 2
```

For binary classification:

```text
H = -(p(Yes) × log₂(p(Yes))
     + p(No) × log₂(p(No)))
```

---

# 20. Why the Negative Sign?

For probabilities between 0 and 1:

```text
log₂(p)
```

is negative.

For example:

```text
log₂(0.5) = -1
```

The negative sign in the entropy formula makes the final entropy value positive.

---

# 21. Entropy Example - 10 Yes, 0 No

Consider:

```text
10 Yes
0 No
```

Probabilities:

```text
p(Yes) = 1.0
p(No) = 0.0
```

Entropy:

```text
H = -(1.0 × log₂(1.0))
```

Since:

```text
log₂(1) = 0
```

Therefore:

```text
H = 0
```

Interpretation:

```text
Completely pure
Prediction is certain
```

---

# 22. Entropy Example - 9 Yes, 1 No

Consider:

```text
9 Yes
1 No
```

Probabilities:

```text
p(Yes) = 0.9
p(No) = 0.1
```

Entropy:

```text
H = -(0.9 × log₂(0.9)
     + 0.1 × log₂(0.1))
```

Approximately:

```text
H = 0.469
```

Interpretation:

```text
Almost pure
Prediction is nearly certain
```

---

# 23. Entropy Example - 7 Yes, 3 No

Consider:

```text
7 Yes
3 No
```

Probabilities:

```text
p(Yes) = 0.7
p(No) = 0.3
```

Entropy:

```text
H = -(0.7 × log₂(0.7)
     + 0.3 × log₂(0.3))
```

Approximately:

```text
H = 0.881
```

Interpretation:

```text
Some disorder
Prediction is uncertain
```

---

# 24. Entropy Example - 5 Yes, 5 No

Consider:

```text
5 Yes
5 No
```

Probabilities:

```text
p(Yes) = 0.5
p(No) = 0.5
```

Entropy:

```text
H = -(0.5 × log₂(0.5)
     + 0.5 × log₂(0.5))
```

Since:

```text
log₂(0.5) = -1
```

Therefore:

```text
H = -(0.5 × -1 + 0.5 × -1)

H = -(-0.5 - 0.5)

H = 1.0
```

Interpretation:

```text
Maximum entropy
Maximum disorder
Prediction is no better than a coin flip
```

---

# 25. Entropy Comparison

| Configuration | Entropy |
| ------------- | ------: |
| 10 Yes, 0 No  |   0.000 |
| 9 Yes, 1 No   |   0.469 |
| 7 Yes, 3 No   |   0.881 |
| 5 Yes, 5 No   |   1.000 |

The pattern is:

```text
More pure
    ↓
Lower entropy
```

and:

```text
More mixed
    ↓
Higher entropy
```

As the group becomes more mixed, entropy increases.

As the group becomes purer, entropy decreases toward zero.

---

# 26. Entropy and Decision Tree Splitting

The Decision Tree wants to make prediction easier.

Therefore, it wants to create groups with lower entropy.

Suppose:

```text
Before split
    ↓
High entropy
```

After a good split:

```text
After split
    ↓
Low entropy
```

The split has reduced disorder.

This reduction is what we quantify using:

# Information Gain

---

# 27. Information Gain

The drop in entropy has a name:

# Information Gain

Formula:

```text
Information Gain
=
Entropy Before
-
Weighted Entropy After
```

Information Gain tells us how much a split reduced disorder.

---

# 28. High Information Gain

A high Information Gain means:

```text
The split dramatically reduced disorder.
```

Therefore, the resulting groups became much more predictable.

---

# 29. Low Information Gain

A low Information Gain means:

```text
The split barely helped.
```

The resulting groups are not significantly more predictable.

---

# 30. How the Decision Tree Chooses a Split

The algorithm tries:

```text
Every possible column
```

and for numerical columns:

```text
Every possible threshold
```

Then it evaluates the quality of the resulting split.

Basic process:

```text
Try a possible split
        ↓
Calculate entropy
        ↓
Calculate weighted entropy after split
        ↓
Calculate Information Gain
        ↓
Compare with other splits
        ↓
Choose highest Information Gain
```

The split with the highest Information Gain is selected.

This determines:

* Which column becomes the root
* Which column is selected at later levels
* Which threshold is used for numerical features

---

# 31. Example - Age Split

Consider the customer dataset:

| Age | Bought |
| --: | ------ |
|  22 | No     |
|  28 | No     |
|  26 | No     |
|  31 | No     |
|  35 | Yes    |
|  38 | Yes    |
|  42 | Yes    |
|  45 | Yes    |

Suppose we choose:

```text
Age > 32
```

The data becomes:

### Group 1

```text
Age <= 32

No
No
No
No
```

### Group 2

```text
Age > 32

Yes
Yes
Yes
Yes
```

Both groups are completely pure.

Therefore:

```text
Entropy of Group 1 = 0
Entropy of Group 2 = 0
```

The split has made the prediction completely easy.

---

# 32. Closing the Loop - Entropy Reduction

Before the split, the data contains both classes.

Therefore there is uncertainty.

After splitting on:

```text
Age > 32
```

we get:

```text
Age <= 32 → No

Age > 32 → Yes
```

The child groups are completely pure.

The entropy can therefore go from:

```text
1.0 → 0
```

This is the best possible outcome.

---

# 33. Human Intuition vs Algorithm

When we looked at the data and said:

```text
Age looks like the right column.
```

we were intuitively selecting the feature that made prediction easier.

Mathematically, the algorithm expresses this idea using:

```text
Entropy
```

and:

```text
Information Gain
```

So:

```text
Human intuition
      ↓
Choose easier groups
      ↓
Lower entropy
      ↓
Larger entropy reduction
      ↓
Higher Information Gain
```

---

# 34. Information Gain - Main Idea

The Decision Tree algorithm tries different features and thresholds.

It selects the split that produces the:

```text
Highest Information Gain
```

because the highest Information Gain means the greatest reduction in disorder.

Therefore:

```text
Highest Information Gain
        ↓
Best split
```

---

# 35. Simplified Decision Tree Building Process

The basic idea is:

```text
Start with the dataset
        ↓
Consider possible columns
        ↓
Consider possible thresholds
        ↓
Measure entropy
        ↓
Calculate Information Gain
        ↓
Choose the highest Information Gain split
        ↓
Divide the data
        ↓
Repeat
        ↓
Eventually create leaf predictions
```

The complete algorithm, exact calculation of Information Gain, handling numerical thresholds, stopping criteria, implementation, and evaluation are covered in the next stage.

---

# 36. Entropy vs Information Gain

## Entropy

Entropy measures:

```text
How mixed or disordered is the group?
```

It tells us the uncertainty in the group.

---

## Information Gain

Information Gain measures:

```text
How much did the split reduce the disorder?
```

Therefore:

```text
Entropy
    ↓
Measures disorder
```

while:

```text
Information Gain
    ↓
Measures reduction in disorder
```

---

# 37. KNN vs Decision Tree

## KNN

```text
Distance-based
Uses nearest data points
Simple and transparent
No training time
Non-parametric
Sensitive to scale
Sensitive to irrelevant features
Slow during inference
Affected by curse of dimensionality
```

## Decision Tree

```text
Rule-based
Uses feature-based questions
Creates a tree structure
Uses splits
Uses thresholds for numerical features
Uses entropy to measure disorder
Uses Information Gain to choose useful splits
```

---

# 38. Important Decision Tree Terms

Remember these terms:

```text
Decision Tree
Root Node
Internal Node
Leaf Node
Split
Threshold
Purity
Categorical Feature
Numerical Feature
Entropy
Information Gain
```

---

# 39. Important Formulas

## Entropy

```text
H = -Σ pᵢ log₂(pᵢ)
```

## Information Gain

```text
Information Gain
=
Entropy Before
-
Weighted Entropy After
```

---

# 40. Important Relationships

### Purity and Entropy

```text
More Pure
    ↓
Lower Entropy
    ↓
Easier Prediction
```

### Disorder and Entropy

```text
More Mixed
    ↓
Higher Entropy
    ↓
Harder Prediction
```

### Good Split and Information Gain

```text
Good Split
    ↓
Purer Child Groups
    ↓
Lower Entropy
    ↓
Higher Information Gain
```

---

# 41. Complete Decision Tree Intuition

The complete intuition learned today is:

```text
Dataset
   ↓
Ask a question
   ↓
Split the data
   ↓
Create smaller groups
   ↓
Check how pure the groups are
   ↓
Measure purity/disorder using Entropy
   ↓
Measure reduction in disorder using Information Gain
   ↓
Choose the split with highest Information Gain
   ↓
Continue splitting
   ↓
Reach leaf nodes
   ↓
Make predictions
```
