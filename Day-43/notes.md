# Day 43 – Docker Fundamentals and Amazon ECR

## 1. What Is Docker?

Docker is a platform used to package and run applications in containers.

It packages an application and the dependencies it needs into a Docker image. The image can then be used to create containers in different environments.

### Example

1. Package a Python application into a Docker image.
2. Run that image as a container on a local computer or a cloud server.

## 2. Docker Image

A Docker image is a read-only template used to create containers. It contains the application code, required dependencies, and configuration needed to run the application.

Docker images can be stored in a container registry and shared with other systems.

## 3. Docker Container

A container is a running instance of a Docker image.

**Relationship:**

Dockerfile → Build → Docker Image → Run → Container

Example:

- Image: `swaggy:23`
- Container name: `swaggy-container`

One image can be used to create multiple containers.

## 4. Dockerfile

A Dockerfile contains instructions used to build a Docker image.

Common instructions:

- `FROM` – Specifies the base image.
- `WORKDIR` – Sets the working directory.
- `COPY` – Copies files into the image.
- `RUN` – Executes commands while building the image.
- `CMD` – Specifies the default command when the container starts.

Example:

```dockerfile
FROM python:3.12-slim
WORKDIR /app
COPY app.py .
CMD ["python", "app.py"]
```

## 5. Build a Docker Image

Command:

```bash
docker build -t swaggy:23 .
```

Explanation:

- `docker build` builds an image.
- `-t` assigns a name and tag.
- `swaggy` is the image name.
- `23` is the image tag.
- `.` represents the current build context.

The current directory should contain the Dockerfile and the application file.

### Docker Build Cache

Docker can reuse previously built layers when the relevant instructions and inputs have not changed.

This reduces unnecessary work and can speed up repeated builds.

For example:

1. Rebuilding without changing `app.py` or the Dockerfile may reuse cached layers.
2. Changing `app.py` requires the affected layer to be rebuilt, while eligible earlier layers may still be reused.

## 6. Run a Docker Container

Command:

```bash
docker run --name swaggy-container swaggy:23
```

Explanation:

- `docker run` creates and starts a container.
- `--name swaggy-container` assigns the container name.
- `swaggy:23` identifies the image to run.

To list running containers:

```bash
docker ps
```

To list all containers, including stopped ones:

```bash
docker ps -a
```

To list local images:

```bash
docker images
```

## 7. Container Registries

A container registry stores Docker images so they can be distributed and retrieved.

### Docker Hub

Docker Hub is a commonly used container registry that supports public and private repositories.

Example use: sharing an image with another developer through a repository.

### Amazon ECR

Amazon Elastic Container Registry (ECR) is AWS's managed container image registry.

It supports private repositories and can be integrated with AWS services and CI/CD pipelines.

Example use: storing an application image for deployment to an AWS environment.

**Important:** Docker images are not automatically uploaded to a registry just because they are built locally. They must be tagged and pushed.

## 8. Typical Amazon ECR Workflow

1. Test the application and its performance.
2. Promote the approved model or application version.
3. Configure AWS credentials securely.
4. Create or select an ECR repository.
5. Authenticate Docker to Amazon ECR.
6. Build the Docker image.
7. Tag the image with the ECR repository address.
8. Push the image to ECR.

### Step 1: Configure AWS Credentials

For local development, configure credentials using the AWS CLI:

```bash
aws configure
```

Enter the required AWS access key, secret key, default region, and output format when prompted.

Do not commit AWS credentials or secret keys to GitHub.

### Step 2: Create an ECR Repository

Example:

```bash
aws ecr create-repository --repository-name swaggy --region ap-south-1
```

Use the AWS region appropriate for your account and deployment.

### Step 3: Authenticate Docker to ECR

Replace `ACCOUNT_ID` with your AWS account ID.

```bash
aws ecr get-login-password --region ap-south-1 | docker login --username AWS --password-stdin ACCOUNT_ID.dkr.ecr.ap-south-1.amazonaws.com
```

### Step 4: Build the Image

```bash
docker build -t swaggy:23 .
```

### Step 5: Tag the Image for ECR

```bash
docker tag swaggy:23 ACCOUNT_ID.dkr.ecr.ap-south-1.amazonaws.com/swaggy:23
```

### Step 6: Push the Image

```bash
docker push ACCOUNT_ID.dkr.ecr.ap-south-1.amazonaws.com/swaggy:23
```

Replace `ACCOUNT_ID` with the actual 12-digit AWS account ID. The repository must exist, and the IAM identity must have the required permissions.

## 9. GitHub Actions

GitHub Actions is a CI/CD automation platform integrated with GitHub.

A workflow can automatically build, test, and publish Docker images when code is pushed or when a workflow is triggered.

Typical workflow:

1. Check out the repository.
2. Set up Python and run tests.
3. Configure AWS authentication securely.
4. Authenticate to Amazon ECR.
5. Build and tag the Docker image.
6. Push the image to ECR.

Use GitHub repository secrets or an appropriate AWS identity federation setup to protect credentials. Never place access keys directly in the workflow file.

## 10. Model Testing and Promotion

Before deploying an ML model, evaluate it using appropriate validation or test data.

Common classification metrics include:

- Accuracy
- Precision
- Recall
- F1-score

Model promotion means approving a tested model version for the next stage, such as staging or production.

For example:

1. Compare candidate model performance against the required acceptance criteria.
2. Approve the selected model version and package it for deployment.

A Docker image makes an application environment easier to reproduce, but it does not by itself prove that the model is accurate or ready for production.
