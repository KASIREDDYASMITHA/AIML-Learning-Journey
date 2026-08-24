# Day 16 — Decision Trees: Information Gain, Recursion, and Hyperparameters

## From Entropy to the Full Decision Tree Algorithm

Today we moved from the concept of **Entropy** to understanding how a Decision Tree actually selects splits, builds itself recursively, handles numerical columns, creates decision boundaries, and controls its complexity using hyperparameters.

---

# 1. Information Gain

Information Gain measures how much the entropy/disorder decreases after performing a split.

The goal of a Decision Tree is to find the split that produces the **maximum reduction in entropy**.

### Formula

```text
IG = H(parent) - H(after split)
```

For multiple child nodes:

```text
IG = H(parent) - Σ (|child| / |parent|) × H(child)
```

Where:

* `H(parent)` = Entropy before the split
* `H(child)` = Entropy of each child node
* `|child|` = Number of samples in the child
* `|parent|` = Number of samples in the parent
* `|child| / |parent|` = Weight of that child
* `Σ` = Sum over all child nodes

### Main Idea

```text
Higher Information Gain
        ↓
Larger reduction in entropy
        ↓
Better split
```

At every node, the Decision Tree tries possible splits and selects the split with the **highest Information Gain**.

### Important Cases

If the children become perfectly pure:

```text
IG = Full Parent Entropy
```

If the split does not change the disorder:

```text
IG = 0
```

Therefore:

> The higher the Information Gain, the better the split.

---

# 2. Why Do We Use Weighted Entropy?

After splitting a parent node into child nodes, we need to calculate the entropy after the split.

We should **not simply average the entropy of all children equally**.

Instead, we calculate a **weighted average**, where each child's entropy is multiplied by the fraction of samples that went into that child.

### Formula

```text
Weighted Entropy
= Σ (child size / parent size) × child entropy
```

### Why?

Suppose:

* Child A contains only 1 sample.
* Child B contains 9 samples.

Giving both children equal importance would be misleading.

The child containing 9 samples represents much more of the dataset, so it should have a larger influence on the final entropy.

Therefore:

> Weighting by group size gives a more accurate representation of the disorder after the split.

---

# 3. Simple Average vs Weighted Average

Suppose:

```text
H(Child A) = 0.0
H(Child B) = 0.991
```

## Method 1 — Simple Average

```text
Simple Average
= (0.0 + 0.991) / 2
= 0.496
```

If parent entropy is:

```text
H(parent) = 0.971
```

Then:

```text
IG = 0.971 - 0.496
   = 0.475
```

This makes the split appear relatively strong.

But this is misleading because Child A and Child B do not contain the same number of samples.

---

## Method 2 — Weighted Average

Suppose:

```text
Child A = 1 sample
Child B = 9 samples
Parent = 10 samples
```

Then:

```text
Weighted Entropy
= (1/10 × 0.0) + (9/10 × 0.991)

= 0 + 0.8919

≈ 0.892
```

Therefore:

```text
IG = 0.971 - 0.892
   = 0.079
```

This correctly shows that the split did not improve the disorder very much.

### Conclusion

Simple averaging treats:

```text
1 sample = 9 samples
```

which is incorrect.

Weighted averaging gives more importance to larger groups.

Therefore:

> Weighted entropy is the correct way to calculate the entropy after a split.

---

# 4. Information Gain on Our Dataset

Consider a parent node containing:

```text
4 Yes
4 No
```

Therefore:

```text
Total = 8 samples
```

The parent contains an equal number of Yes and No examples, so it is completely disordered.

### Parent Entropy

```text
H(parent) = 1.0
```

This is the maximum entropy for a binary classification problem.

---

## Split: Age > 32

After splitting:

### Left Child

```text
4 No
0 Yes
```

This child is perfectly pure.

```text
H(left) = 0
```

### Right Child

```text
4 Yes
0 No
```

This child is also perfectly pure.

```text
H(right) = 0
```

---

## Weighted Entropy After the Split

```text
H(after split)
= (4/8 × 0) + (4/8 × 0)

= 0
```

Therefore:

```text
IG = H(parent) - H(after split)

IG = 1.0 - 0

IG = 1.0
```

### Result

```text
Information Gain = 1.0
```

This is the **maximum possible Information Gain** for this binary case.

The split changed:

```text
Completely disordered parent
            ↓
Two perfectly pure children
```

Therefore, no other split can improve the disorder more than this.

This mathematically explains why **Age > 32** is an excellent first split for this dataset.

---

# 5. Recursion — How the Decision Tree Builds Itself

A Decision Tree is built using the same split-selection process repeatedly.

The tree does not make only one split.

Instead:

```text
Parent Dataset
      ↓
Find Best Split
      ↓
Create Child Nodes
      ↓
For each child:
    Find Best Split Again
      ↓
Create More Child Nodes
      ↓
Repeat
```

This repeated process is called **recursion**.

### Recursive Idea

At each node:

1. Look at the current subset of data.
2. Calculate possible splits.
3. Calculate Information Gain for the splits.
4. Select the split with the highest Information Gain.
5. Divide the data into child nodes.
6. Repeat the same process on each child node.
7. Stop when a stopping condition is reached.

Therefore:

> A Decision Tree builds itself by recursively applying the same split-selection logic to smaller and smaller subsets of the data.

---

# 6. Numerical Columns — Finding the Best Threshold

For categorical columns, splitting can be relatively intuitive.

Example:

```text
Colour = Red / Blue / Green
```

But numerical columns contain continuous values.

Example:

```text
Salary
25000
32000
40000
48000
58000
62000
75000
85000
```

We cannot simply say:

```text
Split on Salary
```

We need to decide:

```text
Salary > ?
```

The `?` is called the **threshold**.

---

# 7. Searching for the Best Threshold

For a numerical feature, the Decision Tree considers possible threshold values.

For every candidate threshold:

1. Split the dataset.
2. Calculate the entropy of the child nodes.
3. Calculate weighted entropy.
4. Calculate Information Gain.
5. Compare it with other thresholds.
6. Select the threshold with the highest Information Gain.

### Example Dataset

| Salary | Label |
| -----: | ----- |
| 25,000 | No    |
| 32,000 | No    |
| 40,000 | No    |
| 48,000 | No    |
| 58,000 | Yes   |
| 62,000 | Yes   |
| 75,000 | Yes   |
| 85,000 | Yes   |

A possible split is:

```text
Salary > 53,000
```

This separates:

```text
Salary <= 53,000
        ↓
4 No
```

and

```text
Salary > 53,000
        ↓
4 Yes
```

Both children are perfectly pure.

Therefore:

```text
H(parent) = 1.0
H(children) = 0
IG = 1.0
```

So:

> Salary > 53,000 gives the maximum Information Gain for this dataset.

It is an equally perfect split, just like:

```text
Age > 32
```

---

# 8. What Does a Split Actually Do to Feature Space?

A Decision Tree split can be visualised geometrically.

Suppose we have two features:

```text
Age
Salary
```

These can be represented as axes in a feature space.

Each data point is placed according to its feature values.

For example:

```text
Age → X-axis
Salary → Y-axis
```

A split creates a boundary in this feature space.

---

# 9. Example: Age > 32

Suppose the dataset contains:

```text
Lower Age + Lower Salary → No
Higher Age + Higher Salary → Yes
```

The split:

```text
Age > 32
```

creates a vertical boundary in the feature space.

Conceptually:

```text
Age <= 32          Age > 32
   No                 Yes
```

The feature space is divided into two regions.

Every point in the left region receives one prediction, and every point in the right region receives another prediction.

Therefore:

> Every Decision Tree split creates a boundary in feature space.

---

# 10. Each New Split Creates Smaller Regions

After the first split, another split can be applied to one of the resulting regions.

For example:

```text
Original Feature Space
        ↓
First Split
        ↓
Two Rectangular Regions
        ↓
Second Split
        ↓
Smaller Rectangular Regions
```

Each additional split cuts an existing region into smaller regions.

The final regions correspond to the leaf nodes of the Decision Tree.

---

# 11. Hypercubes in Feature Space

With two features, the regions created by Decision Tree splits can be visualised as rectangles.

With more features, these regions become higher-dimensional shapes called **hypercubes** or hyperrectangular regions.

The main idea is:

```text
Feature space
     ↓
Splits create regions
     ↓
Each region corresponds to a prediction
```

For a new data point, the Decision Tree determines which region the point falls into.

The prediction associated with that region is then returned.

Therefore:

> A Decision Tree can be understood as dividing feature space into regions and assigning a prediction to each region.

---

# 12. Hyperparameters in Decision Trees

Hyperparameters are settings that control how the Decision Tree grows.

They are chosen before training and are not directly learned from the training data.

Important Decision Tree hyperparameters include:

1. `max_depth`
2. `min_samples_split`
3. `min_samples_leaf`
4. `max_features`
5. `criterion`

These parameters control the complexity of the tree and help reduce overfitting.

---

# 13. Hyperparameter 1 — Max Depth

## Problem: Overfitting

If a Decision Tree is allowed to grow without any limit, it can continue splitting until the training data is almost perfectly memorised.

A very deep tree can:

```text
Fit training data extremely well
        ↓
Memorise noise
        ↓
Perform poorly on unseen data
```

This is called **overfitting**.

---

## What is Max Depth?

`max_depth` controls the maximum number of levels the Decision Tree is allowed to grow.

For example:

```text
max_depth = 3
```

means the tree can have at most 3 levels of decisions from the root to a leaf.

### Deep Tree

```text
max_depth = None
```

Can create a very deep tree.

Result:

```text
Complex tree
↓
May memorise training data
↓
Higher risk of overfitting
```

### Shallow Tree

```text
max_depth = 3
```

Result:

```text
Simpler tree
↓
Better generalisation
↓
Lower risk of overfitting
```

However, if the tree is made too shallow, it may fail to learn important patterns.

This is called **underfitting**.

Therefore:

> `max_depth` is one of the most important parameters for controlling Decision Tree complexity.

---

# 14. Hyperparameter 2 — Min Samples Split

`min_samples_split` specifies the minimum number of samples required in a node before that node can be split.

For example:

```text
min_samples_split = 5
```

means a node must contain at least 5 samples before the algorithm is allowed to split it.

If a node contains fewer than 5 samples:

```text
No further split
```

### Why is this useful?

A node containing only a few samples may represent noise rather than a meaningful pattern.

Increasing `min_samples_split`:

```text
Fewer splits
↓
Simpler tree
↓
Less overfitting
```

### Main Idea

```text
Min Samples Split
        ↓
Controls where splitting can start
```

---

# 15. Hyperparameter 3 — Min Samples Leaf

`min_samples_leaf` specifies the minimum number of samples that must be present in a leaf node.

For example:

```text
min_samples_leaf = 5
```

means every final leaf must contain at least 5 samples.

This prevents the tree from creating very small leaves.

### Effect of Increasing It

```text
Larger minimum leaf size
        ↓
Larger leaf regions
        ↓
Smoother decision boundary
        ↓
Lower risk of overfitting
```

### Difference Between Min Samples Split and Min Samples Leaf

```text
min_samples_split
        ↓
Controls whether a node is allowed to split

min_samples_leaf
        ↓
Controls how small the resulting leaf can be
```

Simple way to remember:

> `min_samples_split` controls where splitting starts.

> `min_samples_leaf` controls how small the final groups can become.

---

# 16. Hyperparameter 4 — Max Features

`max_features` controls how many features/columns the algorithm considers when searching for the best split at a node.

Instead of considering every feature, the algorithm can consider only a subset.

This introduces randomness and prevents the tree from always depending on the same dominant feature.

Common choices include:

```text
sqrt(n_features)
log2(n_features)
```

where:

```text
n_features = total number of input features
```

### Why is this useful?

It can:

```text
Reduce dominance of one feature
        ↓
Introduce randomness
        ↓
Create more diverse trees
```

This idea becomes especially important when working with tree ensembles such as **Random Forests**.

---

# 17. Hyperparameter 5 — Criterion

`criterion` specifies how the Decision Tree evaluates the quality of a split.

Two common criteria are:

### Entropy

Entropy measures disorder.

Using entropy, the tree chooses splits using **Information Gain**.

```text
criterion = "entropy"
```

### Gini Impurity

Gini Impurity is another mathematical measure of disorder/impurity.

```text
criterion = "gini"
```

Both approaches are used to find good splits.

### General Difference

```text
Entropy
→ Information-theoretic measure
→ Uses Information Gain

Gini
→ Impurity-based measure
→ Usually slightly faster
```

Both can produce similar Decision Trees on many datasets.

---

# 18. Decision Tree Hyperparameters — Quick Reference

| Hyperparameter      | What It Controls                            | Effect of Increasing                                  |
| ------------------- | ------------------------------------------- | ----------------------------------------------------- |
| `max_depth`         | Maximum depth of tree                       | Simpler tree, less overfitting, possible underfitting |
| `min_samples_split` | Minimum samples required to split a node    | Fewer splits, smoother tree                           |
| `min_samples_leaf`  | Minimum samples allowed in a leaf           | Larger leaf regions, smoother boundary                |
| `max_features`      | Number of features considered at each split | More randomness, less dependence on one feature       |
| `criterion`         | How split quality is measured               | Controls Entropy vs Gini                              |

---

# 19. How the Complete Decision Tree Algorithm Works

The complete process can now be understood as follows:

```text
Start with the complete dataset
          ↓
Calculate parent entropy
          ↓
Consider possible features
          ↓
For each feature:
    consider possible splits
          ↓
Calculate child entropies
          ↓
Calculate weighted child entropy
          ↓
Calculate Information Gain
          ↓
Choose split with maximum Information Gain
          ↓
Split the dataset
          ↓
Repeat the same process recursively
          ↓
Check stopping conditions / hyperparameters
          ↓
Create leaf nodes
          ↓
Assign predictions
```

For numerical features:

```text
Feature
   ↓
Try candidate thresholds
   ↓
Calculate IG for every threshold
   ↓
Choose threshold with maximum IG
```

---

# 20. Stopping the Tree

A Decision Tree does not have to keep splitting forever.

It stops when conditions such as the following are reached:

* Maximum depth has been reached.
* There are not enough samples to split.
* A resulting leaf would contain too few samples.
* The node is already pure.
* No useful split remains.

Hyperparameters help control these stopping conditions.

---

# 21. Overfitting in Decision Trees

A Decision Tree is powerful but can easily overfit.

### Without restrictions

```text
Very deep tree
       ↓
Many small regions
       ↓
Memorises training examples
       ↓
Very high training accuracy
       ↓
Poor performance on unseen data
```

### With suitable restrictions

```text
Controlled depth
       ↓
Reasonable number of splits
       ↓
Larger and more meaningful regions
       ↓
Better generalisation
```

Important parameters for controlling overfitting include:

```text
max_depth
min_samples_split
min_samples_leaf
max_features
```

---

# 22. Important Example From Today's Class

Our dataset had:

```text
4 Yes
4 No
```

Parent entropy:

```text
H(parent) = 1.0
```

Using:

```text
Age > 32
```

we obtained:

```text
Left child  → 4 No, 0 Yes
Right child → 4 Yes, 0 No
```

Therefore:

```text
H(left) = 0
H(right) = 0
```

Weighted entropy:

```text
= (4/8 × 0) + (4/8 × 0)
= 0
```

Information Gain:

```text
IG = 1.0 - 0
   = 1.0
```

Therefore:

```text
Age > 32
→ Perfect split
→ Maximum Information Gain
```

Similarly, for the numerical feature:

```text
Salary > 53,000
```

the split also produced perfectly pure groups:

```text
4 No
4 Yes
```

Therefore:

```text
IG = 1.0
```

So both:

```text
Age > 32
Salary > 53,000
```

can produce equally perfect splits for this particular dataset.

