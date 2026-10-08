# Day 39 - ML Model Deployment, Testing and CI/CD


## Topics Learned

Today I learned about:

- ML model creation
- Model packaging
- Model execution
- MLflow Model Registry
- Model Stages
- Staging and Production
- Model artifacts
- FastAPI
- Pydantic request schema
- API endpoints
- API testing
- Registry testing
- Performance testing
- GitHub Actions
- CI/CD pipeline
- Pull Requests
- Branch merging

---

# 1. ML Model Lifecycle

A machine learning model usually goes through different stages before it is used in production.

Basic flow:

Model Creation
        ↓
Model Training
        ↓
Model Evaluation
        ↓
Model Logging
        ↓
Model Registry
        ↓
Staging
        ↓
Testing
        ↓
Production

The purpose of this lifecycle is to make sure that only a properly tested model reaches production.

---

# 2. Model Creation

The first step is to create and train a machine learning model.

Example:

A classification model can be trained using historical data.

The basic process is:

1. Load the dataset
2. Prepare the data
3. Split the data
4. Train the model
5. Evaluate the model
6. Save the model
7. Register the model

Example machine learning models:

- Logistic Regression
- Decision Tree
- Random Forest
- Linear Regression

---

# 3. Model Packaging

After creating the model, the model and its required files need to be packaged properly.

A package can contain:

- Trained model
- Preprocessing information
- Configuration
- Dependencies
- Supporting files

Packaging makes it easier to move the model between development, testing and production environments.

---

# 4. Model Execution

After creating and packaging the model, the model can be executed.

The model receives input data and produces a prediction.

Example:

Input:
Age = 25
Salary = 40000

Model:
Prediction

Output:
Approved

---

# 5. MLflow

MLflow is an open-source platform used to manage the machine learning lifecycle.

It can be used for:

- Experiment tracking
- Logging parameters
- Logging metrics
- Logging models
- Storing artifacts
- Model Registry
- Model version management

MLflow helps track different versions of machine learning models.

---

# 6. MLflow Model Registry

The MLflow Model Registry is used to manage registered machine learning models.

A registered model can have multiple versions.

Example:

Model Name:
EmailPhishingModel

Versions:

Version 1
Version 2
Version 3

Each version can be evaluated before being used in production.

---

# 7. Model Artifacts

Artifacts are files generated during the machine learning process.

Examples:

- Trained model files
- Plots
- Evaluation results
- Data files
- Configuration files

MLflow can store these artifacts along with experiment information.

---

# 8. Staging

Staging means the model is ready for testing but is not yet being used by real production users.

Example:

Model Version 3
        ↓
Staging

The staging model can be tested before production deployment.

---

# 9. Production

Production is the environment where the model is used by real applications or users.

Example:

Model Version 3
        ↓
Production

A model should be moved to production only after successful testing.

---

# 10. Model Promotion

A common model promotion flow is:

Development
     ↓
Staging
     ↓
Testing
     ↓
Production

The model is first placed in staging.

After successful testing, it can be promoted to production.

---

# 11. FastAPI

FastAPI is a Python web framework used for creating APIs.

It is commonly used to expose machine learning models through HTTP endpoints.

Example:

Client
   ↓
API Request
   ↓
FastAPI
   ↓
Machine Learning Model
   ↓
Prediction
   ↓
API Response

---

# 12. app.py

The FastAPI application can contain a prediction endpoint.

Example:

POST /predict

The endpoint receives input data and sends it to the machine learning model.

---

# 13. Pydantic

Pydantic is used for data validation.

FastAPI uses Pydantic models to define the expected request structure.

Example:

class PredictionRequest(BaseModel):
    feature1: float
    feature2: float

This means the API expects feature1 and feature2 as numeric values.

Pydantic helps validate incoming API requests.

---

# 14. API Endpoint

An API endpoint is a URL through which an application can communicate with the model.

Example:

POST /predict

Input:

{
    "feature1": 5.1,
    "feature2": 3.5
}

Output:

{
    "prediction": 1
}

---

# 15. Manual API Testing

API functionality can be tested manually.

A browser can be used to open:

GET /

For POST requests, tools such as:

- Swagger UI
- Postman
- curl

can be used.

FastAPI automatically provides Swagger UI.

Usually it can be accessed through:

/docs

Example:

http://127.0.0.1:8000/docs

---

# 16. Types of Testing

Three important types of testing discussed today are:

1. Registry Testing
2. Performance Testing
3. API Testing

---

# 17. Registry Testing

Registry testing checks whether the correct model version is registered and available.

Things to verify:

- Model name
- Model version
- Model stage
- Model availability
- Model artifacts

Example:

EmailPhishingModel
Version 3
Stage: Staging

---

# 18. API Testing

API testing checks whether the API works correctly.

Things to test:

- Endpoint availability
- Request validation
- Correct prediction response
- Invalid input handling
- HTTP status codes

Example:

POST /predict

Valid input should return a prediction.

Invalid input should return an appropriate validation error.

---

# 19. Performance Testing

Performance testing checks how efficiently the API responds.

Important measurements include:

- Response time
- Number of requests handled
- Latency
- Throughput
- Resource usage

Example:

If an API takes 5 seconds for every request, its performance may be poor.

If it takes 100 milliseconds for a normal request, performance is much better.

---

# 20. Staging to Production

After testing is successfully completed, the model can be promoted.

Flow:

Model
 ↓
Staging
 ↓
Testing
 ↓
Testing Successful
 ↓
Production

The important idea is:

Do not directly move an untested model to production.

---

# 21. GitHub Actions

GitHub Actions is used to automate workflows.

It can be used for:

- Running tests
- Installing dependencies
- Checking code
- Building applications
- Deploying applications
- Implementing CI/CD

---

# 22. CI/CD

CI means Continuous Integration.

CD means Continuous Delivery or Continuous Deployment.

A simple CI/CD flow is:

Developer writes code
        ↓
Push code to GitHub
        ↓
GitHub Actions starts
        ↓
Install dependencies
        ↓
Run tests
        ↓
If tests pass
        ↓
Continue deployment process

---

# 23. GitHub Actions Workflow File

GitHub Actions workflow files are stored inside:

.github/workflows/

Example:

.github/workflows/ci.yml

The YAML file defines the automation process.

---

# 24. Workflow Trigger

A GitHub Actions workflow can run when code is pushed.

Example:

on:
  push:

It can also run when a Pull Request is created or updated.

Example:

on:
  pull_request:

---

# 25. Pull Request

A Pull Request is used to propose changes before merging them into another branch.

Typical workflow:

Create feature branch
        ↓
Write code
        ↓
Push branch
        ↓
Create Pull Request
        ↓
GitHub Actions runs tests
        ↓
Review
        ↓
Merge

---

# 26. Branch Merge

After successful testing and review, the feature branch can be merged into the main branch.

Example:

feature branch
       ↓
Pull Request
       ↓
main branch

---

# 27. Complete CI/CD Flow

A simplified complete workflow is:

Code
 ↓
Git Push
 ↓
GitHub
 ↓
GitHub Actions
 ↓
Install Dependencies
 ↓
Run Tests
 ↓
Tests Pass
 ↓
Build / Deploy
 ↓
Production

If tests fail:

Code
 ↓
GitHub Actions
 ↓
Tests Fail
 ↓
Deployment stops

This prevents broken code from being deployed.

---

# 28. Important Commands

Install dependencies:

pip install -r requirements.txt

Start FastAPI:

uvicorn app:app --reload

Run tests:

pytest

---

# 29. Important URLs

FastAPI application:

http://127.0.0.1:8000

Swagger API documentation:

http://127.0.0.1:8000/docs

---

# 30. Key Takeaways

1. A machine learning model should go through a proper lifecycle.
2. MLflow can track experiments and manage models.
3. Model Registry helps manage model versions.
4. Staging is used for testing before production.
5. FastAPI can expose a machine learning model as an API.
6. Pydantic validates API input.
7. API testing checks whether the endpoint works correctly.
8. Performance testing checks response efficiency.
9. A tested model can be promoted from staging to production.
10. GitHub Actions can automate CI/CD.
11. Workflow files are stored inside .github/workflows.
12. Pull Requests help review code before merging.
13. Automated tests can prevent bad code from reaching production.

---

# 31. Overall Flow

Machine Learning Model
        ↓
Training
        ↓
Evaluation
        ↓
MLflow Logging
        ↓
Model Registry
        ↓
Staging
        ↓
FastAPI
        ↓
API Testing
        ↓
Performance Testing
        ↓
Registry Testing
        ↓
All Tests Passed
        ↓
Production
        ↓
GitHub Actions
        ↓
CI/CD Automation