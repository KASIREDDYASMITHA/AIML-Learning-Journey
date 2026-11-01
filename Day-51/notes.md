# Day 51: Building Neural Networks with Keras

## 1. Introduction

Today I learned how to build neural networks using Keras for binary and multiclass classification.

In previous lessons, neural network operations were calculated manually. Keras simplifies this process by providing tools to define layers, train models, and make predictions.

The underlying concepts remain the same:
- Weights and biases
- Weighted sums and dot products
- Activation functions
- Output-layer architecture
- Loss functions
- Model training and evaluation

## 2. Important Keras Concepts

### Sequential
Sequential is a model that organizes neural network layers in a linear order.

Example:
```python
from tensorflow.keras.models import Sequential

model = Sequential()
```

### Dense
Dense represents a fully connected neural network layer. Each neuron connects to every neuron in the next layer.

Example:
```python
from tensorflow.keras.layers import Dense

model.add(Dense(11, activation="sigmoid", input_shape=(11,)))
```

### Activation Functions
An activation function is applied to a neuron's weighted sum to produce its output.

Common activation functions:

- **Sigmoid:** Produces an output between 0 and 1. Commonly used in the output layer for binary classification.
- **ReLU:** Returns zero for negative inputs and the input itself for positive inputs. Commonly used in hidden layers.
- **Softmax:** Converts output scores into probabilities that sum to 1. Commonly used for multiclass classification.

### Input Shape
The input shape specifies the number and arrangement of features expected by the model.

Example:
```python
input_shape=(11,)
```

This represents 11 input features.

## 3. Binary Classification: Customer Churn

Customer churn prediction estimates whether a customer will leave a service or remain a customer.

Target labels:
- 0: Customer stays.
- 1: Customer leaves.

Binary classification predicts one of two possible classes.

### Step 1: Remove Unnecessary Columns

Identifiers and names generally do not directly describe the customer's behavior.

The faculty notes remove these columns:
```python
df.drop(
    columns=["RowNumber", "CustomerId", "Surname"],
    inplace=True
)
```

Removing such columns can prevent irrelevant identifiers from being used as predictive features.

### Step 2: Encode Categorical Variables

Machine learning models require numerical inputs. Text categories must therefore be converted into numbers.

One-hot encoding creates separate indicator columns for categorical values.

Example:
```python
df = pd.get_dummies(
    df,
    columns=["Geography", "Gender"],
    drop_first=True
)
```

The faculty notes describe an input layer with 11 features after preprocessing.

### Step 3: Split the Dataset

The dataset is divided into training and testing sets.

```python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=0
)
```

- Training data is used to fit the model.
- Testing data is used to evaluate the trained model.
- `test_size=0.2` reserves 20% of the data for testing.
- `random_state=0` makes the split reproducible for the same input data and environment.

### Step 4: Scale the Features

Features may have different numerical ranges. Scaling helps prevent large-valued features from dominating the weighted sums simply because of their scale.

```python
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()

X_train_trf = scaler.fit_transform(X_train)
X_test_trf = scaler.transform(X_test)
```

The scaler learns its parameters from the training set. The same transformation is then applied to the testing set to avoid data leakage.

### Step 5: Build the Neural Network

The architecture shown in the faculty notes is:

```python
model = Sequential()

model.add(Dense(11, activation="sigmoid", input_dim=11))
model.add(Dense(11, activation="sigmoid"))
model.add(Dense(1, activation="sigmoid"))
```

Layer structure:
1. Input: 11 features.
2. First Dense layer: 11 neurons.
3. Second Dense layer: 11 neurons.
4. Output layer: 1 neuron with sigmoid activation.

The output represents the predicted probability of the positive class.

For the architecture above, the trainable parameter count is:

- First layer: (11 × 11) + 11 = 132
- Second layer: (11 × 11) + 11 = 132
- Output layer: (11 × 1) + 1 = 12
- Total: 276 parameters

Each layer's parameter count includes its weights and biases.

### Step 6: Compile the Model

Compiling configures the optimizer, loss function, and evaluation metrics.

```python
model.compile(
    optimizer="Adam",
    loss="binary_crossentropy",
    metrics=["accuracy"]
)
```

- **Adam:** An optimization algorithm that updates model parameters during training.
- **Binary cross-entropy:** A loss function suited to binary classification with probability outputs.
- **Accuracy:** The proportion of predictions classified correctly.

### Step 7: Train the Model

```python
history = model.fit(
    X_train_trf,
    y_train,
    batch_size=50,
    epochs=100,
    verbose=1,
    validation_split=0.2
)
```

- `batch_size=50`: The model processes up to 50 training examples per batch.
- `epochs=100`: The model can pass through the training data 100 times.
- `validation_split=0.2`: Keras reserves 20% of the supplied training data for validation.

During training, the optimizer adjusts the weights to reduce the loss.

### Step 8: Make Predictions

```python
y_prob = model.predict(X_test_trf)
```

The model returns probabilities rather than final class labels.

A threshold of 0.5 can be used to convert probabilities into binary predictions.

```python
y_pred = (y_prob >= 0.5).astype(int).ravel()
```

The threshold is a decision rule, not a guarantee that the model is well calibrated.

### Step 9: Evaluate the Model

```python
from sklearn.metrics import accuracy_score

accuracy = accuracy_score(y_test, y_pred)
print("Test Accuracy:", accuracy)
```

Test accuracy measures the proportion of testing examples predicted correctly. It should be interpreted alongside other metrics, particularly when the classes are imbalanced.

## 4. Training and Validation Curves

The training history contains loss and accuracy values for each epoch.

Useful history keys:
- `history.history["loss"]`
- `history.history["val_loss"]`
- `history.history["accuracy"]`
- `history.history["val_accuracy"]`

Training and validation curves help identify learning behavior.

### Overfitting

Overfitting occurs when a model learns the training data too closely and performs less effectively on unseen data.

Example 1: Training loss continues decreasing while validation loss increases.

Example 2: Training accuracy is high, but validation accuracy remains noticeably lower.

A growing gap between training and validation performance can indicate overfitting.

## 5. Multiclass Classification: MNIST

MNIST is a dataset of handwritten digit images representing digits from 0 to 9.

The standard dataset contains:
- 60,000 training images.
- 10,000 testing images.
- Each image is 28 × 28 pixels.
- Each label is an integer from 0 to 9.

This is a multiclass classification problem because the model must choose among ten classes.

### Step 1: Load the Dataset

```python
from tensorflow import keras

(X_train, y_train), (X_test, y_test) = (
    keras.datasets.mnist.load_data()
)
```

### Step 2: Normalize Pixel Values

Pixel values range from 0 to 255.

Dividing by 255 converts them into a range from 0 to 1.

```python
X_train = X_train.astype("float32") / 255.0
X_test = X_test.astype("float32") / 255.0
```

Normalization gives the model inputs on a consistent scale.

### Step 3: Flatten the Images

Each image has 28 rows and 28 columns.

The number of pixels is:

28 × 28 = 784

A Flatten layer converts each 28 × 28 image into a one-dimensional vector of 784 values.

```python
from tensorflow.keras.layers import Flatten

model.add(Flatten(input_shape=(28, 28)))
```

### Step 4: Build the Network

The architecture from the faculty notes is:

```python
model = Sequential()

model.add(Flatten(input_shape=(28, 28)))
model.add(Dense(128, activation="relu"))
model.add(Dense(32, activation="relu"))
model.add(Dense(10, activation="softmax"))
```

Layer structure:
1. Flatten: converts the image into 784 input values.
2. Dense layer: 128 neurons with ReLU.
3. Dense layer: 32 neurons with ReLU.
4. Output layer: 10 neurons with Softmax.

Each output neuron corresponds to one digit class.

Softmax produces a probability distribution across the ten classes.

### Step 5: Compile the Model

```python
model.compile(
    optimizer="Adam",
    loss="sparse_categorical_crossentropy",
    metrics=["accuracy"]
)
```

Sparse categorical cross-entropy is appropriate when multiclass targets are represented as integer class labels, such as 0 through 9.

### Step 6: Train the Model

```python
history = model.fit(
    X_train,
    y_train,
    epochs=25,
    validation_split=0.2
)
```

The model trains for up to 25 epochs while validation data helps monitor generalization.

### Step 7: Predict the Digit

```python
y_prob = model.predict(X_test)
y_pred = y_prob.argmax(axis=1)
```

The model produces ten probabilities per image. `argmax` selects the index with the highest probability.

For example, if the predicted probabilities are highest for class 2, the predicted digit is 2.

### Step 8: Evaluate Accuracy

```python
from sklearn.metrics import accuracy_score

accuracy = accuracy_score(y_test, y_pred)
print("Test Accuracy:", accuracy)
```

The faculty notes state that a well-trained MNIST model typically achieves approximately 97–98% test accuracy. This is a reference range, not a guaranteed result for every run.

## 6. Binary vs. Multiclass Classification

| Feature | Binary Classification | Multiclass Classification |
|---|---|---|
| Example | Customer churn | Handwritten digits |
| Number of classes | 2 | 10 |
| Output neurons | 1 | 10 |
| Output activation | Sigmoid | Softmax |
| Loss function | Binary cross-entropy | Sparse categorical cross-entropy |
| Prediction | Apply a threshold | Select the largest probability |

The output architecture and loss function must match the prediction task and label format.

## 7. Important Keras Methods

| Method | Purpose |
|---|---|
| `Sequential()` | Creates a sequential model |
| `Dense()` | Adds a fully connected layer |
| `Flatten()` | Converts image grids into vectors |
| `compile()` | Configures training |
| `fit()` | Trains the model |
| `predict()` | Generates predictions |
| `evaluate()` | Evaluates the model on supplied data |
| `argmax()` | Selects the index of the largest value |

## 8. Plotting Training Curves

Example for plotting training and validation loss:

```python
import matplotlib.pyplot as plt

plt.plot(history.history["loss"], label="Train Loss")
plt.plot(history.history["val_loss"], label="Validation Loss")

plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.title("Training vs Validation Loss")
plt.legend()
plt.show()
```

The same approach can be used to plot training and validation accuracy.
