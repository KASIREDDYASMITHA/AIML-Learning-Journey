
# Day 56 - Backpropagation from First Principles

## Overview
Today I learned the fundamentals of Backpropagation and understood how a neural network traces the dependency chain from the final loss back through its layers.

## Topics Covered
- What happens during neural network training
- Trainable parameters: Weights (W) and Biases (b)
- Forward Propagation
- Loss Calculation using Mean Squared Error (MSE)
- Understanding the dependency chain
- Relationship between Loss and Prediction
- Relationship between Prediction and Pre-activation
- Hidden layer and output layer calculations
- Backward direction of Backpropagation
- Difference between Forward Propagation and Backpropagation
- Why Backpropagation starts from the Loss
- Introduction to Gradient Descent

## Key Concepts

1. Training means finding suitable values for weights and biases.
2. The architecture, activation functions, and loss function remain fixed during training.
3. Loss depends on the network prediction.
4. Every weight and bias affects the final loss through a chain of calculations.
5. Forward Propagation moves from input to output.
6. Backpropagation traces dependencies from loss towards the input.
7. Backpropagation identifies how each weight and bias contributes to the final loss.

## Network Architecture

2 Inputs -> 1 Hidden Neuron (ReLU) -> 1 Output Neuron (Linear)

## Example

Input: x = [1, 1]
Actual Output: y = 1.0
Predicted Output: y_hat = 0.77

Hidden Pre-activation: z1 = 0.9
Hidden Activation: a1 = 0.9
Output Pre-activation: z2 = 0.77

MSE Loss = (1.0 - 0.77)^2
         = 0.0529
         ≈ 0.053

## Dependency Chain

W1, b1, x -> z1 -> a1 -> z2 -> y_hat -> Loss

Output layer:
z2 = W2 * a1 + b2

Hidden layer:
z1 = W1 * x + b1

Hidden activation:
a1 = ReLU(z1)

Output prediction:
y_hat = z2

Loss:
Loss = (y - y_hat)^2

## Important Difference

Forward Propagation:
Input -> Output -> Prediction

Backpropagation:
Loss -> Output -> Hidden Layers -> Input


