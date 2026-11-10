# AIML Learning Journey - Day 60

## Topic: Forward Propagation, Backpropagation and Gradient Descent Algorithms

### Overview
I learned how forward propagation, backpropagation
and different gradient descent algorithms work together to
train a neural network.

The lesson uses one dataset containing five rows, two input
features and one target output.

### Topics Covered

1. Forward Propagation
2. Mean Squared Error (MSE) Loss
3. Backpropagation
4. Gradient Calculation
5. Batch Gradient Descent
6. Stochastic Gradient Descent (SGD)
7. Mini-Batch Gradient Descent
8. Learning Rate
9. Weight and Bias Updates
10. Comparison of Gradient Descent Algorithms

### Neural Network Architecture

2 Inputs → 1 Hidden Neuron (ReLU) → 1 Output (Linear)

### Gradient Descent Comparison

| Algorithm | Learning Rate | Updates per Epoch | Final Average Loss |
|-----------|---------------|-------------------|--------------------|
| Batch GD | 0.1 | 1 | 0.0771 |
| SGD | 0.02 | 5 | 0.0809 |
| Mini-Batch GD | 0.02 | 3 | 0.0923 |

Initial Average Loss: 0.3478


### Key Learning

- Forward propagation calculates predictions.
- Backpropagation calculates gradients.
- Gradient descent updates weights and biases.
- Batch GD uses the entire dataset for one update.
- SGD updates weights after every individual row.
- Mini-Batch GD updates weights after processing small groups.

