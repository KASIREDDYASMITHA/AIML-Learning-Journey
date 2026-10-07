# AIML Day 37 - Model Registry, ML Testing, DVC and Logging

## Topics Covered

Today I learned the basics of:

- Model Registry
- Model versions
- Model staging and production
- ML model testing
- API testing
- AI/ML testing challenges
- DVC basics
- dvc.yaml
- params.yaml
- Logging
- Logging levels
- File handlers
- Virtual environments

---

## 1. Model Registry

A Model Registry is a centralized place used to store, manage and track different versions of machine learning models.

A model registry helps us keep track of:

- Model versions
- Model stages
- Model metadata
- Model status
- Model deployment information

Example:

```text
Model
  |
  ├── Version 1
  ├── Version 2
  └── Version 3