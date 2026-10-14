# AIML Day 45 — The Perceptron

## Overview

This lesson covers the perceptron, a basic artificial neuron used
for binary classification.

## Topics Covered

- Biological neuron and artificial neuron
- Inputs, weights and bias
- Weighted sum and step activation function
- Prediction and loss calculation
- Perceptron weight and bias update rules
- Training from zero
- Epochs and convergence
- OR gate classification
- Linear separability and decision boundaries
- XOR gate and the limitations of a single perceptron
- Introduction to neural networks

## Important Formulas

Weighted sum:

z = w1*x1 + w2*x2 + b

Prediction:

y_pred = step(z)

Loss:

loss = y - y_pred

Weight update:

w_new = w_old + (loss * x)

Bias update:

b_new = b_old + loss
