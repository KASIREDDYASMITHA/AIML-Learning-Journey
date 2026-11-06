
# Day 56 - Backpropagation from First Principles

## 1. What Is Neural Network Training?

Whenever we say that a neural network learns, it means that the values stored inside its weights (W) and biases (b) are changed to improve its predictions.

### What Changes?
- Weights (W)
- Biases (b)

### What Remains Fixed During Training?
- Network architecture
- Activation functions
- Loss function

### Goal of Training

The goal is to find suitable values of weights and biases that make predictions as accurate as possible on the training data.

Training is the process of finding better values for every weight and bias in the network.

---

## 2. Steps Before Backpropagation

The first four steps were already covered in previous classes.

### Step 1: Pick a Training Example

Select one training example containing:
- Input vector (x)
- Actual output or target (y)

### Step 2: Forward Propagation

Pass the input through every layer of the neural network.

Each layer performs:
- Weight multiplication
- Bias addition
- Activation function

Finally, the network produces a prediction (y_hat).

### Step 3: Choose a Loss Function

Choose an appropriate loss function depending on the task.

Examples:
- MSE (Mean Squared Error) for regression.
- Cross-Entropy Loss for classification.

### Step 4: Calculate the Loss

Compare the predicted output with the actual output using the selected loss function.

The result is a single numerical value representing the prediction error.

---

## 3. Understanding Loss

Loss represents how far the predicted output is from the actual output.

- Higher loss indicates a larger prediction error.
- Lower loss indicates a smaller prediction error.

Example:
- Loss = 2.10: Prediction has a larger error.
- Loss = 0.05: Prediction has a smaller error.

The objective is to reduce the loss.

However, simply knowing that loss should decrease does not tell us which weights and biases should change.

---

## 4. Wrong Question vs Right Question

Wrong Question:

"How do I make the loss smaller?"

This question is too general. It does not tell us which parameter to change or how it affects the loss.

Right Question:

"Why is the loss this particular value?"

The loss is the result of a sequence of calculations.

By tracing those calculations, we can understand which values inside the network contributed to the final loss.

This is the basic idea behind Backpropagation.

---

## 5. Neural Network Architecture - Case A

Consider the simple neural network used in class.

Architecture:

2 Inputs -> 1 Hidden Neuron -> 1 Output Neuron

Hidden Layer:
- One neuron
- ReLU activation function

Output Layer:
- One neuron
- Linear activation function

### Input and Target

Input:

x = [1, 1]

Actual output:

y = 1.0

### Forward Pass Results

| Parameter | Value |
|---|---:|
| Hidden pre-activation (z1) | 0.9 |
| Hidden activation (a1) | 0.9 |
| Output pre-activation (z2) | 0.77 |
| Prediction (y_hat) | 0.77 |
| MSE Loss | 0.053 |

These values were already calculated in the previous class.

---

## 6. Loss Is the End of a Chain

The loss value does not appear randomly.

It is produced by a sequence of calculations.

For example:

1. Loss = 0.053 because the prediction is 0.77 and the actual output is 1.0.
2. Prediction = 0.77 because the output neuron's calculation produced that value.
3. The output neuron's calculation depends on weights, bias, and hidden-layer output.
4. The hidden-layer output depends on its pre-activation value.
5. The hidden-layer pre-activation depends on the input, weights, and bias.

Every number is connected to the calculations before it.

---

## 7. Link 1 - Loss Depends on Prediction

For Mean Squared Error:

Loss = (y - y_hat)^2

Where:
- y = Actual output
- y_hat = Predicted output

The loss directly depends on the prediction.

If the prediction changes, the loss also changes.

Dependency:

y_hat -> Loss

Example:

Actual output = 1.0

Prediction = 0.77

Loss = (1.0 - 0.77)^2

Loss = 0.0529

---

## 8. Link 2 - Prediction Depends on Output Pre-activation

The output neuron uses a Linear Activation Function.

A linear activation does not transform the pre-activation value.

Therefore:

y_hat = a2 = z2

Where:
- z2 = Output pre-activation
- a2 = Output activation
- y_hat = Prediction

Dependency:

z2 -> y_hat -> Loss

Any change in z2 directly affects the prediction and consequently the loss.

---

## 9. Link 3 - Output Pre-activation Depends on Three Values

The output neuron's calculation is:

z2 = W2 * a1 + b2

Where:
- W2 = Weight connecting the hidden neuron to the output neuron.
- a1 = Hidden neuron activation.
- b2 = Output neuron bias.

The output pre-activation depends on three quantities:

1. Output layer weight (W2)
2. Hidden layer activation (a1)
3. Output layer bias (b2)

Changing any one of these values can change z2, which affects the prediction and loss.

Dependency:

W2, a1, b2 -> z2 -> y_hat -> Loss

---

## 10. Link 4 - Hidden Activation Depends on Hidden Pre-activation

The hidden neuron uses the ReLU activation function.

Formula:

a1 = ReLU(z1)

ReLU is defined as:

ReLU(z) = max(0, z)

It returns:
- The same value if the input is positive.
- Zero if the input is negative or zero.

Example 1:

ReLU(0.9) = 0.9

Example 2:

ReLU(-0.5) = 0

In our network:

z1 = 0.9

a1 = ReLU(0.9) = 0.9

Dependency:

z1 -> a1 -> z2 -> y_hat -> Loss

For a positive z1, changing z1 changes a1.

---

## 11. Link 5 - Hidden Pre-activation Depends on Inputs

The hidden neuron's calculation is:

z1 = W1 * x + b1

Where:
- W1 = Weight vector connecting inputs to the hidden neuron.
- x = Input vector.
- b1 = Hidden neuron bias.

The hidden pre-activation depends on three quantities:

1. Input vector (x)
2. Hidden layer weights (W1)
3. Hidden layer bias (b1)

The input data is fixed for the selected training example.

The weights and biases are trainable parameters.

Dependency:

W1, x, b1 -> z1 -> a1 -> z2 -> y_hat -> Loss

---

## 12. Complete Dependency Chain

The complete dependency chain is:

W1, b1, x
      |
      v
     z1
      |
      v
     a1
      |
      v
     z2
      |
      v
    y_hat
      |
      v
     Loss

Every weight and bias is connected to the final loss through intermediate calculations.

The input is fixed, and the loss is the final outcome.

The weights and biases are the trainable parameters.

---

## 13. Neuron Output Notation

The class introduces a notation to identify neuron outputs in different layers.

### Hidden Layer Output

o1_1

Meaning:
- First index 1: Layer 1.
- Second index 1: Neuron 1.

This represents the output of the first hidden neuron.

It is equivalent to a1.

It depends on:
- W1
- b1
- Input x

### Output Layer Output

o2_1

Meaning:
- First index 2: Layer 2.
- Second index 1: Neuron 1.

This represents the output of the output neuron.

It is equivalent to y_hat.

It depends on:
- W2
- b2
- o1_1

Therefore:

o2_1 depends on W2, b2, and o1_1.

o1_1 depends on W1, b1, and x.

---

## 14. All Trainable Parameters Affect Loss

The trainable parameters in this network are:

- W1
- b1
- W2
- b2

Every weight and bias affects the final loss indirectly.

No parameter directly skips the intermediate calculations.

For example:

W2 affects z2, which affects y_hat, which affects Loss.

W1 affects z1, which affects a1, which affects z2, which affects y_hat, which affects Loss.

This dependency chain accounts for all trainable parameters.

---

## 15. Improving the Network Means Choosing Better Numbers

The goal of training is to find better values for weights and biases.

When better values are selected, forward propagation produces a better prediction and a smaller loss.

There is no other trainable lever in this network.

The architecture, activation functions, and loss function remain fixed during training.

Only weights and biases are adjusted.

---

## 16. Why Backpropagation Starts from the Loss

To understand how changing W1 affects the loss, we need to understand each intermediate relationship.

We must know:

1. How does changing W1 affect z1?
2. How does changing z1 affect a1?
3. How does changing a1 affect z2?
4. How does changing z2 affect y_hat?
5. How does changing y_hat affect Loss?

We cannot directly determine the effect of an early weight without tracing the intermediate calculations.

Therefore, the analysis starts at the loss and moves backwards through the network.

---

## 17. Forward Propagation vs Backpropagation

### Forward Propagation

- Starts from the input.
- Moves from left to right.
- Calculates values layer by layer.
- Produces the final prediction.

Direction:

Input -> Hidden Layer -> Output Layer -> Prediction

### Backpropagation

- Starts from the loss.
- Moves from right to left.
- Traces the dependencies.
- Determines how each weight and bias contributed to the final loss.

Direction:

Loss -> Output Layer -> Hidden Layer -> Input Side

---

## 18. Why Is It Called Backpropagation?

Backpropagation means propagating the influence of the loss backwards through the network.

It moves layer by layer from the output towards the input.

The algorithm traces how each weight and bias contributed to the final loss.

It does not propagate the input data backwards.

It traces the responsibility of the network parameters for the final loss.

---

## 19. What Is Still Missing?

Today's class explains:

- Why the analysis moves backwards.
- Which parameters contribute to the loss.
- How every parameter is connected to the loss.
- Why the dependency chain is important.

What is not covered yet:

- Precisely measuring how changing a weight changes the loss.
- Calculating gradients.
- Updating weights and biases.

A gradient measures how the loss changes with respect to a parameter.

Gradient Descent uses gradients to determine how much to adjust weights and in which direction.

These concepts are covered in the next class.

---

## 20. Definition of Backpropagation

Backpropagation is the process of tracing the chain of dependencies from the loss backward through the network, layer by layer, to determine how much each individual weight and bias contributed to the final loss.

---

## 21. Complete Training Loop

The training process discussed in class consists of the following steps:

Step 1: Pick a Data Point

Select one training example containing input x and actual output y.

Step 2: Forward Propagate

Pass the input through the network to produce prediction y_hat.

Step 3: Choose a Loss Function

Select an appropriate loss function such as MSE or Cross-Entropy.

Step 4: Calculate the Loss

Calculate the error between actual output and predicted output.

Step 5: Trace the Dependency Chain

Identify how each calculation is connected to the final loss.

Step 6: Backpropagate

Trace backwards through the network to understand each weight's and bias's contribution to the loss.

Step 7: Gradient Descent

Calculate the precise adjustment for each weight and bias to reduce the loss. This is the next class's topic.

---

