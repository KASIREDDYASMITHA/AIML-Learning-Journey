# Day 55 - Loss Functions

## 1. Introduction to Loss Functions

A Loss Function is a mathematical function used to measure how far a model's predicted output is from the actual output.

It tells the neural network how wrong its prediction is.

The loss function acts like the eyes of a neural network because it helps the network measure its performance.

### Example

Suppose a model predicts a house price.

Actual Price = 100000
Predicted Price = 95000

The loss function measures the difference between these two values.

A smaller loss indicates that the prediction is closer to the actual value.

A larger loss indicates that the prediction is farther from the actual value.

## 2. Importance of Loss Functions

1. Measure the prediction error.
2. Evaluate model performance.
3. Help the network understand how wrong its predictions are.
4. Provide a training signal for backpropagation.
5. Help improve the model by adjusting weights.

The loss value is used during backpropagation to calculate how weights should change.

## 3. Basic Loss Function Formula

Loss = L(y, y_pred)

Where:

- y = Actual value or true label
- y_pred = Predicted value
- L = Loss function

The loss function returns a single numerical value.

### Interpretation

- Small loss = Prediction is close to the actual value.
- Large loss = Prediction is far from the actual value.

For a batch of N examples:

Average Loss = (Sum of individual losses) / N

## 4. Types of Model Outputs

There are three major types of outputs.

### A. Regression

Regression predicts a continuous numerical value.

Examples:
- House price prediction.
- Temperature prediction.
- Salary prediction.

Output: A raw numerical value.

### B. Binary Classification

Binary classification predicts one of two classes.

Examples:
- Spam or Not Spam.
- Churn or Not Churn.
- Yes or No.

Output: A single probability between 0 and 1.

### C. Multi-Class Classification

Multi-class classification predicts one class from multiple classes.

Examples:
- Digit classification (0 to 9).
- Cat, Dog or Bird classification.
- Different product categories.

Output: A vector of probabilities.

## 5. Types of Loss Functions

Loss functions are divided into two main categories.

### Regression Losses

1. Mean Squared Error (MSE)
2. Mean Absolute Error (MAE)
3. Huber Loss

### Classification Losses

4. Binary Cross-Entropy (BCE)
5. Categorical Cross-Entropy (CCE)

# PART 1: REGRESSION LOSS FUNCTIONS

## 6. Mean Squared Error (MSE)

MSE stands for Mean Squared Error.

It calculates the average of the squared differences between actual and predicted values.

### Formula

MSE = (1/n) * Sum((y - y_pred)^2)

Where:

- y = Actual value
- y_pred = Predicted value
- n = Number of observations

### Example

Actual value = 1.0

Case A:
Predicted value = 0.77

Error = 1.0 - 0.77 = 0.23

MSE = (0.23)^2 = 0.0529

Case B:
Predicted value = 2.45

Error = 1.0 - 2.45 = -1.45

MSE = (-1.45)^2 = 2.1025

### Advantages

- Smooth and differentiable.
- Heavily penalizes large errors.
- Useful when large prediction errors are especially costly.

### Disadvantages

- Highly sensitive to outliers.
- Squaring increases the effect of large errors.

### Applications

- House price prediction.
- Regression problems where large errors should be penalized heavily.

## 7. Mean Absolute Error (MAE)

MAE stands for Mean Absolute Error.

It calculates the average of the absolute differences between actual and predicted values.

### Formula

MAE = (1/n) * Sum(|y - y_pred|)

### Example

Actual value = 1.0

Case A:
Predicted value = 0.77

MAE = |1.0 - 0.77|

MAE = 0.23

Case B:
Predicted value = 2.45

MAE = |1.0 - 2.45|

MAE = 1.45

### Advantages

- Treats every unit of error equally.
- Less sensitive to outliers than MSE.
- Easy to understand and interpret.

### Disadvantages

- Less smooth than MSE.
- Gradient is undefined at exactly zero error.

### Applications

Regression problems where outliers should not dominate the training process.

## 8. Huber Loss

Huber Loss combines the advantages of MSE and MAE.

It behaves like MSE for small errors and MAE for large errors.

It uses a threshold called delta (δ).

### Formula

Let a = y - y_pred.

If |a| <= δ:

Huber Loss = 0.5 * a^2

If |a| > δ:

Huber Loss = δ * (|a| - 0.5 * δ)

### Example

Delta (δ) = 0.5

Case A:

Error = 0.23

Since 0.23 <= 0.5:

Huber Loss = 0.5 * (0.23)^2

Huber Loss = 0.02645

Case B:

Error = 1.45

Since 1.45 > 0.5:

Huber Loss = 0.5 * (1.45 - 0.25)

Huber Loss = 0.60

### Advantages

- Smooth for small errors.
- Less sensitive to outliers.
- Combines the benefits of MSE and MAE.

### Disadvantages

- Requires selecting a threshold called delta.
- Choosing an unsuitable delta can affect the balance.

### Applications

Regression problems with occasional outliers where smooth optimization is preferred.

# PART 2: CLASSIFICATION LOSS FUNCTIONS

## 9. Binary Cross-Entropy (BCE)

Binary Cross-Entropy is used for binary classification problems.

It measures the difference between the actual binary label and the predicted probability.

The predicted probability is generally between 0 and 1.

### Formula

BCE = -[y * log(y_pred) + (1-y) * log(1-y_pred)]

Where:

- y = Actual label (0 or 1)
- y_pred = Predicted probability

### Example

Actual label = 1

Customer A:

Predicted probability = 0.90

BCE = -log(0.90)

BCE = 0.1053 approximately

Customer B:

Predicted probability = 0.14

BCE = -log(0.14)

BCE = 1.9661 approximately

Customer A has a smaller loss because the prediction is closer to the actual label.

Customer B has a larger loss because the model predicted a low probability even though the actual label is 1.

### Advantages

- Suitable for probability-based binary classification.
- Penalizes confident incorrect predictions heavily.
- Provides a useful learning signal.

### Disadvantages

- Extremely confident incorrect predictions can produce very large loss values.
- Requires careful numerical handling near probabilities 0 and 1.

### Applications

- Spam detection.
- Email classification.
- Customer churn prediction.
- Fraud detection.

## 10. Categorical Cross-Entropy (CCE)

Categorical Cross-Entropy is used for multi-class classification problems.

It measures the difference between the actual class and the predicted probability distribution.

### Formula

CCE = -Sum(y_c * log(y_pred_c))

Where:

- y_c = Actual value for class c.
- y_pred_c = Predicted probability for class c.
- C = Total number of classes.

For one-hot encoded labels, the formula simplifies to:

CCE = -log(Probability of the true class)

### Example

Suppose there are three classes:

Class 1
Class 2
Class 3

Actual class = Class 3

Image A:

Predicted probabilities = [0.15, 0.07, 0.79]

Loss = -log(0.79)

Loss = 0.2367 approximately

Image B:

Predicted probabilities = [0.33, 0.33, 0.33]

Loss = -log(0.33)

Loss = 1.1087 approximately

Image A has a smaller loss because it assigns a high probability to the correct class.

Image B has a larger loss because the network is uncertain about the correct class.

### Advantages

- Rewards high probability assigned to the correct class.
- Works with multiple classes.
- Can be used for problems with many output classes.

### Disadvantages

- Confident incorrect predictions can produce high loss.
- Poor network activations, such as dead neurons, can affect predictions.

### Applications

- Handwritten digit recognition.
- Image classification.
- Animal classification.
- Multi-class text classification.

## 11. Comparison of Five Loss Functions

| Loss Function | Used For | Main Characteristic |
|---|---|---|
| MSE | Regression | Penalizes large errors heavily |
| MAE | Regression | Treats errors proportionally |
| Huber | Regression | Combines MSE and MAE |
| BCE | Binary Classification | Penalizes confident wrong predictions |
| CCE | Multi-Class Classification | Measures probability assigned to the correct class |

## 12. Difference Between MSE, MAE and Huber

MSE:
- Squares the prediction error.
- Large errors receive much higher penalties.
- Sensitive to outliers.

MAE:
- Uses absolute error.
- Errors increase proportionally.
- More robust to outliers.

Huber:
- Uses squared error for small errors.
- Uses linear error for large errors.
- Balances smoothness and outlier resistance.

## 13. Difference Between BCE and CCE

Binary Cross-Entropy:
- Used for binary classification.
- Usually has one sigmoid probability output.
- Example: Spam or Not Spam.

Categorical Cross-Entropy:
- Used for multi-class classification.
- Usually has multiple softmax probability outputs.
- Example: Classifying digits from 0 to 9.

## 14. Relationship Between Loss Functions and Backpropagation

The loss function measures how wrong the network's prediction is.

Backpropagation uses the loss to calculate gradients.

These gradients help update the network weights.

The objective is to reduce the loss during training.

Note: Backpropagation is a separate topic that will be covered in a future class.
