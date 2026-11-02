# AIML Day 51 - Building Networks with Keras

## 1. Introduction

Today's topic is building neural networks using Keras for
binary and multi-class classification.

Previously, we learned about neural network calculations,
weighted sums, weights, biases, activation functions, and
output layers manually.

Keras automates much of this work. We define the model
architecture, and Keras handles the forward pass, training,
and weight updates.

The fundamental mathematical concepts remain the same.

## 2. Important Keras Concepts

### Sequential

Sequential is a model that contains layers arranged in order.

Example:
model = Sequential()

### Dense

Dense is a fully connected neural network layer.
Each neuron connects to every neuron in the next layer.

Example:
Dense(11, activation='sigmoid')

### Activation Function

An activation function is applied to the weighted sum
to produce the neuron's output.

Important activation functions:

1. Sigmoid
   - Produces an output between 0 and 1.
   - Commonly used in binary classification output layers.

2. ReLU
   - Replaces negative values with zero.
   - Commonly used in hidden layers.

3. Softmax
   - Converts output scores into class probabilities.
   - Commonly used for multi-class classification.

### input_dim and input_shape

These specify the expected input dimensions.

Example:
Dense(11, activation='sigmoid', input_dim=11)

The input layer expects 11 features.

## 3. Example 1 - Customer Churn Classification

### Problem Statement

Predict whether a bank customer will leave the bank.

Target variable:
- Exited = 1: Customer leaves.
- Exited = 0: Customer stays.

This is a binary classification problem because there are
two possible output classes.

### Step 1: Remove Unnecessary Columns

RowNumber, CustomerId, and Surname are identifiers rather
than useful predictive features in this example.

Code:

df.drop(
    columns=['RowNumber', 'CustomerId', 'Surname'],
    inplace=True
)

### Step 2: Encode Categorical Features

Neural networks require numerical inputs.

Geography and Gender contain categorical text values.

One-hot encoding converts categories into numerical columns.

Code:

df = pd.get_dummies(
    df,
    columns=['Geography', 'Gender'],
    drop_first=True,
    dtype=int
)

For the standard dataset, this produces 11 input features
after the identifier columns are removed.

### Step 3: Separate Features and Target

X contains the input features.

y contains the target variable.

Code:

X = df.drop(columns=['Exited'])
y = df['Exited']

### Step 4: Split the Dataset

The dataset is divided into training and testing sets.

- Training data is used to learn the model.
- Testing data is used to evaluate its performance.

Code:

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=0
)

The test size of 0.2 means 20% of the data is reserved
for testing.

### Step 5: Scale the Features

StandardScaler transforms features using the mean and
standard deviation calculated from the training data.

Code:

scaler = StandardScaler()

X_train_trf = scaler.fit_transform(X_train)
X_test_trf = scaler.transform(X_test)

Important:
- fit_transform() is used on training data.
- transform() is used on testing data.
- Do not fit the scaler on testing data.

Scaling prevents features with large numerical ranges
from dominating the weighted sums.

### Step 6: Build the Neural Network

Architecture:

Input: 11 features
Hidden layer 1: 11 neurons
Hidden layer 2: 11 neurons
Output layer: 1 neuron

Code:

model = Sequential()

model.add(Dense(11, activation='sigmoid', input_dim=11))
model.add(Dense(11, activation='sigmoid'))
model.add(Dense(1, activation='sigmoid'))

The output layer produces one probability between 0 and 1.

### Step 7: Understand the Parameters

Layer 1:
11 x 11 weights + 11 biases = 132 parameters

Layer 2:
11 x 11 weights + 11 biases = 132 parameters

Output layer:
11 x 1 weights + 1 bias = 12 parameters

Total parameters:
132 + 132 + 12 = 276

All 276 parameters are trainable.

### Step 8: Compile the Model

Code:

model.compile(
    optimizer='Adam',
    loss='binary_crossentropy',
    metrics=['accuracy']
)

Optimizer:
Adam updates the model's weights during training.

Loss:
Binary cross-entropy measures the error in binary
classification predictions.

Metrics:
Accuracy measures the proportion of correct predictions.

### Step 9: Train the Model

Code:

history = model.fit(
    X_train_trf,
    y_train,
    batch_size=50,
    epochs=100,
    verbose=1,
    validation_split=0.2
)

Epoch:
One complete pass through the training dataset.

Batch size:
The number of training examples processed in a batch.

Validation split:
20% of the supplied training data is reserved for
validation during training.

### Step 10: Make Predictions

Code:

y_prob = model.predict(X_test_trf)

The model returns probabilities, not final class labels.

A threshold of 0.5 can convert the probabilities into
binary predictions.

Code:

y_pred = (y_prob >= 0.5).astype(int).ravel()

Example 1:
Probability = 0.82
Predicted class = 1

Example 2:
Probability = 0.23
Predicted class = 0

These examples illustrate thresholding; they are not
actual predictions from a trained model.

### Step 11: Evaluate the Model

Code:

accuracy_score(y_test, y_pred)

Accuracy is the fraction of predictions that match the
actual labels.

The faculty notes show approximately 86% validation
accuracy at the end of the illustrated training run.
Actual results depend on the data and training setup.

### Step 12: Plot Loss and Accuracy

The training history stores loss and accuracy values
for training and validation data.

Important values:

history.history['loss']
history.history['val_loss']
history.history['accuracy']
history.history['val_accuracy']

Loss curves help us observe how model error changes.

Accuracy curves help us observe how prediction
performance changes.

Overfitting warning:
If training loss keeps decreasing while validation loss
starts increasing, the model may be overfitting.

## 4. Example 2 - MNIST Digit Classification

### Problem Statement

Classify handwritten images into digits from 0 to 9.

The MNIST dataset contains 70,000 labelled images.

Each image contains 28 rows and 28 columns of pixel values.

- Training set: 60,000 images.
- Testing set: 10,000 images.
- Pixel values: 0 to 255.
- Number of classes: 10.

This is a multi-class classification problem.

### Step 1: Load the Dataset

Code:

(X_train, y_train), (X_test, y_test) = (
    keras.datasets.mnist.load_data()
)

The dataset is available through Keras.

### Step 2: Normalize Pixel Values

Pixel values range from 0 to 255.

Dividing by 255 converts them into the range 0 to 1.

Code:

X_train = X_train.astype('float32') / 255.0
X_test = X_test.astype('float32') / 255.0

Normalization helps maintain a consistent input scale.

### Step 3: Understand Flatten

Each image has a shape of (28, 28).

A Dense layer needs a one-dimensional feature vector.

Flatten converts each 28 x 28 image into 784 features.

Calculation:

28 x 28 = 784 pixels

Code:

Flatten(input_shape=(28, 28))

### Step 4: Build the Neural Network

Architecture:

Input image: 28 x 28 pixels
Flatten: 784 features
Hidden layer 1: 128 neurons with ReLU
Hidden layer 2: 32 neurons with ReLU
Output layer: 10 neurons with Softmax

Code:

model = Sequential()

model.add(Flatten(input_shape=(28, 28)))
model.add(Dense(128, activation='relu'))
model.add(Dense(32, activation='relu'))
model.add(Dense(10, activation='softmax'))

The output layer contains 10 neurons, one for each digit.

Softmax produces 10 probabilities whose sum is 1.

### Step 5: Compile the Model

Code:

model.compile(
    optimizer='Adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

Sparse categorical cross-entropy is suitable because
the labels are integers from 0 to 9.

Example labels:
2, 5, 7

One-hot encoded labels are not required for this loss.

### Step 6: Train the Model

Code:

history = model.fit(
    X_train,
    y_train,
    epochs=25,
    validation_split=0.2
)

The model trains for 25 epochs.

20% of the supplied training data is used for validation.

### Step 7: Predict the Digit

Code:

y_prob = model.predict(X_test)
y_pred = y_prob.argmax(axis=1)

The model produces 10 probabilities per image.

argmax(axis=1) selects the index of the largest probability.

Example 1:
Probabilities = [0.02, 0.03, 0.80, 0.01, ...]
Predicted digit = 2

Example 2:
Probabilities = [0.01, 0.04, 0.03, 0.75, ...]
Predicted digit = 3

These are illustrative probability examples, not actual
model output.

### Step 8: Evaluate Accuracy

Code:

accuracy_score(y_test, y_pred)

A well-trained MNIST model can often achieve approximately
97% to 98% test accuracy, depending on its configuration.

This is an expected reference range, not a guaranteed result.

### Step 9: Predict One Image

Code:

prediction = model.predict(
    X_test[1].reshape(1, 28, 28)
).argmax(axis=1)

The reshape operation creates a batch containing
one image.

The expected input shape is (1, 28, 28).

## 5. Binary vs Multi-Class Classification

Binary classification:

- Example: Customer churn prediction.
- Number of output neurons: 1.
- Output activation: Sigmoid.
- Loss function: Binary cross-entropy.
- Target: 0 or 1.

Multi-class classification:

- Example: MNIST digit classification.
- Number of output neurons: 10.
- Output activation: Softmax.
- Loss function: Sparse categorical cross-entropy.
- Target: Integer labels from 0 to 9.

The output layer and loss function depend on the problem.

## 6. Important Differences Between the Two Models

Customer Churn:
- Tabular customer data.
- 11 numerical input features in the standard example.
- Two possible classes.
- 100 training epochs.
- Batch size of 50.
- Sigmoid output.

MNIST:
- Grayscale image data.
- 784 input values after flattening.
- Ten possible classes.
- 25 training epochs.
- Default Keras batch size.
- Softmax output.
