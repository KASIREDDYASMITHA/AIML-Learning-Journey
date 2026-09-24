# AIML Learning Journey - Day 25

# Pandas Basics and Dataset Exploration

## 1. What is Pandas?

Pandas is a Python library mainly used for:

* Data manipulation
* Data analysis
* Working with structured data
* Reading and processing datasets
* Cleaning datasets
* Preparing data for Machine Learning

Pandas is commonly imported as:

```python
import pandas as pd
```

Here, `pd` is the commonly used alias for Pandas.

---

# 2. DataFrame

A DataFrame is a two-dimensional table-like data structure in Pandas.

It contains:

* Rows
* Columns
* Data

Example:

```python
import pandas as pd

data = {
    "Name": ["A", "B", "C"],
    "Age": [20, 21, 22]
}

df = pd.DataFrame(data)

print(df)
```

Output:

```text
  Name  Age
0    A   20
1    B   21
2    C   22
```

Here:

```text
df
```

is the variable name that stores the DataFrame.

---

# 3. DataFrame Variable

A DataFrame can be stored in any valid Python variable name.

Example:

```python
df = pd.DataFrame(data)
```

Here:

* `df` = variable name
* `pd.DataFrame()` = creates a DataFrame

We can also use:

```python
dataframe = pd.DataFrame(data)
```

The variable name does not have to be `df`.

However, `df` is commonly used as a short name for DataFrame.

---

# 4. Rows and Columns

A DataFrame contains rows and columns.

Example:

```text
       Name  Age
0      A     20
1      B     21
2      C     22
```

Here:

* `Name` and `Age` are columns.
* `0`, `1`, `2` are row indexes.
* There are 3 rows.
* There are 2 columns.

---

# 5. Shape

`shape` tells us the number of rows and columns in a DataFrame.

Syntax:

```python
df.shape
```

Example:

```python
print(df.shape)
```

Output:

```text
(3, 2)
```

The first value represents:

```text
Number of rows
```

The second value represents:

```text
Number of columns
```

Therefore:

```text
(3, 2)
```

means:

```text
3 rows
2 columns
```

Important:

`shape` is an attribute, so we do NOT use parentheses.

Correct:

```python
df.shape
```

Incorrect:

```python
df.shape()
```

---

# 6. Rows

Rows represent individual records or observations in a dataset.

Example:

```text
Name   Age
A      20
B      21
C      22
```

Each line represents one row.

For a dataset containing customer information, one row can represent one customer.

For a delivery dataset, one row can represent one delivery order.

---

# 7. Columns

Columns represent individual features or attributes of the dataset.

Example:

```text
Name
Age
City
Salary
```

Each of these is a column.

In Machine Learning, columns often represent features or target variables.

---

# 8. columns

`columns` gives the names of all columns in the DataFrame.

Syntax:

```python
df.columns
```

Example:

```python
print(df.columns)
```

Important:

`columns` is an attribute.

Therefore:

```python
df.columns
```

is correct.

Do not write:

```python
df.columns()
```

---

# 9. dtypes

`dtypes` tells us the data type of each column.

Syntax:

```python
df.dtypes
```

Example:

```python
print(df.dtypes)
```

Possible output:

```text
Name    object
Age      int64
Salary   float64
```

Common Pandas data types include:

* `int64` - integer numbers
* `float64` - decimal numbers
* `object` - usually text/string data
* `bool` - True/False values

`dtypes` is an attribute, so parentheses are not used.

Correct:

```python
df.dtypes
```

---

# 10. head()

`head()` displays the first few rows of the DataFrame.

Syntax:

```python
df.head()
```

By default, it displays the first 5 rows.

We can also specify the number of rows:

```python
df.head(10)
```

This displays the first 10 rows.

Unlike `shape` and `dtypes`, `head()` is a method, so parentheses are required.

---

# 11. tail()

`tail()` displays the last few rows of the DataFrame.

Example:

```python
df.tail()
```

By default, it displays the last 5 rows.

We can specify the number of rows:

```python
df.tail(10)
```

---

# 12. info()

`info()` provides information about the DataFrame.

Example:

```python
df.info()
```

It provides information such as:

* Number of rows
* Column names
* Number of non-null values
* Data types
* Memory usage

---

# 13. describe()

`describe()` provides statistical information about numerical columns.

Example:

```python
df.describe()
```

It can provide:

* Count
* Mean
* Standard deviation
* Minimum
* 25% percentile
* 50% percentile
* 75% percentile
* Maximum

Example:

```python
df["Age"].describe()
```

---

# 14. Reading a CSV File

Pandas can be used to read CSV files.

Syntax:

```python
df = pd.read_csv("filename.csv")
```

Example:

```python
df = pd.read_csv("swiggy.csv")
```

After loading the dataset, we can inspect it using:

```python
print(df.head())
print(df.shape)
print(df.columns)
print(df.dtypes)
```

---

# 15. Selecting a Column

We can select a single column using:

```python
df["Age"]
```

Example:

```python
print(df["Age"])
```

We can also select multiple columns:

```python
df[["Name", "Age"]]
```

---

# 16. Dataset Exploration

Before applying Machine Learning algorithms, we should understand the dataset.

Basic dataset exploration includes:

```python
df.head()
df.tail()
df.shape
df.columns
df.dtypes
df.info()
df.describe()
```

This helps us understand:

* What data is available
* Number of rows
* Number of columns
* Data types
* Missing values
* Numerical information
* Dataset structure

---

# 17. Swiggy Dataset

The dataset used today is a Swiggy delivery dataset.

The dataset contains:

```text
45,593 rows
20 columns
```

Some columns include:

* ID
* Delivery_person_ID
* Delivery_person_Age
* Delivery_person_Ratings
* Restaurant_latitude
* Restaurant_longitude
* Delivery_location_latitude
* Delivery_location_longitude
* Order_Date
* Time_Orderd
* Time_Order_picked
* Weatherconditions
* Road_traffic_density
* Vehicle_condition
* Type_of_order
* Type_of_vehicle
* multiple_deliveries
* Festival
* City
* Time_taken(min)

---

# 18. Attributes vs Methods

This is an important concept.

## Attributes

Attributes provide information about an object.

Examples:

```python
df.shape
df.columns
df.dtypes
```

They do not use parentheses.

## Methods

Methods perform an operation.

Examples:

```python
df.head()
df.tail()
df.info()
df.describe()
```

They use parentheses.

---

# 19. Examples

### Example 1: shape

```python
print(df.shape)
```

If output is:

```text
(45593, 20)
```

It means:

```text
45593 rows
20 columns
```

### Example 2: dtypes

```python
print(df.dtypes)
```

This shows the data type of every column.

---

# 20. Why Pandas is Important in AIML

Pandas is important because Machine Learning requires data preparation.

A typical Machine Learning workflow is:

```text
Collect Data
     ↓
Load Dataset
     ↓
Explore Dataset
     ↓
Clean Dataset
     ↓
Preprocess Dataset
     ↓
Feature Selection
     ↓
Train Model
     ↓
Evaluate Model
```

Pandas is heavily used during:

* Data loading
* Data exploration
* Data cleaning
* Data preprocessing
* Feature selection
* Data manipulation

---

# 21. Important Points to Remember

```text
df.shape      → number of rows and columns
df.columns    → column names
df.dtypes     → data types
df.head()     → first rows
df.tail()     → last rows
df.info()     → DataFrame information
df.describe() → statistical summary
```

Remember:

```text
Attributes → no ()
Methods    → use ()
```

Examples:

```python
df.shape
df.columns
df.dtypes
```

are attributes.

Whereas:

```python
df.head()
df.tail()
df.info()
df.describe()
```

are methods
