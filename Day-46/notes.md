# Day 46 — Perceptron to Multi-Layer Perceptron (MLP)

## 1. Introduction

Today I learned how to implement a Perceptron from scratch using Python and how a Multi-Layer Perceptron (MLP) solves problems that a single perceptron cannot solve.

Topics covered:
- Perceptron forward pass
- Step activation function
- Loss calculation
- Weight and bias updates
- Training loop and epochs
- OR logic gate
- XOR logic gate
- Linear separability
- Multi-Layer Perceptron using Scikit-learn
- Hidden layers and decision boundaries

## 2. Dataset

We use four combinations of two binary inputs.

| x1 | x2 | OR | XOR |
|---:|---:|---:|---:|
| 0 | 0 | 0 | 0 |
| 1 | 0 | 1 | 1 |
| 0 | 1 | 1 | 1 |
| 1 | 1 | 1 | 0 |

OR returns 1 when at least one input is 1.

Example 1: OR(1, 0) = 1

Example 2: OR(1, 1) = 1

XOR returns 1 when the two inputs are different.

Example 1: XOR(1, 0) = 1

Example 2: XOR(1, 1) = 0

## 3. Perceptron

A perceptron is a simple artificial neuron that makes a binary classification using a weighted sum and a threshold.

### Forward Pass

First, calculate the weighted sum:

z = X · w + b

Where:
- X = input features
- w = weights
- b = bias
- z = weighted sum

Then apply the step activation function:

ŷ = step(z)

The step function used in this lesson is:

- Return 1 if z > 0.
- Return 0 otherwise.

Python:

```python
def step(z):
    return (z > 0).astype(int)
```

## 4. Loss Calculation

Loss tells us whether the prediction is correct.

Loss = y - ŷ

Where:
- y = actual label
- ŷ = predicted label

Interpretation:

- Loss = 0: prediction is correct.
- Loss = +1: the model predicted 0 when the actual label was 1.
- Loss = -1: the model predicted 1 when the actual label was 0.

Examples:

1. Actual = 1, Predicted = 0 → Loss = 1.
2. Actual = 0, Predicted = 1 → Loss = -1.

## 5. Weight and Bias Update

When a prediction is incorrect, the perceptron updates its weights and bias.

Weight update:

w_new = w_old + (loss × X)

Bias update:

b_new = b_old + loss

The weights determine the contribution of the input features. The bias shifts the decision boundary.

Example 1: If loss = 1 and X = [1, 0], the first weight increases by 1 and the second weight remains unchanged.

Example 2: If loss = -1, the bias decreases by 1.

## 6. Training Loop and Epoch

An epoch is one complete pass through all the training examples.

During training:
1. Predict the output for each input.
2. Calculate the loss.
3. Update the weights and bias.
4. Calculate the total absolute error.
5. Repeat for multiple epochs.

Training stops when total_loss = 0, meaning all training examples are classified correctly.

Note: A perceptron is guaranteed to converge in a finite number of updates when the training data is linearly separable and the standard perceptron learning rule is used. It is not guaranteed to converge on non-linearly separable data.

## 7. OR Gate — Perceptron Training

The OR gate is linearly separable. A single straight decision boundary can separate its output classes.

The perceptron can learn the OR gate by adjusting its weights and bias.

Expected result: predictions match the OR labels [0, 1, 1, 1].

Example 1: Input [0, 0] → Output 0.

Example 2: Input [0, 1] → Output 1.

## 8. XOR Gate — Why the Perceptron Fails

XOR is not linearly separable.

Its output is 1 for (1, 0) and (0, 1), but 0 for (0, 0) and (1, 1).

A single straight line cannot separate these two classes correctly.

Example 1: XOR(1, 0) = 1.

Example 2: XOR(1, 1) = 0.

The perceptron cannot solve XOR using a single linear decision boundary. Increasing the number of epochs does not remove this architectural limitation.

## 9. Multi-Layer Perceptron (MLP)

An MLP is a neural network containing an input layer, one or more hidden layers, and an output layer.

A hidden layer transforms the input representation so that a more complex classification problem can become solvable.

For the XOR example, the faculty notes use an MLP with:
- One hidden layer
- Two hidden neurons
- ReLU activation
- L-BFGS solver
- random_state = 42

The model is implemented using Scikit-learn's MLPClassifier.

## 10. Perceptron vs. MLP

| Feature | Perceptron | MLP |
|---|---|---|
| Architecture | Single neuron | Multiple connected neurons |
| Decision boundary | Linear | Can represent nonlinear boundaries |
| OR gate | Can learn | Can learn |
| XOR gate | Cannot learn with a single linear boundary | Can learn with a suitable hidden layer |
| Training | Perceptron update rule | Optimisation and backpropagation |

