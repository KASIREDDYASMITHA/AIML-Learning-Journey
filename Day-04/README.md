# Day 4 - Supervised Learning

## Topic

Supervised Learning - Regression, Classification and When to Use What

## What I Learned

Today I learned the fundamentals of supervised learning and the two major types of supervised learning:

1. Regression
2. Classification

I also learned how to decide whether a problem is a regression or classification problem based on the type of output we need.

---

## Topics Covered

- What is Supervised Learning?
- Labeled Training Data
- Pattern Recognition
- Generalization
- Types of Supervised Learning
- Regression
- Classification
- Regression Examples
- Classification Examples
- Regression vs Classification
- Evaluation Metrics
- Algorithm Families
- Logistic Regression
- Decision Tree Regressor
- Decision Tree Classifier
- SVM Classifier
- Why the Output Type Matters
- Interview Questions

---

## Key Idea

The most important question to ask before choosing a machine learning algorithm is:

> Is my output a number or a category?

### If the output is a number:

Use Regression.

Examples:

- House price prediction
- Salary estimation
- Student score prediction
- Temperature prediction

### If the output is a category:

Use Classification.

Examples:

- Spam or Not Spam
- Disease Positive or Negative
- Cat, Dog or Bird
- Positive or Negative sentiment

---

## Learning Summary

Supervised learning uses labeled training data.

The model learns the relationship between input features and the correct output.

The goal is not to memorize the training data. The model should learn patterns that allow it to make predictions on unseen data.

---

## Main Difference

| Regression | Classification |
|---|---|
| Predicts a number | Predicts a category |
| Output is continuous | Output is discrete |
| Answers "How much?" | Answers "Which class?" |
| Example: House price | Example: Spam detection |
| Metrics: MAE, RMSE | Metrics: Accuracy, Log Loss, F1 Score |

---

## Important Interview Point

Logistic Regression is a classification algorithm even though its name contains "Regression".

It produces a probability that can be converted into a class label using a threshold.

---

## Day 4 Takeaway

The right tool depends on the problem.

Always understand the required output first, then choose the appropriate algorithm and evaluation metric.

> Output type -> Algorithm choice -> Evaluation metric