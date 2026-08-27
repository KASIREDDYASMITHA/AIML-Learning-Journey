# Classification Evaluation — Complete Notes

## 1. Classification Evaluation

Classification evaluation is the process of measuring how well a classification model performs.

The goal is not simply to count how many predictions are correct.

We need to understand:

* What type of mistakes the model makes
* How often those mistakes happen
* Whether false positives or false negatives are more costly
* Whether the dataset is balanced or imbalanced
* Which evaluation metric is appropriate for the problem

A single metric such as accuracy may hide important problems in a classification model.

---

# 2. Accuracy Can Be Misleading

Accuracy measures the proportion of total predictions that are correct.

A model can have very high accuracy while performing badly on the class that actually matters.

For example, when one class is much larger than another, a model can simply predict the majority class for every sample and still obtain high accuracy.

Therefore:

> Accuracy alone should not be trusted when classes are imbalanced.

The final class evaluation framework emphasizes that a model predicting the majority class can obtain high accuracy without actually solving the important classification problem.

---

# 3. Four Classification Outcomes

Every binary classification prediction falls into one of four categories.

## True Positive — TP

The model predicts Positive and the actual class is Positive.

Example:

A patient actually has a disease and the model correctly predicts that the patient has the disease.

---

## True Negative — TN

The model predicts Negative and the actual class is Negative.

Example:

A patient does not have a disease and the model correctly predicts that the patient is healthy.

---

## False Positive — FP

The model predicts Positive but the actual class is Negative.

This is a false alarm.

It is also called a Type I Error.

Example:

A healthy patient is incorrectly classified as having a disease.

---

## False Negative — FN

The model predicts Negative but the actual class is Positive.

This means the model missed a real positive case.

It is also called a Type II Error.

Example:

A patient has a disease but the model incorrectly predicts that the patient is healthy.

---

# 4. Confusion Matrix

A confusion matrix organizes the four possible classification outcomes:

| Actual / Predicted | Positive | Negative |
| ------------------ | -------: | -------: |
| Positive           |       TP |       FN |
| Negative           |       FP |       TN |

The confusion matrix is the foundation of classification evaluation.

The main metrics are calculated from:

* TP
* FP
* FN
* TN

A single accuracy value cannot show which types of errors are being made.

Therefore, the full confusion matrix should always be examined.

---

# 5. Accuracy

Accuracy measures how many predictions were correct out of all predictions.

Formula:

```text
Accuracy = (TP + TN) / (TP + FP + FN + TN)
```

Accuracy is useful when:

* Classes are reasonably balanced
* False positives and false negatives have similar importance

Accuracy becomes dangerous when the dataset is highly imbalanced.

Example:

Suppose 90% of samples are Negative and only 10% are Positive.

A model that predicts Negative for every sample can achieve approximately 90% accuracy while completely failing to identify the Positive class.

---

# 6. Precision

Precision answers:

> Of all the samples predicted as Positive, how many were actually Positive?

Formula:

```text
Precision = TP / (TP + FP)
```

Precision focuses on false positives.

A high Precision means that when the model predicts Positive, it is usually correct.

Precision is particularly important when false alarms are costly.

Examples:

1. Spam filtering
2. Content moderation

If a legitimate email is incorrectly classified as spam, that is a costly false positive.

---

# 7. Recall

Recall answers:

> Of all the samples that were actually Positive, how many did the model correctly identify?

Formula:

```text
Recall = TP / (TP + FN)
```

Recall focuses on false negatives.

A high Recall means the model catches most of the actual Positive cases.

Recall is especially important when missing a Positive case is dangerous.

Examples:

1. Disease detection
2. Fraud investigation

In these situations, missing an actual Positive case can have serious consequences.

---

# 8. Precision vs Recall

Precision and Recall measure different things.

## Precision

Focuses on avoiding false positives.

```text
Precision = TP / (TP + FP)
```

Question:

> When the model says Positive, how often is it correct?

---

## Recall

Focuses on avoiding false negatives.

```text
Recall = TP / (TP + FN)
```

Question:

> Of all actual Positive cases, how many did the model find?

---

Neither metric is automatically better.

The correct metric depends on the real-world cost of errors.

---

# 9. Why Precision Alone Is Not Enough

A model can achieve very high Precision by being extremely conservative.

For example, suppose the model predicts Positive only once and that prediction is correct.

Then:

```text
Precision = 100%
```

But the model may have missed almost all actual Positive cases.

Therefore, the model can have:

```text
Precision = 100%
Recall = 10%
```

This is not a good classification model.

Precision alone does not measure completeness.

---

# 10. Why Recall Alone Is Not Enough

A model can achieve perfect Recall by predicting every sample as Positive.

Then:

```text
Recall = 100%
```

because every actual Positive case is detected.

However, if most Negative samples are also incorrectly classified as Positive, Precision becomes very low.

Therefore:

```text
Recall = 100%
Precision = 10%
```

can still represent a practically useless model.

Recall alone encourages predicting too many Positive cases.

---

# 11. F1 Score

F1 Score combines Precision and Recall into a single metric.

It uses the harmonic mean of Precision and Recall.

Formula:

```text
F1 = 2 × (Precision × Recall) / (Precision + Recall)
```

The harmonic mean is useful because it is strongly affected by the smaller value.

If either Precision or Recall is very low, the F1 Score will also be low.

Therefore, a model needs both reasonably good Precision and Recall to achieve a high F1 Score.

---

# 12. Why Harmonic Mean?

The arithmetic mean can hide extreme differences.

Example:

```text
Precision = 0%
Recall = 100%

Arithmetic Mean = 50%
```

A score of 50% may sound acceptable, but the model has completely failed one of the two objectives.

F1 avoids this problem because it uses the harmonic mean.

The same principle applies when Precision is very high but Recall is very low.

F1 penalizes extreme imbalance between Precision and Recall.

---

# 13. Multiclass Classification

Classification problems do not always have only two classes.

For example:

```text
Cat
Dog
Bird
```

A multiclass confusion matrix can be represented as:

| Actual / Predicted | Cat | Dog | Bird |
| ------------------ | --: | --: | ---: |
| Cat                |  40 |   5 |    5 |
| Dog                |   3 |  32 |    5 |
| Bird               |   2 |   3 |   55 |

The diagonal values represent correct predictions.

```text
Cat → Cat = 40
Dog → Dog = 32
Bird → Bird = 55
```

The off-diagonal values represent classification errors.

Overall accuracy:

```text
Accuracy = (40 + 32 + 55) / 150

Accuracy = 127 / 150

Accuracy = 84.7%
```

---

# 14. Per-Class Evaluation

For multiclass classification, each class can be treated as a binary classification problem.

For one class:

* That class becomes Positive
* All other classes become Negative

Then calculate:

* TP
* FP
* FN
* Precision
* Recall
* F1 Score

Example:

## Cat

```text
TP = 40
FP = 5
FN = 10

Precision = 40 / 45 = 88.9%

Recall = 40 / 50 = 80%

F1 = 84.2%
```

## Dog

```text
TP = 32
FP = 8
FN = 8

Precision = 80%

Recall = 80%

F1 = 80%
```

## Bird

```text
TP = 55
FP = 10
FN = 5

Precision = 84.6%

Recall = 91.7%

F1 = 88%
```

---

# 15. Macro Averaging

Macro averaging calculates the metric separately for every class and then takes a simple average.

Every class receives equal importance regardless of its size.

For example:

```text
Macro Precision
= (88.9 + 80 + 84.6) / 3
= 84.5%
```

```text
Macro Recall
= (80 + 80 + 91.7) / 3
= 83.9%
```

```text
Macro F1
= (84.2 + 80 + 88) / 3
= 84.1%
```

Macro averaging is useful when all classes are considered equally important.

---

# 16. Weighted Averaging

Weighted averaging considers the number of actual samples in each class.

Larger classes receive greater weight.

For the example:

```text
Cat = 50 samples
Dog = 40 samples
Bird = 60 samples
Total = 150 samples
```

Weighted Precision:

```text
(88.9 × 50 + 80 × 40 + 84.6 × 60) / 150
= 84.8%
```

Weighted Recall:

```text
(80 × 50 + 80 × 40 + 91.7 × 60) / 150
= 84.7%
```

Weighted F1:

```text
(84.2 × 50 + 80 × 40 + 88 × 60) / 150
= 84.6%
```

Weighted averaging is useful when the class distribution reflects the real-world distribution.

---

# 17. Macro vs Weighted Averaging

## Macro

* Treats every class equally
* Does not care about class size
* Useful when every class is equally important

## Weighted

* Gives more importance to larger classes
* Uses the number of actual samples as weights
* Useful when class sizes represent the real-world distribution

When classes have different sizes, Macro and Weighted metrics can tell different stories.

Therefore, both should be considered when appropriate.

---

# 18. How to Choose the Correct Metric

The first step is to understand the problem domain.

Ask:

```text
What does a False Positive cost?
What does a False Negative cost?
```

The answer determines which metric should receive priority.

---

# 19. When Recall Should Be Prioritized

If missing a Positive case is catastrophic, prioritize Recall.

Examples:

1. Cancer detection
2. Fraud detection

The model should try to catch as many real Positive cases as possible, even if this creates additional false alarms.

---

# 20. When Precision Should Be Prioritized

If false alarms are costly, prioritize Precision.

Examples:

1. Spam filtering
2. Content moderation

The model should avoid incorrectly flagging legitimate or acceptable cases as Positive.

---

# 21. When F1 Score Should Be Used

When both false positives and false negatives matter, F1 Score can provide a useful balance between Precision and Recall.

Example:

Credit card fraud detection.

Both types of mistakes matter:

* Missing fraud can cause financial loss.
* Blocking a legitimate transaction can inconvenience the customer.

Therefore, F1 can be useful for comparing models.

---

# 22. Never Depend Only on Accuracy for Imbalanced Data

When one class dominates the dataset, accuracy can become misleading.

A model may achieve high accuracy simply by predicting the majority class.

Therefore, for imbalanced classification problems, examine:

* Precision
* Recall
* F1 Score
* Per-class performance
* Confusion Matrix

Do not judge the model using accuracy alone.

---

# 23. Always Examine the Confusion Matrix

A single metric cannot show exactly how a model is failing.

The confusion matrix shows:

```text
TP → Correct Positive predictions
TN → Correct Negative predictions
FP → False alarms
FN → Missed Positive cases
```

The confusion matrix therefore provides the foundation for understanding classification performance.

---

# 24. Scenario 1 — Cancer Screening

Suppose there are:

```text
1,000 patients
100 have cancer
```

The model decides who should receive a biopsy.

## Model A

```text
TP = 85
FN = 15
FP = 20
TN = 880

Recall = 85%
Precision = 81%
Accuracy = 96.5%
```

## Model B

```text
TP = 95
FN = 5
FP = 80
TN = 820

Recall = 95%
Precision = 54%
Accuracy = 91.5%
```

Model B should be deployed.

Reason:

A False Negative means a cancer case may be missed.

A False Positive means an unnecessary biopsy.

In this scenario, missing cancer is much more serious than performing an additional biopsy.

Therefore:

```text
Cancer Screening → Prioritize Recall
```

---

# 25. Scenario 2 — Spam Filter

Suppose there are:

```text
1,000 emails
200 spam
800 legitimate
```

## Model A

```text
TP = 180
FN = 20
FP = 10
TN = 790

Precision = 94.7%
Recall = 90%
Accuracy = 97%
```

## Model B

```text
TP = 195
FN = 5
FP = 50
TN = 750

Precision = 79.6%
Recall = 97.5%
Accuracy = 94.5%
```

Model A should be deployed.

Reason:

A False Positive means a legitimate email may be incorrectly placed in the spam folder.

A False Negative means a spam email reaches the inbox.

In this scenario, losing an important legitimate email is more harmful than receiving occasional spam.

Therefore:

```text
Spam Filtering → Prioritize Precision
```

---

# 26. Scenario 3 — Credit Card Fraud

Suppose there are:

```text
10,000 transactions
100 fraudulent
9,900 legitimate
```

## Model A

```text
TP = 40
FN = 60
FP = 10
TN = 9890

Recall = 40%
Precision = 80%
F1 = 53.3%
Accuracy = 99.3%
```

## Model B

```text
TP = 70
FN = 30
FP = 50
TN = 9850

Recall = 70%
Precision = 58.3%
F1 = 63.6%
Accuracy = 99.2%
```

Model B should be deployed.

Both errors matter:

* Missing fraud can cause financial loss.
* Blocking a legitimate transaction is inconvenient but reversible.

F1 provides a useful balance.

Model B has:

```text
F1 = 63.6%
```

while Model A has:

```text
F1 = 53.3%
```

Although their accuracy values are almost identical, F1 reveals that Model B performs better for this problem.

Therefore:

```text
Fraud Detection → F1 can be prioritized when both error types matter
```

---

# 27. Classification Threshold

A classifier often produces a probability rather than directly producing a final class label.

Example:

```text
Model output = 0.73
```

This means the model assigns a probability of 73% to the Positive class.

A threshold is then used to convert this probability into a class label.

For example:

```text
Threshold = 0.5
Probability = 0.73
```

Since:

```text
0.73 > 0.5
```

the prediction becomes:

```text
Positive
```

---

# 28. Why Is 0.5 Used?

A threshold of 0.5 is commonly used as a default.

However, 0.5 is not automatically the correct threshold for every problem.

The appropriate threshold depends on the consequences of false positives and false negatives.

Changing the threshold changes model behavior.

---

# 29. Low Threshold

Example:

```text
Threshold = 0.3
```

Anyone with a predicted probability above 30% is classified as Positive.

This generally results in:

```text
Recall ↑
Precision ↓
```

More Positive cases are detected, but more false alarms can occur.

A lower threshold can be appropriate when missing a Positive case is very costly.

Examples:

1. Disease detection
2. Fraud detection

---

# 30. High Threshold

Example:

```text
Threshold = 0.8
```

The model predicts Positive only when it is highly confident.

This generally results in:

```text
Precision ↑
Recall ↓
```

There are fewer false alarms, but more actual Positive cases may be missed.

A higher threshold can be appropriate when false positives are costly.

Examples:

1. Spam filtering
2. Loan approval

---

# 31. Precision-Recall Trade-Off

The classification threshold directly affects Precision and Recall.

As the threshold increases:

```text
Precision increases
Recall decreases
```

As the threshold decreases:

```text
Recall increases
Precision decreases
```

Therefore, threshold selection is an important model evaluation decision.

---
