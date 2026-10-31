# AIML Learning Journey - Day 50
# Inside the MLP: Architecture, Notation, and the Dot Product

## 1. Introduction to Multilayer Perceptrons

A Multilayer Perceptron (MLP) is a neural network made up
of interconnected neurons organized into layers.

A single perceptron makes a decision using a weighted sum
and an activation function. An MLP contains multiple neurons
and layers that transform information to learn more complex
patterns.

Example 1:
A network can use house size and room count to predict a
house price.

Example 2:
A network can use email features to classify an email as
spam or not spam.

## 2. Layers of an MLP

An MLP commonly contains three types of layers.

### Input Layer
- Receives the input features.
- Passes the data to the next layer.
- Does not perform the learned weighted-sum computation.

Example 1: Three input features representing house size,
location score, and number of rooms.

Example 2: Pixel values supplied to a digit-recognition
network.

### Hidden Layer
- Transforms the information received from the previous layer.
- Contains neurons that perform weighted sums and apply
  activation functions.
- Is called hidden because its intermediate outputs are not
  the final answer.

Example 1: A hidden layer with four neurons.

Example 2: A network with two hidden layers that transforms
input features before making a prediction.

### Output Layer
- Produces the final network output.
- Its size and interpretation depend on the task.

Example 1: One output neuron predicting a house price.

Example 2: Ten output neurons representing the digits 0 to 9.

## 3. Fully Connected (Dense) Layers

In a fully connected layer, every neuron connects to every
neuron in the next layer.

Each connection has a weight, and each neuron has a bias.

For a layer with 2 inputs and 3 neurons:

Number of weights = 2 * 3 = 6
Number of biases = 3
Total parameters = 6 + 3 = 9

Example 1:
Two input features connect to three output neurons.
The layer contains six weights and three biases.

Example 2:
Three input features connect to four neurons.
The layer contains twelve weights and four biases.

## 4. Important Terminology

### Width
The number of neurons in a layer.

Example 1: A hidden layer with 4 neurons has width 4.

Example 2: A hidden layer with 10 neurons has width 10.

### Depth
The number of layers in a network. The exact counting
convention can vary, so state whether the input layer is
included when reporting depth.

Example 1: A network with one hidden layer is relatively
shallow.

Example 2: A network with several hidden layers is deeper.

### Feedforward Network
Information flows from the input through the hidden layers
to the output without recurrent loops.

Example 1: Input -> Hidden Layer -> Output Layer.

Example 2: Input -> Hidden Layer 1 -> Hidden Layer 2 -> Output.

### Parameters
The trainable weights and biases adjusted during training.

Example 1: A layer with 6 weights and 3 biases has 9 parameters.

Example 2: A network with 20 weights and 6 biases has
26 parameters.

## 5. Mathematical Notation

The following notation is used for neural network layers.

- x: Input feature vector.
- X: Batch input matrix, with one example per row.
- W^(l): Weight matrix for layer l.
- b^(l): Bias vector for layer l.
- z^(l): Weighted sum before activation at layer l.
- a^(l): Activation output at layer l.
- L: Total number of layers under the chosen counting convention.
- i: Index of a neuron.
- l: Layer index.

The superscript (l) identifies the layer. It is not an exponent
in this notation.

Example 1:
a_2^(1) represents the activation of neuron 2 in layer 1.

Example 2:
W^(1) represents the weight matrix connecting the input
(layer 0 activations) to layer 1.

Each layer has its own weight matrix and bias vector.

## 6. Forward Propagation

Forward propagation calculates the network output by passing
information through its layers.

Two equations describe the operation of each layer.

Weighted sum:

z^(l) = W^(l) a^(l-1) + b^(l)

Activation:

a^(l) = activation(z^(l))

Here:
- W contains the weights.
- a^(l-1) contains the previous layer's activations.
- b contains the biases.
- z contains the values before activation.
- a contains the values after activation.

Example 1:
A hidden layer calculates z = W @ x + b and applies ReLU.

Example 2:
The next layer uses the previous layer's activation values
to calculate its own weighted sums.

## 7. Why Matrix Multiplication Is Needed

When a layer contains multiple neurons, each neuron needs
its own weighted sum.

Instead of calculating every weighted sum separately,
matrix multiplication calculates them together.

This is more compact and works efficiently with numerical
libraries such as NumPy.

Example 1:
Two input features connected to three neurons require three
weighted sums.

Example 2:
A network with hundreds of neurons can calculate all the
weighted sums of a layer using one matrix operation.

## 8. Weight Matrix Shape

If a layer has:
- n input features
- m output neurons

Then the weight matrix has shape:

W.shape = (m, n)

There is one row per output neuron and one column per input
feature.

The input vector has shape (n,), and the bias vector has
shape (m,).

Example 1:
Two inputs and three neurons:

W.shape = (3, 2)
b.shape = (3,)

Example 2:
Three inputs and four neurons:

W.shape = (4, 3)
b.shape = (4,)

The inner dimensions must match for matrix multiplication.

## 9. Worked Example: One Layer

Input:

x = [1, 2]

Weight matrix:

W = [
    [0.2,  0.5],
    [0.8, -0.3],
    [0.1,  0.4]
]

Bias:

b = [0.1, 0.0, -0.2]

There are two input features and three output neurons.

Neuron 1:

z1 = (0.2 * 1) + (0.5 * 2) + 0.1
z1 = 0.2 + 1.0 + 0.1
z1 = 1.3

Neuron 2:

z2 = (0.8 * 1) + (-0.3 * 2) + 0.0
z2 = 0.8 - 0.6
z2 = 0.2

Neuron 3:

z3 = (0.1 * 1) + (0.4 * 2) - 0.2
z3 = 0.1 + 0.8 - 0.2
z3 = 0.7

Therefore:

z = [1.3, 0.2, 0.7]

The same result can be calculated in one operation:

z = W @ x + b

## 10. Activation Functions

An activation function is applied to the weighted-sum output.

The function is applied independently to each element of z.

### ReLU

ReLU(z) = max(0, z)

Example 1:
ReLU(-2) = 0

Example 2:
ReLU(3) = 3

For the worked example:

z = [1.3, 0.2, 0.7]

After ReLU:

a = [1.3, 0.2, 0.7]

ReLU does not change these values because they are positive.

Other activation functions include sigmoid and step activation.

The appropriate activation depends on the network and task.

## 11. Batch Processing

A batch contains multiple input examples processed together.

If every input example has n features and there are B examples:

X.shape = (B, n)

If a layer has m output neurons:

W.shape = (m, n)

The batch weighted sums are calculated using:

Z = X @ W.T + b

Here:
- X has one example per row.
- W.T is the transpose of W.
- b is added to every row through broadcasting.
- Z contains one row of weighted sums per input example.

Example 1:
Three examples, two input features, and three neurons:

X.shape = (3, 2)
W.shape = (3, 2)
Z.shape = (3, 3)

Example 2:
Five examples, four input features, and six neurons:

X.shape = (5, 4)
W.shape = (6, 4)
Z.shape = (5, 6)

Batch size is the number of examples processed together
in a forward pass.

## 12. Counting Network Parameters

Consider this network:

3 inputs -> 4 hidden neurons -> 2 output neurons

### Layer 1

Weight matrix shape = (4, 3)

Weights = 4 * 3 = 12
Biases = 4
Total = 12 + 4 = 16

### Layer 2

Weight matrix shape = (2, 4)

Weights = 2 * 4 = 8
Biases = 2
Total = 8 + 2 = 10

### Entire Network

Total weights = 12 + 8 = 20
Total biases = 4 + 2 = 6
Total parameters = 20 + 6 = 26

Training adjusts these trainable parameters using an
optimization process. Backpropagation calculates gradients
used to update them.

Example 1:
A layer with 3 inputs and 4 neurons has 16 parameters.

Example 2:
A layer with 4 inputs and 2 neurons has 10 parameters.

## 13. Output Layers for Different Tasks

The hidden layers perform the general-purpose transformations.
The output layer is designed according to the task.

### Regression

Regression predicts a continuous numerical value.

Output neurons: 1 for a single-target regression task.

Example 1: Predicting a house price.

Example 2: Predicting a delivery time.

The output is interpreted as a numerical prediction.

### Binary Classification

Binary classification distinguishes between two classes.

A common design uses one output neuron representing the
probability of the positive class, with a sigmoid activation.

A threshold such as 0.5 can convert the probability into
a yes/no prediction.

Example 1: Spam or not spam.

Example 2: Fraud or not fraud.

The threshold is a decision rule, not a universal requirement.

### Multiclass Classification

Multiclass classification selects among multiple classes.

A common design uses one output neuron per class, with a
softmax activation when class probabilities are required.

Example 1: Digit recognition with ten classes uses ten
output neurons.

Example 2: Classifying an image as a cat, dog, or bird uses
three output neurons in a standard three-class design.

The predicted class is commonly the one with the highest
output probability.

## 14. What Is Fixed and What Is a Design Choice?

The input layer size is determined by the number of input
features.

The output layer size depends on the task and the chosen
output representation.

The number and width of hidden layers are design choices.

Example 1:
A dataset with 3 input features requires an input
representation with 3 features.

Example 2:
A digit classifier for ten digit classes commonly uses
10 output neurons in a one-neuron-per-class design.

The hidden-layer architecture can be selected and evaluated
based on the problem.

## 15. Important Equations

Single example:

z = W @ x + b

Activation:

a = activation(z)

Batch of examples:

Z = X @ W.T + b

ReLU:

ReLU(z) = max(0, z)

Parameter count for a dense layer:

Parameters = (input_features * output_neurons)
             + output_neurons

Equivalent formula:

Parameters = (n * m) + m

## 16. Day 50 Summary

Today I learned:

1. The basic architecture of an MLP.
2. The roles of input, hidden, and output layers.
3. How weights and biases are associated with neurons.
4. How to represent a layer using a weight matrix.
5. How to calculate weighted sums with matrix multiplication.
6. How activation functions transform weighted sums.
7. How to process multiple examples using batches.
8. How to check matrix dimensions.
9. How to calculate trainable parameters.
10. How output-layer design differs between regression,
    binary classification, and multiclass classification.

Main takeaway:

Every layer follows the same basic pattern:

Weighted sum -> Activation

The hidden layers transform the input, while the output
layer produces a result appropriate for the task.