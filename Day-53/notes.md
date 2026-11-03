# Day 53 – Regression with Keras

## 1. Introduction to Regression

Regression is a supervised machine learning technique used to predict continuous numerical values.

Examples:
1. Predicting house prices.
2. Predicting employee salaries.

In classification, the model predicts a category or class.

In regression, the model predicts a numerical value.

Example:

Classification:
- 0 = Not Purchased
- 1 = Purchased

Regression:
- House Price = $351,883
- House Price = $630,402

## 2. House Price Prediction Dataset

In today's class, we worked with a custom house price dataset.

Dataset Information:
- Total Houses: 600
- Input Features: 5
- Target Variable: 1

### Input Features

| Feature | Description |
|---|---|
| sqft | House area in square feet |
| bedrooms | Number of bedrooms |
| age_years | Age of the house |
| distance_km | Distance in kilometres |
| location_score | Location score |

### Target Variable

price – House price in dollars.

Example:

| sqft | bedrooms | age_years | distance_km | location_score | price |
|---|---|---|---|---|---|
| 1850 | 3 | 12 | 8.2 | 6 | 351883 |
| 3100 | 5 | 4 | 3.1 | 9 | 630402 |
| 1200 | 2 | 22 | 14.7 | 4 | 198540 |

The features have different numerical scales.

For example:
- sqft can be in thousands.
- location_score ranges from 1 to 10.

Therefore, feature scaling is important.

## 3. Splitting Features and Target

First, separate the input features and target variable.

```python
X = df.drop(columns=['price'])

y = df['price'].values
```

X represents input features.

y represents the target variable.

### Train-Test Split

```python
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
)
```

- Training Data: 80%
- Testing Data: 20%

## 4. Feature Scaling

StandardScaler is used to standardize the input features.

```python
scaler = StandardScaler()

X_train_trf = scaler.fit_transform(X_train)

X_test_trf = scaler.transform(X_test)
```

Why do we use feature scaling?

Because different features have different numerical ranges.

For example:
- sqft = 1850
- location_score = 6

Scaling helps bring features onto comparable scales.

## 5. Target Scaling

In regression, we also scale the target variable.

```python
y_scaler = StandardScaler()

y_train_trf = y_scaler.fit_transform(
    y_train.reshape(-1, 1)
).flatten()

y_test_trf = y_scaler.transform(
    y_test.reshape(-1, 1)
).flatten()
```

### Why do we scale the target?

House prices can be in hundreds of thousands.

MSE squares the prediction errors.

Large target values can produce very large loss values and gradients during training.

Target scaling helps make training more stable.

### Important Methods

**reshape(-1, 1)**

Converts a one-dimensional array into a two-dimensional column.

**flatten()**

Converts an array into a one-dimensional array.

**inverse_transform()**

Converts scaled values back into their original scale.

## 6. Building the Regression Model Using Keras

```python
model = Sequential()

model.add(Dense(16, activation='relu', input_dim=5))

model.add(Dense(8, activation='relu'))

model.add(Dense(1))
```

### Model Architecture

5 Input Features → 16 Neurons → 8 Neurons → 1 Output Neuron

Explanation:

- Input Layer: 5 features.
- Hidden Layer 1: 16 neurons with ReLU.
- Hidden Layer 2: 8 neurons with ReLU.
- Output Layer: 1 neuron without an explicitly specified activation function.

## 7. Why No Activation Function in the Output Layer?

In regression, we predict continuous numerical values.

Therefore, we generally use a linear output layer.

### Sigmoid

- Restricts output between 0 and 1.
- Useful for binary classification probabilities.
- Not suitable for unrestricted house price prediction.

### Softmax

- Converts outputs into class probabilities.
- The probabilities sum to 1.
- Used in multi-class classification.

### Linear Activation

- Allows the model to produce unrestricted real-valued outputs.
- Suitable for predicting house prices.

```python
model.add(Dense(1))
```

No activation function is specified in this output layer.

Keras therefore uses a linear output by default.

## 8. Model Compilation

```python
model.compile(
    optimizer='Adam',
    loss='mse',
    metrics=['mae']
)
```

### Optimizer – Adam

Adam is an optimization algorithm used to update model weights during training.

### Loss Function – MSE

MSE stands for Mean Squared Error.

It calculates the average squared difference between actual and predicted values.

Formula:

MSE = Average of (Predicted Value - Actual Value)²

### Metric – MAE

MAE stands for Mean Absolute Error.

It calculates the average absolute difference between actual and predicted values.

Formula:

MAE = Average of |Predicted Value - Actual Value|

MAE is easier to interpret because it uses the same unit as the target.

## 9. Model Training

```python
history = model.fit(
    X_train_trf,
    y_train_trf,
    epochs=100,
    batch_size=32,
    verbose=1,
    validation_split=0.2
)
```

Explanation:

- epochs=100: Model trains for 100 epochs.
- batch_size=32: Processes 32 samples per batch.
- verbose=1: Displays training progress.
- validation_split=0.2: Uses 20% of training data for validation.

Important:

We train the model using scaled target values (y_train_trf), not the original house prices.

## 10. Model Prediction

```python
y_pred_scaled = model.predict(
    X_test_trf
).flatten()
```

The predictions are in scaled form.

We need to convert them back into the original price scale.

```python
y_pred = y_scaler.inverse_transform(
    y_pred_scaled.reshape(-1, 1)
).flatten()
```

This converts the predictions back into actual dollar values.

## 11. Model Evaluation

```python
mae = mean_absolute_error(y_test, y_pred)

r2 = r2_score(y_test, y_pred)
```

### MAE – Mean Absolute Error

Measures the average absolute difference between actual and predicted values.

Lower MAE indicates smaller average prediction errors.

### R² Score

R² measures how much variation in the target variable is explained by the model.

A score closer to 1 generally indicates a better fit.
