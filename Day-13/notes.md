# Day 13 Notes - Classification, Encoding and K-Nearest Neighbours

## 1. Classification

So far, in regression, we predicted numerical values.

Example:

```text
Input  -> House size
Output -> House price
```

The output of regression is a continuous numerical value.

In classification, the output is a **category or label**.

Examples:

```text
Email -> Spam / Not Spam
Scan  -> Malignant / Benign
Image -> Cat / Dog / Bird
```

### Definition

Classification is a supervised machine learning problem where the model predicts a category or label from a fixed set of possible categories.

---

# 2. Classification vs Regression

| Regression           | Classification              |
| -------------------- | --------------------------- |
| Predicts a number    | Predicts a category         |
| Output is continuous | Output is a label           |
| Example: House price | Example: Spam/Not Spam      |
| Fits a line/curve    | Creates a decision boundary |

Regression tries to fit a continuous relationship.

Classification divides the feature space into different labelled regions.

---

# 3. Decision Boundary

A classification model draws a **decision boundary** that separates different classes.

For example:

```text
        Class A
     x  x  x
    x  x  x

----------- Decision Boundary -----------

        Class B
     o  o  o
    o  o  o
```

A new point is classified depending on which side of the boundary it falls.

The decision boundary divides the feature space into labelled regions.

Different classification algorithms use different methods to find this boundary.

---

# 4. Binary Classification

Binary classification has exactly **two possible output categories**.

Examples:

```text
Spam / Not Spam
Fraud / Not Fraud
Pass / Fail
```

The output is commonly represented using:

```text
0 or 1
```

Example:

```text
0 -> Not Spam
1 -> Spam
```

---

# 5. Multiclass Classification

Multiclass classification has **more than two possible output categories**.

Examples:

### Digit Recognition

```text
0, 1, 2, 3, 4, 5, 6, 7, 8, 9
```

### Disease Type

```text
A, B, C
```

### Animal Classification

```text
Cat, Dog, Bird
```

The output is one of many possible labels.

---

# 6. Machine Learning Models Understand Numbers

Machine learning algorithms work with numerical values.

However, classification data can contain:

```text
Words
Categories
Strings
Labels
```

Example:

```text
Red
Blue
Green
```

Before using such categorical data with a model, we need to convert it into a numerical representation.

This process is called **Encoding**.

---

# 7. Encoding

Encoding means converting categorical data into numerical form so that a machine learning model can process it.

Two important encoding techniques learned today are:

1. Label Encoding
2. One-Hot Encoding

---

# 8. Label Encoding

Label encoding assigns a number to each category.

Example:

```text
Red   -> 0
Blue  -> 1
Green -> 2
```

Another example:

```text
Low    -> 0
Medium -> 1
High   -> 2
```

## Advantage

* Simple
* Compact
* Easy to implement

## Disadvantage

For categories that do not have an order, label encoding can create a false relationship.

For example:

```text
Red   -> 0
Blue  -> 1
Green -> 2
```

The model may interpret the values as:

```text
Green > Blue > Red
```

But colours do not naturally have this order.

Therefore, label encoding is safer when categories have a meaningful natural order.

Example:

```text
Low < Medium < High
```

---

# 9. One-Hot Encoding

One-hot encoding creates a separate binary column for every category.

Example:

| Colour | Is_Red | Is_Blue | Is_Green |
| ------ | ------ | ------- | -------- |
| Red    | 1      | 0       | 0        |
| Blue   | 0      | 1       | 0        |
| Green  | 0      | 0       | 1        |
| Red    | 1      | 0       | 0        |

Each category gets its own column.

There is no numerical ranking between the categories.

### Main idea

```text
Label Encoding
-> Compact
-> May create false ordering

One-Hot Encoding
-> More columns
-> Does not imply ordering
```

---

# 10. K-Nearest Neighbours

K-Nearest Neighbours is commonly abbreviated as:

```text
KNN
```

The basic idea is simple:

> A new data point can be classified by looking at the closest labelled data points around it.

The nearest neighbours vote.

The majority class wins.

---

# 11. Understanding the Name KNN

## K

K represents the number of neighbours that get a vote.

Example:

```text
K = 3
```

means we consider the 3 nearest neighbours.

---

## Nearest

Nearest means the closest points according to a selected distance measure.

---

## Neighbours

Neighbours are surrounding training data points that already have known labels.

---

## Complete Meaning

KNN finds the K closest labelled points to a new data point and uses majority voting to determine its class.

---

# 12. K is a Hyperparameter

A hyperparameter is a setting that we choose.

The model does not learn it automatically from the data.

In KNN:

```text
K = Hyperparameter
```

We choose K before making predictions.

---

# 13. Parameters vs Hyperparameters

## Parameters

Parameters are learned from the training data.

Example:

In Linear Regression:

```text
y = mx + b
```

The model learns:

```text
m -> slope
b -> intercept
```

These are parameters.

---

## Hyperparameters

Hyperparameters are selected by us.

Examples:

```text
K in KNN
Learning rate
Number of trees
```

The model does not learn K from the dataset.

---

# 14. Distance in KNN

KNN needs to determine which points are nearest.

For this, we use distance metrics.

Two important distance metrics are:

1. Euclidean Distance
2. Manhattan Distance

---

# 15. Euclidean Distance

Euclidean distance is the straight-line distance between two points.

For two points:

```text
P1 = (x1, y1)
P2 = (x2, y2)
```

Formula:

```text
d = √((x1 - x2)² + (y1 - y2)²)
```

It can be visualised as the direct distance between two points.

Example:

```text
P1 •
   \
    \
     \  straight-line distance
      \
       • P2
```

Euclidean distance is commonly the default distance metric used in KNN implementations.

---

# 16. Manhattan Distance

Manhattan distance allows movement only horizontally and vertically.

Formula:

```text
d = |x1 - x2| + |y1 - y2|
```

It is similar to moving through city blocks.

Example:

```text
• -----
      |
      |
      •
```

Only horizontal and vertical movement is considered.

Manhattan distance can be useful when the features represent grid-like movement.

---

# 17. KNN Example

Consider the following training data:

| Point | x1 | x2 | Class |
| ----- | -- | -- | ----- |
| A     | 1  | 2  | Red   |
| B     | 2  | 3  | Red   |
| C     | 3  | 2  | Red   |
| D     | 6  | 5  | Blue  |
| E     | 7  | 4  | Blue  |
| F     | 6  | 6  | Blue  |

We receive a new point:

```text
Q = (4, 4)
```

We want to classify Q.

Initially:

```text
K = 3
```

---

# 18. Step 1 - Compute Distances

Using Euclidean distance:

### Point A

```text
A = (1, 2)

d = √((4 - 1)² + (4 - 2)²)
  = √(9 + 4)
  = √13
  ≈ 3.61
```

### Point B

```text
B = (2, 3)

d = √((4 - 2)² + (4 - 3)²)
  = √(4 + 1)
  = √5
  ≈ 2.24
```

### Point C

```text
C = (3, 2)

d = √((4 - 3)² + (4 - 2)²)
  = √(1 + 4)
  = √5
  ≈ 2.24
```

### Point D

```text
D = (6, 5)

d = √((4 - 6)² + (4 - 5)²)
  = √(4 + 1)
  = √5
  ≈ 2.24
```

### Point E

```text
E = (7, 4)

d = √((4 - 7)² + (4 - 4)²)
  = √9
  = 3.00
```

### Point F

```text
F = (6, 6)

d = √((4 - 6)² + (4 - 6)²)
  = √(4 + 4)
  ≈ 2.83
```

---

# 19. Distance Table

| Point | Distance from Q |
| ----- | --------------- |
| A     | 3.61            |
| B     | 2.24            |
| C     | 2.24            |
| D     | 2.24            |
| E     | 3.00            |
| F     | 2.83            |

---

# 20. Step 2 - Sort the Distances

From smallest to largest:

```text
B -> 2.24
C -> 2.24
D -> 2.24
F -> 2.83
E -> 3.00
A -> 3.61
```

---

# 21. Step 3 - Pick K Nearest

We selected:

```text
K = 3
```

Therefore, select:

```text
B
C
D
```

Their classes are:

```text
B -> Red
C -> Red
D -> Blue
```

---

# 22. Step 4 - Voting

Votes:

```text
Red  -> 2
Blue -> 1
```

Red has the majority.

Therefore:

```text
Q -> Red
```

---

# 23. Complete KNN Process

The KNN inference process is:

```text
1. Compute distance
2. Sort distances
3. Pick K nearest neighbours
4. Vote
5. Assign label
```

This is the core logic of KNN classification.

---

# 24. KNN Training

KNN behaves differently from algorithms such as Linear Regression.

## Linear Regression during training

Linear Regression:

```text
1. Computes required values
2. Finds model parameters
3. Stores m and b
4. Uses the learned equation for prediction
```

---

## KNN during training

KNN:

```text
1. Does not build a traditional mathematical model
2. Stores the training data
3. Performs most calculations during prediction
```

KNN is therefore called a:

**Lazy Learner**

---

# 25. Lazy Learning

KNN defers computation until prediction time.

### Training Time

```text
Store training data
```

### Prediction Time

```text
Calculate distances
        ↓
Sort distances
        ↓
Select K nearest
        ↓
Vote
        ↓
Predict class
```

Therefore:

**KNN is fast to train but can be slow to predict on large datasets.**

Every prediction may require calculating distances to the training points.

---

# 26. Effect of K

The value of K can change the prediction.

Using the same point:

```text
Q = (4, 4)
```

---

## K = 1

Nearest point:

```text
B -> Red
```

Therefore:

```text
Q -> Red
```

A very small K is highly sensitive to local noise and outliers.

---

## K = 3

Neighbours:

```text
B -> Red
C -> Red
D -> Blue
```

Votes:

```text
Red  -> 2
Blue -> 1
```

Therefore:

```text
Q -> Red
```

---

## K = 5

Neighbours:

```text
B -> Red
C -> Red
D -> Blue
E -> Blue
F -> Blue
```

Votes:

```text
Red  -> 2
Blue -> 3
```

Therefore:

```text
Q -> Blue
```

---

# 27. Why K Matters

The same point can receive different predictions for different values of K.

```text
K = 1 -> Red
K = 3 -> Red
K = 5 -> Blue
```

Therefore, choosing an appropriate K is important.

---

# 28. Small K

When K is small:

```text
Boundary -> More complex
```

The decision boundary can become jagged and irregular.

Advantages:

* Sensitive to local patterns

Disadvantages:

* Sensitive to noise
* Sensitive to outliers
* Higher risk of overfitting

Example:

```text
K = 1
```

can strongly react to one nearby data point.

---

# 29. Large K

When K is large:

```text
Boundary -> Smoother
```

The model considers a broader group of neighbours.

Advantages:

* Less sensitive to individual noise points
* Smoother decision boundary

Disadvantages:

* May ignore important local patterns
* Higher risk of underfitting

---

# 30. Overfitting and Underfitting

## Overfitting

The model becomes too sensitive to the training data.

In KNN:

```text
Very small K
        ↓
Complex boundary
        ↓
May memorize noise
        ↓
Overfitting
```

---

## Underfitting

The model becomes too simple and fails to capture important patterns.

In KNN:

```text
Very large K
        ↓
Very smooth boundary
        ↓
May miss real patterns
        ↓
Underfitting
```

---

# 31. Choosing K

Some useful guidelines:

### Use odd K for binary classification

An odd value can help reduce the possibility of a tie.

Example:

```text
K = 3
K = 5
K = 7
```

---

### Rough starting point

A rough first guess can be:

```text
K = √n
```

where `n` is the number of training samples.

---

### Evaluate different K values

Instead of blindly selecting one K:

```text
Try multiple K values
        ↓
Evaluate performance
        ↓
Use cross-validation
        ↓
Select a suitable K
```

---

# 32. Important Definitions

### Classification

Predicting a category or label instead of a continuous numerical value.

### Decision Boundary

A boundary that separates different classes in the feature space.

### Binary Classification

Classification with exactly two output categories.

### Multiclass Classification

Classification with more than two output categories.

### Encoding

Converting categorical values into numerical representations.

### Label Encoding

Assigning an integer to each category.

### One-Hot Encoding

Representing each category using a separate binary column.

### KNN

A classification algorithm that predicts a class using the nearest labelled data points.

### K

The number of nearest neighbours considered for voting.

### Parameter

A value learned by the model from data.

### Hyperparameter

A setting selected by the user rather than learned by the model.

### Euclidean Distance

Straight-line distance between two points.

### Manhattan Distance

Distance calculated using horizontal and vertical movements.

### Lazy Learner

A learning approach where most computation is postponed until prediction time.

---

# 33. Day 13 Summary

Today I learned how machine learning can move from:

```text
Predicting Numbers
        ↓
Regression
```

to:

```text
Predicting Categories
        ↓
Classification
```

I learned that classification models divide the feature space using a decision boundary.

I also learned that machine learning models work with numerical values, so categorical data may need encoding.

The two encoding techniques studied were:

```text
Label Encoding
One-Hot Encoding
```

Then I learned K-Nearest Neighbours.

The main idea of KNN is:

```text
Find nearest neighbours
        ↓
Let them vote
        ↓
Majority wins
```

The complete KNN process is:

```text
Compute Distance
       ↓
Sort
       ↓
Pick K Nearest
       ↓
Vote
       ↓
Assign Label
```

I also learned:

* Euclidean Distance
* Manhattan Distance
* Parameters
* Hyperparameters
* Lazy Learning
* Effect of K
* Overfitting
* Underfitting
* Decision boundary changes with K

---

# 34. Key Takeaways

```text
Classification -> Predicts categories

Decision Boundary -> Separates classes

Binary Classification -> 2 classes

Multiclass Classification -> More than 2 classes

Encoding -> Converts categories into numerical form

Label Encoding -> Assigns numbers to categories

One-Hot Encoding -> Creates binary columns

KNN -> Uses nearest labelled neighbours

K -> Number of neighbours

Euclidean -> Straight-line distance

Manhattan -> Grid-like distance

KNN -> Lazy learner

Small K -> Complex boundary / Overfitting risk

Large K -> Smooth boundary / Underfitting risk
```

---

# 35. Next Step

The next learning step is to implement KNN in Python.

Planned tasks:

1. Implement KNN from scratch.
2. Use a real dataset.
3. Implement KNN without libraries.
4. Use `KNeighborsClassifier` from scikit-learn.
5. Compare the results.
6. Evaluate using:

   * Accuracy
   * Confusion Matrix
   * Classification Report
