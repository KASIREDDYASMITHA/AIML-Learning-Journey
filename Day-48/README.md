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

