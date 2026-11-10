# AIML Learning Journey - Day 60
# Forward Propagation, Backpropagation and Gradient Descent

## 1. Introduction

Today I learned how all the important components of neural
network training work together.

The main concepts covered are:

1. Forward Propagation
2. Loss Calculation
3. Backpropagation
4. Gradient Descent
5. Batch Gradient Descent
6. Stochastic Gradient Descent
7. Mini-Batch Gradient Descent

We use the same dataset to understand all three gradient
descent algorithms.

---

## 2. Dataset

We use a dataset containing:

- 5 rows
- 2 input features
- 1 target output

| Row | x1 | x2 | y |
|-----|----|----|---|
| 1 | 1 | 1 | 1.0 |
| 2 | 2 | 1 | 1.8 |
| 3 | 0 | 2 | 0.9 |
| 4 | 1 | 0 | 0.4 |
| 5 | 2 | 2 | 2.5 |

### Starting Weights and Biases

Input-to-hidden layer:

W1 = [0.5, 0.3]

b1 = 0.1

Hidden-to-output layer:

W2 = 0.8

b2 = 0.05

---

## 3. Neural Network Architecture

The neural network contains:

2 Inputs → 1 Hidden Neuron → 1 Output

The hidden neuron uses ReLU activation.

The output neuron uses Linear activation.

### ReLU Activation Function

ReLU stands for Rectified Linear Unit.

Formula:

ReLU(x) = max(0, x)

It returns:
- x, when x is greater than 0.
- 0, when x is less than or equal to 0.

Example 1:

ReLU(5) = 5

Example 2:

ReLU(-3) = 0

### Linear Activation Function

The linear activation function returns the input value
without applying a nonlinear transformation.

Formula:

f(x) = x

---

## 4. Forward Propagation

Forward propagation is the process of passing input data
through the neural network to calculate the predicted output.

### Step 1: Calculate Hidden Layer Input

z1 = (x1 * w1) + (x2 * w2) + b1

### Step 2: Apply ReLU

h = max(0, z1)

### Step 3: Calculate Output

y_predicted = (h * W2) + b2

### Example: Row 1

Given:

x1 = 1
x2 = 1

W1 = [0.5, 0.3]
b1 = 0.1
W2 = 0.8
b2 = 0.05

Hidden layer:

z1 = (1 * 0.5) + (1 * 0.3) + 0.1

z1 = 0.9

ReLU(0.9) = 0.9

Output:

y_predicted = (0.9 * 0.8) + 0.05

y_predicted = 0.77

Therefore, the predicted output is 0.77.

---

## 5. Loss Function

A loss function measures the difference between the actual
output and the predicted output.

The faculty lesson uses squared error for its numerical
calculations.

Formula used for reproducing the results:

Loss = (y - y_predicted)²

Example:

Actual output = 1.0

Predicted output = 0.77

Loss = (1.0 - 0.77)²

Loss = 0.0529

Approximately 0.053.

### Individual Row Losses

| Row | Actual Output | Predicted Output | Loss |
|-----|---------------|------------------|------|
| 1 | 1.0 | 0.77 | 0.053 |
| 2 | 1.8 | 1.17 | 0.397 |
| 3 | 0.9 | 0.61 | 0.084 |
| 4 | 0.4 | 0.53 | 0.017 |
| 5 | 2.5 | 1.41 | 1.188 |

Row 5 has the highest loss.

This means the prediction for Row 5 is much farther
from its actual target than the other predictions.

---

## 6. Average Loss

Average loss gives one value representing the overall
error across the complete dataset.

Formula:

Average Loss = Sum of Individual Losses / Number of Rows

Total Loss:

0.053 + 0.397 + 0.084 + 0.017 + 1.188

Total = 1.739

Number of rows = 5

Average Loss = 1.739 / 5

Average Loss = 0.3478

The objective of training is to reduce the average loss.

---

## 7. Backpropagation

Backpropagation is the process of calculating gradients
by propagating the error backward through the neural network.

It helps determine how much each weight and bias
contributes to the prediction error.

The gradients are calculated using the chain rule.

### Important Gradients

- dW1: Gradient of input-to-hidden weights.
- db1: Gradient of hidden layer bias.
- dW2: Gradient of hidden-to-output weight.
- db2: Gradient of output layer bias.

### Gradient Calculation

Let:

Error = Predicted Output - Actual Output

For the squared error used in the faculty calculations:

dL/dy_predicted = 2 * Error

Output layer:

dW2 = 2 * Error * Hidden Output

db2 = 2 * Error

Hidden layer:

dz1 = 2 * Error * W2 * ReLU Derivative

For positive hidden layer input:

ReLU Derivative = 1

Therefore:

dW1 = dz1 * Input

db1 = dz1

### Row 1 Gradients

dW1 = [-0.368, -0.368]

db1 = -0.368

dW2 = -0.414

db2 = -0.460

### Row 5 Gradients

dW1 = [-3.488, -3.488]

db1 = -1.744

dW2 = -3.706

db2 = -2.180

Observation:

Row 5 produces much larger gradients than Row 1
because its prediction error is much larger.

---

## 8. Gradient Descent

Gradient Descent is an optimization algorithm used to
minimize the loss function.

It updates weights and biases in the direction that
reduces the loss.

### Weight Update Formula

New Weight = Old Weight - Learning Rate * Gradient

w = w - η * dw

Where:

- w = Current weight
- η = Learning rate
- dw = Gradient

The learning rate controls the size of each update.

A very large learning rate can cause overshooting.

A very small learning rate can make training slow.

---

## 9. Batch Gradient Descent

Batch Gradient Descent calculates gradients using
the entire dataset before updating the weights.

### Working

1. Pass all rows through the network.
2. Calculate the gradients for every row.
3. Average all the gradients.
4. Update the weights and biases once.

### Averaged Gradients

dW1 = [-1.133, -1.158]

db1 = -0.675

dW2 = -1.227

db2 = -0.844

### Learning Rate

η = 0.1

### Weight Update Example

W1 = [0.5, 0.3]

New W1:

[0.5, 0.3] - 0.1 * [-1.133, -1.158]

W1 = [0.613, 0.416]

Similarly:

b1 = 0.168

W2 = 0.923

b2 = 0.134

### Result

Initial Average Loss = 0.3478

After One Update = 0.0771

### Key Points

- Uses the complete dataset.
- Performs one update per epoch.
- Produces a more stable gradient.
- Can be slower on very large datasets because it
  waits for the complete dataset before updating.

---

## 10. Stochastic Gradient Descent (SGD)

Stochastic Gradient Descent updates weights immediately
after processing each individual training row.

Instead of calculating the average gradient of all rows,
it uses the gradient of one row at a time.

### Working

1. Take Row 1.
2. Calculate its gradient.
3. Update weights and biases.
4. Move to Row 2 using the updated weights.
5. Repeat until all rows are processed.

For five rows, SGD performs five updates in one epoch.

### Learning Rate

η = 0.1 initially.

The learning rate of 0.1 produces a much worse result
because individual gradients can be large.

Initial Average Loss = 0.3478

After Five Updates = 1.71

### Why Did SGD Become Worse?

- SGD uses individual row gradients.
- It does not average gradients across all rows.
- A row with a large error can produce a large update.
- A large learning rate can cause overshooting.

### Solution

Reduce the learning rate.

New Learning Rate:

η = 0.02

After five updates:

Initial Average Loss = 0.3478

Final Average Loss = 0.0809

### Key Points

- Updates after every individual row.
- Performs more updates per epoch.
- Can learn quickly.
- Individual updates can be noisy.
- Requires an appropriate learning rate.

---

## 11. Mini-Batch Gradient Descent

Mini-Batch Gradient Descent combines the ideas of
Batch Gradient Descent and SGD.

It divides the dataset into smaller groups called batches.

It calculates the average gradient for each batch
and updates the weights after processing that batch.

### Dataset Division

We have five rows and choose a batch size of 2.

Batch 1:

Rows 1 and 2

Batch 2:

Rows 3 and 4

Batch 3:

Row 5

### Working

1. Process Batch 1 and calculate average gradients.
2. Update weights and biases.
3. Process Batch 2 using updated weights.
4. Calculate average gradients and update again.
5. Process Batch 3 and perform the final update.

### Learning Rate

η = 0.02

### Result

Initial Average Loss = 0.3478

After Three Updates = 0.0923

### Key Points

- Divides the dataset into smaller batches.
- Averages gradients within each batch.
- Updates weights after every batch.
- Provides a balance between Batch GD and SGD.
- Commonly used for training neural networks.

---

## 12. Comparison of Three Gradient Descent Algorithms

| Feature | Batch GD | SGD | Mini-Batch GD |
|---------|----------|-----|---------------|
| Data used | Entire dataset | One row | Small group |
| Gradient | Average of all rows | Individual row | Average of batch |
| Updates per epoch | 1 | 5 | 3 |
| Stability | More stable | More variable | Balanced |
| Learning rate in lesson | 0.1 | 0.02 | 0.02 |
| Final loss | 0.0771 | 0.0809 | 0.0923 |

### Main Difference

Batch GD:

Uses all training examples before one update.

SGD:

Uses one training example for each update.

Mini-Batch GD:

Uses a small group of training examples for each update.

---

## 13. Final Results

All three algorithms start with:

Initial Average Loss = 0.3478

| Algorithm | Learning Rate | Updates | Final Average Loss |
|-----------|---------------|---------|--------------------|
| Batch GD | 0.1 | 1 | 0.0771 |
| SGD | 0.02 | 5 | 0.0809 |
| Mini-Batch GD | 0.02 | 3 | 0.0923 |

### Observations

1. Batch GD gives the lowest final loss in this experiment.
2. SGD performs five updates in one epoch.
3. SGD with learning rate 0.1 increases the loss significantly.
4. Reducing SGD learning rate to 0.02 improves the result.
5. Mini-Batch GD provides an intermediate approach.

There is no universal winner. The appropriate algorithm
depends on the dataset, learning rate and training requirements.

---

## 14. Complete Neural Network Training Process

The complete training process consists of:

1. Forward Propagation:
   Calculates predicted outputs.

2. Loss Calculation:
   Measures prediction errors.

3. Backpropagation:
   Calculates gradients for weights and biases.

4. Gradient Combination:
   Combines gradients using Batch GD, SGD or Mini-Batch GD.

5. Weight Update:
   Updates parameters using the learning rate.

6. Repeat:
   Continues training to reduce the loss.

---
