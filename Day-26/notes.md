# Day 26 - Pandas and Data Cleaning

## 1. Dataset Size and Unique Values

A dataset can contain many rows but fewer unique entities.

Example:

- Total rows = 45,593
- Unique rider IDs = 1,320

This means that the dataset contains many ride records for the same rider.

### Important Idea

Number of rows and number of unique values are different.

For example:

```python
df.shape