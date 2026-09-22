# Day 23 - ROC Curve and AUC

## 1. Classification

In binary classification, the model predicts two classes:

- Positive
- Negative

The prediction depends on a classification threshold.

Example:

Prediction probability = 0.80
Threshold = 0.50

0.80 >= 0.50 → Positive

If the threshold changes, the prediction can also change.

---

## 2. Confusion Matrix

A classification model produces four outcomes:

|                    | Actual Positive | Actual Negative |
|--------------------|-----------------|-----------------|
| Predicted Positive | TP              | FP              |
| Predicted Negative | FN              | TN              |

### TP - True Positive

Actual positive and predicted positive.

Example:
A spam email is correctly identified as spam.

### TN - True Negative

Actual negative and predicted negative.

Example:
A normal email is correctly identified as normal.

### FP - False Positive

Actual negative but predicted positive.

Example:
A normal email is incorrectly classified as spam.

### FN - False Negative

Actual positive but predicted negative.

Example:
A spam email is incorrectly classified as normal.

---

## 3. TPR - True Positive Rate

TPR measures how many actual positive cases are correctly identified.

### Formula

TPR = TP / (TP + FN)

TPR is also called:

- Recall
- Sensitivity

### Example 1

TP = 80
FN = 20

TPR = 80 / (80 + 20)
    = 80 / 100
    = 0.8

TPR = 80%

### Example 2

TP = 90
FN = 10

TPR = 90 / (90 + 10)
    = 90 / 100
    = 0.9

TPR = 90%

Higher TPR means more actual positive cases are correctly detected.

---

## 4. FPR - False Positive Rate

FPR measures how many actual negative cases are incorrectly classified as positive.

### Formula

FPR = FP / (FP + TN)

### Example 1

FP = 10
TN = 90

FPR = 10 / (10 + 90)
    = 10 / 100
    = 0.1

FPR = 10%

### Example 2

FP = 20
TN = 80

FPR = 20 / (20 + 80)
    = 20 / 100
    = 0.2

FPR = 20%

Lower FPR means fewer negative cases are incorrectly classified as positive.

---

## 5. Classification Threshold

A classification model often produces a probability.

Example:

Prediction probability = 0.75

If threshold = 0.50:

0.75 >= 0.50 → Positive

If threshold = 0.80:

0.75 < 0.80 → Negative

Therefore, changing the threshold changes the predictions.

When predictions change:

TP, TN, FP and FN can change.

Therefore:

TPR and FPR can also change.

---

## 6. ROC Curve

ROC stands for:

Receiver Operating Characteristic

ROC curve shows the relationship between:

X-axis → False Positive Rate (FPR)
Y-axis → True Positive Rate (TPR)

ROC curve is obtained by changing the classification threshold and calculating the corresponding FPR and TPR values.

### ROC Curve

TPR
 ^
 |                    *
 |                *
 |            *
 |        *
 |    *
 | *
 +--------------------------> FPR
 0                          1

Each point represents a particular classification threshold.

---

## 7. Good ROC Curve

A good classifier generally tries to achieve:

- High TPR
- Low FPR

The ideal point is:

FPR = 0
TPR = 1

This means:

- No false positives
- All positive cases are correctly identified

---

## 8. Random Classifier

A random classifier has no useful separation between positive and negative classes.

Its ROC curve is approximately a diagonal line.

TPR
 ^
1|                 *
 |              *
 |           *
 |        *
 |     *
 |  *
0|*________________________> FPR
 0                         1

For a random classifier:

AUC = 0.5

---

## 9. AUC

AUC stands for:

Area Under the Curve

In ROC analysis:

AUC = Area Under the ROC Curve

AUC summarizes the ROC curve into a single value.

### AUC Values

AUC = 1.0
→ Perfect classification

AUC = 0.5
→ Random classification

AUC < 0.5
→ Worse than random for the given scoring direction

AUC generally ranges from:

0 to 1

---

## 10. Trapezoidal Rule

When ROC points are given, the area under the ROC curve can be calculated using the trapezoidal rule.

For two consecutive ROC points:

Point 1 = (FPR1, TPR1)
Point 2 = (FPR2, TPR2)

Formula:

Area = (FPR2 - FPR1) × (TPR1 + TPR2) / 2

### Example

Point 1 = (0.2, 0.4)
Point 2 = (0.6, 0.8)

Width:

Width = 0.6 - 0.2
      = 0.4

Average height:

Average height = (0.4 + 0.8) / 2
               = 0.6

Area:

Area = 0.4 × 0.6
     = 0.24

---

## 11. Total AUC

If the ROC curve contains multiple points, calculate the area between every two consecutive points.

Example:

P1 = (0, 0)
P2 = (0.33, 0.6)
P3 = (0.67, 0.8)
P4 = (1, 1)

Calculate:

Area1 = Area between P1 and P2
Area2 = Area between P2 and P3
Area3 = Area between P3 and P4

Then:

Total AUC = Area1 + Area2 + Area3

---

## 12. ROC and Threshold Relationship

Threshold changes
        ↓
Predictions change
        ↓
TP, TN, FP, FN change
        ↓
TPR and FPR change
        ↓
ROC points change
        ↓
ROC Curve
        ↓
AUC

---

## 13. Important Formulas

### True Positive Rate

TPR = TP / (TP + FN)

### False Positive Rate

FPR = FP / (FP + TN)

### Trapezoidal Rule

Area = (FPR2 - FPR1) × (TPR1 + TPR2) / 2

### Total AUC

AUC = Area1 + Area2 + Area3 + ...

---

## 14. Important Differences

### TPR

TPR = TP / (TP + FN)

Measures the proportion of actual positive cases correctly identified.

Also called:

- Recall
- Sensitivity

### FPR

FPR = FP / (FP + TN)

Measures the proportion of actual negative cases incorrectly classified as positive.

### ROC

ROC is a graph of:

FPR on X-axis
TPR on Y-axis

### AUC

AUC is the area under the ROC curve.

---

## 15. Quick Revision

TP = Actual Positive + Predicted Positive

TN = Actual Negative + Predicted Negative

FP = Actual Negative + Predicted Positive

FN = Actual Positive + Predicted Negative

TPR = TP / (TP + FN)

FPR = FP / (FP + TN)

ROC:

X-axis → FPR
Y-axis → TPR

Random Classifier:

AUC = 0.5

Perfect Classifier:

AUC = 1.0

Trapezoidal Rule:

Area = (FPR2 - FPR1) × (TPR1 + TPR2) / 2

---

## 16. Day 23 Core Concept

Threshold
    ↓
TPR and FPR
    ↓
ROC Curve
    ↓
Area Under ROC Curve
    ↓
AUC

The main objective of ROC-AUC is to evaluate the classification model across different classification thresholds.