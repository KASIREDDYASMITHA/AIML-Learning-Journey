# AIML Day 31 - MLflow and Experiment Tracking

## 1. Machine Learning Project Organization

A Machine Learning project should be organized
properly so that it is easy to understand,
maintain, test, and share.

Jupyter Notebooks are useful for experimentation.
However, a complete ML project should also
contain organized Python files, documentation,
and dependency information.

A typical ML project contains:

- Python source code
- Jupyter Notebooks
- README file
- Requirements file
- Dataset
- Model files
- Experiment tracking information

### Example

A machine learning project can have the
following structure:

project/
    notebooks/
    src/
    models/
    data/
    README.md
    requirements.txt

## 2. Converting Notebooks into Proper Repositories

Jupyter Notebooks are useful for writing and
executing code step by step.

However, when a project becomes larger,
we should organize the code into separate files.

A proper repository makes it easier to:

- Understand the project.
- Reuse code.
- Debug errors.
- Collaborate with others.
- Maintain the project.
- Track changes using Git and GitHub.

### Important Files

1. README.md

The README file explains the purpose of
the project, its requirements, and how
to run it.

2. requirements.txt

This file contains the Python libraries
needed to run the project.

3. Python files

Python files contain the actual program
and reusable code.

4. Notebooks

Notebooks can be used for data exploration,
experimentation, and visualization.

## 3. Machine Learning Experimentation

In Machine Learning, we cannot decide that
a model is the best without experimentation.

We need to train and evaluate models using
appropriate data and evaluation metrics.

Different models may produce different
results on the same dataset.

### Example 1

Train a Logistic Regression model and
evaluate its accuracy.

### Example 2

Train a Decision Tree model on the same
dataset and compare its performance.

We can compare the models using:

- Accuracy
- Precision
- Recall
- F1-score

The results help us understand how
different models perform.

A model with higher accuracy is not
automatically the best model for every
problem. We must consider the problem
and the relevant evaluation metrics.

## 4. MLflow

MLflow is an open-source platform used
to manage the Machine Learning lifecycle.

It helps us track experiments, parameters,
metrics, and trained models.

MLflow makes it easier to compare
different Machine Learning experiments.

### Main Features of MLflow

1. Experiment Tracking
2. Model Management
3. Model Evaluation
4. Model Deployment Support

### Experiment Tracking

Experiment tracking means recording
the details of Machine Learning experiments.

We can record:

- Model name
- Model parameters
- Evaluation metrics
- Trained model
- Experiment results

### Example

Suppose we train two models:

Model 1: Logistic Regression

Model 2: Decision Tree

We can record their parameters and
evaluation metrics using MLflow.

We can then compare the recorded
experiments instead of relying on memory.

## 5. MLflow Experiment Tracking

MLflow provides functions to record
information about Machine Learning runs.

Important functions:

### mlflow.set_experiment()

Creates or selects an experiment.

### mlflow.start_run()

Starts a new experiment run.

### mlflow.log_param()

Records a parameter.

### mlflow.log_metric()

Records an evaluation metric.

### mlflow.log_model()

Stores a trained model.

### mlflow.log_artifact()

Stores a file generated during an experiment.

## 6. MLflow Tracking

MLflow can be used with local tracking
or a remote tracking server.

### Local Tracking

Experiments can be stored on the local
computer.

For example, MLflow can store experiment
information in a local mlruns directory.

### Remote Tracking

MLflow can also connect to a remote
tracking server.

This allows experiment information
to be stored and accessed remotely.

A remote tracking server needs to be
configured before it can be used.

## 7. DagsHub

DagsHub is a platform for managing
Machine Learning projects.

It supports collaboration and provides
tools for managing ML experiments.

It can integrate with GitHub and MLflow.

DagsHub can be used to manage code,
data, and experiment information.

### Example

1. Create a machine learning project.
2. Store the code in a GitHub repository.
3. Connect the project to DagsHub.
4. Configure MLflow tracking.
5. Record and compare experiments.

DagsHub can provide hosted experiment
tracking, depending on the project setup.

## 8. Importance of Experiment Tracking

Experiment tracking is useful because:

1. It records model parameters.
2. It stores evaluation metrics.
3. It helps compare experiments.
4. It improves reproducibility.
5. It helps organize model development.
6. It makes it easier to understand
   previous experiments.

## 9. Practical Implementation

In today's practical program, we use
the Iris dataset from Scikit-learn.

We train two models:

1. Logistic Regression
2. Decision Tree Classifier

For each model, we record:

- Model parameters
- Accuracy
- Precision
- Recall
- F1-score
- Trained model

MLflow stores the experiment information
so that we can inspect and compare
the results.
