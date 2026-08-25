# AIML Day 17 Notes

## Underfitting, Overfitting, and Decision Tree Hyperparameters

---

## 1. Underfitting

Underfitting occurs when a machine learning model is **too simple to learn the real structure or patterns present in the data**.

A simple example is a student who studies only one page of a 100-page textbook. The student has not learned enough information and therefore performs badly in the examination.

A machine learning model can make the same mistake.

If the model is too simple:

* It cannot capture important patterns.
* It performs badly on training data.
* It also performs badly on new/unseen data.
* The model has high bias.

### Characteristics of Underfitting

* Training accuracy is low.
* Test accuracy is also low.
* Training and test accuracy are usually close.
* The model has insufficient complexity.
* The model fails to learn the actual structure of the data.

### Example

For a Decision Tree with:

**Max Depth = 1**

* Training Accuracy = 72%
* Test Accuracy = 70%

Both accuracies are low and there is only a small gap between them.

This indicates **underfitting**.

The tree is too shallow and does not have enough splits to capture the complexity of the dataset.

---

# 2. Overfitting

Overfitting occurs when a machine learning model is **too complex and memorizes the training data instead of learning the general pattern**.

An example is a student who memorizes every line of a textbook, including irrelevant examples and mistakes. The student may perform perfectly when asked about the exact material but may fail when asked to apply the concepts to a new situation.

A machine learning model can behave in the same way.

If the model is too complex:

* It memorizes the training data.
* It may also learn noise and outliers.
* Training accuracy becomes very high.
* Test accuracy becomes significantly lower.
* The model has high variance.

### Characteristics of Overfitting

* Training accuracy is very high.
* Test accuracy is considerably lower.
* There is a large training-test gap.
* The model is too complex.
* The model does not generalize well to unseen data.

### Example

For a Decision Tree with:

**Max Depth = Unlimited**

* Training Accuracy = 100%
* Test Accuracy = 78%

The 22-point gap indicates overfitting.

The tree has become too complex and has memorized the training data, including noise.

---

# 3. The Sweet Spot

The goal is not to make the model as simple as possible or as complex as possible.

The goal is to find the **right level of complexity**.

This is the sweet spot where:

* Training accuracy is high.
* Test accuracy is high.
* Training and test accuracy are close.
* The model learns the actual structure.
* The model does not memorize noise.
* The model generalizes well to unseen data.

### Example

For a Decision Tree with:

**Max Depth = 4**

* Training Accuracy = 93%
* Test Accuracy = 91%
* Gap = 2 percentage points

This is a good example of a well-generalized model.

The tree learns the real structure of the dataset without tightly fitting individual observations.

---

# 4. Comparing Different Tree Depths

The same dataset and algorithm can produce very different results when only the tree depth changes.

| Max Depth | Training Accuracy | Test Accuracy | Result       |
| --------- | ----------------: | ------------: | ------------ |
| 1         |               72% |           70% | Underfitting |
| 4         |               93% |           91% | Sweet Spot   |
| Unlimited |              100% |           78% | Overfitting  |

### Depth = 1

* Very shallow tree.
* Very simple decision boundary.
* Large crude regions.
* Many points are misclassified.
* Both training and test performance are low.
* Indicates underfitting.

### Depth = 4

* Learns the general structure.
* Decision boundary is smoother and more sensible.
* Training and test accuracy are both high.
* Small training-test gap.
* Good generalization.

### Unlimited Depth

* Tree continues splitting until training examples can be isolated.
* Decision boundary becomes very complex and jagged.
* Model memorizes training data.
* Training accuracy can reach 100%.
* Test accuracy decreases.
* Indicates overfitting.

---

# 5. Decision Tree Hyperparameters

Hyperparameters are settings that control how a machine learning model is built.

For Decision Trees, hyperparameters act as **control knobs** that determine the complexity of the tree.

The major hyperparameters covered today are:

1. Max Depth
2. Min Samples Split
3. Min Samples Leaf
4. Max Features
5. Criterion

---

# 6. Max Depth

`Max Depth` specifies the maximum number of levels a Decision Tree can grow from the root node to a leaf node.

Every additional level allows:

* More questions.
* More splits.
* More specific regions.
* Greater model complexity.

### Effect of Max Depth

#### Max Depth = 1 or 2

* Tree stops very early.
* Produces large and crude regions.
* May misclassify many points.
* Model may underfit.

#### Max Depth = 20+ or None

* Tree can become very deep.
* May create tiny regions.
* Can isolate individual training points.
* Can memorize noise.
* Model may overfit.

#### Max Depth = 3–6

* Often provides a useful starting range.
* Can capture general structure.
* May provide a good balance between simplicity and complexity.

### Practical Approach

Start with values such as:

* 2
* 4
* 6
* 8

Observe the test accuracy and choose a depth that gives good generalization.

Start with `Max Depth = 3 or 4`, then increase gradually.

Stop increasing it when test accuracy stops improving or begins to decrease.

### Important Point

`Max Depth` is usually the **first hyperparameter to tune** because it has a major effect on the complexity of a Decision Tree.

---

# 7. Min Samples Split

`Min Samples Split` specifies the minimum number of data points a node must contain before the node is allowed to split.

If a node contains fewer samples than this threshold, it will not split further and becomes a leaf.

### Example

Suppose:

```text
min_samples_split = 10
```

A node needs at least 10 samples before it can be considered for splitting.

### Low Min Samples Split

Example:

```text
min_samples_split = 2
```

* Almost any node can split.
* Tree can grow deeper.
* Small regions can be created.
* More sensitive to noise.
* Can lead to overfitting.

### High Min Samples Split

Example:

```text
min_samples_split = 50
```

* Only large nodes can split.
* Tree stops earlier in sparse regions.
* Produces broader and more general regions.
* If set too high, it may cause underfitting.

### Purpose

`Min Samples Split` prevents the tree from making decisions based on very small groups of observations.

It provides statistical caution by requiring sufficient evidence before allowing another split.

---

# 8. Min Samples Leaf

`Min Samples Leaf` specifies the minimum number of data points that must be present in a final leaf node.

Even if a split is allowed by `Min Samples Split`, the split will be blocked if either resulting child would contain fewer samples than the specified minimum.

### Low Min Samples Leaf

Example:

```text
min_samples_leaf = 1
```

* A leaf can contain only one data point.
* Creates very small prediction regions.
* Can memorize individual observations.
* Increases the risk of overfitting.

### High Min Samples Leaf

Example:

```text
min_samples_leaf = 20
```

* Every final region must contain at least 20 samples.
* Produces broader and smoother regions.
* Reduces sensitivity to individual observations.
* If too high, small but genuine patterns may be removed.
* Can lead to underfitting.

### Purpose

`Min Samples Leaf` ensures that every final prediction region has enough observations to support the prediction.

---

# 9. Min Samples Split vs Min Samples Leaf

These two hyperparameters work together.

### Min Samples Split

Controls whether a node is allowed to **split**.

### Min Samples Leaf

Controls the minimum number of samples that must remain in each **final region** after splitting.

Therefore:

```text
Min Samples Split → Controls entry into splitting
Min Samples Leaf  → Controls minimum final region size
```

Both can be used to control overfitting.

---

# 10. Max Features

`Max Features` controls how many feature columns the Decision Tree considers when searching for a split.

Instead of considering every available feature at each split, the tree can consider only a subset.

### Max Features = None

The tree considers all available features.

Advantages:

* Every feature is available.
* The best split can be selected from all columns.

Possible disadvantage:

* Dominant features may be repeatedly selected.
* Less diversity between trees when used in ensemble methods.

### Max Features = sqrt

The tree considers a random subset of features based on the square root of the total number of features.

This creates more variety in the features considered at different nodes.

### Max Features = log2

The tree uses a subset based on the logarithm base 2 of the number of features.

### Importance in Random Forests

`Max Features` becomes especially important in **Random Forests**.

A Random Forest contains many Decision Trees.

Each tree can consider different random subsets of features.

This creates diversity among the trees, which helps the ensemble perform better.

For a single Decision Tree, `sqrt` can be considered a reasonable starting point.

---

# 11. Criterion

`Criterion` is the measure used to evaluate the quality of a candidate split.

It answers:

> How good is this split?

The two important choices covered today are:

* Gini
* Entropy

Both are measures related to impurity.

---

# 12. Gini Impurity

Gini Impurity measures the probability of incorrectly classifying a randomly selected point if it were labeled according to the class distribution in the node.

Formula:

```text
Gini = 1 - Σ pᵢ²
```

where `pᵢ` represents the probability of a sample belonging to class `i`.

### Advantages

* Computationally faster.
* Does not require logarithmic calculations.
* It is the default criterion in `sklearn`'s `DecisionTreeClassifier`.
* Usually produces results similar to Entropy.

---

# 13. Entropy

Entropy is based on information theory.

It uses **Information Gain** to evaluate splits.

Entropy:

* Comes from information theory.
* Rewards splits that create very pure child nodes.
* Uses logarithmic calculations.
* Can be slightly more computationally expensive than Gini.

### Gini vs Entropy

In practice, both often produce very similar results.

The difference in accuracy is usually small.

Therefore:

* Start with Gini.
* Use Entropy if an information-theoretic approach is preferred.
* Do not spend too much time obsessing over this parameter.

---

# 14. Summary of the Five Hyperparameters

| Hyperparameter    | Main Purpose                                             |
| ----------------- | -------------------------------------------------------- |
| Max Depth         | Controls maximum tree depth and overall complexity       |
| Min Samples Split | Controls the minimum samples required before splitting   |
| Min Samples Leaf  | Controls the minimum samples allowed in a leaf           |
| Max Features      | Controls how many features are considered for each split |
| Criterion         | Measures the quality/impurity of candidate splits        |

---

# 15. Direction of Hyperparameter Effects

### Max Depth

Increasing Max Depth:

```text
More complexity → higher overfitting risk
```

Decreasing Max Depth:

```text
Less complexity → higher underfitting risk
```

### Min Samples Split

Increasing Min Samples Split:

```text
Fewer splits → simpler tree → possible underfitting
```

Decreasing Min Samples Split:

```text
More splits → more complexity → possible overfitting
```

### Min Samples Leaf

Increasing Min Samples Leaf:

```text
Larger leaves → smoother boundary → possible underfitting
```

Decreasing Min Samples Leaf:

```text
Smaller leaves → more detailed boundary → possible overfitting
```

### Max Features

More features:

```text
Less randomness per split
```

Fewer features:

```text
More diversity
```

This is particularly useful for ensemble methods such as Random Forest.

### Criterion

Gini and Entropy generally produce similar results.

Criterion is not the primary bias-variance control.

---

# 16. Bias-Variance Trade-off

The underfitting and overfitting problem can be understood using the **bias-variance trade-off**.

## High Bias

High bias is associated with underfitting.

The model:

* Makes strong simplifying assumptions.
* Misses genuine patterns.
* Is too simple.
* Has poor training and test performance.

### Solution

Increase model complexity.

For example:

* Increase Max Depth.
* Allow more useful splits.
* Reduce overly restrictive sample parameters.

---

## High Variance

High variance is associated with overfitting.

The model:

* Is highly sensitive to the training dataset.
* Learns noise and individual observations.
* Changes significantly with small changes in training data.
* Performs very well on training data but poorly on unseen data.

### Solution

Constrain model complexity.

For example:

* Reduce Max Depth.
* Increase Min Samples Split.
* Increase Min Samples Leaf.
* Control the number of features considered.

---

# 17. Training-Test Accuracy Gap

The difference between training accuracy and test accuracy is an important diagnostic.

Before changing hyperparameters, examine this gap.

## Case 1: Both Scores Low

Example:

```text
Training Accuracy = 72%
Test Accuracy = 70%
```

Diagnosis:

```text
Underfitting
```

The model needs more complexity.

---

## Case 2: Large Gap

Example:

```text
Training Accuracy = 100%
Test Accuracy = 78%
```

Diagnosis:

```text
Overfitting
```

The model has too much freedom and needs stronger constraints.

---

## Case 3: Both High and Gap is Small

Example:

```text
Training Accuracy = 93%
Test Accuracy = 91%
```

Diagnosis:

```text
Good Generalization / Sweet Spot
```

The model has learned useful structure without heavily memorizing the training data.

### Key Rule

```text
Both low → Underfitting
Large train-test gap → Overfitting
Both high + small gap → Good generalization
```

---

# 18. Practical Hyperparameter Tuning Workflow

A repeatable tuning process is important.

## Step 1: Establish a Baseline

Train a Decision Tree using default settings.

Record:

* Training accuracy
* Test accuracy

Then determine whether the model is underfitting or overfitting.

---

## Step 2: Tune Max Depth First

Try values such as:

```text
2, 4, 6, 8
```

Compare test accuracy.

Find the depth where test accuracy performs best before declining.

---

## Step 3: Tune Min Samples Split and Min Samples Leaf

After selecting a suitable depth:

* Increase `Min Samples Split`.
* Increase `Min Samples Leaf`.
* Tune them together.
* Observe whether overfitting decreases.

---

## Step 4: Set Max Features

For a single Decision Tree:

```text
sqrt
```

can be a reasonable starting point.

For ensemble methods such as Random Forest, Max Features becomes more important because it controls feature diversity between trees.

---

## Step 5: Consider Criterion Last

Compare:

```text
Gini
Entropy
```

Only after the more important complexity-related parameters have been considered.

---

# 19. Decision Trees and the Broader Machine Learning Landscape

Decision Trees are important because they form the foundation of several powerful machine learning algorithms.

## Decision Tree

* Single tree.
* Easy to interpret.
* Fast to train.
* Can overfit without proper tuning.

It is the basic building block.

## Random Forest

* Contains many Decision Trees.
* Trees use random subsets of data and features.
* Max Features helps create diversity.
* Combining many trees helps reduce variance.

## Gradient Boosted Trees

* Trees are built sequentially.
* Each new tree attempts to correct errors made by previous trees.
* The same fundamental hyperparameter concepts remain important.

Understanding Decision Tree hyperparameters provides a foundation for later learning algorithms such as:

* XGBoost
* LightGBM
* Other tree-based ensemble methods

---

# 20. Common Mistakes When Tuning Decision Trees

## Mistake 1: Evaluating Only Training Data

A training accuracy of 100% may look impressive.

However, it does not tell us how the model performs on unseen data.

Always evaluate both:

```text
Training Performance
Test Performance
```

---

## Mistake 2: Tuning Max Depth in Isolation

Max Depth interacts with:

* Min Samples Split
* Min Samples Leaf

Changing only one parameter without considering the others can produce misleading results.

---

## Mistake 3: Obsessing Over Criterion

Practitioners may spend too much time comparing Gini and Entropy.

The accuracy difference is often small.

More attention should be given to:

* Max Depth
* Min Samples Split
* Min Samples Leaf

---

## Mistake 4: Skipping the Diagnostic Step

Do not randomly try hyperparameter combinations.

First determine:

```text
Underfitting?
        ↓
Need more complexity

Overfitting?
        ↓
Need stronger constraints
```

Read the training-test gap before changing the parameters.

---

# 21. Hyperparameters and Decision Boundaries

Every hyperparameter choice affects the shape of the model's decision boundary.

## Shallow Tree

Example:

```text
Depth = 1–2
```

Characteristics:

* Very few splits.
* Large regions.
* Crude decision boundary.
* Cannot represent complex patterns well.
* Can underfit.

---

## Well-Tuned Tree

Example:

```text
Depth = 4–6
```

Characteristics:

* Captures important structure.
* Decision boundary is detailed enough to model real patterns.
* Does not excessively follow individual noise points.
* Usually provides better generalization.

---

## Overfit Tree

Example:

```text
Depth = Unlimited
```

Characteristics:

* Very complex boundary.
* Jagged and irregular regions.
* Can create tiny regions for individual training observations.
* Memorizes noise.
* Performs poorly on unseen data.

---

# 22. Dataset Size and Hyperparameter Selection

There is no universal best hyperparameter value.

The correct values depend on:

* Dataset size.
* Features.
* Amount of noise.
* Complexity of the underlying pattern.

## Small Datasets

With fewer observations:

* Noise has a larger influence.
* Small groups are less statistically reliable.
* Overfitting risk is higher.

Possible approach:

* Keep Max Depth relatively low.
* Increase Min Samples Split.
* Increase Min Samples Leaf.
* Require more evidence before making splits.

The faculty notes give a practical range of approximately:

```text
Max Depth = 2–4
```

for small datasets.

---

## Large Datasets

With more observations:

* Deeper trees may generalize better.
* Each node can contain enough samples to represent real patterns.
* Higher Max Depth values may be possible.

Min Samples Split can also be higher in absolute terms while still allowing detailed splits.

### Important Point

There is no universal best value.

The appropriate hyperparameter depends on the dataset and the true complexity of the problem.

---

# 23. Cross-Validation

A single train-test split can introduce randomness into hyperparameter tuning.

**Cross-validation** makes evaluation more reliable.

## K-Fold Cross-Validation

The dataset is divided into `K` folds.

Process:

1. Split the dataset into K folds.
2. Train using K-1 folds.
3. Use the remaining fold for evaluation.
4. Rotate the validation fold.
5. Repeat the process.
6. Calculate the average score.

Every data point gets opportunities to be part of both training and validation sets.

The average score across the folds provides a more reliable estimate of generalization performance than relying on a single train-test split.

In Scikit-learn, `cross_val_score` can be used for this purpose.

---

# 24. Important Practical Rules

### Rule 1

Always compare training and test performance.

### Rule 2

Do not assume 100% training accuracy means a good model.

### Rule 3

Use the training-test gap to diagnose the problem.

### Rule 4

Tune `Max Depth` first.

### Rule 5

Use `Min Samples Split` and `Min Samples Leaf` to control overfitting.

### Rule 6

`Max Features` becomes especially important for Random Forests and other ensemble methods.

### Rule 7

Treat `Criterion` as a lower-priority parameter because Gini and Entropy often give similar results.

### Rule 8

There is no universal best hyperparameter value.

### Rule 9

Dataset size affects appropriate hyperparameter choices.

### Rule 10

Use cross-validation when a single train-test split may be unreliable.

---
