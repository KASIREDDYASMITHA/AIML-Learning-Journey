# Day 48 — Inside the Multilayer Perceptron (MLP)

## 1. Introduction

A Multilayer Perceptron (MLP) is a neural network consisting of neurons organized into layers.

A single perceptron makes a decision using its weighted inputs and a bias. An MLP connects multiple neurons in layers so that the network can learn more complex patterns.

For example:
- Predicting a house price from its features.
- Classifying an email as spam or not spam.

## 2. Architecture of an MLP

An MLP has three main types of layers.

### Input Layer
- Receives the raw input features.
- Passes the input to the next layer.
- Does not perform the layer computation described by the dense hidden layers.

Example: A house-price model may receive house size, number of rooms, and location score.

### Hidden Layer
- Performs transformations on the input.
- Contains neurons with weights and biases.
- Applies an activation function to the weighted sums.

Example: A network may contain one hidden layer with four neurons.

### Output Layer
- Produces the final prediction.
- Its size and interpretation depend on the task.

Example: One output neuron can predict a continuous house price.

## 3. Fully Connected or Dense Layer

In a fully connected layer, every neuron connects to every neuron in the next layer.

Each connection has a weight, and each neuron has a bias.

For a layer with 2 input features and 3 output neurons:

- Weights = 2 × 3 = 6
- Biases = 3
- Total trainable parameters = 6 + 3 = 9

## 4. Important Terminology

### Width
The number of neurons in a layer.

Example: A hidden layer containing 8 neurons has a width of 8.

### Depth
The number of layers in a network. The precise convention for counting layers can vary, so specify whether the input layer is included when reporting depth.

Example: A network with several hidden layers is deeper than a network with one hidden layer.

### Feedforward
Information flows from the input toward the output without loops in a feedforward network.

Example: Input → Hidden Layer → Output Layer.

### Parameters
The weights and biases that training adjusts.

Example: A network may learn 20 weights and 6 biases, giving 26 trainable parameters.

## 5. Mathematical Notation

The following notation is used throughout the lesson.

- `x`: Input feature vector.
- `W^(l)`: Weight matrix for layer `l`.
- `b^(l)`: Bias vector for layer `l`.
- `z^(l)`: Weighted sum before activation.
- `a^(l)`: Activation output of layer `l`.
- `L`: Total number of layers under the chosen counting convention.
- `X`: Batch input matrix containing multiple examples.

The superscript `(l)` indicates a layer number. A subscript such as `a_2^(1)` identifies neuron 2 in layer 1.

Each layer has its own weight matrix and bias vector.

## 6. Forward-Pass Equations

Every dense layer follows the same two-step process.

### Step 1: Calculate the weighted sum

`z^(l) = W^(l) a^(l-1) + b^(l)`

### Step 2: Apply an activation function

`a^(l) = activation(z^(l))`

The activation output of one layer becomes the input to the next layer.

## 7. Dot Product and Matrix Multiplication

When a layer contains many neurons, calculating each weighted sum separately becomes inefficient.

Matrix multiplication allows the weighted sums of multiple neurons to be calculated together.

For one input vector:

`z = W @ x + b`

Here, `@` represents matrix multiplication in Python.

### Example from the faculty notes

Input:

`x = [1, 2]`

Weight matrix:

`W = [[0.2, 0.5],`
`     [0.8, -0.3],`
`     [0.1, 0.4]]`

Bias:

`b = [0.1, 0.0, -0.2]`

Neuron 1:

`z1 = (0.2 × 1) + (0.5 × 2) + 0.1 = 1.3`

Neuron 2:

`z2 = (0.8 × 1) + (-0.3 × 2) + 0.0 = 0.2`

Neuron 3:

`z3 = (0.1 × 1) + (0.4 × 2) - 0.2 = 0.7`

Therefore:

`z = [1.3, 0.2, 0.7]`

The matrix operation produces the same results as the three individual weighted sums.

## 8. Matrix Shape Rules

If a layer receives `n` input features and contains `m` output neurons, its weight matrix must have shape:

`W.shape = (m, n)`

The bias vector has shape:

`b.shape = (m,)`

For the example above:

- Input shape: `(2,)`
- Weight matrix shape: `(3, 2)`
- Bias shape: `(3,)`
- Output shape: `(3,)`

The inner dimensions must match for matrix multiplication to work.

A shape mismatch is a common implementation error.

## 9. Activation Functions

An activation function is applied independently to each element of the weighted-sum vector.

Examples:

### ReLU
`ReLU(z) = max(0, z)`

Example 1: `ReLU(-2) = 0`

Example 2: `ReLU(3) = 3`

For `z = [1.3, 0.2, 0.7]`, ReLU produces:

`a = [1.3, 0.2, 0.7]`

All these values are already positive.

Other activation functions discussed in the lesson include sigmoid and step activation.

## 10. Batch Input Processing

Instead of processing one example at a time, several examples can be stacked into a matrix `X`.

Each row represents one example.

Example:

`X = [[1, 2],`
`     [0, 1],`
`     [1, 1]]`

Here, the batch size is 3 because there are three rows.

For row-wise examples, all layer outputs can be calculated together:

`Z = X @ W.T + b`

Here, `W.T` is the transpose of the weight matrix. NumPy broadcasts the bias vector across the rows.

The resulting output has one row for each input example and one column for each output neuron.

## 11. Counting Trainable Parameters

For a dense layer:

`Parameters = (number of inputs × number of neurons) + number of neurons`

The second term accounts for the biases.

### Example: 3 inputs → 4 hidden neurons → 2 output neurons

Layer 1:
- Weight matrix shape: `(4, 3)`
- Weights: 4 × 3 = 12
- Biases: 4
- Total: 16

Layer 2:
- Weight matrix shape: `(2, 4)`
- Weights: 2 × 4 = 8
- Biases: 2
- Total: 10

Total trainable parameters:

`16 + 10 = 26`

Training adjusts these weights and biases. Backpropagation is used to calculate gradients for learning.

## 12. Output Layers for Different Tasks

The hidden layers can use the same general computation across different tasks. The output layer changes according to the task.

### Regression
- Predicts a continuous numerical value.
- Typically uses one output neuron for a single target.
- A linear output is a common choice.

Example: Predicting a house price.

### Binary Classification
- Predicts between two classes.
- Commonly uses one output neuron with a sigmoid activation to represent the positive-class probability.
- A threshold such as 0.5 can convert the probability into a class decision.

Example: Spam or not spam.

### Multiclass Classification
- Predicts one class among several classes.
- Commonly uses one output neuron per class.
- Softmax is often used to convert output scores into class probabilities.

Example: Recognizing handwritten digits from 0 to 9 requires 10 output neurons.

The precise output activation and loss function depend on the problem formulation.

## 13. Architecture Choices

Some choices are determined by the problem:

- Input size: determined by the number of input features.
- Output size: determined by the task and target representation.

Other choices are design decisions:

- Number of hidden layers.
- Number of neurons in each hidden layer.
- Choice of hidden-layer activation functions.

These choices can affect model capacity and performance.
