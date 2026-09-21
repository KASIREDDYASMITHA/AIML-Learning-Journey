# Day 22 - Classification Evaluation

## 1. Classification Evaluation

Classification evaluation is used to understand how well a classification model is performing.

Accuracy alone is not always enough because it does not show the type of mistakes made by the model.

The goal of classification evaluation is to understand:

- Correct predictions
- False alarms
- Missed positive cases
- The cost of different types of mistakes

---

# 2. Why Accuracy Alone Is Not Enough

Consider a disease detection problem.

Suppose there are 10,000 patients:

- 100 patients have the disease
- 9,900 patients do not have the disease

If a model predicts "Healthy" for every patient:

- 9,900 predictions are correct
- 100 sick patients are missed

Accuracy:

Accuracy = Correct Predictions / Total Predictions

Accuracy = 9900 / 10000

Accuracy = 99%

Although the accuracy is 99%, the model failed to identify even one sick patient.

This happens because the dataset is highly imbalanced.

Therefore, accuracy alone can be misleading.

---

# 3. Four Types of Predictions

Every classification prediction belongs to one of four categories.

## True Positive (TP)

The model predicts Positive and the actual value is Positive.

Example:

A sick patient is correctly identified as sick.

---

## True Negative (TN)

The model predicts Negative and the actual value is Negative.

Example:

A healthy patient is correctly identified as healthy.

---

## False Positive (FP)

The model predicts Positive but the actual value is Negative.

Example:

A healthy patient is incorrectly identified as sick.

False Positive is also called a Type I Error.

It can be considered a false alarm.

---

## False Negative (FN)

The model predicts Negative but the actual value is Positive.

Example:

A sick patient is incorrectly identified as healthy.

False Negative is also called a Type II Error.

It means a positive case was missed.

---

# 4. Confusion Matrix

A confusion matrix organizes TP, TN, FP and FN.

|                  | Predicted Positive | Predicted Negative |
|------------------|--------------------|--------------------|
| Actual Positive  | TP                 | FN                 |
| Actual Negative  | FP                 | TN                 |

Example:

Suppose a disease detection model is tested on 100 patients.

- 10 patients are actually sick
- 90 patients are actually healthy
- TP = 8
- FN = 2
- FP = 5
- TN = 85

The confusion matrix is:

|                  | Predicted Positive | Predicted Negative |
|------------------|--------------------|--------------------|
| Actual Positive  | 8                  | 2                  |
| Actual Negative  | 5                  | 85                 |

---

# 5. Accuracy

Accuracy tells us the percentage of total predictions that are correct.

Formula:

Accuracy = (TP + TN) / (TP + FP + FN + TN)

For the example:

TP = 8
TN = 85
FP = 5
FN = 2

Accuracy:

Accuracy = (8 + 85) / (8 + 5 + 2 + 85)

Accuracy = 93 / 100

Accuracy = 93%

---

# 6. Precision

Precision answers:

"Of all the cases predicted as Positive, how many were actually Positive?"

Formula:

Precision = TP / (TP + FP)

For the example:

Precision = 8 / (8 + 5)

Precision = 8 / 13

Precision = 61.5%

Precision is important when False Positives are costly.

Examples:

- Spam filtering
- Fraud alerts
- Content moderation

---

# 7. Recall

Recall answers:

"Of all the cases that were actually Positive, how many did the model correctly identify?"

Formula:

Recall = TP / (TP + FN)

For the example:

Recall = 8 / (8 + 2)

Recall = 8 / 10

Recall = 80%

Recall is important when False Negatives are costly.

Examples:

- Disease detection
- Fraud investigation
- Criminal identification

---

# 8. Precision vs Recall

Precision focuses on False Positives.

Recall focuses on False Negatives.

High Precision:

The model makes fewer false alarms.

High Recall:

The model misses fewer positive cases.

Neither precision nor recall should always be considered alone.

---

# 9. F1 Score

F1 Score combines Precision and Recall using the harmonic mean.

Formula:

F1 = 2 × (Precision × Recall) / (Precision + Recall)

For the example:

Precision = 0.615
Recall = 0.80

F1 = 2 × (0.615 × 0.80) / (0.615 + 0.80)

F1 ≈ 0.696

F1 ≈ 69.6%

The harmonic mean is useful because it is strongly affected when one of Precision or Recall is very low.

A high F1 Score generally requires both Precision and Recall to be reasonably good.

---

# 10. Why Not Arithmetic Mean?

Suppose:

Precision = 0%
Recall = 100%

Arithmetic Mean:

(0 + 100) / 2 = 50%

A score of 50% may look acceptable, but the model has zero precision.

Therefore, arithmetic mean can hide extreme imbalance.

---

# 11. Why Harmonic Mean?

The harmonic mean gives more importance to the smaller value.

If either Precision or Recall is close to zero, F1 Score also becomes low.

Therefore, F1 Score is useful when both Precision and Recall matter.

---

# 12. Multiclass Classification

In multiclass classification, there are more than two classes.

Example:

- Cat
- Dog
- Bird

A 3-class problem has a 3 × 3 confusion matrix.

Example:

| Actual / Predicted | Cat | Dog | Bird |
|--------------------|-----|-----|------|
| Cat                | 40  | 5   | 5    |
| Dog                | 3   | 32  | 5    |
| Bird               | 2   | 3   | 55   |

Diagonal values represent correct predictions.

Off-diagonal values represent incorrect predictions.

Overall Accuracy:

Accuracy = (40 + 32 + 55) / 150

Accuracy = 127 / 150

Accuracy = 84.7%

---

# 13. Per-Class Evaluation

For multiclass classification, each class can be treated as a binary classification problem.

For example, for the Cat class:

- Cat = Positive
- Dog and Bird = Negative

Cat:

TP = 40

FP = 3 + 2 = 5

FN = 5 + 5 = 10

Precision:

Precision = 40 / (40 + 5)

Precision = 88.9%

Recall:

Recall = 40 / (40 + 10)

Recall = 80%

---

# 14. Macro Averaging

Macro averaging calculates the metric independently for each class and then takes the simple average.

Formula:

Macro Metric = Sum of Class Metrics / Number of Classes

Macro averaging gives equal importance to every class.

It is useful when all classes are considered equally important.

Example:

Macro Precision:

(88.9 + 80 + 84.6) / 3

= 84.5%

Macro Recall:

(80 + 80 + 91.7) / 3

= 83.9%

Macro F1:

(84.2 + 80 + 88) / 3

= 84.1%

---

# 15. Weighted Averaging

Weighted averaging gives more importance to classes with more samples.

The metric is weighted according to the number of actual samples in each class.

Example:

Classes:

Cat = 50 samples
Dog = 40 samples
Bird = 60 samples

Weighted Precision:

(88.9 × 50 + 80 × 40 + 84.6 × 60) / 150

≈ 84.8%

Weighted Recall:

(80 × 50 + 80 × 40 + 91.7 × 60) / 150

≈ 84.7%

Weighted F1:

(84.2 × 50 + 80 × 40 + 88 × 60) / 150

≈ 84.6%

Macro averaging treats classes equally.

Weighted averaging gives more importance to larger classes.

---

# 16. How to Choose the Evaluation Metric

The metric depends on the problem.

## When Missing a Positive Is Very Costly

Prioritize Recall.

Examples:

- Disease detection
- Fraud detection
- Crime detection

A False Negative can be very costly.

---

## When False Alarms Are Very Costly

Prioritize Precision.

Examples:

- Spam filtering
- Loan approval
- Content moderation

A False Positive can be very costly.

---

## When Both Errors Matter

Use F1 Score.

F1 balances Precision and Recall.

---

# 17. Classification Threshold

A classification model can produce a probability instead of directly producing a class label.

Example:

Model output:

0.73

This means the model gives a probability of 73%.

A threshold is then used to convert the probability into a class.

For example:

Threshold = 0.5

If probability >= 0.5:

Predict Positive.

If probability < 0.5:

Predict Negative.

---

# 18. Low Threshold

Example:

Threshold = 0.3

More cases will be predicted as Positive.

This generally:

- Increases Recall
- Can decrease Precision
- Catches more positive cases
- Creates more false alarms

This can be useful when missing a positive case is very costly.

---

# 19. High Threshold

Example:

Threshold = 0.8

Only highly confident predictions are classified as Positive.

This generally:

- Increases Precision
- Can decrease Recall
- Produces fewer false alarms
- May miss more positive cases

This can be useful when False Positives are very costly.

---

# 20. Precision-Recall Trade-off

As the threshold increases:

Precision generally increases.

Recall generally decreases.

As the threshold decreases:

Recall generally increases.

Precision generally decreases.

Therefore, the threshold directly affects the balance between Precision and Recall.

The default threshold of 0.5 is not always the best choice.

---

# 21. TPR and FPR

TPR stands for True Positive Rate.

TPR is also related to Recall.

Formula:

TPR = TP / (TP + FN)

FPR stands for False Positive Rate.

Formula:

FPR = FP / (FP + TN)

ROC analysis uses:

X-axis = False Positive Rate (FPR)

Y-axis = True Positive Rate (TPR)

A change in the classification threshold changes the TPR and FPR.

This creates different points that can be used to build an ROC curve.

