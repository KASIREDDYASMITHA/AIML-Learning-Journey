# Day 2 - Machine Learning Development Life Cycle

## Topic

Building the foundation of a Logistic Regression classification problem using the Machine Learning Development Life Cycle (MLDLC).

## Problem Statement

Can a machine predict whether a person will be late based on:

- Distance from home to destination
- Time left before being marked late

This is a **Binary Classification** problem because the output has two possible classes:

- `0` → On Time
- `1` → Late

## Machine Learning Development Life Cycle

The ML Development Life Cycle is a repeatable process used for developing machine learning projects.

The stages introduced in today's class are:

1. Problem Definition
2. Data Collection
3. Exploratory Data Analysis (EDA)
4. Data Preprocessing
5. Model Training
6. Model Evaluation
7. Save and Deploy
8. Prediction on New Data

Today's learning was covered up to:

**Data Preprocessing → Feature Scaling**

## Dataset

Dataset file:

`late_to_office_dataset.csv`

The dataset contains:

- `distance_km` → Distance from home to destination
- `time_left_minutes` → Minutes remaining before being marked late
- `will_be_late` → Target variable

Target values:

- `0` → On Time
- `1` → Late