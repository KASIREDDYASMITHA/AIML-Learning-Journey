# Day 14 - KNN: Effect of K and Decision Boundary

## Topic

K Nearest Neighbours (KNN)

Today's class focused on how the value of K affects KNN predictions and the shape of the decision boundary.

---

# 1. Effect of K on the Prediction

The value of K has a major effect on the result produced by KNN.

For the same query point, changing K can produce a different predicted class.

Example:

Query point:

Q = (4, 4)

The training dataset contains:

| Point | x1 | x2 | Class |
|------|----|----|-------|
| A | 1 | 2 | Red |
| B | 2 | 3 | Red |
| C | 3 | 2 | Red |
| D | 6 | 5 | Blue |
| E | 7 | 4 | Blue |
| F | 6 | 6 | Blue |

---

# 2. K = 1

When:

K = 1

Only the single nearest neighbour is considered.

For Q:

Nearest neighbour = B

B belongs to the Red class.

Therefore:

Q = Red

### Problem with K = 1

K = 1 is very sensitive to local noise.

If the nearest point is an outlier or noisy point, the prediction can change completely.

So:

Small K → High sensitivity to individual points

---

# 3. K = 3

When:

K = 3

The three nearest neighbours are considered.

The nearest neighbours are:

- B → Red
- C → Red
- D → Blue

Votes:

Red = 2

Blue = 1

Therefore:

Q = Red

K = 3 gives a more balanced local view than K = 1.

It is more resistant to a single outlier.

---

# 4. K = 5

When:

K = 5

The five nearest neighbours are considered.

The neighbours are:

- B → Red
- C → Red
- D → Blue
- E → Blue
- F → Blue

Votes:

Red = 2

Blue = 3

Therefore:

Q = Blue

---

# 5. Same Point, Different K

The same query point can receive different predictions depending on K.

For Q:

K = 1 → Red

K = 3 → Red

K = 5 → Blue

Therefore:

The choice of K matters enormously.

K is not just a minor setting. It can completely change the prediction.

---

# 6. Why Use Odd K for Binary Classification?

In binary classification, there are two possible classes.

Example:

- Red
- Blue

If K is even, a tie can occur.

Example:

K = 4

Suppose:

Red = 2 votes

Blue = 2 votes

There is no majority.

Using an odd value of K helps avoid ties in binary classification.

Examples of odd K:

- K = 1
- K = 3
- K = 5
- K = 7

Therefore:

For binary classification, odd K values are generally preferred.

---

# 7. Starting Value of K

A rough first guess for K can be:

K = √n

where:

n = number of training examples

This is only a starting point.

It is NOT a rule that guarantees the best K.

The final value of K should be selected by testing multiple values and evaluating model performance.

---

# 8. Cross-Validation for Choosing K

Instead of randomly choosing one K, we can try multiple values of K.

For example:

K = 1

K = 3

K = 5

K = 7

K = 9

Then evaluate their performance.

Cross-validation can be used to compare different K values and select a value that generalizes well.

---

# 9. How K Shapes the Decision Boundary

The value of K also changes the shape of the KNN decision boundary.

The decision boundary separates different classes in the feature space.

---

# 10. Small K

Example:

K = 1

A small K makes KNN highly sensitive to individual training points.

The decision boundary becomes:

- Jagged
- Irregular
- Very closely wrapped around the training points

This can cause overfitting.

---

# 11. Overfitting with Small K

Overfitting happens when the model becomes too closely focused on the training data.

With a very small K:

- Noise can strongly affect predictions
- Individual points have a large influence
- The decision boundary becomes very complex
- The model may memorize noise instead of learning general patterns

Therefore:

Small K → Complex boundary → Higher risk of overfitting

---

# 12. Large K

Example:

K = 15

A large K considers many neighbouring points.

The decision boundary becomes:

- Smooth
- Broad
- Less sensitive to individual points

However, if K becomes too large, important local patterns can be lost.

---

# 13. Underfitting with Large K

Underfitting happens when the model is too simple to capture the actual patterns in the data.

With a very large K:

- The model considers too many points
- Local patterns may be ignored
- The decision boundary becomes too smooth
- Important patterns may be missed

Therefore:

Large K → Smooth boundary → Higher risk of underfitting

---

# 14. Small K vs Large K

## Small K

Example:

K = 1

Characteristics:

- Jagged decision boundary
- Highly sensitive to local data
- Sensitive to noise
- Can overfit

## Large K

Example:

K = 15

Characteristics:

- Smooth decision boundary
- Less sensitive to individual points
- More general
- Can underfit

---

# 15. The Right K

The goal is not:

"Choose the smallest K."

The goal is not:

"Choose the largest K."

The goal is to find a suitable K that provides a good balance.

The ideal K should produce a decision boundary that is:

- Smooth enough to generalize
- Sensitive enough to capture meaningful patterns
- Not excessively affected by noise

The correct K should be selected using model evaluation and cross-validation.

---

# 16. KNN as a Lazy Learner

KNN is called a lazy learning algorithm.

Why?

Because KNN does almost no computation during the training phase.

Instead, it stores the training data and performs the major computation when a prediction is requested.

---

# 17. Training in KNN

During training:

- KNN does not calculate a traditional model equation
- It does not learn parameters such as slope and intercept
- It stores the training dataset
- It defers computation until prediction time

Therefore:

KNN training is very fast.

---

# 18. Inference in KNN

When a new data point arrives, KNN performs the actual work.

For every prediction, KNN:

1. Calculates the distance from the query point to training points.
2. Sorts the points according to distance.
3. Selects the K nearest neighbours.
4. Looks at their classes.
5. Performs majority voting.
6. Assigns the predicted class.

Therefore:

KNN is fast to train but can be slow to predict on large datasets.

---

# 19. Why KNN Can Be Slow During Prediction

Suppose the training dataset contains a very large number of points.

For every new query point, KNN may need to calculate distances to all training points.

Therefore, as the dataset becomes larger:

- More distances need to be calculated
- More computation is required during inference
- Prediction can become slower

This is one of the main characteristics of lazy learning.

---

# 20. KNN Decision Process

The complete KNN inference process is:

Distance

↓

Sort

↓

Select K nearest neighbours

↓

Majority vote

↓

Assign class

This is the fundamental prediction process of KNN.

---

# 21. Important Relationship Between K and Decision Boundary

The value of K directly influences the complexity of the decision boundary.

### Small K

Small K:

→ Complex boundary

→ Jagged boundary

→ Sensitive to noise

→ Risk of overfitting

### Large K

Large K:

→ Smooth boundary

→ Broad regions

→ Less sensitivity to individual points

→ Risk of underfitting

---

# 22. Important Concepts

## Classification

Classification predicts a category rather than a continuous numerical value.

Examples:

- Spam / Not Spam
- Fraud / Not Fraud
- Cat / Dog / Bird

---

## Decision Boundary

A decision boundary separates different classes in feature space.

A new point is assigned a class depending on which region of the feature space it falls into.

---

## K

K represents the number of nearest neighbours that participate in the prediction.

K is a hyperparameter.

---

## Hyperparameter

A hyperparameter is a setting chosen by the user before or during model configuration rather than learned automatically from the training data.

For KNN:

K is a hyperparameter.

---

## Euclidean Distance

Euclidean distance measures straight-line distance between points.

Formula:

d = √((x1 - x2)² + (y1 - y2)²)

It is the default distance metric in many KNN implementations.

---

## Manhattan Distance

Manhattan distance measures distance using horizontal and vertical movement.

Formula:

d = |x1 - x2| + |y1 - y2|

It is similar to navigating city blocks.

---

# 23. KNN Summary

KNN:

- Stores the training data
- Does little during training
- Performs most computation during inference
- Uses distance to find nearby points
- Selects K nearest neighbours
- Uses majority voting for classification

