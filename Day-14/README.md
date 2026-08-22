# AIML Learning Journey - Day 14

## Topic: KNN - Effect of K, Decision Boundary and Lazy Learning

Today I continued learning Classification and K Nearest Neighbours (KNN).

### What I Learned Today

- How changing K changes the prediction in KNN
- K = 1, K = 3 and K = 5
- Why K is an important hyperparameter
- Small K can cause overfitting
- Large K can cause underfitting
- How K affects the decision boundary
- Why odd K values are useful for binary classification
- Rough starting point for K: √n
- Using cross-validation to select K
- KNN is a lazy learning algorithm
- KNN performs most of its computation during inference

### Important Example

For the same query point Q:

- K = 1 → Red
- K = 3 → Red
- K = 5 → Blue

This shows that the choice of K can completely change the prediction.

### Key Takeaway

Small K:
- More sensitive to individual points and noise
- More complex and jagged decision boundary
- Higher risk of overfitting

Large K:
- Smoother and broader decision boundary
- Less sensitive to individual points
- Higher risk of underfitting

The goal is to choose a K that generalizes well.

### Tomorrow

- Implement KNN from scratch in Python
- Implement KNN using sklearn
- Compare results
- Evaluate using:
  - Accuracy
  - Confusion Matrix
  - Classification Report