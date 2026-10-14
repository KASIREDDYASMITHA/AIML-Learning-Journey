# AIML Day 45 — The Perceptron

## 1. Introduction

A perceptron is the simplest type of artificial neuron used for
binary classification.

It takes input values, multiplies them by their corresponding weights,
adds the results and a bias, and applies an activation function to
produce a binary prediction.

The output is either 0 or 1.

Examples:
- Predicting whether an email is spam or not spam.
- Predicting whether a simple binary condition is true or false.

## 2. Biological Neuron and Artificial Neuron

A biological neuron contains dendrites, a cell body and an axon.

These concepts can be related to an artificial neuron:

- Dendrites -> Inputs
- Synaptic strength -> Weights
- Firing threshold -> Activation function
- Cell body computation -> Weighted sum and bias
- Neuron response -> Output

The perceptron is a mathematical model inspired by the basic idea
of a biological neuron.

## 3. Inputs, Weights and Bias

### Inputs

Inputs are the values provided to a perceptron.

Example:
x1 = 1
x2 = 0

### Weights

Weights represent the contribution of each input to the final
calculation.

Example:
w1 = 0.5
w2 = 0.8

### Bias

Bias is an additional value added to the weighted sum. It shifts
the decision boundary.

Example:
b = -0.3

## 4. Perceptron Calculation

The weighted sum is calculated using:

z = w1*x1 + w2*x2 + b

Here:
- x1, x2 = Input values
- w1, w2 = Weights
- b = Bias
- z = Weighted sum or pre-activation value

The predicted output is:

y_pred = step(z)

The step activation function converts the weighted sum into a
binary output.

## 5. Worked Example

Given:

x1 = 1
x2 = 0
w1 = 0.5
w2 = 0.8
b = -0.3

Step 1: Multiply each input by its weight.

x1*w1 = 1*0.5 = 0.5
x2*w2 = 0*0.8 = 0.0

Step 2: Add the weighted inputs.

0.5 + 0.0 = 0.5

Step 3: Add the bias.

z = 0.5 + (-0.3)
z = 0.2

Step 4: Apply the step function.

Since z > 0, the output is 1.

Therefore:

y_pred = 1

## 6. Step Activation Function

The step function produces a binary output.

step(z) = 1, if z > 0
step(z) = 0, if z <= 0

For this lesson, step(0) = 0.

Examples:

- If z = 0.2, output = 1.
- If z = -0.3, output = 0.

The step function makes the perceptron a binary classifier.

## 7. How Inputs Affect the Output

Consider:

w1 = 0.5
w2 = 0.8
b = -0.3

Case 1:

x1 = 1
x2 = 0

z = (1*0.5) + (0*0.8) - 0.3
z = 0.2

Output = 1

Case 2:

x1 = 0
x2 = 0

z = (0*0.5) + (0*0.8) - 0.3
z = -0.3

Output = 0

The weights and bias remain unchanged in this comparison.
Changing the input changes the prediction.

## 8. Loss

Loss represents the difference between the actual output and
the predicted output in this lesson.

loss = y - y_pred

Here:
- y = Actual output
- y_pred = Predicted output

Examples:

| Actual y | Predicted y_pred | Loss | Meaning |
|----------|------------------|------|---------|
| 1 | 0 | +1 | Under-prediction |
| 0 | 1 | -1 | Over-prediction |
| 1 | 1 | 0 | Correct prediction |
| 0 | 0 | 0 | Correct prediction |

If the prediction is correct, the loss is zero and no update is
needed under this learning rule.

## 9. The Perceptron Learning Rule

The perceptron updates its weights and bias when it makes an
incorrect prediction.

Weight update:

w_new = w_old + (loss * x)

Bias update:

b_new = b_old + loss

For two inputs:

w1_new = w1_old + (loss * x1)
w2_new = w2_old + (loss * x2)
b_new = b_old + loss

If loss = 0, the parameters do not change.

If loss is not zero, the parameters are corrected using the rule.

## 10. Training From Zero

Initially:

w1 = 0
w2 = 0
b = 0

The perceptron starts without learned weights.

For every training example:

1. Calculate the weighted sum.
2. Predict the output using the step function.
3. Calculate loss = actual output - predicted output.
4. Update the weights and bias if the prediction is wrong.
5. Repeat the training data until the model makes no updates
   during a complete epoch, or until a maximum epoch limit is reached.

An epoch means one complete pass through the training dataset.

## 11. Logical OR Gate

The OR gate produces 1 if at least one input is 1.

Truth table:

| x1 | x2 | OR output |
|----|----|-----------|
| 0 | 0 | 0 |
| 1 | 0 | 1 |
| 0 | 1 | 1 |
| 1 | 1 | 1 |

The OR gate is linearly separable. A single straight decision
boundary can separate its class-0 example from its class-1 examples.

### Training Example

Start with:

w1 = 0
w2 = 0
b = 0

Training example:

x1 = 0, x2 = 0, y = 0

z = (0*0) + (0*0) + 0
z = 0

Since step(0) = 0:

y_pred = 0
loss = 0 - 0 = 0

No update is required.

Next example:

x1 = 1, x2 = 0, y = 1

z = (1*0) + (0*0) + 0
z = 0

y_pred = 0
loss = 1 - 0 = 1

Update:

w1 = 0 + (1*1) = 1
w2 = 0 + (1*0) = 0
b = 0 + 1 = 1

The weights and bias change because the prediction was wrong.

Further training examples may cause additional updates. Training
continues until a complete pass produces no updates.

One valid final solution for OR is:

w1 = 1
w2 = 1
b = 0

With these values:

z = x1 + x2

The predicted outputs are:

- (0, 0): z = 0 -> output 0
- (1, 0): z = 1 -> output 1
- (0, 1): z = 1 -> output 1
- (1, 1): z = 2 -> output 1

All four OR examples are classified correctly.

## 12. Decision Boundary

The decision boundary is where the weighted sum equals zero.

w1*x1 + w2*x2 + b = 0

For two inputs, this equation represents a straight line.

One side of the line is classified as 1, and the other side
is classified as 0, according to the perceptron's prediction rule.

The perceptron learns weights and bias that define this line.

## 13. Linear Separability

A dataset is linearly separable when one straight line can separate
the examples belonging to different classes.

Examples:

- OR is linearly separable.
- AND is also linearly separable.

For a two-input perceptron, a single straight decision boundary
is sufficient for these problems.

## 14. XOR Gate

XOR produces 1 only when its two inputs are different.

Truth table:

| x1 | x2 | XOR output |
|----|----|------------|
| 0 | 0 | 0 |
| 1 | 0 | 1 |
| 0 | 1 | 1 |
| 1 | 1 | 0 |

Unlike OR, XOR is not linearly separable.

The class-0 examples are (0, 0) and (1, 1).
The class-1 examples are (1, 0) and (0, 1).

These diagonally opposite points cannot be separated correctly
using one straight line.

Therefore, a single perceptron cannot correctly classify all
four XOR examples, regardless of how long it is trained.

## 15. Limitation of a Single Perceptron

A single perceptron creates one linear decision boundary.

It can solve linearly separable binary classification problems,
but it cannot solve XOR.

Adding and connecting multiple perceptrons creates a neural network
that can represent more complex decision boundaries.

A network with multiple layers and suitable activations can learn
the XOR pattern.

## 16. Key Takeaways

1. A perceptron is a basic artificial neuron.
2. Inputs are multiplied by weights.
3. The weighted sum includes a bias.
4. The step function produces a binary prediction.
5. Loss = actual output - predicted output.
6. Incorrect predictions cause weight and bias updates.
7. OR is linearly separable.
8. XOR is not linearly separable.
9. A single perceptron cannot solve XOR.
10. Multiple connected perceptrons form a neural network.
