# Day 23 - ROC Curve and AUC

## Topics Covered

- True Positive Rate (TPR)
- False Positive Rate (FPR)
- ROC Curve
- Random Classifier
- AUC (Area Under the Curve)
- Trapezoidal Rule for calculating AUC

## Key Formulas

### True Positive Rate (TPR)

TPR = TP / (TP + FN)

TPR is also called Recall or Sensitivity.

### False Positive Rate (FPR)

FPR = FP / (FP + TN)

## ROC Curve

ROC curve is a graph of:

- X-axis → False Positive Rate (FPR)
- Y-axis → True Positive Rate (TPR)

Different classification thresholds produce different FPR and TPR values.

## Random Classifier

A random classifier gives an ROC curve close to the diagonal line.

AUC of a random classifier = 0.5

## AUC

AUC means Area Under the ROC Curve.

- AUC = 1.0 → perfect separation
- AUC = 0.5 → random classification
- AUC below 0.5 → worse than random for the given scoring direction

## Trapezoidal Rule

For two consecutive ROC points:

AUC = (FPR2 - FPR1) × (TPR1 + TPR2) / 2

The total AUC is obtained by adding the area of all trapezoids.

## Programs

1. Calculate TPR and FPR from confusion matrix values.
2. Calculate AUC using the trapezoidal rule.
3. Calculate the AUC of a random classifier.

