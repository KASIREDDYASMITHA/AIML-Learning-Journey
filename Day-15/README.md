# Day 15 - KNN & Introduction to Decision Trees

## Topics Covered

Today I completed the KNN and started learning Decision Trees.

### KNN
- Strengths and weaknesses of KNN
- KNN is simple and easy to understand
- No training time
- Handles multiclass classification
- Non-parametric algorithm
- Slow inference
- Sensitive to irrelevant features
- Sensitive to feature scaling
- Curse of dimensionality

### Decision Trees
- Classification using if-else rules
- Converting if-else rules into a tree
- Decision Tree terminology
- Root node
- Splits
- Internal nodes
- Leaf nodes
- Selecting the best column
- Selecting the best numerical threshold

### Entropy
- Entropy measures disorder or uncertainty
- Low entropy means a group is easier to predict
- High entropy means a group is harder to predict
- Pure group has entropy = 0
- Equal binary classes have entropy = 1
- Entropy formula:
  H = -Σ pᵢ log₂(pᵢ)

### Information Gain
- Information Gain measures the reduction in entropy after a split
- Information Gain = Entropy before - Weighted Entropy after
- Decision Trees choose the split with the highest Information Gain

## Practical Work

Implemented:
- A simple Decision Tree style classifier using if-else logic
- Entropy calculation in Python
- Entropy examples for different class distributions

