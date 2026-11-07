# Day 57 – Gradient Descent

## 1. Introduction to Gradient Descent

Gradient Descent is an optimization algorithm used in Machine Learning and Deep Learning to minimize the loss function.

The main objective is to find the best values of weights and biases that produce minimum prediction error.

The loss function represents the difference between the actual output and predicted output.

### Loss Curve
- The loss curve represents the relationship between model parameters (weights) and loss.
- The lowest point of the curve represents the minimum loss.
- The objective of Gradient Descent is to move towards this minimum point.

### Example
If a model predicts 80 instead of the actual value 100, the loss represents the prediction error. Gradient Descent adjusts the parameters to reduce this error.

## 2. Understanding the Gradient

A gradient represents the slope of the loss function at the current point.

It provides two important pieces of information:

1. Direction – Which direction the curve is rising.
2. Steepness – How sharply the curve rises.

Gradient Descent uses this information to decide how to update the weights.

### Positive Gradient
- A positive gradient means the loss increases when the weight increases.
- Therefore, the weight should decrease to move towards lower loss.

Example:
If the gradient is +5, the weight should move in the negative direction.

### Negative Gradient
- A negative gradient means the loss decreases when the weight increases.
- Therefore, the weight should increase to move towards lower loss.

Example:
If the gradient is -5, the weight should move in the positive direction.

### Important Rule
Always move in the direction opposite to the gradient.

## 3. Gradient Descent Update Rule

The basic update rule is:

w_new = w_old - gradient

However, directly subtracting the gradient can result in steps that are too large or too small.

Therefore, we introduce the learning rate.

The final update formula is:

w_new = w_old - η × gradient

Where:

- w_new = Updated weight
- w_old = Previous weight
- η (eta) = Learning rate
- gradient = Slope of the loss function

## 4. Learning Rate

Learning Rate is a hyperparameter that controls the size of each step taken during Gradient Descent.

It is selected before training and is not learned directly by the network.

Common learning rates:
- 0.1
- 0.01
- 0.001

### Learning Rate Too Large

When the learning rate is too large:
- The weight may jump beyond the minimum point.
- It may repeatedly move from one side to another.
- Loss may increase instead of decreasing.
- Training may diverge.

This is called Overshooting.

Example:
A learning rate of 1.1 can cause divergence for the function f(w) = (w - 3)².

### Learning Rate Too Small

When the learning rate is too small:
- Weight updates become very small.
- Loss decreases very slowly.
- Training takes more time.
- Computational cost increases.

Example:
A learning rate of 0.001 may take many more iterations than 0.1 to approach the minimum.

## 5. Backpropagation vs Gradient Descent

Both work together during neural network training, but they perform different jobs.

### Backpropagation
- Calculates the gradient for each trainable parameter.
- Works backward from the loss through the network.
- Uses the chain rule.
- Determines how much each parameter contributes to the loss.

### Gradient Descent
- Uses the gradients calculated by backpropagation.
- Updates weights and biases.
- Moves parameters towards lower loss.

Important difference:

Backpropagation answers: HOW MUCH did each parameter contribute to the error?

Gradient Descent answers: WHAT SHOULD WE DO with those gradients?

## 6. Chain Rule in Backpropagation

The chain rule calculates how the loss changes with respect to each parameter by multiplying local derivatives along the dependency path.

For example:

Loss → ŷ → z² → a¹ → z¹ → W¹

Each connection has a local sensitivity.

Multiplying these local sensitivities gives the gradient for the corresponding weight.

## 7. Worked Example – Weight Updates

Consider a neural network:

2 Inputs → 1 Hidden Neuron (ReLU) → 1 Output (Linear)

Input:
x = [1, 1]

Actual output:
y = 1.0

Initial parameters:

- W¹ = [0.5, 0.3]
- b¹ = 0.1
- W² = 0.8
- b² = 0.05

Forward propagation:

z¹ = 0.9

a¹ = ReLU(0.9) = 0.9

z² = 0.9 × 0.8 + 0.05 = 0.77

Predicted output = 0.77

Squared error = (1.0 - 0.77)² = 0.0529 ≈ 0.053

### Gradients from Backpropagation

| Parameter | Gradient |
|---|---:|
| W¹ component 1 | -0.368 |
| W¹ component 2 | -0.368 |
| b¹ | -0.368 |
| W² | -0.414 |
| b² | -0.46 |

Learning rate = 0.1

Using:

w_new = w_old - η × gradient

Updated parameters:

| Parameter | Old Value | New Value |
|---|---:|---:|
| W¹ component 1 | 0.5 | 0.537 |
| W¹ component 2 | 0.3 | 0.337 |
| b¹ | 0.1 | 0.137 |
| W² | 0.8 | 0.841 |
| b² | 0.05 | 0.096 |

All gradients are negative, so all parameters increase.

### After the Update

Using the updated parameters:

z¹ = 1.010

a¹ = 1.010

z² ≈ 0.946

New predicted output ≈ 0.946

Old loss ≈ 0.053

New loss ≈ 0.003

The loss decreases significantly after just one update.

## 8. How a Neural Network Learns

The complete training process follows four major steps:

1. Forward Propagation – Pass input through the network to generate predictions.
2. Compute Loss – Calculate the difference between actual and predicted output.
3. Backpropagation – Calculate gradients for all trainable parameters.
4. Update Weights – Use Gradient Descent to update weights and biases.

This cycle repeats across training examples and epochs.

## 9. Types of Gradient Descent

The three types differ based on how many training examples are used to calculate the gradient for each update.

### A. Batch Gradient Descent

Batch Gradient Descent uses the entire training dataset to calculate the gradient before updating the parameters.

Characteristics:
- Uses all training examples for each update.
- One epoch produces one weight update.
- Gradient is averaged across the complete dataset.
- Stable and consistent updates.
- Slow for very large datasets.

Example:
For 1,000 training examples, all 1,000 examples are processed before one update.

Algorithm:

For each epoch:
1. Calculate gradients using all examples.
2. Average the gradients.
3. Update weights.

Advantages:
- Stable gradient estimates.
- Smooth convergence when learning rate is suitable.

Disadvantages:
- Computationally expensive for large datasets.
- Requires processing the complete dataset before each update.

Best for:
Small datasets where full-dataset computation is manageable.

### B. Stochastic Gradient Descent (SGD)

SGD calculates the gradient using only one randomly selected training example at a time.

Characteristics:
- Uses one example per update.
- One epoch produces as many updates as there are training examples.
- Updates weights immediately.
- Training starts improving quickly.
- The optimization path is noisy.

Example:
For 1,000 training examples, one epoch produces 1,000 updates.

Algorithm:

For each epoch:
1. Shuffle the dataset.
2. Select one training example.
3. Calculate its gradient.
4. Update weights immediately.
5. Repeat for all examples.

Advantages:
- Fast updates.
- Useful for very large datasets.
- Noise can sometimes help escape shallow local minima.

Disadvantages:
- Noisy and irregular updates.
- Less smooth convergence.
- Individual examples may give misleading gradient directions.

Best for:
Very large datasets and online learning situations.

### C. Mini-Batch Gradient Descent

Mini-Batch Gradient Descent uses a small group of training examples to calculate the gradient for each update.

Common batch sizes:
- 32
- 64
- 128
- 256

Characteristics:
- Uses a small batch instead of the complete dataset.
- Calculates the average gradient for each batch.
- Updates weights after processing each batch.
- More stable than pure SGD.
- Faster per epoch than full Batch GD in many practical settings.

Example:
For 1,000 examples and batch size 32:

Number of updates per epoch = 1000 / 32 ≈ 32 updates (with a final partial batch).

Algorithm:

For each epoch:
1. Divide the dataset into small batches.
2. Calculate the average gradient for each batch.
3. Update weights after each batch.
4. Repeat until all batches are processed.

Advantages:
- Balance between speed and stability.
- Efficient use of GPU parallel processing.
- Commonly used in deep learning.

Disadvantages:
- Batch size must be selected.
- Some gradient noise remains.

Best for:
Most practical deep learning applications.

## 10. Comparison of Three Types

| Feature | Batch GD | SGD | Mini-Batch GD |
|---|---|---|---|
| Examples per update | All | 1 | Small group |
| Updates per epoch | 1 | N | Approximately N/B |
| Speed per update | Slow | Very fast | Fast |
| Stability | Very stable | Noisy | Fairly stable |
| Best use | Small datasets | Huge datasets / online learning | Most deep learning tasks |

Where:
N = Number of training examples

B = Batch size

## 11. Advanced Optimization Techniques

The basic update rule is also called Vanilla Gradient Descent.

More advanced optimizers build on the same foundation.

### Momentum
- Remembers the direction of previous updates.
- Uses previous gradient information in the current update.
- Helps smooth the optimization path.
- Can accelerate movement through flat regions.

### Adam (Adaptive Moment Estimation)
- Uses the history of gradients.
- Adapts the effective learning rate for individual parameters.
- Combines momentum-like and adaptive learning-rate ideas.
- Commonly used in deep learning.
