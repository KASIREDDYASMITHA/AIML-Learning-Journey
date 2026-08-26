# Day 18 - Decision Trees: Hyperparameter Tuning and Generalisation

## 1. Decision Trees vs. The Broader Machine Learning Landscape

Decision Trees are not only useful as standalone models. They are also the foundation for some powerful machine learning algorithms.

### Decision Tree

A Decision Tree is a single tree-based model.

Characteristics:

* Interpretable
* Fast to train
* Easy to understand
* Can overfit without proper hyperparameter tuning
* Acts as a building block for more advanced tree-based algorithms

A Decision Tree can become very complex if it is allowed to grow without restrictions.

---

### Random Forest

Random Forest is an ensemble method that uses many Decision Trees.

Characteristics:

* Uses multiple trees
* Each tree is trained using a random subset of the data and features
* `Max Features` becomes an important parameter for controlling diversity
* The predictions of multiple trees are combined
* The ensemble helps reduce variance

The diversity between trees is one of the reasons Random Forest is powerful.

---

### Gradient Boosted Trees

Gradient Boosted Trees also use multiple Decision Trees, but they are built sequentially.

Each new tree tries to correct the errors made by the previous trees.

Characteristics:

* Trees are built one after another
* Each tree focuses on correcting previous errors
* The same Decision Tree hyperparameters are relevant
* Understanding Decision Tree hyperparameters provides a foundation for advanced algorithms such as XGBoost and LightGBM

### Important Point

The concepts learned today, such as:

* Max Depth
* Min Samples Split
* Min Samples Leaf
* Max Features

transfer directly to more advanced tree-based algorithms.

---

# 2. Common Mistakes When Tuning Decision Trees

There are several common mistakes that should be avoided while tuning Decision Trees.

## Mistake 1: Evaluating Only on Training Data

A training accuracy of 100% may look impressive, but it does not tell us how well the model performs on unseen data.

A model can memorise the training data and still perform poorly on new data.

Therefore:

* Training accuracy should be checked.
* Test accuracy should also be checked.
* The difference between training and test performance should be examined.

Always evaluate both training and test performance.

---

## Mistake 2: Tuning Max Depth in Isolation

Max Depth is an important hyperparameter, but it should not always be tuned independently.

It interacts with:

* Min Samples Split
* Min Samples Leaf

Changing only Max Depth without considering the other hyperparameters can produce misleading results.

Therefore, these parameters should be considered together when controlling overfitting.

---

## Mistake 3: Obsessing Over Criterion

Decision Trees commonly use:

* Gini
* Entropy

The difference in accuracy between them is often small.

Spending too much time comparing Gini and Entropy is usually less useful than properly tuning:

* Max Depth
* Min Samples Split
* Min Samples Leaf

Therefore, Criterion should generally be considered later during tuning.

---

## Mistake 4: Skipping the Diagnostic Step

Randomly trying different hyperparameter combinations is inefficient.

Before changing hyperparameters:

1. Check training accuracy.
2. Check test accuracy.
3. Calculate or observe the training-test gap.
4. Decide whether the model is underfitting or overfitting.
5. Change the hyperparameters in the appropriate direction.

### Important Rule

Read the training-test gap first, then decide what to change.

---

# 3. Connecting Hyperparameters to the Decision Boundary

Every hyperparameter setting can change the shape of the Decision Tree's decision boundary.

Understanding this relationship is important because it helps us understand what the model is actually learning.

---

## Shallow Tree - Depth = 1 to 2

A shallow Decision Tree has very few splits.

The decision boundary contains only a small number of straight-line cuts.

Characteristics:

* Large regions share the same prediction.
* The boundary is crude.
* The model is fast.
* It cannot capture complicated patterns.
* It often performs poorly on complex datasets.

This is associated with **underfitting**.

### Simple idea

Too little complexity → too simple boundary → underfitting.

---

## Well-Tuned Tree - Depth = 4 to 6

A well-tuned Decision Tree has enough depth to capture the important structure in the data.

The decision boundary becomes a stepped approximation of the actual class boundary.

Characteristics:

* Captures real patterns.
* Ignores individual noise points.
* Boundary is reasonably smooth.
* Generalises well to unseen data.
* Training and test performance are usually close.

This represents good generalisation.

### Simple idea

Balanced complexity → meaningful boundary → good generalisation.

---

## Overfit Tree - Unlimited Depth

When the tree is allowed to grow without sufficient restrictions, it can become extremely complex.

The decision boundary becomes a chaotic and jagged maze.

Characteristics:

* Very small prediction regions
* Can create a separate region for individual training points
* Memorises training data
* Sensitive to noise
* Fragile when new data is introduced
* Performs very well on training data but poorly on unseen data

This is associated with **overfitting**.

### Simple idea

Too much complexity → complicated boundary → overfitting.

---

# 4. Effect of Dataset Size on Hyperparameter Choice

There is no single universal value for Decision Tree hyperparameters.

The correct values depend on:

* Amount of data
* Features
* Complexity of the underlying pattern
* Noise in the dataset

The same Decision Tree can behave differently on small and large datasets.

---

# 5. Small Datasets

When the dataset contains fewer observations, noise can have a much larger influence.

For example, a node containing only three data points may not provide enough statistical evidence for a reliable split.

### Recommended approach for small datasets

Keep:

* `Max Depth` relatively low
* `Min Samples Split` higher
* `Min Samples Leaf` higher

A practical range mentioned in the class is:

### Max Depth

Keep Max Depth around:

```text
2 - 4
```

### Min Samples Split and Min Samples Leaf

Increase these values more aggressively.

The purpose is to make sure that each split and prediction region is supported by enough data.

### Why?

Small datasets have a higher risk of overfitting.

A very deep tree can easily memorise individual observations instead of learning the actual pattern.

---

# 6. Large Datasets

Large datasets contain many more observations.

Because each node can contain enough data points, the model can sometimes support deeper trees without immediately overfitting.

### Characteristics

* Higher Max Depth can be used.
* More detailed patterns can be captured.
* Min Samples Split can be higher in absolute terms.
* Fine-grained splits can still be possible.

For example:

```text
Min Samples Split = 20 to 50
```

can still allow meaningful splits when the dataset is large.

### Important Point

The correct hyperparameter value depends on the dataset.

There is no universal "best" value.

The right setting depends on:

* Data size
* Features
* Noise
* Complexity of the actual pattern

The training-test gap remains an important diagnostic regardless of dataset size.

---

# 7. Cross-Validation

Evaluating hyperparameters using only one train-test split can introduce randomness into tuning decisions.

Different train-test splits can sometimes produce different results.

Cross-validation helps make the evaluation more reliable.

---

## How Cross-Validation Works

In K-fold cross-validation:

1. The dataset is divided into K folds.
2. The model is trained using K-1 folds.
3. The remaining fold is used for evaluation.
4. The process is repeated by changing the fold used for evaluation.
5. The scores from all folds are averaged.

### Example

Suppose we use:

```text
K = 5
```

The dataset is divided into 5 parts.

For each iteration:

```text
4 folds → Training
1 fold  → Testing
```

This process is repeated so that every fold gets a chance to act as the test fold.

Finally:

```text
Average of all K scores
```

is calculated.

---

## Why Cross-Validation Is Useful

Cross-validation provides a more reliable estimate of generalisation performance than depending on a single train-test split.

It reduces the effect of randomness caused by one particular split.

For smaller datasets, a single train-test split may not be reliable enough.

In Scikit-learn, `cross_val_score` can be used for cross-validation.

---

# 8. Practical Decision Tree Tuning Workflow

A systematic tuning process is better than randomly trying hyperparameter values.

## Step 1 - Establish a Baseline

First, create a Decision Tree using the default settings.

Then record:

* Training accuracy
* Test accuracy

Next, diagnose the model.

Ask:

```text
Is the model underfitting?
Is the model overfitting?
Is the model already generalising well?
```

---

## Step 2 - Tune Max Depth First

Max Depth should be the first major hyperparameter to tune.

Try values such as:

```text
2
4
6
8
```

Record the test accuracy for each value.

The goal is to identify the depth where test accuracy reaches its highest point before beginning to decline.

### Key idea

Increase complexity gradually.

Do not immediately choose a very deep tree.

---

## Step 3 - Tune Min Samples Split and Min Samples Leaf

After selecting a suitable Max Depth, tune:

* `Min Samples Split`
* `Min Samples Leaf`

These can help reduce overfitting, especially in sparse regions of the feature space.

They should be considered together because:

* Min Samples Split controls whether a node is allowed to split.
* Min Samples Leaf controls the minimum number of observations allowed in a final leaf.

---

## Step 4 - Set Max Features

For a single Decision Tree:

```text
sqrt
```

is presented as a reasonable default.

When working with ensemble methods such as Random Forest, Max Features becomes much more important because it controls feature diversity between trees.

---

# 9. Important Tuning Order

The recommended tuning order is:

```text
1. Max Depth
2. Min Samples Split
3. Min Samples Leaf
4. Max Features
5. Criterion
```

Max Depth should be tuned first because it has a major effect on model complexity.

Min Samples Split and Min Samples Leaf should then be considered together.

Max Features becomes particularly important when moving toward ensemble methods.

Criterion should generally be considered last.

---

# 10. Training-Test Gap as a Diagnostic Tool

The difference between training accuracy and test accuracy provides an important signal about model behaviour.

---

## Case 1 - Both Scores Are Low

Example:

```text
Training Accuracy ≈ 72%
Test Accuracy ≈ 70%
```

The scores are both low and there is only a small gap.

### Diagnosis

The model is **underfitting**.

The model is too simple and needs more complexity.

### Possible direction

Allow deeper or more flexible splits.

---

## Case 2 - Large Training-Test Gap

Example:

```text
Training Accuracy = 100%
Test Accuracy ≈ 78%
```

There is a large gap:

```text
100% - 78% = 22%
```

### Diagnosis

The model is **overfitting**.

It has too much freedom and is memorising the training data.

### Possible direction

Constrain model complexity.

---

## Case 3 - Both Scores Are High and Close

Example:

```text
Training Accuracy ≈ 93%
Test Accuracy ≈ 91%
```

The gap is:

```text
93% - 91% = 2%
```

### Diagnosis

This represents a good model.

The model has:

* High training performance
* High test performance
* Small training-test gap
* Good generalisation

This is the desired situation.

---

# 11. Decision Boundary and Model Complexity

The complexity of the Decision Tree directly affects the shape of its decision boundary.

### Underfitting

```text
Low complexity
      ↓
Simple boundary
      ↓
Cannot capture real patterns
```

### Well-Tuned Model

```text
Balanced complexity
      ↓
Boundary captures real structure
      ↓
Good generalisation
```

### Overfitting

```text
Very high complexity
      ↓
Jagged and complicated boundary
      ↓
Memorises noise
      ↓
Poor generalisation
```

---

# 12. Important Concepts to Remember

## Underfitting

Underfitting occurs when the model is too simple.

The model:

* Learns too little from the training data.
* Performs poorly on training data.
* Performs poorly on new data.

---

## Overfitting

Overfitting occurs when the model becomes too complex.

The model:

* Learns the training data extremely well.
* Can memorise noise and individual observations.
* Performs poorly on unseen data.

---

## Generalisation

Generalisation means that the model performs well not only on training data but also on unseen data.

A good model should learn the real structure of the data rather than memorising individual training examples.

---

# 13. Key Hyperparameters Recap

## Max Depth

Controls the maximum depth of the tree.

Main purpose:

* Controls model complexity.
* First hyperparameter to tune.
* Has a major impact on the bias-variance trade-off.

---

## Min Samples Split

Controls the minimum number of data points required in a node before the node can be split.

Main purpose:

* Prevents splitting very small and unreliable groups.
* Helps control overfitting.

---

## Min Samples Leaf

Controls the minimum number of data points that must exist in a final leaf.

Main purpose:

* Prevents extremely small prediction regions.
* Helps create smoother and more reliable regions.
* Helps reduce overfitting.

---

## Max Features

Controls how many feature columns are considered when finding a split.

Main purpose:

* Controls feature diversity.
* Becomes especially important for ensemble methods such as Random Forest.

---

## Criterion

Determines how the quality of a candidate split is measured.

Common choices:

```text
Gini
Entropy
```

Both measure impurity in different ways.

Gini is the default in Scikit-learn's `DecisionTreeClassifier` and is computationally faster because it does not require logarithm calculations.

In practice, Gini and Entropy often produce very similar results.

---

# 14. Decision Tree Hyperparameter Direction

A useful way to remember the effect of hyperparameters is:

### Increase complexity

```text
More depth
More splits
Smaller leaf sizes
More freedom
        ↓
Higher overfitting risk
```

### Reduce complexity

```text
Less depth
Fewer splits
Larger leaf sizes
More restrictions
        ↓
Higher underfitting risk
```

The goal is to find the balance between these two extremes.

---

# 15. Tomorrow's Learning

The next class will move from theory to practical implementation.

Topics planned for tomorrow:

### Decision Tree Implementation

A `DecisionTreeClassifier` will be implemented using Scikit-learn on a real dataset.

The hyperparameters discussed today will be applied directly in code.

---

### Visualising the Tree and Decision Boundary

The Decision Tree structure and its resulting decision boundary will be visualised.

This will help understand how different hyperparameter choices change the model.

---

### Complete Classification Evaluation

The evaluation toolkit will include:

* Accuracy
* Confusion Matrix
* Precision
* Recall
* F1 Score

The class will focus on understanding when each metric is useful.

---
