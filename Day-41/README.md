# AIML Learning Journey — Day 41

## Topics Covered

- Data Version Control (DVC)
- Dataset and model versioning
- Local and remote storage
- AWS S3 as a DVC remote
- `dvc add`, `dvc push`, and `dvc pull`
- FastAPI for serving machine learning models
- Git hooks and automated checks
- Model validation before promotion

## Short Overview

DVC is used to manage versions of large machine learning datasets and model files. Git tracks source code and DVC metadata, while DVC manages the actual data and model artifacts.

AWS S3 can be configured as remote storage for DVC. The commands `dvc push` and `dvc pull` transfer tracked artifacts between local storage and the remote.

FastAPI exposes a trained machine learning model through HTTP endpoints so that applications can request predictions.

Git hooks can automate checks before commits or pushes.

## Practical Program

`day41_dvc_fastapi_demo.py` demonstrates:

1. Creating a sample dataset.
2. Training a machine learning model.
3. Saving the dataset and model artifacts.
4. Serving predictions through FastAPI.

## Important Commands

```bash
pip install dvc dvc[s3] fastapi uvicorn pandas scikit-learn joblib
git init
dvc init
dvc add data/iris.csv
dvc add models/iris_model.pkl
dvc remote add -d myremote s3://YOUR-BUCKET-NAME/aiml-day41
dvc push
dvc pull
```

