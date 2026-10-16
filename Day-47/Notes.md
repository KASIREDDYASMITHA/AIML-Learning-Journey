# Day 47 – AIML Notes
## Inside the MLP: Architecture, Notation, and the Dot Product

## 1. Introduction to MLP

A Multi-Layer Perceptron (MLP) is a neural network made up of neurons arranged in layers.

A single perceptron makes a decision using a weighted sum and an activation function. An MLP connects multiple neurons in layers so that the network can learn more complex patterns.

Each layer transforms the output received from the previous layer.

## 2. Architecture of a Neural Network

A neural network generally contains three types of layers.

### 2.1 Input Layer
- Receives the raw input features.
- Passes the input data into the network.
- The input layer itself performs no learned computation.

Example: A house-price model may receive house size, location score, and number of rooms.

### 2.2 Hidden Layer
- Performs transformations on the input.
- Contains neurons with weights, biases, and activation functions.
- May contain one or multiple layers.
- Is called hidden because its intermediate outputs are not the final answers.

Example: Hidden neurons transform house features into intermediate representations useful for prediction.

### 2.3 Output Layer
- Produces the final prediction.
- Its size and interpretation depend on the task.

Examples:
- Regression: predicts a continuous number.
- Binary classification: predicts the probability of a positive class.
- Multi-class classification: produces a score for each class.

## 3. Dense or Fully Connected Layer

In a dense layer, every neuron connects to every neuron in the next layer.

Each connection has its own weight, and each neuron has its own bias.

For a layer with 2 input features and 3 output neurons:

Weights = 2 × 3 = 6

Biases = 3

Total parameters = 6 + 3 = 9

## 4. Important Terminology

### Width
The number of neurons in a layer.

Example: A hidden layer with 4 neurons has a width of 4.

### Depth
The number of layers in a network. A deep network has many hidden layers.

### Dense Layer
A layer in which every neuron connects to every neuron in the next layer.

### Feedforward Network
Information flows in one direction, from input toward output, without recurrent loops.

### Parameters
The weights and biases learned and adjusted during training.

## 5. Mathematical Notation

| Symbol | Meaning |
|---|---|
| `x` | Input feature vector |
| `X` | Batch input matrix; each row is one example |
| `W^(l)` | Weight matrix of layer `l` |
| `b^(l)` | Bias vector of layer `l` |
| `z^(l)` | Pre-activation weighted sum at layer `l` |
| `a^(l)` | Activation output at layer `l` |
| `L` | Total number of layers |
| `l` | Layer index |

The superscript `(l)` identifies the layer number. A subscript such as `i` identifies a neuron within that layer.

Each layer has its own weight matrix and bias vector.

## 6. Forward Propagation Equations

Every layer follows two steps.

### Step 1: Calculate the weighted sum

`z^(l) = W^(l) @ a^(l-1) + b^(l)`

Where:
- `W^(l)` is the current layer's weight matrix.
- `a^(l-1)` is the previous layer's activation output.
- `b^(l)` is the current layer's bias vector.
- `z^(l)` is the pre-activation value.

For the first layer, the input feature vector `x` is used instead of a previous hidden-layer output.

### Step 2: Apply the activation function

`a^(l) = activation(z^(l))`

The activation function is applied independently to each element of the weighted-sum vector.

The resulting activation becomes the input to the next layer.

This repeated process is called forward propagation.

## 7. Why Matrix Multiplication Is Needed

When a layer has multiple neurons, calculating each weighted sum separately is repetitive.

Matrix multiplication combines these calculations into one operation.

Instead of computing every neuron's weighted sum individually, the network stores its weights in a matrix and calculates all the weighted sums together.

This is compact and efficient.

## 8. Worked Example: One Input and Three Neurons

Given:

Input vector:

`x = [1, 2]`

Weight matrix:

`W = [[0.2, 0.5],`
`     [0.8, -0.3],`
`     [0.1, 0.4]]`

Bias vector:

`b = [0.1, 0.0, -0.2]`

There are 2 input features and 3 output neurons.

Therefore, the weight matrix shape is `(3, 2)`.

### Neuron 1

`z1 = (0.2 × 1) + (0.5 × 2) + 0.1`

`z1 = 0.2 + 1.0 + 0.1 = 1.3`

### Neuron 2

`z2 = (0.8 × 1) + (-0.3 × 2) + 0.0`

`z2 = 0.8 - 0.6 = 0.2`

### Neuron 3

`z3 = (0.1 × 1) + (0.4 × 2) - 0.2`

`z3 = 0.1 + 0.8 - 0.2 = 0.7`

Final weighted-sum vector:

`z = [1.3, 0.2, 0.7]`

Using matrix notation:

`z = W @ x + b`

The result is the same as calculating each neuron separately.

## 9. Weight Matrix Shape Rule

If:
- `n` = number of input features
- `m` = number of output neurons

Then:

`W.shape = (m, n)`

The matrix contains one row per output neuron and one column per input feature.

Example 1:
- 2 input features
- 3 neurons
- Weight matrix shape: `(3, 2)`

Example 2:
- 4 input features
- 5 neurons
- Weight matrix shape: `(5, 4)`

The number of weights is `m × n`.

A mismatched matrix shape causes a multiplication error.

## 10. Activation Functions

After calculating `z`, an activation function transforms the result into the layer's output.

### ReLU

Rectified Linear Unit:

`ReLU(z) = max(0, z)`

Examples:
- `ReLU(2.5) = 2.5`
- `ReLU(-1.5) = 0`

For the example above:

`z = [1.3, 0.2, 0.7]`

After ReLU:

`a = [1.3, 0.2, 0.7]`

All values remain unchanged because they are positive.

### Sigmoid

The sigmoid function maps values into the range `(0, 1)`.

`sigmoid(z) = 1 / (1 + exp(-z))`

It is commonly used in the output layer for binary classification.

### Step Function

A step function applies a threshold to produce a discrete output. The exact threshold convention depends on its definition.

## 11. Batch Processing

A batch contains multiple input examples processed together.

Consider:

`X = [[1, 2],`
`     [0, 1],`
`     [1, 1]]`

Each row is one input example.

There are 3 examples and 2 features, so:

`X.shape = (3, 2)`

For the weight matrix of shape `(3, 2)`, all batch outputs can be computed using:

`Z = X @ W.T + b`

Here, `W.T` is the transpose of the weight matrix.

The result has shape `(3, 3)`:
- 3 rows for the input examples.
- 3 columns for the output neurons.

Batch size is the number of examples processed in one forward pass.

## 12. Counting Neural Network Parameters

A dense layer with `n` inputs and `m` output neurons has:

Number of weights = `n × m`

Number of biases = `m`

Total parameters = `(n × m) + m`

Equivalently:

`Total parameters = m × (n + 1)`

### Example: 3 → 4 → 2 Network

Architecture:
- 3 input features
- 4 hidden neurons
- 2 output neurons

Layer 1:
- Weight shape: `(4, 3)`
- Weights: `4 × 3 = 12`
- Biases: `4`
- Subtotal: `16`

Layer 2:
- Weight shape: `(2, 4)`
- Weights: `2 × 4 = 8`
- Biases: `2`
- Subtotal: `10`

Total weights = `12 + 8 = 20`

Total biases = `4 + 2 = 6`

Total parameters = `20 + 6 = 26`

Training adjusts these parameters through optimization, using gradients calculated by backpropagation.

## 13. What Is Fixed and What Can Be Chosen?

### Determined by the problem
- Input layer size: determined by the number of input features.
- Output layer size: determined by the task.

### Architecture design choices
- Number of hidden layers.
- Number of neurons in each hidden layer.

The input and output requirements constrain the two ends of the network; the hidden architecture is selected by the model designer.

## 14. Output Layers for Different Tasks

### 14.1 Regression

Regression predicts a continuous numerical value.

Example: House-price prediction.

Inputs may include:
- House size
- Location score
- Number of rooms

Output layer: 1 neuron.

Its raw output represents the predicted value.

### 14.2 Binary Classification

Binary classification distinguishes between two classes.

Example: Spam detection.

The output layer uses 1 neuron to represent the probability of the positive class, typically using a sigmoid activation.

A threshold, commonly `0.5`, converts the probability into a class decision.

Example:
- Probability = `0.80` → spam if the threshold is `0.5`.
- Probability = `0.20` → not spam if the threshold is `0.5`.

### 14.3 Multi-Class Classification

Multi-class classification chooses among more than two classes.

Example: Recognizing handwritten digits from 0 to 9.

There are 10 classes, so the output layer has 10 neurons.

Each output corresponds to a class score or probability, depending on the output activation.

The predicted class is commonly selected using the index of the largest output value (`argmax`).

## 15. Main Insight

The hidden layers learn intermediate representations and use the same forward-propagation process regardless of the task.

The output layer is specialized for the task through its number of neurons, activation, and interpretation.

Examples:
- House-price prediction: one numerical output.
- Spam detection: one positive-class probability.
- Digit recognition: ten class outputs.
