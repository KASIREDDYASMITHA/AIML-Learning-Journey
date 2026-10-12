
# AIML Learning Journey - Day 42

## Topics Covered

- Raw Swiggy CSV data processing
- Data Cleaning and Exploratory Data Analysis (EDA)
- MLflow experiment tracking
- DagsHub integration
- Docker, Dockerfile, Docker Image and Container
- Amazon ECR (Elastic Container Registry)

## Learning Summary

Today I learned how raw CSV data is cleaned and explored before machine learning. I also learned how MLflow can track experiments, how DagsHub can host and manage ML experiment tracking, and how Docker packages an application with its dependencies for consistent execution.

Amazon ECR is used to store and manage Docker container images in AWS.

## Project Workflow

Raw CSV Data
-> Data Cleaning
-> Exploratory Data Analysis
-> MLflow Tracking (Optional)
-> Docker Image
-> Docker Container
-> Amazon ECR (Image Storage)


## Run Locally

Install the dependencies:

```bash
python -m pip install -r requirements.txt
```

Place the dataset at:

`data/raw/swiggy.csv`

Run the program:

```bash
python swiggy_eda.py
```

The program creates a cleaned CSV file and an EDA summary report.

## Build and Run with Docker

Build the image:

```bash
docker build -t swiggy-eda:day42 .
```

Run the container:

```bash
docker run --rm -v "%cd%/data:/app/data" swiggy-eda:day42
```

