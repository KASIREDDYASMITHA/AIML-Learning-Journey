# AIML Day 42 - Data Pipeline, MLflow, DagsHub and Docker

## 1. Raw Data to EDA

A machine learning project often begins with raw data stored in a CSV file.

Example workflow:

Raw Data -> Data Cleaning -> EDA -> Feature Engineering -> Model Training -> Evaluation -> Deployment

### Raw Data

Raw data is the original data collected from a source. It may contain missing values, duplicate records, incorrect data types and inconsistent categories.

Example: `swiggy.csv`

### Data Cleaning

Data cleaning prepares raw data for analysis by identifying and handling data-quality problems.

Common operations:

- Inspect the dataset.
- Remove duplicate records.
- Handle missing values.
- Correct inconsistent column names.
- Check data types.
- Identify invalid or inconsistent values.

Example 1: Remove duplicate restaurant records.

Example 2: Fill missing numerical values using the median when appropriate.

Note: The correct cleaning method depends on the meaning of the columns. Missing values should not be filled blindly.

### Exploratory Data Analysis (EDA)

EDA helps us understand the structure, quality, distribution and relationships in a dataset.

Common operations:

- View the first few rows.
- Check the number of rows and columns.
- Inspect data types.
- Count missing values.
- Calculate descriptive statistics.
- Examine unique categorical values.
- Identify unusual values and outliers.
- Visualize distributions and relationships.

Example 1: Calculate the average delivery time if the dataset contains a valid delivery-time column.

Example 2: Find which restaurant category occurs most frequently if a category column exists.

The actual column names must be checked before performing column-specific analysis.

## 2. MLflow

MLflow is an open-source platform for managing machine learning workflows.

It can record experiment parameters, evaluation metrics, artifacts and model information.

### Important Terms

- Experiment: A collection of related runs.
- Run: One execution of an experiment.
- Parameters: Settings used during an experiment.
- Metrics: Numerical results used to evaluate an experiment.
- Artifacts: Files produced during a run, such as reports, plots and model files.
- Tracking URI: The location where experiment tracking data is stored.

Examples:

1. Record a model's `max_depth` parameter and its accuracy.
2. Compare the evaluation metrics of two models across separate runs.

MLflow tracking is optional in the Python program for this day. Without a tracking URI, the program runs locally and still creates its output files.

## 3. DagsHub

DagsHub is a platform for collaborating on machine learning projects and managing experiment tracking and related project assets.

It can integrate with MLflow for remote experiment tracking.

Typical workflow:

1. Create or open a DagsHub repository.
2. Configure its MLflow tracking URI.
3. Configure authentication securely.
4. Run experiments and log parameters, metrics and artifacts.
5. Compare runs through the tracking interface.

Example 1: Store experiment results for a model trained on a dataset.

Example 2: Compare metrics from experiments run with different preprocessing settings.

DagsHub does not automatically clean data or improve model accuracy. Those tasks still require code and correct experiments.

## 4. Docker

Docker is a platform used to package and run applications in containers.

It helps applications run consistently across environments by packaging application code and dependencies.

### Dockerfile

A Dockerfile is a text file containing instructions used to build a Docker image.

Examples of Dockerfile instructions:

- `FROM`: Selects a base image.
- `WORKDIR`: Sets the working directory.
- `COPY`: Copies files into the image.
- `RUN`: Executes commands during image building.
- `ENV`: Sets environment variables.
- `CMD`: Specifies the default command when the container starts.

### Docker Image

A Docker image is a packaged template containing the application and the filesystem layers needed to run it.

Example: `swiggy-eda:day42`

### Docker Container

A container is a running instance of an image.

Example: Run the Swiggy EDA application inside a container.

### Docker Workflow

Dockerfile -> Docker Image -> Docker Container

Important distinction:

- Dockerfile: Build instructions.
- Image: Packaged application template.
- Container: Running instance of that image.

A container does not automatically contain every file on your laptop. Input datasets and generated outputs may need to be mounted as volumes.

## 5. Amazon ECR

Amazon Elastic Container Registry (ECR) is an AWS-managed container image registry.

It stores Docker-compatible container images so they can be pulled by authorized systems for deployment.

Typical workflow:

1. Build a Docker image.
2. Create an ECR repository.
3. Authenticate Docker to ECR.
4. Tag the image with the ECR repository URI.
5. Push the image to ECR.
6. Pull the image when required by an authorized environment.

Example 1: Store a Swiggy EDA image in a private ECR repository.

Example 2: Allow an authorized deployment environment to pull a tagged application image.

ECR stores images. It does not itself run the application; a runtime such as Amazon ECS, Amazon EKS or another compatible environment is needed.

## 6. End-to-End Workflow

1. Read raw CSV data.
2. Inspect and clean the dataset.
3. Perform EDA.
4. Save the cleaned data and analysis report.
5. Optionally record experiment information using MLflow.
6. Use DagsHub when remote experiment tracking is required.
7. Build a Docker image.
8. Run the application in a Docker container.
9. Push the image to Amazon ECR when preparing for deployment.


