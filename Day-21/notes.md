# Day 21 - ROC Curve

## 1. Classification Terms

In binary classification, the model prediction can be compared with the actual value.

There are four important terms:

- TP - True Positive
- TN - True Negative
- FP - False Positive
- FN - False Negative

### Confusion Matrix

| Actual | Predicted | Result |
|--------|-----------|--------|
| Positive | Positive | TP |
| Negative | Negative | TN |
| Negative | Positive | FP |
| Positive | Negative | FN |

### TP - True Positive

The actual value is positive and the model also predicts positive.

Example:

Actual = Customer will leave  
Predicted = Customer will leave

This is TP.

### TN - True Negative

The actual value is negative and the model also predicts negative.

Example:

Actual = Customer will stay  
Predicted = Customer will stay

This is TN.

### FP - False Positive

The actual value is negative but the model predicts positive.

Example:

Actual = Customer will stay  
Predicted = Customer will leave

This is FP.

### FN - False Negative

The actual value is positive but the model predicts negative.

Example:

Actual = Customer will leave  
Predicted = Customer will stay

This is FN.

---

# 2. Precision

Precision tells us how many of the predicted positive values are actually positive.

Formula:

Precision = TP / (TP + FP)

Precision is affected by False Positives.

If FP increases, Precision decreases.

---

# 3. Recall

Recall tells us how many of the actual positive values were correctly identified by the model.

Recall is also called True Positive Rate (TPR).

Formula:

TPR = Recall = TP / (TP + FN)

Recall is strongly affected by False Negatives.

If FN increases, Recall decreases.

---

# 4. F1 Score

F1 Score combines Precision and Recall.

Formula:

F1 Score = 2 × Precision × Recall / (Precision + Recall)

F1 Score is useful when both Precision and Recall are important.

---

# 5. True Positive Rate (TPR)

True Positive Rate measures the proportion of actual positive cases correctly predicted as positive.

Formula:

TPR = TP / (TP + FN)

TPR is also called:

Recall
Sensitivity

A higher TPR means the model identifies more actual positive cases.

---

# 6. False Positive Rate (FPR)

False Positive Rate measures the proportion of actual negative cases incorrectly predicted as positive.

Formula:

FPR = FP / (FP + TN)

A lower FPR means fewer negative cases are incorrectly classified as positive.

---

# 7. Classification Threshold

A classification model can produce a probability or score.

For example:

0.85
0.72
0.61
0.43
0.25

A threshold is used to convert these scores into class predictions.

For example, if:

Threshold = 0.50

Then:

Probability >= 0.50 → Positive
Probability < 0.50 → Negative

Changing the threshold changes the number of predicted positive and negative values.

---

# 8. Low Threshold

When the threshold is low, more observations are classified as positive.

Therefore:

TP generally increases
FP generally increases

So:

TPR generally increases
FPR generally increases

A low threshold makes the model more likely to predict the positive class.

---

# 9. High Threshold

When the threshold is high, fewer observations are classified as positive.

Therefore:

TP generally decreases
FP generally decreases

So:

TPR generally decreases
FPR generally decreases

A high threshold makes the model more strict before predicting the positive class.

---

# 10. ROC Curve

ROC stands for:

Receiver Operating Characteristic

A ROC Curve is used to evaluate the performance of a binary classification model across different classification thresholds.

The ROC Curve plots:

X-axis → False Positive Rate (FPR)

Y-axis → True Positive Rate (TPR)

Therefore:

ROC Curve = TPR vs FPR

---

# 11. Why Do We Change the Threshold?

A classification model can give different probability scores.

For example:

0.95
0.82
0.71
0.60
0.42
0.30
0.15

If we change the threshold, the predicted classes change.

This produces different values of:

TP
TN
FP
FN
TPR
FPR

The different TPR and FPR values are used to construct the ROC Curve.

---

# 12. ROC Curve Example

Suppose we have a churn prediction model.

Churn means that a customer leaves the company.

Positive class:

Customer will leave.

Negative class:

Customer will stay.

The model predicts whether a customer will leave.

Different thresholds produce different TPR and FPR values.

Example:

| Threshold | TPR | FPR |
|-----------|-----|-----|
| 0.90 | 0.20 | 0.05 |
| 0.70 | 0.50 | 0.15 |
| 0.50 | 0.70 | 0.30 |
| 0.30 | 0.85 | 0.55 |
| 0.10 | 1.00 | 1.00 |

These points can be plotted on a graph.

X-axis = FPR

Y-axis = TPR

---

# 13. How TP Changes the ROC Curve

Suppose a diabetic patient is added to the dataset.

If the model correctly predicts the patient as positive:

TP increases.

Since:

TPR = TP / (TP + FN)

TPR increases.

If FP remains unchanged:

FPR remains unchanged.

Therefore, the ROC point moves upward.

---

# 14. How FP Changes the ROC Curve

Suppose a non-diabetic patient is incorrectly predicted as positive.

Then:

FP increases.

Since:

FPR = FP / (FP + TN)

FPR increases.

If TP remains unchanged:

TPR remains unchanged.

Therefore, the ROC point moves to the right.

---

# 15. ROC Curve and Threshold

### Low Threshold

Low threshold means more observations are classified as positive.

Usually:

TPR increases
FPR increases

### High Threshold

High threshold means fewer observations are classified as positive.

Usually:

TPR decreases
FPR decreases

Therefore, changing the threshold moves the operating point along the ROC Curve.

---

# 16. Churn Prediction Example

Suppose a business wants to predict customer churn.

Churn means:

Customer leaves the service.

Stay means:

Customer continues using the service.

The model predicts:

Positive → Customer will leave

Negative → Customer will stay

The business team can use the model to identify customers who may leave.

For example, the company may provide a discount to customers predicted to churn.

---

# 17. Benefit and Cost Interpretation

In a business problem, correctly identifying customers who will leave can provide a benefit.

This can be represented using TPR.

Incorrectly giving discounts to customers who would have stayed can represent a cost.

This can be represented using FPR.

Therefore:

Higher TPR → More actual positive cases are identified.

Higher FPR → More negative cases are incorrectly identified as positive.

The actual business benefit and cost depend on the specific application.

---

# 18. ROC Graph

A ROC graph has:

X-axis → FPR

Y-axis → TPR

The ideal operating point is toward:

TPR = 1
FPR = 0

The diagonal line from:

(0, 0) to (1, 1)

represents random classification performance.

---

# 19. Important ROC Points

At a very high threshold, very few observations are predicted positive.

Therefore:

TPR can be close to 0
FPR can be close to 0

At a very low threshold, almost all observations can be predicted positive.

Therefore:

TPR can approach 1
FPR can approach 1

Changing the threshold creates different points on the ROC Curve.

---

# 20. Manual Understanding of ROC Curve

Suppose we have actual labels and model scores.

For every threshold:

1. Choose a threshold.
2. Convert scores into positive or negative predictions.
3. Calculate TP.
4. Calculate TN.
5. Calculate FP.
6. Calculate FN.
7. Calculate TPR.
8. Calculate FPR.
9. Plot FPR on the X-axis.
10. Plot TPR on the Y-axis.

Repeat this for different thresholds.

The resulting points form the ROC Curve.

---

# 21. Key Formulas

## Precision

Precision = TP / (TP + FP)

## Recall / TPR

TPR = TP / (TP + FN)

## FPR

FPR = FP / (FP + TN)

## F1 Score

F1 = 2 × Precision × Recall / (Precision + Recall)

---

# 22. Key Points Learned Today

- TP, TN, FP and FN are classification outcomes.
- Precision focuses on predicted positives.
- Recall focuses on actual positives.
- TPR is the same as Recall.
- FPR measures incorrectly predicted positive negative cases.
- Threshold controls how strict the classifier is.
- Lowering the threshold generally increases both TPR and FPR.
- Increasing the threshold generally decreases both TPR and FPR.
- ROC stands for Receiver Operating Characteristic.
- ROC Curve plots TPR against FPR.
- Different thresholds produce different ROC points.
- TP changes move the ROC point vertically when FPR remains unchanged.
- FP changes move the ROC point horizontally when TPR remains unchanged.
- ROC Curve helps analyze a binary classification model across different thresholds.