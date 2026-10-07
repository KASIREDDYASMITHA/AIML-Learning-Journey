

# Topic: Logging, Virtual Environment, DVC, MLflow and ML Model Deployment

---

## 1. Logging

Logging is the process of recording information about what is happening inside a program while it is running.

Logging is useful in machine learning projects because we need to know:

- When the program started
- When data was loaded
- When preprocessing was completed
- When model training started
- When model training completed
- Whether an error occurred
- Whether a warning occurred
- When an API request was received
- When a prediction was generated

Instead of depending only on `print()` statements, we can use Python's built-in `logging` module.

---

## 2. Why Do We Need Logging?

When we use `print()` statements, the information is normally displayed only in the console.

If the console output disappears, we may lose the information.

With logging, we can save messages into a file.

Example:

```text
Application Started
Data Loaded
Preprocessing Completed
Model Training Started
Model Training Completed
Model Evaluation Completed