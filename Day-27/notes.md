# AIML Learning Journey - Day 27

# Pandas Data Analysis and Data Cleaning

## 1. Introduction to Pandas

Pandas is a Python library used for:

- Data analysis
- Data manipulation
- Data cleaning
- Data preprocessing
- Working with tabular data
- Preparing data for Machine Learning

The two important Pandas data structures are:

1. Series
2. DataFrame

A DataFrame is a two-dimensional table containing rows and columns.

Example:

```python
import pandas as pd

data = {
    "name": ["Asmitha", "Rahul", "Sneha"],
    "age": [22, 25, 24],
    "salary": [45000, 50000, 55000]
}

df = pd.DataFrame(data)

print(df)
```

---

# 2. DataFrame

A DataFrame stores data in rows and columns.

Example:

```python
import pandas as pd

data = {
    "name": ["A", "B", "C"],
    "age": [22, 25, 24],
    "city": ["Hyderabad", "Bengaluru", "Chennai"]
}

df = pd.DataFrame(data)

print(df)
```

Output:

```text
  name  age       city
0    A   22  Hyderabad
1    B   25  Bengaluru
2    C   24    Chennai
```

Here:

- `name` is a column
- `age` is a column
- `city` is a column
- Each row represents one record

---

# 3. Data Inspection

Before performing data analysis or Machine Learning, we should understand the dataset.

Important commands:

```python
df.shape
df.dtypes
df.describe()
df.head()
```

These commands help us understand:

- Number of rows
- Number of columns
- Datatypes
- Statistical information
- First few records

---

# 4. df.shape

`df.shape` returns the number of rows and columns.

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
(10, 5)
```

This means:

- 10 rows
- 5 columns

The first value is the number of rows.

The second value is the number of columns.

---

# 5. df.dtypes

`df.dtypes` shows the datatype of every column.

Syntax:

```python
df.dtypes
```

Example:

```python
print(df.dtypes)
```

Common datatypes:

- `int64` - integer values
- `float64` - decimal values
- `object` - text/string values
- `bool` - True/False
- `datetime64` - date and time values

Example:

```text
name      object
age        int64
salary     int64
```

---

# 6. df.describe()

`df.describe()` gives statistical information about numerical columns.

Syntax:

```python
df.describe()
```

Example:

```python
print(df.describe())
```

It generally provides:

- count
- mean
- standard deviation
- minimum
- 25%
- 50%
- 75%
- maximum

Example:

```text
count
mean
std
min
25%
50%
75%
max
```

This helps us understand the numerical distribution of the dataset.

---

# 7. describe() With a Specific Column

We can also describe a particular column.

Example:

```python
print(df["age"].describe())
```

We can also convert a column to another datatype before describing it.

Example:

```python
print(df["age"].astype(float).describe())
```

`astype()` is used to convert a column into a required datatype.

---

# 8. df.head()

`df.head()` displays the first five rows by default.

Syntax:

```python
df.head()
```

Example:

```python
print(df.head())
```

We can specify the number of rows.

Example:

```python
print(df.head(10))
```

This displays the first 10 rows.

`head()` is useful for quickly checking the structure and values of a dataset.

---

# 9. df.tail()

`df.tail()` displays the last five rows by default.

Example:

```python
print(df.tail())
```

We can specify the number of rows:

```python
print(df.tail(10))
```

---

# 10. Selecting Data Using loc[]

`loc[]` is used to select rows and columns using labels or conditions.

Syntax:

```python
df.loc[]
```

---

## 10.1 Selecting One Row

```python
print(df.loc[0])
```

This selects the row with index 0.

---

## 10.2 Selecting Multiple Rows

```python
print(df.loc[0:3])
```

This selects rows from index 0 to index 3.

---

## 10.3 Selecting Specific Columns

```python
print(df.loc[:, ["name", "age"]])
```

Here:

```text
:
```

means all rows.

```text
["name", "age"]
```

means select only these columns.

---

## 10.4 Selecting Rows Using a Condition

```python
print(df.loc[df["age"] > 25])
```

This selects rows where age is greater than 25.

---

## 10.5 Selecting Rows and Columns Together

```python
print(
    df.loc[
        df["salary"] > 50000,
        ["name", "salary"]
    ]
)
```

This selects:

- rows where salary is greater than 50000
- only name and salary columns

---

# 11. Selecting Data Using iloc[]

`iloc[]` is used to select rows and columns using integer positions.

Example:

```python
print(df.iloc[0])
```

This selects the first row.

Selecting the first three rows:

```python
print(df.iloc[0:3])
```

Selecting first two columns:

```python
print(df.iloc[:, 0:2])
```

Difference:

```text
loc  -> label based
iloc -> position based
```

---

# 12. Filtering Data

Filtering means selecting only the rows that satisfy a condition.

Example:

```python
result = df[df["age"] > 25]

print(result)
```

This returns rows where age is greater than 25.

---

# 13. Filtering Using AND

The `&` operator is used when both conditions should be true.

Example:

```python
result = df[
    (df["age"] > 25) &
    (df["salary"] > 50000)
]

print(result)
```

Both conditions must be satisfied.

---

# 14. Filtering Using OR

The `|` operator is used when either condition can be true.

Example:

```python
result = df[
    (df["city"] == "Hyderabad") |
    (df["city"] == "Bengaluru")
]

print(result)
```

This selects employees from either Hyderabad or Bengaluru.

---

# 15. Selecting Numerical Columns

Numerical columns contain numeric values.

Examples:

```text
age
salary
height
weight
marks
```

Example:

```python
numeric_columns = df.select_dtypes(
    include=["number"]
)

print(numeric_columns)
```

This selects columns having numerical datatypes.

---

# 16. Selecting Categorical Columns

Categorical columns contain categories such as:

```text
city
gender
department
color
```

Example:

```python
categorical_columns = df.select_dtypes(
    include=["object"]
)

print(categorical_columns)
```

This selects object/string columns.

---

# 17. Removing Data Using drop()

`drop()` is used to remove rows or columns.

---

## 17.1 Removing a Column

```python
df = df.drop("age", axis=1)
```

Here:

```text
axis=1
```

means column.

---

## 17.2 Removing Multiple Columns

```python
df = df.drop(
    ["age", "salary"],
    axis=1
)
```

---

## 17.3 Removing a Row

```python
df = df.drop(2)
```

This removes the row with index 2.

---

## 17.4 Using inplace=True

```python
df.drop(2, inplace=True)
```

`inplace=True` modifies the original DataFrame.

Without `inplace=True`, we normally assign the result back:

```python
df = df.drop(2)
```

---

# 18. Replacing Values Using replace()

`replace()` is used to replace incorrect, inconsistent, or unwanted values.

Example:

```python
df["city"] = df["city"].replace(
    "Hyd",
    "Hyderabad"
)
```

Here:

```text
Hyd
```

is replaced with:

```text
Hyderabad
```

---

# 19. Replacing Multiple Values

Multiple values can be replaced using a dictionary.

```python
df["city"] = df["city"].replace({
    "Hyd": "Hyderabad",
    "Blr": "Bengaluru",
    "Mad": "Chennai"
})
```

This is useful for standardizing inconsistent category names.

For example:

```text
Hyd
HYD
Hyderabad
```

can be standardized to:

```text
Hyderabad
```

---

# 20. fillna()

`fillna()` is used to fill missing values.

Example:

```python
df["age"] = df["age"].fillna(
    df["age"].mean()
)
```

Here, missing age values are replaced with the mean age.

Another example:

```python
df["city"] = df["city"].fillna(
    "Unknown"
)
```

Missing city values are replaced with `"Unknown"`.

---

# 21. isnull() and isna()

Both `isnull()` and `isna()` can be used to detect missing values.

Example:

```python
print(df.isnull())
```

or:

```python
print(df.isna())
```

They return `True` where a value is missing.

---

# 22. Counting Missing Values

To count missing values in every column:

```python
print(df.isnull().sum())
```

or:

```python
print(df.isna().sum())
```

Example output:

```text
name      0
age       1
salary    2
city      0
```

This means:

- name has 0 missing values
- age has 1 missing value
- salary has 2 missing values
- city has 0 missing values

---

# 23. Handling Invalid Values

A dataset may contain values that are not technically missing but are logically incorrect.

Example:

```text
age = 200
```

For a normal person dataset, this may be considered invalid.

We can replace invalid values with `NaN`.

First import NumPy:

```python
import numpy as np
```

Then:

```python
df.loc[
    (df["age"] < 18) |
    (df["age"] > 100),
    "age"
] = np.nan
```

Now invalid age values are converted into missing values.

---

# 24. Cleaning Invalid Values Using Conditions

General pattern:

```python
df.loc[
    condition,
    "column"
] = np.nan
```

Example:

```python
df.loc[
    df["salary"] < 0,
    "salary"
] = np.nan
```

This converts negative salary values into missing values.

Another example:

```python
df.loc[
    df["marks"] > 100,
    "marks"
] = np.nan
```

This converts marks greater than 100 into missing values.

---

# 25. Latitude

Latitude represents the north-south position of a location.

Valid latitude range:

```text
-90 to 90
```

Therefore:

```text
latitude < -90
```

or:

```text
latitude > 90
```

is invalid.

Example:

```python
df.loc[
    (df["latitude"] < -90) |
    (df["latitude"] > 90),
    "latitude"
] = np.nan
```

---

# 26. Longitude

Longitude represents the east-west position of a location.

Valid longitude range:

```text
-180 to 180
```

Values outside this range are invalid.

Example:

```python
df.loc[
    (df["longitude"] < -180) |
    (df["longitude"] > 180),
    "longitude"
] = np.nan
```

---

# 27. Checking Latitude and Longitude After Cleaning

After cleaning:

```python
print(
    df[
        ["latitude", "longitude"]
    ]
)
```

We can also check missing values:

```python
print(df.isna().sum())
```

This helps us verify whether invalid latitude or longitude values were converted to missing values.

---

# 28. Data Cleaning Using a Function

Data cleaning logic can also be placed inside a function.

Example:

```python
def clean_lat_long(df):

    df.loc[
        (df["latitude"] < -90) |
        (df["latitude"] > 90),
        "latitude"
    ] = np.nan

    df.loc[
        (df["longitude"] < -180) |
        (df["longitude"] > 180),
        "longitude"
    ] = np.nan

    return df
```

Then:

```python
df = clean_lat_long(df)
```

After cleaning:

```python
print(df.isna().sum())
```

---

# 29. Applying Functions to Data

Pandas provides `apply()` to apply a function to values in a Series or DataFrame.

Example:

```python
df["age"] = df["age"].apply(
    lambda x: x if x >= 18 else np.nan
)
```

Here, the lambda function checks each age.

Another example:

```python
df["name"] = df["name"].apply(
    lambda x: x.upper()
)
```

This converts names into uppercase.

---

# 30. groupby()

`groupby()` is used to group data according to a column.

It is commonly used with aggregation functions.

Common aggregation functions:

```text
mean()
sum()
max()
min()
count()
```

---

# 31. groupby() with mean()

Example:

```python
result = df.groupby(
    "city"
)["salary"].mean()

print(result)
```

This calculates the average salary for each city.

---

# 32. groupby() with sum()

```python
result = df.groupby(
    "city"
)["salary"].sum()

print(result)
```

This calculates total salary for each city.

---

# 33. groupby() with max()

```python
result = df.groupby(
    "city"
)["salary"].max()

print(result)
```

This finds the maximum salary in each city.

---

# 34. groupby() with min()

```python
result = df.groupby(
    "city"
)["salary"].min()

print(result)
```

This finds the minimum salary in each city.

---

# 35. groupby() with count()

```python
result = df.groupby(
    "city"
)["name"].count()

print(result)
```

This counts the number of employees in each city.

---

# 36. Date Handling

Dates are important in data analysis.

Pandas provides:

```python
pd.to_datetime()
```

to convert values into datetime format.

Example:

```python
df["date"] = pd.to_datetime(
    df["date"]
)
```

Check datatype:

```python
print(df["date"].dtype)
```

---

# 37. Filtering Using Dates

After converting the column to datetime, we can filter using dates.

Example:

```python
result = df[
    df["date"] >= "2026-01-01"
]

print(result)
```

This selects rows from January 1, 2026 onwards.

---

# 38. Date Range Filtering

We can filter data between two dates.

Example:

```python
result = df[
    (df["date"] >= "2026-01-01") &
    (df["date"] <= "2026-03-31")
]

print(result)
```

This selects data between:

```text
2026-01-01
```

and:

```text
2026-03-31
```

---

# 39. Categorical Data

Categorical data represents values belonging to categories.

Examples:

```text
City
Gender
Department
Color
Traffic
Education
Product Type
```

Example:

```text
City
Hyderabad
Bengaluru
Chennai
Hyderabad
```

Here `City` is a categorical feature.

---

# 40. Categorical Data Type

A categorical column can be converted into Pandas categorical datatype.

Example:

```python
df["city"] = df["city"].astype("category")
```

Check the datatype:

```python
print(df["city"].dtype)
```

Categorical data can be useful for memory efficiency and preprocessing.

---

# 41. One-Hot Encoding

Machine Learning algorithms generally require numerical input.

Categorical values such as:

```text
Hyderabad
Bengaluru
Chennai
```

need to be converted into numerical representation.

One-hot encoding creates separate columns for each category.

Pandas provides:

```python
pd.get_dummies()
```

Example:

```python
df = pd.get_dummies(
    df,
    columns=["city"]
)
```

---

# 42. Example of One-Hot Encoding

Original data:

```text
city
Hyderabad
Bengaluru
Chennai
```

After one-hot encoding:

```text
city_Bengaluru
city_Chennai
city_Hyderabad
```

Example:

```text
city_Bengaluru  city_Chennai  city_Hyderabad
0               0             1
1               0             0
0               1             0
```

Meaning:

```text
1 = category is present
0 = category is not present
```

---

# 43. Why Data Cleaning Is Important

Real-world datasets are rarely perfect.

They may contain:

- Missing values
- Invalid values
- Incorrect datatypes
- Duplicate records
- Inconsistent category names
- Outliers
- Incorrect dates
- Invalid geographic values

Data cleaning helps us prepare reliable data for analysis and Machine Learning.

---

# 44. General Data Cleaning Workflow

The general workflow is:

```text
Raw Data
   ↓
Inspect Data
   ↓
Understand Columns
   ↓
Check Datatypes
   ↓
Find Missing Values
   ↓
Find Invalid Values
   ↓
Replace / Remove Invalid Data
   ↓
Handle Missing Values
   ↓
Convert Datatypes
   ↓
Encode Categorical Data
   ↓
Clean Data
   ↓
Machine Learning
```

---

# 45. Important Commands Learned Today

```python
df.shape

df.dtypes

df.describe()

df.head()

df.tail()

df.loc[]

df.iloc[]

df.drop()

df.replace()

df.fillna()

df.isnull()

df.isna()

df.groupby()

pd.to_datetime()

pd.get_dummies()

df.astype()

df.apply()
```

---

# 46. Quick Revision

## shape

```python
df.shape
```

Returns number of rows and columns.

---

## dtypes

```python
df.dtypes
```

Returns datatype of every column.

---

## describe

```python
df.describe()
```

Returns statistical information.

---

## head

```python
df.head()
```

Returns first five rows.

---

## tail

```python
df.tail()
```

Returns last five rows.

---

## loc

```python
df.loc[]
```

Label-based selection.

---

## iloc

```python
df.iloc[]
```

Position-based selection.

---

## drop

```python
df.drop()
```

Removes rows or columns.

---

## replace

```python
df.replace()
```

Replaces values.

---

## fillna

```python
df.fillna()
```

Fills missing values.

---

## isnull / isna

```python
df.isnull()
df.isna()
```

Checks missing values.

---

## groupby

```python
df.groupby()
```

Groups data for analysis.

---

## to_datetime

```python
pd.to_datetime()
```

Converts values into datetime format.

---

## get_dummies

```python
pd.get_dummies()
```

Performs one-hot encoding.

---

## astype

```python
df.astype()
```

Changes datatype.

---

## apply

```python
df.apply()
```

Applies a function to data.

---

# 47. Important Examples

## Example 1: Find Missing Values

```python
print(df.isna().sum())
```

## Example 2: Replace Invalid Values

```python
df.loc[
    df["age"] > 100,
    "age"
] = np.nan
```

## Example 3: Group Data

```python
print(
    df.groupby("city")["salary"].mean()
)
```

## Example 4: Convert Dates

```python
df["date"] = pd.to_datetime(
    df["date"]
)
```

## Example 5: One-Hot Encoding

```python
df = pd.get_dummies(
    df,
    columns=["city"]
)
```

---

# 48. Complete Example

```python
import pandas as pd
import numpy as np

data = {
    "name": [
        "Asmitha",
        "Rahul",
        "Sneha",
        "Arjun",
        "Priya",
        "Kiran"
    ],

    "age": [
        22,
        25,
        24,
        200,
        27,
        23
    ],

    "city": [
        "Hyderabad",
        "Hyd",
        "Bengaluru",
        "Chennai",
        "Hyd",
        "Bengaluru"
    ],

    "salary": [
        45000,
        50000,
        55000,
        60000,
        48000,
        52000
    ],

    "latitude": [
        17.3850,
        17.4000,
        12.9716,
        13.0827,
        17.4500,
        200.0000
    ],

    "longitude": [
        78.4867,
        78.4800,
        77.5946,
        80.2707,
        78.5000,
        300.0000
    ],

    "date": [
        "2026-01-10",
        "2026-01-20",
        "2026-02-15",
        "2026-02-25",
        "2026-03-10",
        "2026-03-20"
    ]
}

df = pd.DataFrame(data)

# Inspect data

print("Shape:")
print(df.shape)

print("\nData Types:")
print(df.dtypes)

print("\nFirst Five Rows:")
print(df.head())

print("\nStatistical Description:")
print(df.describe())

# Select columns

print("\nName and Salary:")
print(
    df.loc[:, ["name", "salary"]]
)

# Filter data

print("\nSalary Greater Than 50000:")
print(
    df.loc[df["salary"] > 50000]
)

# Replace inconsistent values

df["city"] = df["city"].replace(
    "Hyd",
    "Hyderabad"
)

# Clean invalid age

df.loc[
    (df["age"] < 18) |
    (df["age"] > 100),
    "age"
] = np.nan

# Clean latitude

df.loc[
    (df["latitude"] < -90) |
    (df["latitude"] > 90),
    "latitude"
] = np.nan

# Clean longitude

df.loc[
    (df["longitude"] < -180) |
    (df["longitude"] > 180),
    "longitude"
] = np.nan

# Convert date

df["date"] = pd.to_datetime(
    df["date"]
)

# Check missing values

print("\nMissing Values:")
print(df.isna().sum())

# GroupBy

print("\nAverage Salary By City:")
print(
    df.groupby("city")["salary"].mean()
)

# One-Hot Encoding

encoded_df = pd.get_dummies(
    df,
    columns=["city"]
)

print("\nEncoded Data:")
print(encoded_df)
```

---
