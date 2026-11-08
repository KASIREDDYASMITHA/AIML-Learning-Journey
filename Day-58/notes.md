
# Day 58 - Gradient Descent Notes

## 1. Introduction to Gradient Descent

Gradient Descent is an optimization algorithm used to minimize the loss function by updating the weights and biases of a machine learning or deep learning model.

The main objective is to find the minimum point of the loss curve.

The loss function measures the difference between the predicted output and the actual output.

### Why Do We Need Gradient Descent?

- To minimize the loss.
- To improve model predictions.
- To update weights and biases.
- To help the model learn from training data.

## 2. Understanding the Loss Curve

A loss curve represents the relationship between a model parameter (weight) and the resulting loss.

- The bottom of the curve represents the minimum loss.
- Our objective is to reach the lowest point.
- Gradient Descent helps us move towards this minimum.

We cannot see the entire loss curve during actual training. We only know our current weights and the loss they produce.

## 3. What is a Gradient?

A gradient represents the slope of the loss function at the current parameter value.

It provides two important pieces of information:

1. Direction: Which direction the curve is rising.
2. Steepness: How sharply the curve rises.

The gradient helps us decide how to update the weights.

## 4. Positive Gradient

When the gradient is positive:

- The loss increases when the weight increases.
- We should decrease the weight.
- The weight moves towards the minimum.

Example:

If the gradient is +5, the weight should decrease.

## 5. Negative Gradient

When the gradient is negative:

- The loss decreases when the weight increases.
- We should increase the weight.
- The weight moves towards the minimum.

Example:

If the gradient is -5, the weight should increase.

## 6. Gradient Descent Update Rule

The basic update rule is:

w_new = w_old - gradient

However, directly subtracting the gradient can result in very large or very small updates.

Therefore, we introduce the learning rate.

## 7. Learning Rate

The learning rate controls the size of each weight update.

Formula:

w_new = w_old - η × gradient

Where:

- w_new = Updated weight
- w_old = Previous weight
- η (eta) = Learning rate
- gradient = Slope of the loss function

The learning rate is a hyperparameter selected before training.

Common learning rate values:

- 0.1
- 0.01
- 0.001

### Learning Rate Too Large

- Updates become very large.
- The weight may overshoot the minimum.
- Loss may oscillate.
- Training may diverge.

Example: The weight repeatedly jumps from one side of the minimum to the other.

### Learning Rate Too Small

- Updates become very small.
- Loss decreases very slowly.
- Training requires more iterations.
- Computational cost increases.

Example: The model takes thousands of steps to reach a minimum that could be reached much faster.

## 8. Backpropagation vs Gradient Descent

### Backpropagation

- Calculates the gradient for each trainable parameter.
- Uses the chain rule.
- Propagates information backward from the loss through the network.
- Determines how much each parameter contributes to the loss.

### Gradient Descent

- Uses the gradients calculated by backpropagation.
- Updates weights and biases.
- Moves parameters in the direction that reduces loss.

Important:

Backpropagation answers HOW MUCH.

Gradient Descent answers WHAT TO DO WITH IT.

## 9. Weight Update Example

Given:

Old weight = 0.5

Gradient = -0.368

Learning rate = 0.1

Formula:

w_new = w_old - η × gradient

Substitution:

w_new = 0.5 - (0.1 × -0.368)

w_new = 0.5 + 0.0368

w_new = 0.5368

Therefore, the updated weight is approximately 0.537.

Since the gradient is negative, the weight increases.

## 10. How Does a Neural Network Learn?

The complete learning process:

1. Forward Propagation
   - Pass input through the network.
   - Generate predictions.

2. Compute Loss
   - Compare predictions with actual values.
   - Calculate the error.

3. Backpropagation
   - Calculate gradients.
   - Determine the contribution of each parameter to the loss.

4. Update Weights
   - Apply Gradient Descent.
   - Update weights and biases.

This process repeats over multiple training examples and epochs.

## 11. Types of Gradient Descent

There are three main types:

1. Batch Gradient Descent
2. Stochastic Gradient Descent (SGD)
3. Mini-Batch Gradient Descent

The main difference is the number of training examples used to calculate the gradient for each update.

## 12. Batch Gradient Descent

Batch Gradient Descent uses the entire training dataset to calculate the gradient before updating the weights.

Characteristics:

- Uses all training examples.
- One weight update per epoch.
- Stable and consistent gradient.
- Computationally expensive for large datasets.

Example:

If the dataset contains 1,000 examples, all 1,000 examples are processed before one weight update.

Advantages:

- Stable updates.
- Accurate estimate of the overall gradient.
- Smooth convergence with an appropriate learning rate.

Disadvantages:

- Slow for large datasets.
- Requires processing the entire dataset before updating weights.
- Can require significant memory.

## 13. Stochastic Gradient Descent (SGD)

SGD uses only one randomly selected training example to calculate the gradient and update the weights.

Characteristics:

- Uses one example per update.
- Updates weights immediately.
- One epoch produces many updates.
- Training path can be noisy.

Example:

If the dataset contains 1,000 examples, SGD produces 1,000 updates per epoch.

Advantages:

- Fast individual updates.
- Starts learning quickly.
- Can be useful for very large datasets and online learning.

Disadvantages:

- Noisy updates.
- Less stable convergence.
- Individual examples may give misleading gradient directions.

## 14. Mini-Batch Gradient Descent

Mini-Batch Gradient Descent uses a small group of training examples to calculate the gradient before updating weights.

Common batch sizes:

- 32
- 64
- 128
- 256

Example:

If the dataset contains 1,000 examples and the batch size is 32:

Number of updates per epoch = 1000 / 32

Approximately 31 full batches, with one smaller final batch.

Advantages:

- Faster than Batch Gradient Descent for large datasets.
- More stable than pure SGD.
- Supports parallel processing on GPUs.
- Commonly used in deep learning.

Disadvantages:

- Requires selecting a batch size.
- Still has some gradient noise.
- Batch size needs tuning.

## 15. Comparison of Gradient Descent Types

| Feature | Batch GD | SGD | Mini-Batch GD |
|---|---|---|---|
| Examples per update | All | One | Small group |
| Updates per epoch | One | One per example | One per batch |
| Speed per update | Slow | Fast | Fast |
| Stability | Very stable | Noisy | Fairly stable |
| Best use | Small datasets | Large/online learning | Most deep learning tasks |

## 16. Introduction to Advanced Optimizers

### Momentum

- Remembers the direction of previous updates.
- Uses past gradient information.
- Helps smooth the optimization path.
- Can accelerate movement through flat regions.

### Adam Optimizer

Adam stands for Adaptive Moment Estimation.

- Uses historical gradient information.
- Adapts the effective learning rate for individual parameters.
- Reduces the need for manual learning-rate tuning.

Both Momentum and Adam build on the basic Gradient Descent foundation.

## 17. Important Formulas

Gradient Descent:

w_new = w_old - η × gradient

Number of Batch GD updates per epoch:

1

Number of SGD updates per epoch:

Number of training examples

Number of Mini-Batch updates per epoch:

Ceiling (Number of training examples / Batch size)

## 18. Final Learning Summary

- Gradient Descent minimizes the loss function.
- Gradient indicates the direction and steepness of the loss curve.
- Positive gradient means decrease the weight.
- Negative gradient means increase the weight.
- Learning rate controls the update size.
- Backpropagation calculates gradients.
- Gradient Descent updates weights.
- Batch GD uses all examples.
- SGD uses one example.
- Mini-Batch GD uses a small group of examples.
- Momentum and Adam are advanced optimization techniques.

The complete learning cycle is:

Forward Propagation → Loss Calculation → Backpropagation → Weight Update

This process repeats until the model learns to produce better predictions.
