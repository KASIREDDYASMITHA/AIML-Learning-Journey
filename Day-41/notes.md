# AIML Day 41 — DVC, AWS S3, FastAPI and Git Hooks

## 1. Introduction

In machine learning projects, we work with source code, datasets, trained models, and deployment applications.

As a project develops, datasets and models may change. We need a way to track these changes, share artifacts, and reproduce experiments.

The main tools discussed today are:

- Git
- DVC
- AWS S3
- FastAPI
- Git hooks

## 2. What Is DVC?

DVC stands for Data Version Control.

It is an open-source tool used to version and manage large files in machine learning projects, including datasets, model files, and pipeline artifacts.

Git is suitable for source code and small text files. Large datasets and model files are often managed with DVC instead of being committed directly to Git.

### Example 1: Dataset versioning

A crop recommendation project uses a dataset containing nitrogen, phosphorus, potassium, temperature, humidity, pH, rainfall, and crop labels.

If the dataset changes, DVC can help track the version used by an experiment.

### Example 2: Model versioning

A phishing detection project trains a model using Logistic Regression. Later, a new model is trained with updated data.

DVC can track the different model artifacts and help retrieve the version required for a particular experiment.

## 3. Git vs. DVC

### Git

- Tracks source code and project configuration.
- Records changes through commits.
- Supports collaboration through repositories such as GitHub.
- Normally does not store large datasets and model files efficiently.

### DVC

- Tracks versions of datasets and model artifacts.
- Stores metadata in files that can be tracked by Git.
- Can use local or remote storage for the actual artifacts.
- Helps retrieve the artifacts corresponding to a particular project version.

**Important:** Git and DVC complement each other; DVC does not replace Git.

## 4. How DVC Tracks Data and Models

When a file is added using DVC, DVC creates metadata and tracks the artifact through its cache and storage system.

For example:

```bash
dvc add data/iris.csv
dvc add models/iris_model.pkl
```

These commands normally create `.dvc` metadata files for the corresponding artifacts.

Git should track the source code, DVC metadata, and relevant project configuration. The large artifact contents are managed by DVC.

## 5. What Is a DVC Remote?

A DVC remote is a storage location used to store and retrieve DVC-managed artifacts.

Remote storage can be hosted on a supported cloud service or another supported storage system.

Examples include:

1. Amazon S3
2. Other DVC-supported cloud or remote storage systems

### Local storage

Artifacts are stored on the local machine or in local DVC cache storage.

Example: a developer trains a model and keeps its artifact on their computer.

### Remote storage

Artifacts are stored in a shared remote location.

Example: a team stores a dataset and model artifact in an AWS S3 bucket so authorized team members can retrieve them.

## 6. AWS S3 and DVC

Amazon S3 is an object storage service. A bucket can be used as a remote storage destination for DVC.

The general workflow is:

1. Create an S3 bucket.
2. Configure AWS credentials securely.
3. Install the DVC S3 support package.
4. Configure the bucket as a DVC remote.
5. Push DVC-tracked artifacts to the remote.
6. Pull the required artifacts on another machine.

Install the required packages:

```bash
pip install "dvc[s3]"
```

Initialize DVC in a Git repository:

```bash
git init
dvc init
```

Add a remote:

```bash
dvc remote add -d myremote s3://YOUR-BUCKET-NAME/aiml-day41
```

Replace the placeholder with the real bucket name.

Push tracked artifacts:

```bash
dvc push
```

Download the artifacts:

```bash
dvc pull
```

**Security:** Do not place AWS access keys or secret keys in Python source code, Git commits, or public GitHub repositories. Use an approved credential provider, environment configuration, or an IAM role with least-privilege permissions.

## 7. Important DVC Commands

### `dvc add`

Tracks a file or directory with DVC.

```bash
dvc add data/iris.csv
```

### `dvc push`

Uploads locally available, DVC-tracked artifacts to the configured remote.

```bash
dvc push
```

### `dvc pull`

Downloads the artifacts required by the current DVC metadata from the configured remote.

```bash
dvc pull
```

### `dvc status`

Checks whether tracked files have changed relative to their recorded state.

```bash
dvc status
```

### `dvc remote list`

Displays configured DVC remotes.

```bash
dvc remote list
```

## 8. Local vs. Remote Storage

| Local storage | Remote storage |
|---|---|
| Stored on the local machine | Stored at a configured remote location |
| Useful for local development | Useful for sharing and collaboration |
| May not be available to teammates | Can be accessed by authorized teammates |
| Can be lost if the machine fails and no backup exists | Provides a shared location, but access controls and backups still matter |

Example: a developer trains a model locally, then pushes the artifact to S3 so a teammate can pull it.

## 9. What Is FastAPI?

FastAPI is a Python web framework used to build APIs.

In machine learning, a trained model can be exposed through an API. Another application can send input features and receive a prediction.

### Example 1: Phishing detection

An application sends email features to a prediction endpoint. The API returns the predicted class.

### Example 2: Crop recommendation

An application sends soil and weather measurements. The API returns a crop recommendation generated by the trained model.

## 10. Basic FastAPI Workflow

1. Train a machine learning model.
2. Save the model artifact.
3. Load the saved artifact in the API application.
4. Define a prediction endpoint.
5. Receive input data.
6. Pass the input to the model.
7. Return the prediction as a response.

A FastAPI application can be run using Uvicorn:

```bash
uvicorn day41_dvc_fastapi_demo:app --reload
```

If the application starts successfully, open:

```text
http://127.0.0.1:8000/docs
```

This page provides interactive API documentation.

## 11. What Are Git Hooks?

Git hooks are scripts that Git can execute when particular Git events occur.

They can help automate checks and enforce development practices.

Examples:

- A pre-commit hook can run formatting or lightweight tests.
- A pre-push hook can run tests before pushing commits to a remote repository.

Hooks do not automatically validate every model or promote a model. The checks must be configured explicitly.

## 12. Model Testing and Promotion

A model should be evaluated before it is approved for deployment.

A possible workflow is:

1. Train the model.
2. Evaluate it on appropriate validation or test data.
3. Compare its metrics against the project's acceptance criteria.
4. Approve the model if it satisfies those criteria.
5. Deploy or promote the approved version.

For classification, possible metrics include accuracy, precision, recall, and F1-score.

For regression, possible metrics include MAE, RMSE, and R².

**Important:** Passing tests does not automatically mean a model is suitable for production. Data quality, model performance, security, and deployment requirements must also be checked.

## 13. Complete Workflow

```text
Source Code + Dataset
        |
        v
Git tracks source code
DVC tracks data and model artifacts
        |
        v
Train the Machine Learning Model
        |
        v
Evaluate the Model
        |
        v
Save and Version the Model
        |
        v
DVC Push to Remote Storage
        |
        v
FastAPI Serves Predictions
```

AWS S3 can act as the DVC remote. Git hooks can automate selected checks during development.



