# Day 21 - ROC Curve

## Topics Learned

- Classification terms: TP, TN, FP, FN
- Precision, Recall and F1 Score
- True Positive Rate (TPR)
- False Positive Rate (FPR)
- Classification threshold
- Low threshold vs High threshold
- ROC Curve
- How TP and FP affect the ROC Curve
- Manually understanding ROC Curve points
- Churn prediction example
- Benefit and Cost interpretation

## Key Formulas

### Precision
Precision = TP / (TP + FP)

### Recall / True Positive Rate
TPR = TP / (TP + FN)

### False Positive Rate
FPR = FP / (FP + TN)

### F1 Score
F1 = 2 × Precision × Recall / (Precision + Recall)

## ROC Curve

A ROC Curve plots:

- X-axis → False Positive Rate (FPR)
- Y-axis → True Positive Rate (TPR)

Different classification thresholds produce different TPR and FPR values.

