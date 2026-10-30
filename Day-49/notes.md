# AIML Learning Journey — Day 49

## Topic: Inside the MLP — Architecture, Notation, and the Dot Product

## 1. Introduction to a Neural Network

A neural network consists of multiple artificial neurons connected together in layers. Each layer transforms the output received from the previous layer.

A single perceptron makes a decision using a weighted sum and an activation function. A Multi-Layer Perceptron (MLP) combines multiple neurons in layers to learn more complex patterns.

## 2. Layers of a Neural Network

A neural network generally contains three types of layers.

### Input Layer
- Receives the input features.
- Does not perform computation in the basic architecture described in the faculty notes.
- Passes the input data to the next layer.

Example 1: House price prediction using house size, location score, and number of rooms.

Example 2: Spam detection using email features.

### Hidden Layer
- Performs transformations on the input data.
- Contains neurons that learn useful intermediate representations.
- Can contain one or more layers.

Example 1: A hidden layer transforms house features into intermediate values useful for price prediction.

Example 2: Hidden layers learn useful patterns from email features for spam detection.

### Output Layer
- Produces the final result.
- Its size depends on the task.
- Its outputs may represent a number, a probability, or class scores.

Example 1: Predicting a house price.

Example 2: Classifying an email as spam or not spam.

## 3. Fully Connected or Dense Layer

In a fully connected layer, every neuron connects to every neuron in the next layer.

Each connection has a weight, and each neuron has a bias.

Every neuron performs two main operations:

1. Calculate the weighted sum and add the bias.
2. Apply an activation function.

### Example

Suppose a layer has 2 input features and 3 neurons.

Number of weights = 2 × 3 = 6

Number of biases = 3

Total parameters = 6 + 3 = 9

## 4. Important Terminology

### Width
The number of neurons in a layer.

Example 1: A hidden layer with 4 neurons has a width of 4.

Example 2: An output layer with 10 neurons has a width of 10.

### Depth
The number of layers in a network. A deep network has multiple hidden layers.

Example 1: A network with one hidden layer is a shallow network.

Example 2: A network with several hidden layers is a deeper network.

### Dense Layer
A layer in which every neuron connects to every neuron in the next layer.

### Feedforward Network
Information flows in one direction, from input through hidden layers to the output, without recurrent loops.

### Parameters
The weights and biases that training adjusts.

Example 1: A layer with 2 inputs and 3 neurons has 9 parameters.

Example 2: A network with 3 inputs, 4 hidden neurons, and 2 output neurons has 26 parameters.

## 5. Neural Network Notation

The following symbols are used to represent the operations of a neural network.

- x: Input feature vector.
- X: Batch input matrix, containing multiple examples.
- W^(l): Weight matrix for layer l.
- b^(l): Bias vector for layer l.
- z^(l): Pre-activation value for layer l.
- a^(l): Activation output for layer l.
- L: Total number of layers in the network.

The superscript (l) represents the layer number.

The subscript i represents the neuron index within a layer.

Example 1: a_2^(1) represents the activation of neuron 2 in layer 1.

Example 2: W^(1) represents the weight matrix connecting the input layer to layer 1.

Every layer has its own weight matrix and bias vector.

## 6. The Two Main Equations

Every layer in a feedforward neural network follows the same two-step process.

### Step 1: Calculate the Weighted Sum

z^(l) = W^(l) a^(l-1) + b^(l)

Where:
- W^(l) is the weight matrix.
- a^(l-1) is the output of the previous layer.
- b^(l) is the bias vector.
- z^(l) is the pre-activation value.

### Step 2: Apply the Activation Function

a^(l) = activation(z^(l))

The activation function is applied to the pre-activation values to produce the layer's output.

Example 1: ReLU activation converts negative values to zero.

Example 2: Sigmoid activation converts values into the range 0 to 1.

The output of one layer becomes the input to the next layer.

## 7. Why Do We Need the Dot Product?

When a layer contains multiple neurons, calculating each weighted sum separately is inefficient.

Matrix multiplication allows us to calculate the weighted sums for all neurons together.

The dot product is a compact way of performing these calculations.

### Example

Input:

x = [1, 2]

Weight matrix:

W = [[0.2, 0.5],
     [0.8, -0.3],
     [0.1, 0.4]]

Bias vector:

b = [0.1, 0.0, -0.2]

The calculation is:

z = W x + b

Neuron 1:

z1 = (0.2 × 1) + (0.5 × 2) + 0.1
z1 = 1.3

