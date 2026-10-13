
# Day 44 - Introduction to Deep Learning

## 1. Introduction to Deep Learning

Deep Learning is a subfield of Machine Learning that uses neural networks with multiple layers to learn patterns from data.

It is inspired by the structure and working principles of biological neurons in the human brain.

Deep Learning is particularly useful for complex data such as:
- Images
- Audio
- Text
- Video

Examples:
1. Recognizing cats and other objects in images.
2. Understanding speech and generating text.

---

## 2. History of Artificial Intelligence

### 1956 - Beginning of Artificial Intelligence

In the summer of 1956, researchers gathered at Dartmouth College and explored the possibility of describing and simulating human intelligence using machines.

This event is considered an important milestone in the history of Artificial Intelligence.

### First AI Winter - 1974

Early AI systems could solve limited problems but could not fulfill many ambitious expectations.

As progress fell short of expectations, funding decreased and researchers left the field. This period became known as the first AI winter.

### Second AI Winter - 1987

Expert systems became popular during the 1980s.

Expert systems use predefined rules and human expertise to solve problems in specific domains.

Limitations:
- Difficult and expensive to maintain.
- Limited ability to generalize.
- Performance can fail when situations fall outside predefined rules.

These limitations contributed to another period of reduced interest and funding.

---

## 3. Why Early AI Struggled

Three major requirements were missing or insufficient:

### 1. Data
Models need enough examples to learn useful patterns.

### 2. Compute
Training complex models requires sufficient computational power.

### 3. Algorithms
Reliable methods were needed to train deep neural networks effectively.

The ideas behind neural networks existed earlier, but these three factors limited their practical success.

---

## 4. What Traditional Machine Learning Does Well

Traditional Machine Learning works well for many structured-data problems.

Common tasks include:

- Classification: predicting a category.
- Regression: predicting a numerical value.
- Clustering: grouping similar data points.

Examples:
1. Classification: identifying whether an email is spam.
2. Regression: estimating a delivery time.

Traditional ML often depends on selecting and preparing suitable input features.

---

## 5. Feature Engineering

Feature engineering is the process of selecting, extracting, or transforming useful input variables for a Machine Learning model.

For image, audio, and text problems, identifying useful features manually can be difficult.

For example:
1. Image recognition may require identifying edges, shapes, and textures.
2. Text classification may require extracting useful words or numerical text representations.

Deep Learning can learn useful representations automatically from data, reducing the need for manually designed features.

---

## 6. Biological Neuron

A biological neuron is a fundamental information-processing cell in the nervous system.

The lecture describes four main stages:

1. Signals arrive through dendrites.
2. Synapses influence the strength of incoming signals.
3. The cell body, or soma, integrates the signals.
4. The neuron generates an electrical response when the relevant conditions are met.

The axon carries signals away from the cell body toward other cells.

These biological ideas inspired the design of artificial neural networks.

---

## 7. Five Computational Ideas in a Neuron

### 1. Multiple Inputs
A neuron receives signals from multiple sources.

### 2. Weights
Each input has an associated strength or importance.

### 3. Summation
The inputs are combined into a total.

### 4. Threshold or Activation
The neuron determines how to respond to the combined signal.

### 5. Forward Output
The resulting signal is passed to the next stage.

---

## 8. Biological Neuron to Artificial Neuron

| Biological Component | Artificial Neuron |
|---|---|
| Dendrites | Inputs |
| Synaptic strength | Weights |
| Cell body | Weighted sum |
| Threshold or response mechanism | Activation function |
| Axon | Output |

An artificial neuron performs mathematical operations on input values to produce an output.

---

## 9. Artificial Neuron

An artificial neuron receives inputs, multiplies them by weights, adds a bias, and applies an activation function.

Let the inputs be:

x1, x2, x3

Let their weights be:

w1, w2, w3

Let the bias be b.

The weighted sum is:

z = x1*w1 + x2*w2 + x3*w3 + b

The output is:

y = activation(z)

Here:
- x represents an input.
- w represents its associated weight.
- b represents the bias.
- z represents the weighted sum plus bias.
- y represents the neuron's output.

---

## 10. Weights

Weights determine how strongly individual inputs influence a neuron's calculation.

A larger positive weight increases the contribution of an input, while a negative weight reduces the weighted sum when the input is positive.

Weights are adjusted during model training.

Example 1:
If x = 2 and w = 3, the weighted contribution is 2*3 = 6.

Example 2:
If x = 2 and w = -3, the weighted contribution is 2*(-3) = -6.

---

## 11. Bias

Bias is an additional learnable parameter added to the weighted sum.

Formula:

z = sum(xi*wi) + b

Bias allows the model to shift the activation response independently of the input values.

Example 1:
If the weighted sum is 4 and the bias is 2, then z = 6.

Example 2:
If the weighted sum is 4 and the bias is -5, then z = -1.

Weights and bias are generally learned during training.

---

## 12. Activation Functions

An activation function transforms the weighted sum into a neuron's output.

### A. Step Function

The step function produces a binary output.

For a threshold of zero:

f(z) = 1 if z >= 0
f(z) = 0 if z < 0

Example 1:
If z = 3, the output is 1.

Example 2:
If z = -2, the output is 0.

### B. Sigmoid Function

Formula:

sigmoid(z) = 1 / (1 + exp(-z))

It maps a real-valued input to a value between 0 and 1.

Example 1:
If z = 0, sigmoid(z) = 0.5.

Example 2:
If z = 2, sigmoid(z) is approximately 0.881.

Sigmoid outputs can be interpreted as probabilities in appropriately designed models, but this interpretation depends on the model and training setup.

### C. ReLU Function

ReLU means Rectified Linear Unit.

Formula:

ReLU(z) = max(0, z)

Example 1:
If z = -4, the output is 0.

Example 2:
If z = 5, the output is 5.

ReLU is widely used in hidden layers of neural networks.

---

## 13. Perceptron

A perceptron is a basic artificial neuron used for binary classification.

It calculates a weighted sum and applies an activation function.

A single perceptron can learn a linear decision boundary.

Limitation:
A single perceptron cannot solve every classification problem. It cannot correctly separate data that is not linearly separable.

Example 1:
The AND logic gate can be represented by a single perceptron.

Example 2:
The XOR logic gate cannot be represented by a single standard perceptron.

---

## 14. Neural Networks and Multiple Layers

A neural network contains interconnected artificial neurons arranged in layers.

### Input Layer
Receives the input features.

### Hidden Layers
Learn intermediate representations from the input data.

### Output Layer
Produces the final prediction.

For image recognition, the learned representations may progress from simple visual patterns to more complex structures.

A simplified example:
1. Early layers learn edge-like patterns.
2. Later layers learn shapes and object parts.

Multiple layers allow neural networks to learn more complex patterns than a single perceptron.

---

## 15. Why Deep Learning Became Successful

### 1. Large Datasets
The internet made enormous amounts of data available.

### 2. GPUs
Graphics Processing Units can perform many mathematical operations in parallel, making neural network training more practical.

### 3. Improved Training Algorithms
Advances in initialization, activation functions, and regularization improved the training of deep networks.

---

## 16. Backpropagation

Backpropagation is an algorithm used to calculate how the loss changes with respect to a neural network's parameters.

These gradients help an optimizer update weights and biases during training.

A simplified training cycle:
1. Perform a forward pass to calculate predictions.
2. Calculate the loss.
3. Use backpropagation to calculate gradients.
4. Update parameters using an optimizer.
5. Repeat over training iterations.

Backpropagation is an important mechanism for training multilayer neural networks.

---

## 17. Improvements in Deep Learning

### Weight Initialization
Choosing suitable initial parameter values can help training begin effectively.

### ReLU Activation
ReLU is computationally simple and often helps gradients propagate more effectively than sigmoid in deep hidden layers.

### Dropout
Dropout randomly disables selected neuron outputs during training to help reduce overfitting.

---

## 18. AlexNet and the Rise of Deep Learning

In 2012, AlexNet achieved a major breakthrough in the ImageNet Large Scale Visual Recognition Challenge.

The lecture compares approximately:
- Classical ML benchmark error rate: 26%.
- AlexNet error rate: 15.3%.

This result demonstrated the effectiveness of deep convolutional neural networks for large-scale image classification.

---

## 19. Important Deep Learning Milestones

According to the lecture:

- 2014: Generative Adversarial Networks (GANs).
- 2016: AlphaGo defeated a world champion in Go.
- 2017: Transformer architecture was introduced.
- 2020: GPT-3 demonstrated large-scale language generation.
- 2022: ChatGPT became widely available.
- 2023: AlphaFold continued to influence biological research.

These milestones demonstrate the expanding applications of modern AI.
