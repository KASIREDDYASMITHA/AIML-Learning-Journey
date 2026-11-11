# Day 61 – Deep Learning Diagnostics
## Vanishing Gradients, Exploding Gradients, and Dying ReLU

## 1. Gradient as a Product

A gradient is not calculated in a single step. It is calculated using the chain rule.

The gradient is a product of multiple local sensitivities along the path from a weight to the loss.

General form:

Gradient = Local Sensitivity 1 × Local Sensitivity 2 × ... × Local Sensitivity n

### Why Does It Matter?

When a neural network has many layers, these values are multiplied repeatedly.

- If the factors are smaller than 1, the gradient becomes smaller.
- If the factors are greater than 1, the gradient becomes larger.
- If any factor is exactly 0, the gradient becomes zero.

This leads to three major problems.

## 2. Vanishing Gradient

Vanishing gradient occurs when gradients become extremely small while propagating backward through a neural network.

### Why Does It Happen?

When multiple small values are multiplied together, the result approaches zero.

For example:

0.5 × 0.5 × 0.5 × 0.5 = 0.0625

As the number of layers increases, the gradient becomes smaller.

### Sigmoid Activation and Vanishing Gradient

The sigmoid activation function is:

Sigmoid(z) = 1 / (1 + e^(-z))

Its derivative is:

Sigmoid'(z) = Sigmoid(z) × (1 - Sigmoid(z))

The maximum derivative of sigmoid is 0.25, which occurs at z = 0.

Every sigmoid layer contributes a factor of at most 0.25 to the gradient chain.

### Example: Four Sigmoid Layers

Starting gradient = 1

Gradient = 1 × 0.25 × 0.25 × 0.25 × 0.25

Gradient = 0.00390625

The gradient becomes 256 times smaller.

### Example: Ten Sigmoid Layers

Gradient = 0.25^10

Gradient ≈ 0.0000009537

The gradient becomes extremely small.

### Effects of Vanishing Gradient

- Early layers receive very small gradients.
- Weight updates become extremely small.
- Early layers learn very slowly or practically stop learning.
- Later layers may continue learning normally.
- Training loss can still decrease even when early layers are not learning effectively.

## 3. Exploding Gradient

Exploding gradient occurs when gradients become extremely large during backpropagation.

### Why Does It Happen?

When local sensitivities are greater than 1, repeated multiplication increases the gradient exponentially.

For example:

2 × 2 × 2 × 2 = 16

As the number of layers increases, the gradient grows rapidly.

### Example: Four Layers

Starting gradient = 1

Weight = 3

Gradient = 1 × 3 × 3 × 3 × 3

Gradient = 81

The gradient becomes 81 times larger.

### Example: Ten Layers

Gradient = 3^10

Gradient = 59049

The gradient becomes extremely large.

### Effects of Exploding Gradient

- Gradients become excessively large.
- Weight updates become very large.
- The model may overshoot the minimum.
- Training becomes unstable.
- The network may fail to learn properly.

### Gradient Descent Update Rule

w_new = w_old - learning_rate × gradient

When the gradient is extremely large, even a small learning rate can produce a very large weight update.

The problem is the gradient magnitude, not necessarily the learning rate.

## 4. Dying ReLU

Dying ReLU occurs when a ReLU neuron continuously produces zero output and receives zero gradient.

### ReLU Activation Function

ReLU(z) = max(0, z)

- If z > 0, output = z.
- If z <= 0, output = 0.

### ReLU Derivative

ReLU'(z) = 1 if z > 0

ReLU'(z) = 0 if z <= 0

For negative inputs, the derivative is exactly zero.

### Example

Suppose:

z = -0.9

ReLU(-0.9) = 0

The neuron produces zero output.

### Why Does a Neuron Die?

During backpropagation:

dL/dz = dL/da × da/dz

For a negative ReLU input:

dL/dz = dL/da × 0

dL/dz = 0

The gradient received by its incoming weights is also zero.

Therefore:

- No gradient reaches the incoming weights.
- No weight update occurs through that neuron.
- The neuron continues producing zero.
- It cannot recover through that zero-gradient path.

## 5. Difference Between the Three Problems

### Vanishing Gradient

- Gradient becomes extremely small.
- Caused by repeated multiplication of small factors.
- Early layers learn very slowly.

### Exploding Gradient

- Gradient becomes extremely large.
- Caused by repeated multiplication of large factors.
- Weight updates become unstable.

### Dying ReLU

- Gradient becomes exactly zero for a neuron with negative ReLU input.
- The gradient path is completely blocked.
- The neuron cannot recover through that path.

## 6. Weight Initialization

Weight initialization means assigning initial values to neural network weights before training begins.

Poor initialization can cause gradient-related problems.

### How Initialization Causes Problems

1. Weights Too Small:
   - Gradients can shrink through layers.
   - Vanishing gradient may occur.

2. Weights Too Large:
   - Gradients can grow uncontrollably.
   - Exploding gradient may occur.
   - Large sigmoid inputs can cause saturation and vanishing gradients.

3. Poorly Placed Weights or Biases:
   - Some ReLU neurons may start with negative pre-activation values.
   - This can contribute to dying ReLU.

## 7. Solutions to Gradient Problems

### A. Xavier / Glorot Initialization

- Designed for sigmoid and tanh activations.
- Helps preserve variance through network layers.
- Reduces the chances of activations and gradients becoming too small or too large.

### B. He Initialization

- Designed for ReLU and its variants.
- Accounts for ReLU setting negative inputs to zero.
- Uses a larger initial weight scale to compensate.

### C. Gradient Clipping

Gradient clipping controls excessively large gradients by limiting their magnitude before applying weight updates.

Rule:

If |gradient| > threshold:

gradient = gradient × (threshold / |gradient|)

It preserves the gradient direction while reducing its magnitude.

Example:

Gradient = 100

Threshold = 10

Clipped gradient = 10

This helps prevent excessively large updates.

### D. Leaky ReLU

Leaky ReLU solves the zero-gradient problem of ReLU for negative inputs by allowing a small nonzero slope.

Leaky ReLU:

f(z) = z if z > 0

f(z) = 0.01 × z if z <= 0

Derivative:

- 1 for positive inputs.
- 0.01 for negative inputs.

Unlike ReLU, Leaky ReLU allows a small gradient to pass through for negative inputs.

## 8. Two Additional Techniques

### Batch Normalization

- Normalizes activations between layers.
- Helps prevent activations from becoming too small or too large.
- Improves training stability.

### Adam Optimizer

- An adaptive optimizer.
- Adjusts effective step sizes during training.
- Can provide additional robustness when gradient scales vary.

These topics will be studied in more detail later.

## 9. Important Formulas

Sigmoid:

Sigmoid(z) = 1 / (1 + e^(-z))

Sigmoid Derivative:

Sigmoid'(z) = Sigmoid(z) × (1 - Sigmoid(z))

Maximum Sigmoid Derivative:

0.25

ReLU:

ReLU(z) = max(0, z)

ReLU Derivative:

1 if z > 0, otherwise 0

Leaky ReLU:

Leaky ReLU(z) = max(0.01 × z, z)

Gradient Descent:

w_new = w_old - learning_rate × gradient

Gradient Clipping:

Clipped Gradient = gradient × (threshold / |gradient|)
