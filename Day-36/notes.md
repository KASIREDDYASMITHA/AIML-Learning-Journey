# Day 36 - Introduction to Model Registry and ML Testing

## 1. Introduction

After training a machine learning model, the work does not end.

We need to:

- Store the model.
- Manage different versions of the model.
- Test the model.
- Decide which model should be used.
- Move the approved model to production.
- Expose the model through an API.

This is where Model Registry and ML Testing are useful.

---

# 2. Model Registry

A Model Registry is a central place used to store and manage different versions of machine learning models.

It helps us manage:

- Model versions
- Model stages
- Model lifecycle
- Model promotion
- Production models

A Model Registry helps answer:

> Which model version do we currently trust and want to use in production?

---

# 3. GitHub vs Model Registry vs DockerHub

GitHub is mainly used as a code repository.

```text
GitHub → Code Registry