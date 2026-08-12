# Algorithms and Evaluation Metrics

## 1. Algorithm Family Map

The algorithm should be selected according to the task and required output.

| Task | Algorithm | Output |
|---|---|---|
| Regression | Linear Regression | A number |
| Regression | Decision Tree Regressor | A number |
| Classification | Logistic Regression | Probability -> Label |
| Classification | SVM Classifier | Label |
| Classification | Decision Tree Classifier | Probability -> Label |

---

# 2. Linear Regression

Linear Regression is used for regression problems.

Its output is a number.

Example:

Hours Studied -> Predicted Marks

The model tries to find a best-fit line through the data.

The line represents the relationship between the input and output.

---

# 3. Decision Tree Regressor

A Decision Tree Regressor can also be used for regression.

The output is a numerical value.

Example:

Input:

- Area
- Number of rooms
- Location

Output:

Predicted house price

The output is a number, so this is a regression task.

---

# 4. Logistic Regression

Despite the word "Regression", Logistic Regression is a classification algorithm.

It produces a probability that can be mapped to a class label.

Example:

Predicted probability:

0.80

If the chosen threshold is 0.5:

0.80 -> Class 1

Another example:

Predicted probability:

0.20

With a threshold of 0.5:

0.20 -> Class 0

Therefore:

Logistic Regression -> Classification

---

# 5. SVM Classifier

SVM Classifier is used for classification.

Its output is a class label.

Example:

Email -> Spam

or

Email -> Not Spam

The classifier attempts to separate different classes.

---

# 6. Decision Tree Classifier

Decision Tree Classifier is used for classification.

It can produce a class prediction and can also provide class probabilities.

Example:

Input:

- Email word patterns
- Sender information
- Message characteristics

Output:

Spam / Not Spam

---

# 7. Regression Evaluation Metrics

Regression evaluates how far the predicted value is from the actual value.

The smaller the prediction error, the better the model generally performs.

The faculty notes list:

- Mean Absolute Error (MAE)
- RMSE

---

## Mean Absolute Error (MAE)

MAE measures the average absolute difference between predicted and actual values.

Simple idea:

Prediction -> Actual

The difference between them represents the error.

Example:

Predicted house price = ₹80 lakh

Actual house price = ₹95 lakh

Difference = ₹15 lakh

A smaller error means the prediction is closer to reality.

---

## RMSE

RMSE is another regression evaluation metric.

It measures prediction error while giving greater influence to larger errors.

The important idea is:

> Regression metrics measure how far the prediction is from reality.

---

# 8. Classification Evaluation Metrics

Classification evaluates how well the model predicts the correct classes.

The faculty notes list:

- Accuracy
- Log Loss
- F1 Score

---

## Accuracy

Accuracy measures how many predictions are correct out of all predictions.

Example:

Suppose the model makes 100 predictions.

90 predictions are correct.

Accuracy = 90%

---

## Log Loss

Log Loss evaluates the probability assigned to the correct class.

It penalizes incorrect predictions, especially when the model is highly confident about the wrong answer.

Example:

Prediction:

90% Spam

Actual:

Not Spam

The model was highly confident but wrong, so this receives a large penalty.

Another example:

Prediction:

51% Spam

Actual:

Not Spam

The model was wrong but less confident, so the penalty is smaller.

---

## F1 Score

F1 Score is another classification evaluation metric.

It is useful when we want to consider both precision and recall together.

---

# 9. Regression vs Classification Metrics

| Problem | Metrics |
|---|---|
| Regression | MAE, RMSE |
| Classification | Accuracy, Log Loss, F1 Score |

---

# 10. Why Metrics Matter

We cannot evaluate every machine learning problem in the same way.

For regression:

We care about how far the prediction is from the actual value.

For classification:

We care about whether the correct class was predicted and, when probabilities are involved, how confident the model was.

---

# 11. Important Concept

The following three things must be aligned:

1. Output type
2. Algorithm
3. Evaluation metric

Example 1:

House Price Prediction

Output -> Number

Task -> Regression

Possible algorithm -> Linear Regression

Metrics -> MAE / RMSE

Example 2:

Spam Detection

Output -> Category

Task -> Classification

Possible algorithm -> Logistic Regression / SVM / Decision Tree Classifier

Metrics -> Accuracy / Log Loss / F1 Score

---

# 12. Common Confusion: Logistic Regression

The name can be misleading.

Logistic Regression contains the word "Regression", but it belongs to the classification family.

Why?

Because its output is a probability that is mapped to a class label.

Therefore:

Logistic Regression -> Classification

Not:

Logistic Regression -> Regression

---

# Final Rule

Do not choose an algorithm just because of its name.

First identify:

> What type of output do I need?

Then choose:

Output Type -> Task -> Algorithm -> Metric