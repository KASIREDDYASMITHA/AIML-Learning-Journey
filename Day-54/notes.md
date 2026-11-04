# Day 54 - Activation Functions

## 1. What is an Activation Function?

An activation function is a mathematical function applied to the output of a neuron.

It transforms the raw weighted sum (z) into the actual neuron output (a).

The activation function decides how much information should pass to the next layer.

### Basic Notation

- z = Raw weighted sum (input to activation function).
- a = Activated output of the neuron.

The activation function transforms z into a.

## 2. Why Do We Need Activation Functions?

Without activation functions, stacking multiple neural network layers would be pointless.

If every layer performs only linear operations, the entire network collapses into a single linear operation.

Even with multiple layers, the network can only learn linear relationships.

Activation functions introduce non-linearity, allowing neural networks to learn complex patterns.

Example:
1. XOR problem: A simple linear model cannot solve the XOR problem.
2. Complex patterns: Neural networks need non-linearity to learn complex relationships.

## 3. Six Types of Activation Functions

### 1. Step Function

Formula:

a = 1 if z > 0
a = 0 otherwise

Explanation:

- If z is greater than zero, output is 1.
- Otherwise, output is 0.
- It produces a binary fire-or-no-fire decision.

Advantages:
- Simple and easy to understand.
- Produces clear binary decisions.

Disadvantages:
- No useful gradient for learning because the gradient is zero almost everywhere.
- All-or-nothing output.
- Cannot express confidence.

Applications:
- Historical use in the original 1958 perceptron.
- Essentially unused in modern neural networks.

### 2. Linear Activation Function

Formula:

a = z

Explanation:

The input is passed directly without any transformation.

It produces a straight diagonal line through the origin.

Advantages:
- Smooth everywhere.
- No flat regions.
- Always provides a gradient.

Disadvantages:
- Stacking linear layers still produces a linear function.
- Does not introduce non-linearity.

Applications:
- Output layer for regression problems.

Example:
House price prediction.

### 3. Sigmoid Function

Formula:

a = 1 / (1 + e^(-z))

Explanation:

Sigmoid transforms the input into a value between 0 and 1.

- For very negative z, output approaches 0.
- For very positive z, output approaches 1.
- It is steepest near z = 0.

Advantages:
- Smooth function.
- Output is bounded between 0 and 1.
- Can be interpreted as a probability.

Disadvantages:

1. Vanishing Gradient:
   For very large positive or negative inputs, the curve becomes nearly flat. This makes learning difficult.

2. Not Zero-Centred:
   Its output is always positive, which can slow down training.

Applications:
- Output layer for binary classification.

Examples:
1. Spam detection.
2. Customer churn prediction.

### 4. ReLU (Rectified Linear Unit)

Formula:

a = max(0, z)

Explanation:

- If z is positive, output is z.
- If z is negative or zero, output is 0.

Advantages:

1. No saturation on the positive side.
2. Computationally fast.
3. Simple max operation.

Disadvantages:

Dying ReLU Problem:

A neuron that consistently receives negative inputs produces zero output and can become permanently inactive.

Applications:
- Default activation function for hidden layers in most modern neural networks.

Example:

Dense(128, activation='relu')

### 5. Leaky ReLU

Formula:

a = z       if z > 0
a = 0.01z   otherwise

Explanation:

Leaky ReLU is similar to ReLU, but it allows a small negative output instead of producing zero for all negative inputs.

Advantages:
- Helps prevent dead neurons.
- Maintains a small gradient for negative inputs.
- Allows neurons to recover.

Disadvantages:
- Requires an additional hyperparameter (negative slope).
- Does not always outperform ReLU.

Applications:
- Used as a replacement for ReLU when dying neurons are suspected.

Example:

Negative slope = 0.01

### 6. Softmax Function

Softmax is different from the other activation functions.

It takes a group of raw scores and converts them into probabilities that sum to 1.

Formula:

softmax(z_i) = e^(z_i) / sum(e^(z_j))

Explanation:

1. Calculate the exponential of each raw score.
2. Add all exponential values.
3. Divide each exponential value by their total.
4. Each output represents a probability.

Advantages:
- Produces probabilities across multiple classes.
- Easy to identify the highest-probability class using argmax.

Disadvantages:
- Applied to a whole output layer rather than an individual neuron.
- Used for multi-class final outputs, not hidden layers.

Applications:
- Multi-class classification.
- MNIST digit classification.

Example:

Dense(10, activation='softmax')

The model produces probabilities for 10 digit classes.

## 4. Comparison of All Six Activation Functions

| Function | Formula | Range | Application |
|----------|---------|-------|-------------|
| Step | 1 if z > 0, else 0 | {0,1} | Historical |
| Linear | a = z | (-infinity, infinity) | Regression |
| Sigmoid | 1/(1+e^(-z)) | (0,1) | Binary classification |
| ReLU | max(0,z) | [0,infinity) | Hidden layers |
| Leaky ReLU | z or 0.01z | (-infinity,infinity) | Hidden layers |
| Softmax | e^(zi)/sum(e^(zj)) | (0,1), sum = 1 | Multi-class classification |

## 5. What Activation Function Should We Use?

### Hidden Layers
- Default: ReLU.
- Alternative: Leaky ReLU when dying neurons are suspected.

### Output Layers

1. Regression:
   Linear activation (no activation).

2. Binary Classification:
   Sigmoid activation.

3. Multi-class Classification:
   Softmax activation.

## 6. Important Problems

### Vanishing Gradient
Occurs when gradients become very small during training, making learning difficult.

Example:
Sigmoid saturation for very large positive or negative inputs.

### Dying ReLU
Occurs when a neuron consistently receives negative inputs and produces zero output.

Example:
A ReLU neuron that remains inactive during training.
