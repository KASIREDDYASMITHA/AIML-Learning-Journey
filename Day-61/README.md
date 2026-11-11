# Day 61 – Deep Learning Diagnostics

## Topics Covered

Today I learned about the major problems that occur during neural network training and how gradients behave when they pass through multiple layers.

### Concepts Learned

1. Gradient as a Product
2. Vanishing Gradient
3. Exploding Gradient
4. Dying ReLU
5. Weight Initialization
6. Xavier / Glorot Initialization
7. He Initialization
8. Gradient Clipping
9. Leaky ReLU
10. Introduction to Batch Normalization and Adam Optimizer


### Key Learnings

- Gradients are calculated using the chain rule.
- Repeated multiplication of small values causes vanishing gradients.
- Repeated multiplication of large values causes exploding gradients.
- ReLU neurons with negative inputs have zero gradients.
- Proper weight initialization helps stabilize neural network training.
- Gradient clipping controls excessively large gradients.
- Leaky ReLU allows a small gradient for negative inputs.
