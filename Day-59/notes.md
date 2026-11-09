
# Day 59 - Backpropagation From First Principles

## 1. Introduction to Backpropagation

When we say that a neural network learns, it means that the values of weights (W) and biases (b) change until the predictions become more accurate.

Training is the process of finding the correct values of weights and biases to minimize the prediction error.

### What Changes During Training?
- Weights (W)
- Biases (b)

### What Stays Fixed?
- Network Architecture
- Activation Functions
- Loss Function

The main goal is to find values of W and b that produce accurate predictions on training data.

---

## 2. Steps Before Backpropagation

The following four steps were already covered in previous classes.

### Step 1: Pick a Training Example
Select one data point containing:
- Input vector (x)
- True label (y)

### Step 2: Forward Propagation
Pass the input through every layer using weights, biases, and activation functions to produce a prediction.

### Step 3: Choose a Loss Function
Select an appropriate loss function depending on the problem.

Examples:
- MSE (Mean Squared Error) - Regression
- Cross-Entropy - Classification

### Step 4: Calculate the Loss
Compare the predicted output with the actual output using the loss function.

The loss represents how far the prediction is from the actual value.

---

## 3. Understanding Loss

Loss represents the prediction error.

- High Loss: Prediction is far from the actual value.
- Low Loss: Prediction is close to the actual value.

The goal of training is to reduce the loss.

Instead of simply asking:

"How do I make the loss smaller?"

We should ask:

"Why is the loss this particular value?"

This helps us identify which calculations and parameters are responsible for the loss.

---

## 4. Neural Network Example - Case A

Consider a simple neural network:

2 Inputs → 1 Hidden Neuron → 1 Output Neuron

### Network Architecture

- Input Layer: 2 inputs
- Hidden Layer: 1 neuron with ReLU activation
- Output Layer: 1 neuron with Linear activation

### Input and Target

Input:

x = [1, 1]

Actual Output:

y = 1.0

### Forward Pass Results

| Parameter | Value |
|---|---:|
| z1 (Hidden Pre-activation) | 0.9 |
| a1 = ReLU(z1) | 0.9 |
| z2 (Output Pre-activation) | 0.77 |
| Predicted Output (ŷ) | 0.77 |
| MSE Loss | 0.0529 ≈ 0.053 |

---

## 5. Loss Is the End of a Chain

Loss does not appear randomly. It is the result of a sequence of calculations.

The dependency chain is:

Weights and Biases
        ↓
Pre-activation
        ↓
Activation
        ↓
Next Layer Calculation
        ↓
Prediction
        ↓
Loss

Every value in the network depends on the calculations before it.

---

## 6. Link 1 - Loss Depends on Prediction

For Mean Squared Error:

Loss = (y - ŷ)²

Where:
- y = Actual output
- ŷ = Predicted output

For our example:

Loss = (1.0 - 0.77)²

Loss = 0.23²

Loss = 0.0529

Therefore, loss directly depends on the predicted output.

Dependency:

ŷ → Loss

---

## 7. Link 2 - Prediction Depends on z2

The output neuron uses a Linear Activation Function.

For linear activation:

ŷ = a2 = z2

Where:
- z2 = Output pre-activation
- a2 = Output activation
- ŷ = Predicted output

Since the output activation is linear, the prediction is equal to z2.

Dependency:

z2 → ŷ → Loss

---

## 8. Link 3 - z2 Depends on Three Things

The output neuron's calculation is:

z2 = W2 × a1 + b2

Where:
- W2 = Weight connecting the hidden neuron to the output neuron.
- a1 = Output of the hidden neuron.
- b2 = Bias of the output neuron.

The output pre-activation depends on:
1. Output layer weight (W2)
2. Output layer bias (b2)
3. Hidden layer activation (a1)

Changing any of these values changes z2 and can affect the final loss.

Dependency:

W2, b2, a1 → z2 → ŷ → Loss

---

## 9. Link 4 - a1 Depends on z1

The hidden neuron uses ReLU activation.

Formula:

a1 = ReLU(z1)

ReLU activation:

ReLU(z) = max(0, z)

Where:
- z1 = Hidden layer pre-activation.
- a1 = Hidden layer activation.

For our example:

z1 = 0.9

a1 = max(0, 0.9)

a1 = 0.9

Since z1 is positive, the ReLU output is equal to z1.

Dependency:

z1 → a1 → z2 → ŷ → Loss

---

## 10. Link 5 - z1 Depends on Inputs

The hidden neuron's calculation is:

z1 = W1 · x + b1

Where:
- W1 = Weight vector connecting inputs to the hidden neuron.
- x = Input vector.
- b1 = Bias of the hidden neuron.

The hidden pre-activation depends on:
1. Input weights (W1)
2. Input values (x)
3. Hidden layer bias (b1)

The input values are fixed for the training example.

Weights and biases are trainable parameters.

Dependency:

W1, b1, x → z1 → a1 → z2 → ŷ → Loss

---

## 11. Complete Dependency Chain

The complete dependency chain is:

W1, b1, x
     ↓
     z1
     ↓
     a1
     ↓
W2, b2 → z2
     ↓
     ŷ
     ↓
    Loss

All trainable parameters are connected to the final loss through intermediate calculations.

Trainable Parameters:
- W1
- b1
- W2
- b2

---

## 12. Neuron Output Notation

The following notation is used to represent neuron outputs.

### Hidden Layer

o1_1 = Output of Neuron 1 in Layer 1.

It is the hidden neuron's output, which was previously represented as a1.

It depends on:
- W1
- b1
- Input x

### Output Layer

o2_1 = Output of Neuron 1 in Layer 2.

It is the final prediction, previously represented as ŷ.

It depends on:
- W2
- b2
- o1_1

Therefore:

o2_1 depends on W2, b2 and o1_1.

o1_1 depends on W1, b1 and x.

---

## 13. Improving the Network

Improving a neural network means finding better values for all weights and biases.

The objective is to produce a smaller loss when forward propagation runs again.

Important points:
- Architecture remains fixed.
- Activation functions remain fixed.
- Loss function remains fixed.
- Weights and biases are the trainable parameters.

There is no other parameter to adjust in this training setup.

---

## 14. Why Backpropagation Starts Backward

To understand how a weight affects the loss, we need to understand how it affects the intermediate calculations.

For example, to understand how W1 affects loss:

1. Understand how W1 affects z1.
2. Understand how z1 affects a1.
3. Understand how a1 affects z2.
4. Understand how z2 affects prediction.
5. Understand how prediction affects loss.

Therefore, the analysis starts at the loss and moves backward through the network.

---

## 15. Forward Propagation vs Backpropagation

### Forward Propagation

- Moves from input to output.
- Direction: Left to Right.
- Calculates predictions using weights, biases and activation functions.

### Backpropagation

- Moves from loss toward input.
- Direction: Right to Left.
- Traces the dependency chain.
- Determines how much each weight and bias contributed to the final loss.

Backpropagation does not propagate input data backward. It propagates the influence or responsibility of the loss through the calculations.

---

## 16. Definition of Backpropagation

Backpropagation is the process of tracing the chain of dependencies from the loss backward through the network, layer by layer, to determine how much each individual weight and bias contributed to the final loss.

---

## 17. Complete Training Loop

The training process covered so far:

1. Pick a Data Point.
   - Select input x and actual output y.

2. Forward Propagate.
   - Pass input through the network to get prediction.

3. Choose a Loss Function.
   - Select an appropriate loss function.

4. Calculate the Loss.
   - Compare prediction with actual output.

5. Trace the Dependency Chain.
   - Understand why the loss has that value.

6. Backpropagate.
   - Trace the dependencies backward to understand each parameter's contribution.

7. Update Weights.
   - Calculate precise parameter adjustments using gradients.

Step 7 will be covered in the next class through Gradient Descent.

---


