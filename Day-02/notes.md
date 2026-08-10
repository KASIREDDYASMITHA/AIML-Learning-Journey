# Day 2 - Machine Learning Notes

## 1. Machine Learning Development Life Cycle (MLDLC)

Machine Learning projects follow a repeatable cycle called the Machine Learning Development Life Cycle (MLDLC).

The main stages are:

1. Problem Definition
2. Data Collection
3. Exploratory Data Analysis (EDA)
4. Data Processing
5. Model Training
6. Model Evaluation
7. Save and Deploy
8. Predict New Data

Today's class was covered up to Data Preprocessing and Feature Scaling.

---

## 2. Problem Definition

Problem:

Predict whether a person will arrive late based on:

- Distance from home to destination
- Time left before being marked late

This is a Binary Classification problem because the output has two possible classes.

### Features

### distance_km

Distance from home to destination.

### time_left_minutes

Minutes before being marked late.

### Target

### will_be_late

```text
0 = On Time
1 = Late