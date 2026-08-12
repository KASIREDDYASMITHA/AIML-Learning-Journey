# Regression vs Classification

## Basic Idea

Regression and classification are both types of supervised learning.

They have a similar overall learning process, but their purposes are different.

The main difference is the type of output they produce.

---

# Regression

Regression predicts a number.

The output is continuous.

It answers:

> How much?

or

> How many?

### Examples

1. Predicting house price
2. Predicting student marks

---

# Classification

Classification predicts a category.

The output is discrete.

It answers:

> Which class?

or

> Yes or No?

### Examples

1. Spam or Not Spam
2. Disease Positive or Negative

---

# Regression Example

Suppose we have:

Hours Studied -> Student Marks

2 hours -> 40
4 hours -> 55
6 hours -> 70
8 hours -> 85

If a new student studies for 7 hours, regression can predict a numerical score.

Possible prediction:

78 marks

The output is a number.

Therefore:

7 hours -> 78 marks

This is regression.

---

# Classification Example

Suppose we have emails.

The model learns from:

Email Features -> Spam / Not Spam

For a new email, the model predicts:

Spam

or

Not Spam

The output is a category.

Therefore, this is classification.

---

# Regression vs Classification Table

| Concept | Regression | Classification |
|---|---|---|
| Main purpose | Predict a number | Predict a category |
| Output | Continuous | Discrete |
| Question | How much? | Which class? |
| Example | House price | Spam detection |
| Example | Student score | Disease diagnosis |
| Model behavior | Predict numerical value | Separate classes |
| Main metrics | MAE, RMSE | Accuracy, Log Loss, F1 Score |

---

# How the Model "Draws a Line"

Both regression and classification can be visualized using a line or boundary.

But the purpose of the line is different.

## Regression

The line goes through the data.

The model uses the line to make numerical predictions.

The question is:

> How much?

Example:

Hours studied -> Predicted marks

---

## Classification

The boundary separates different groups.

The model determines which side of the boundary a data point belongs to.

The question is:

> Which class?

Example:

Email -> Spam or Not Spam

---

# Important Comparison

| Concept | Regression | Classification |
|---|---|---|
| Line / boundary | Through the data | Between the data |
| Purpose | Make numerical predictions | Separate groups |
| Output | Number | Class |
| Question | How much? | Which class? |

---

# Why We Should Not Randomly Use One for the Other

Mathematically, some algorithms can sometimes be adapted for different tasks.

However, the algorithm should match the type of problem.

Using regression for classification can produce numerical predictions that do not naturally represent class probabilities.

Using classification for regression loses the magnitude information of the target.

For example:

If the real target is house price, predicting only:

High

or

Low

throws away the actual price information.

If the target is:

₹50 lakh

predicting only a class does not tell us how much the house actually costs.

---

# Output, Algorithm and Metric Must Align

The output type, algorithm, and evaluation metric should be aligned with the problem.

The basic decision process is:

Problem

-> Determine Output Type

-> Choose Regression or Classification

-> Choose Suitable Algorithm

-> Choose Suitable Evaluation Metric

---

# The One Question to Remember

> Is my output a number or a category?

Number -> Regression

Category -> Classification

This is one of the most important fundamentals in supervised learning.