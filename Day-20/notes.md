# Day 20 – Classification Evaluation

## 1. Classification Evaluation

Classification evaluation is the process of measuring how well a classification model performs.

Accuracy alone is not always enough because it does not show the type of mistakes made by the model.

The goal of classification evaluation is to understand:

* How many predictions are correct
* How many predictions are wrong
* What type of mistakes are being made
* The real-world cost of False Positives and False Negatives

---

# 2. Why Accuracy Alone Is Not Enough

Consider a disease detection problem.

Suppose there are 10,000 patients and only 100 patients have a disease.

If a model predicts:

* Healthy for all 10,000 patients
* Sick for no patient

Then:

* 9,900 healthy patients are correctly predicted
* 100 sick patients are missed

Accuracy:

```text
Accuracy = 9900 / 10000
         = 99%
```

The model has 99% accuracy but fails to detect even one sick patient.

This happens because of class imbalance.

Therefore, accuracy can be misleading when one class is much larger than another.

---

# 3. Four Types of Classification Outcomes

Every classification prediction falls into one of four categories.

## 3.1 True Positive (TP)

The model predicts Positive and the actual value is Positive.

Example:

A patient has a disease and the model correctly predicts that the patient has the disease.

```text
TP = Correct Positive Prediction
```

---

## 3.2 True Negative (TN)

The model predicts Negative and the actual value is Negative.

Example:

A healthy patient is correctly identified as healthy.

```text
TN = Correct Negative Prediction
```

---

## 3.3 False Positive (FP)

The model predicts Positive but the actual value is Negative.

Example:

A healthy patient is incorrectly identified as sick.

This is also called a:

```text
Type I Error
```

```text
FP = False Alarm
```

---

## 3.4 False Negative (FN)

The model predicts Negative but the actual value is Positive.

Example:

A sick patient is incorrectly identified as healthy.

This is also called a:

```text
Type II Error
```

```text
FN = Missed Positive
```

---

# 4. Confusion Matrix

A confusion matrix organizes TP, TN, FP and FN.

For binary classification:

```text
                    Predicted
                  Positive  Negative

Actual Positive      TP        FN

Actual Negative      FP        TN
```

Example:

Suppose a disease detection model is tested on 100 patients.

* 10 patients are actually sick
* 90 patients are actually healthy
* TP = 8
* FN = 2
* FP = 5
* TN = 85

Confusion Matrix:

```text
                    Predicted
                  Positive  Negative

Actual Positive      8         2

Actual Negative      5        85
```

All classification metrics are calculated from these four values.

---

# 5. Accuracy

Accuracy measures the overall percentage of correct predictions.

Formula:

```text
Accuracy = (TP + TN) / (TP + FP + FN + TN)
```

Using:

```text
TP = 8
TN = 85
FP = 5
FN = 2
```

```text
Accuracy = (8 + 85) / 100
         = 93%
```

Therefore, 93 out of 100 predictions were correct.

## Limitation of Accuracy

Accuracy can be misleading when classes are imbalanced.

A model that predicts the majority class for every sample can still get high accuracy.

---

# 6. Precision

Precision answers:

```text
Of all the samples predicted as Positive,
how many were actually Positive?
```

Formula:

```text
Precision = TP / (TP + FP)
```

For our example:

```text
Precision = 8 / (8 + 5)
          = 8 / 13
          = 61.5%
```

Precision tells us how reliable positive predictions are.

## When Precision Is Important

Precision is important when False Positives are costly.

Examples:

* Spam filtering
* Fraud alerts
* Content moderation

High Precision means fewer false alarms.

---

# 7. Recall

Recall answers:

```text
Of all the samples that were actually Positive,
how many did the model correctly identify?
```

Formula:

```text
Recall = TP / (TP + FN)
```

For our example:

```text
Recall = 8 / (8 + 2)
       = 8 / 10
       = 80%
```

The model detected 80% of the actual positive cases.

## When Recall Is Important

Recall is important when False Negatives are costly.

Examples:

* Disease detection
* Fraud investigation
* Criminal identification

High Recall means fewer actual positive cases are missed.

---

# 8. Precision vs Recall

Precision and Recall focus on different types of errors.

### Precision

Focuses on False Positives.

```text
Precision = TP / (TP + FP)
```

Question:

```text
When the model says Positive, how often is it correct?
```

### Recall

Focuses on False Negatives.

```text
Recall = TP / (TP + FN)
```

Question:

```text
Of all actual Positives, how many did the model find?
```

---

# 9. F1 Score

Precision and Recall can sometimes give very different results.

The F1 Score combines Precision and Recall using the harmonic mean.

Formula:

```text
F1 = 2 × (Precision × Recall) / (Precision + Recall)
```

For example:

```text
Precision = 61.5%
Recall = 80%
```

Using decimal values:

```text
Precision = 0.615
Recall = 0.80
```

```text
F1 = 2 × (0.615 × 0.80) / (0.615 + 0.80)

F1 ≈ 69.6%
```

The harmonic mean gives more importance to the smaller value.

Therefore, a model needs both good Precision and good Recall to achieve a high F1 Score.

---

# 10. Why Not Arithmetic Mean?

Suppose:

```text
Precision = 0%
Recall = 100%
```

Arithmetic mean:

```text
(0 + 100) / 2 = 50%
```

This can look acceptable even though the model is not useful.

The F1 Score avoids this problem because the harmonic mean is strongly affected by a very low value.

---

# 11. Multiclass Classification

In multiclass classification, there are more than two classes.

Example:

```text
Cat
Dog
Bird
```

The confusion matrix becomes a 3 × 3 matrix.

Example:

```text
                  Predicted
              Cat    Dog    Bird

Actual Cat     40     5      5

Actual Dog      3    32      5

Actual Bird     2     3     55
```

Total samples:

```text
50 Cats
40 Dogs
60 Birds

Total = 150
```

The diagonal contains correct predictions:

```text
40 + 32 + 55 = 127
```

Overall accuracy:

```text
Accuracy = 127 / 150
         = 84.7%
```

---

# 12. Per-Class Evaluation

For multiclass classification, each class can be treated as a binary classification problem.

For example, when evaluating Cat:

```text
Cat = Positive
Dog + Bird = Negative
```

Then calculate:

* TP
* FP
* FN
* Precision
* Recall
* F1 Score

The same process is repeated for Dog and Bird.

---

# 13. Macro Averaging

Macro averaging calculates the metric independently for each class and then takes the simple average.

Formula:

```text
Macro Metric = Sum of per-class metrics / Number of classes
```

For example:

```text
Macro Precision
= (88.9 + 80 + 84.6) / 3
= 84.5%
```

Macro averaging treats every class equally regardless of its size.

It is useful when all classes are considered equally important.

---

# 14. Weighted Averaging

Weighted averaging gives more importance to classes with more samples.

The metric for each class is multiplied by the number of actual samples in that class.

For example:

```text
Weighted Precision
= (88.9 × 50 + 80 × 40 + 84.6 × 60) / 150
= 84.8%
```

Weighted averaging is useful when class sizes represent the real-world distribution.

---

# 15. Macro vs Weighted Averaging

## Macro Averaging

```text
Every class has equal importance.
```

## Weighted Averaging

```text
Larger classes have more influence.
```

When class sizes are equal, macro and weighted averages can be similar.

When class sizes are different, they can give different results.

---

# 16. How to Choose the Evaluation Metric

The evaluation metric depends on the problem.

## Case 1: Missing a Positive Is Very Costly

Prioritize:

```text
Recall
```

Examples:

* Disease detection
* Fraud detection
* Criminal identification

The goal is to minimize False Negatives.

---

## Case 2: False Alarms Are Very Costly

Prioritize:

```text
Precision
```

Examples:

* Spam filtering
* Loan approval
* Content moderation

The goal is to minimize False Positives.

---

## Case 3: Both Errors Matter

Use:

```text
F1 Score
```

F1 provides a balance between Precision and Recall.

---

## Case 4: Classes Are Imbalanced

Do not rely only on:

```text
Accuracy
```

Also examine:

* Precision
* Recall
* F1 Score
* Confusion Matrix
* Per-class performance

---

# 17. Always Examine the Confusion Matrix

A single metric can hide important information.

The confusion matrix helps identify:

* False Positives
* False Negatives
* Correct Positive predictions
* Correct Negative predictions
* Which classes are being confused

Therefore, the confusion matrix is the foundation of classification evaluation.

---

# 18. Classification Threshold

A classifier often produces a probability rather than directly producing a class label.

Example:

```text
Disease probability = 0.73
```

A threshold is then used to convert the probability into a class.

For example, with threshold 0.5:

```text
0.73 >= 0.5
```

Therefore:

```text
Predicted Class = Positive
```

---

# 19. Low Threshold

Example:

```text
Threshold = 0.3
```

More samples are classified as Positive.

Usually:

```text
Recall increases
Precision decreases
```

This can be useful when missing a positive case is very costly.

Example:

```text
Disease detection
```

---

# 20. High Threshold

Example:

```text
Threshold = 0.8
```

The model only predicts Positive when it is more confident.

Usually:

```text
Precision increases
Recall decreases
```

This can be useful when False Positives are costly.

---

# 21. Precision-Recall Trade-off

Changing the classification threshold changes Precision and Recall.

Example:

```text
Threshold    Precision    Recall      F1

0.3             55%        95%        70%

0.5             61.5%      80%        69.6%

0.7             85%        60%        70.6%

0.9             95%        30%        45.7%
```

General relationship:

```text
Lower Threshold
→ Recall increases
→ Precision decreases
```

```text
Higher Threshold
→ Precision increases
→ Recall decreases
```

The best threshold depends on the problem.

A threshold of 0.5 is a default choice, not a universal rule.

---
