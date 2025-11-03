# Pandas — The Practical Basics (Beginner Friendly)
This short guide gives you the **core skills** to read, inspect, clean, filter, group, reshape, and save data with Pandas. Every concept has a tiny example, the key functions used, and an exercise for you to try.
> Tip: Run the code snippets in a notebook or Python file. Replace the sample data with your own when you feel ready.

---

## 0) Setup and Imports
We import Pandas and NumPy. We also set a random seed for reproducible examples.
```python
import pandas as pd
import numpy as np

np.random.seed(42)
pd.__version__
```
```
1.5.3
```

---

## 1) Core Objects: `Series` and `DataFrame`
- **Series**: One-dimensional labeled array.
- **DataFrame**: Two-dimensional table with rows and columns.
```python
# Series
s = pd.Series([10, 20, 30], name="points")
print(s)
print("Values:", s.values)
print("Index:", s.index.tolist())

# DataFrame
df = pd.DataFrame({
    "name": ["Ana", "Ben", "Cara", "Dan"],
    "age":  [23,    31,   29,     35],
    "score":[88,    92,   79,     85]
})
print("\nDataFrame:")
print(df)
```
```
0    10
1    20
2    30
Name: points, dtype: int64
Values: [10, 20, 30]
Index: [0, 1, 2]

DataFrame:
   name  age  score
0   Ana   23     88
1   Ben   31     92
2  Cara   29     79
3   Dan   35     85
```
### Try it yourself
Create a `Series` of 5 temperatures and a `DataFrame` with two columns: `city` and `temp_c`. Print them.

---

## 2) Reading and Writing Files
Use `pd.read_csv()` and `DataFrame.to_csv()` for CSV. Similar readers exist for Excel (`read_excel`), JSON (`read_json`), and Parquet (`read_parquet`).
```python
# Create a small DataFrame and save to CSV
mini = pd.DataFrame({"id":[1,2,3], "value":[10.5, 11.2, 9.8]})
mini.to_csv("mini.csv", index=False)

# Read it back
mini_read = pd.read_csv("mini.csv")
print(mini_read)
```
```
id  value
0   1   10.5
1   2   11.2
2   3    9.8
```
### Key functions here
- `pd.read_csv(path)`: Read CSV into DataFrame.
- `df.to_csv(path, index=False)`: Save without index column.
### Try it yourself
Make a small table and save it as `my_data.csv`. Read it back and print the first rows with `head()`.

---

## 3) First Look at Your Data
These are the functions you will use **every time** you load new data.
```python
df = pd.DataFrame({
    "name": ["Ana", "Ben", "Cara", "Dan"],
    "age":  [23, 31, 29, 35],
    "score":[88, 92, 79, 85]
})
print("Shape:", df.shape)          # (rows, cols)
print("\ndtypes:\n", df.dtypes)  # column types
print("\nHead:\n", df.head(2))   # first rows
print("\nInfo:")
print(df.info())
print("\nDescribe:\n", df.describe())
```
```
Shape: (4, 3)

dtypes:
name     object
age       int64
score     int64
dtype: object

Head:
  name  age  score
0  Ana   23     88
1  Ben   31     92

Info:
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 4 entries, 0 to 3
Data columns (total 3 columns):
 #   Column  Non-Null Count  Dtype 
---  ------  --------------  ----- 
 0   name    4 non-null      object
 1   age     4 non-null      int64 
 2   score   4 non-null      int64 
dtypes: int64(2), object(1)
memory usage: 228.0+ bytes

Describe:
        age      score
count   4.0   4.000000
mean   29.5  86.000000
std     5.0   5.477226
min    23.0  79.000000
25%    27.5  83.500000
50%    30.0  86.500000
75%    32.0  89.000000
max    35.0  92.000000
```
### Key functions here
- `df.shape`: tuple of (rows, columns)
- `df.dtypes`: data type per column
- `df.head(n)`, `df.tail(n)`: peek at rows
- `df.info()`: non-null counts and types
- `df.describe()`: summary stats for numeric columns
### Try it yourself
Create a DataFrame with 6 rows and 3 numeric columns. Print `shape`, `dtypes`, `head(3)`, and `describe()`.

---

## 4) Selecting Columns and Rows
You have three main tools: **bracket**, **`loc`**, and **`iloc`**.
```python
df = pd.DataFrame({
    "name": ["Ana", "Ben", "Cara", "Dan"],
    "age":  [23, 31, 29, 35],
    "score":[88, 92, 79, 85]
})

# Column selection
print(df["name"])            # a Series
print(df[["name", "score"]]) # a DataFrame

# Row selection by label with .loc (here default index 0..n-1)
print(df.loc[1])             # row with index label 1
print(df.loc[1:3, ["name","score"]])  # slice rows, choose columns

# Row selection by position with .iloc
print(df.iloc[0])            # first row
print(df.iloc[0:2, 1:3])     # rows 0-1, columns 1-2 (age, score)

# Boolean filtering
adults = df[df["age"] >= 30]
print(adults)
```
```
0     Ana
1     Ben
2    Cara
3     Dan
Name: name, dtype: object

   name  score
0   Ana     88
1   Ben     92
2  Cara     79
3   Dan     85

name     Ben
age       31
score     92
Name: 1, dtype: object

   name  score
1   Ben     92
2  Cara     79
3   Dan     85

name     Ana
age       23
score     88
Name: 0, dtype: object

   age  score
0   23     88
1   31     92

  name  age  score
1  Ben   31     92
3  Dan   35     85
```
### Key functions here
- `df["col"]`, `df[["c1","c2"]]`: choose columns
- `df.loc[row_labels, col_labels]`: by **labels**
- `df.iloc[row_pos, col_pos]`: by **positions**
- Boolean masks: `df[df.col > x]`
### Try it yourself
Filter rows where `score >= 85` and select only `name` and `score`.

---

## 5) Sorting and Renaming
```python
df = pd.DataFrame({
    "name": ["Ana", "Ben", "Cara", "Dan"],
    "age":  [23, 31, 29, 35],
    "score":[88, 92, 79, 85]
})

# Sort by one or more columns
print(df.sort_values(by="score", ascending=False))
print(df.sort_values(by=["age", "score"]))  # age then score

# Rename columns
renamed = df.rename(columns={"name":"student", "score":"exam_score"})
print(renamed)
```
```
name  age  score
1   Ben   31     92
0   Ana   23     88
3   Dan   35     85
2  Cara   29     79

   name  age  score
0   Ana   23     88
2  Cara   29     79
1   Ben   31     92
3   Dan   35     85

  student  age  exam_score
0     Ana   23          88
1     Ben   31          92
2    Cara   29          79
3     Dan   35          85
```
### Key functions here
- `df.sort_values(by=..., ascending=...)`
- `df.rename(columns={old:new})`
### Try it yourself
Sort by `age` ascending and then by `score` descending. Rename `age` to `years`.

---

## 6) Handling Missing Values
```python
df = pd.DataFrame({
    "a":[1, np.nan, 3],
    "b":[np.nan, 5, 6],
    "c":["x", "y", None]
})
print("Original:\n", df)

print("\nCheck missing (isna):\n", df.isna())
print("\nCount missing per column:\n", df.isna().sum())

# Fill numeric with mean, categorical with mode
df_filled = df.copy()
df_filled["a"] = df_filled["a"].fillna(df_filled["a"].mean())
df_filled["b"] = df_filled["b"].fillna(df_filled["b"].mean())
df_filled["c"] = df_filled["c"].fillna(df_filled["c"].mode()[0])
print("\nFilled:\n", df_filled)

# Drop rows with any missing
dropped = df.dropna()
print("\nDrop rows with any missing:\n", dropped)
```
```
Original:
     a    b     c
0  1.0  NaN     x
1  NaN  5.0     y
2  3.0  6.0  None

Check missing (isna):
       a      b      c
0  False   True  False
1   True  False  False
2  False  False   True

Count missing per column:
a    1
b    1
c    1
dtype: int64

Filled:
     a    b  c
0  1.0  5.5  x
1  2.0  5.0  y
2  3.0  6.0  x

Drop rows with any missing:
Empty DataFrame
Columns: [a, b, c]
Index: []
```
### Key functions here
- `df.isna()` / `df.isnull()`: detect missing
- `df.fillna(value)`: replace missing values
- `df.dropna()`: remove rows with missing
- `series.mode()`, `series.mean()`: helpful fill values
### Try it yourself
Create a column with missing values and fill it with the column median using `fillna(df.col.median())`.

---

## 7) Type Conversion and Dates
```python
df = pd.DataFrame({
    "age": ["23", "31", "29"],
    "when": ["2025-11-01", "2025/11/02", "Nov 03, 2025"]
})

# Convert to numeric
df["age_num"] = pd.to_numeric(df["age"])

# Parse dates
df["when_dt"] = pd.to_datetime(df["when"])

print(df.dtypes)
print(df)
```
```
age                object
when               object
age_num             int64
when_dt    datetime64[ns]
dtype: object

  age          when  age_num    when_dt
0  23    2025-11-01       23 2025-11-01
1  31    2025/11/02       31 2025-11-02
2  29  Nov 03, 2025       29 2025-11-03
```
### Key functions here
- `pd.to_numeric(series)`: turn strings into numbers
- `pd.to_datetime(series)`: parse many date formats
- `series.astype(dtype)`: convert to a specific type
### Try it yourself
Make a column of strings like `'1','2','3'`, convert to integers with `astype(int)`. Create a `'date'` column and parse it with `to_datetime`.

---

## 8) Creating or Transforming Columns
```python
df = pd.DataFrame({
    "name":["Ana","Ben","Cara","Dan"],
    "height_m":[1.60, 1.82, 1.70, 1.75],
    "weight_kg":[55, 75, 62, 80]
})

# Vectorized calculation: BMI = weight / height^2
df["bmi"] = df["weight_kg"] / (df["height_m"] ** 2)

# map / replace: categorize BMI simply
df["bmi_cat"] = np.where(df["bmi"] >= 25, "high", "normal")

# assign() pattern for pipelines
df2 = (df.assign(height_cm = lambda d: d["height_m"]*100)
         .assign(weight_lb = lambda d: d["weight_kg"]*2.20462))

print(df)
print("\nWith extra columns via assign():\n", df2)
```
```
name  height_m  weight_kg        bmi bmi_cat
0   Ana      1.60         55  21.484375  normal
1   Ben      1.82         75  22.642193  normal
2  Cara      1.70         62  21.453287  normal
3   Dan      1.75         80  26.122449    high

With extra columns via assign():
   name  height_m  weight_kg        bmi bmi_cat  height_cm  weight_lb
0   Ana      1.60         55  21.484375  normal      160.0  121.25410
1   Ben      1.82         75  22.642193  normal      182.0  165.34650
2  Cara      1.70         62  21.453287  normal      170.0  136.68644
3   Dan      1.75         80  26.122449    high      175.0  176.36960
```
### Key functions here
- Vectorized math on columns
- `np.where(cond, a, b)`: fast conditional
- `df.assign(new = lambda d: ...)`: add columns in a chain
- `series.map()` / `series.replace()` also helpful
### Try it yourself
Create `bmi` from your own `height_m` and `weight_kg` columns and classify with three groups: `<18.5='low'`, `18.5–25='normal'`, `>25='high'`.

---

## 9) Grouping and Aggregation
Use `groupby` to summarize. You can aggregate multiple statistics at once.
```python
sales = pd.DataFrame({
    "region":["North","North","South","South","South"],
    "seller":["A","B","A","B","B"],
    "amount":[100, 120, 90, 110, 130]
})

# Average by region
print(sales.groupby("region")["amount"].mean())

# Multiple aggregations
summary = sales.groupby("seller")["amount"].agg(["count","sum","mean","min","max"])
print("\nPer seller summary:\n", summary)
```
```
region
North    110.0
South    110.0
Name: amount, dtype: float64

Per seller summary:
        count  sum   mean  min  max
seller                             
A           2  190   95.0   90  100
B           3  360  120.0  110  130
```
### Key functions here
- `df.groupby(keys)[col].agg(funcs)`: summarize groups
- Common aggs: `'count','sum','mean','median','min','max','std'`
- `transform` for per-row group-wise transformations
### Try it yourself
Make a small DataFrame of students with `class` and `score`. Compute the average score **per class**.

---

## 10) Pivot, Melt, and Reshape
Change between **long** and **wide** formats.
```python
grades = pd.DataFrame({
    "name":["Ana","Ana","Ben","Ben"],
    "subject":["Math","Bio","Math","Bio"],
    "score":[90, 85, 78, 88]
})

# Pivot to wide
wide = grades.pivot(index="name", columns="subject", values="score")
print(wide)

# Melt back to long
long = wide.reset_index().melt(id_vars="name", var_name="subject", value_name="score")
print("\nLong again:\n", long)
```
```
subject  Bio  Math
name              
Ana       85    90
Ben       88    78

Long again:
  name subject  score
0  Ana     Bio     85
1  Ben     Bio     88
2  Ana    Math     90
3  Ben    Math     78
```
### Key functions here
- `df.pivot(index, columns, values)`: long → wide
- `df.melt(id_vars, var_name, value_name)`: wide → long
- `pd.pivot_table(...)` supports aggregation for duplicates
### Try it yourself
Create a long table of weekly steps with columns `person, day, steps`. Pivot to have one row per person and one column per day.

---

## 11) Merging and Concatenating
Combine data from multiple tables.
```python
left = pd.DataFrame({"id":[1,2,3], "name":["Ana","Ben","Cara"]})
right = pd.DataFrame({"id":[1,2,4], "score":[88,92,75]})

# Merge on shared key
inner = pd.merge(left, right, on="id", how="inner")   # intersection
leftj = pd.merge(left, right, on="id", how="left")    # keep all left
outer = pd.merge(left, right, on="id", how="outer")   # union

print("Inner:\n", inner)
print("\nLeft join:\n", leftj)
print("\nOuter:\n", outer)

# Concatenate rows
a = pd.DataFrame({"x":[1,2]})
b = pd.DataFrame({"x":[3,4]})
print("\nConcat rows:\n", pd.concat([a,b], ignore_index=True))
```
```
Inner:
   id name  score
0   1  Ana     88
1   2  Ben     92

Left join:
   id  name  score
0   1   Ana   88.0
1   2   Ben   92.0
2   3  Cara    NaN

Outer:
   id  name  score
0   1   Ana   88.0
1   2   Ben   92.0
2   3  Cara    NaN
3   4   NaN   75.0

Concat rows:
   x
0  1
1  2
2  3
3  4
```
### Key functions here
- `pd.merge(left, right, on=..., how=...)`: SQL-style joins
- `pd.concat([df1, df2], axis=0 or 1)`: stack rows or columns
### Try it yourself
Create two tables: `people(id,name)` and `scores(id,math)`. Do an **outer** join and then fill missing `math` with 0.

---

## 12) Strings and Dates: Quick Tricks
```python
df = pd.DataFrame({
    "email":["ana@example.com", "ben@uni.uk", "cara@company.org"],
    "date":["2025-11-01", "2025-11-02", "2025-11-03"]
})

# String methods via .str
df["domain"] = df["email"].str.split("@").str[1]
df["email_len"] = df["email"].str.len()

# Datetime accessor via .dt
df["date"] = pd.to_datetime(df["date"])
df["year"] = df["date"].dt.year
df["weekday"] = df["date"].dt.day_name()

print(df)
```
```
email       date       domain  email_len  year   weekday
0   ana@example.com 2025-11-01  example.com         15  2025  Saturday
1        ben@uni.uk 2025-11-02       uni.uk         10  2025    Sunday
2  cara@company.org 2025-11-03  company.org         16  2025    Monday
```
### Key functions here
- String: `series.str.split`, `str.len`, `str.contains`, `str.lower`
- Datetime: `pd.to_datetime`, and `series.dt.year`, `series.dt.month`, `series.dt.day_name()`
### Try it yourself
Extract the top-level domain from `email` (e.g., `com`, `uk`, `org`) by splitting on `.` and taking the last part.

---

## 13) Duplicates and Unique Values
```python
df = pd.DataFrame({
    "id":[1,2,2,3,3,3],
    "val":[10,20,20,30,30,40]
})
print("Unique ids:", df["id"].nunique())
print("Value counts for 'id':\n", df["id"].value_counts())

print("\nDuplicates mask:\n", df.duplicated(subset=["id","val"]))
print("\nDrop exact duplicates on both columns:")
print(df.drop_duplicates(subset=["id","val"]))
```
```
Unique ids: 3
Value counts for 'id':
3    3
2    2
1    1
Name: id, dtype: int64

Duplicates mask:
0    False
1    False
2     True
3    False
4     True
5    False
dtype: bool

Drop exact duplicates on both columns:
   id  val
0   1   10
1   2   20
3   3   30
5   3   40
```
### Key functions here
- `series.nunique()`: number of unique values
- `series.value_counts()`: frequency table
- `df.duplicated(subset=...)`: boolean mask of duplicates
- `df.drop_duplicates(subset=...)`: remove duplicates
### Try it yourself
Count how many unique `val` you have and remove duplicate rows keeping only the **first** occurrence.

---

## 14) Index Basics
```python
df = pd.DataFrame({
    "id":[101,102,103],
    "name":["Ana","Ben","Cara"],
    "score":[88,92,79]
})

# Set and reset index
df2 = df.set_index("id")
print(df2)
print("\nRow with index 102 via .loc:")
print(df2.loc[102])

print("\nReset index back to column:")
print(df2.reset_index())
```
```
name  score
id              
101   Ana     88
102   Ben     92
103  Cara     79

Row with index 102 via .loc:
name     Ben
score     92
Name: 102, dtype: object

Reset index back to column:
    id  name  score
0  101   Ana     88
1  102   Ben     92
2  103  Cara     79
```
### Key functions here
- `df.set_index(col)`, `df.reset_index()`
- Use meaningful indexes to speed up `.loc` lookups and joins.
### Try it yourself
Set `name` as the index, select the row for `'Ben'` using `.loc`, then reset the index.

---

## 15) Quick Plotting from Pandas
Pandas uses Matplotlib under the hood. These calls are enough to get started (they return Matplotlib axes).
```python
import matplotlib.pyplot as plt

ts = pd.Series([3, 4, 6, 8, 7], index=[1,2,3,4,5])
ax = ts.plot(kind="line", title="Tiny line plot")
plt.show()

dfp = pd.DataFrame({"A":[1,3,2,4], "B":[5,2,3,1]})
ax = dfp.plot(kind="bar", title="Bar from DataFrame")
plt.show()
```
### Key functions here
- `series.plot(kind=...)`, `df.plot(kind=...)` where kind is `'line','bar','hist','box','area','scatter'` etc.
### Try it yourself
Create a small DataFrame of two numeric columns and draw a bar chart and a line chart.

---

## 16) Common Gotchas
- **Chained assignment**: Avoid `df[df.x>0]["y"] = ...`. Use `.loc` in a single step: `df.loc[df.x>0, "y"] = ...`.
- **Copy vs View**: When in doubt, do `df_copy = df.copy()` before editing.
- **Mixed types** in a column cause headaches. Convert early with `to_numeric` or `to_datetime`.

---

## Cheat Sheet: Functions You Will Use Daily

- **Inspect**: `df.head`, `df.tail`, `df.shape`, `df.info`, `df.describe`
- **Select**: `df[cols]`, `df.loc[...]`, `df.iloc[...]`, boolean masks
- **Clean**: `isna`, `fillna`, `dropna`, `astype`, `to_numeric`, `to_datetime`
- **Transform**: arithmetic on columns, `assign`, `where/np.where`, `map/replace`, string `.str.*`, datetime `.dt.*`
- **Summarize**: `groupby(...).agg(...)`, `value_counts`, `nunique`
- **Reshape**: `pivot`, `melt`, `concat`, `merge`
- **Save**: `to_csv`, `to_parquet` (if available)


---

## Mini Practice — Bring It Together
```python
# Build a tiny dataset
df = pd.DataFrame({
    "city":["Dar","Arusha","Mwanza","Dodoma","Dar"],
    "temp_c":[29, 24, 25, np.nan, 31],
    "rain_mm":[0, 4, 2, 1, 0]
})

# 1) Fill missing temp with the mean
df["temp_c"] = df["temp_c"].fillna(df["temp_c"].mean())

# 2) Add a 'hot' flag (>= 28 C)
df["hot"] = np.where(df["temp_c"]>=28, True, False)

# 3) Average rain by city
avg_rain = df.groupby("city")["rain_mm"].mean()

print(df)
print("\nAverage rain by city:\n", avg_rain)
```
```
city  temp_c  rain_mm    hot
0     Dar   29.00        0   True
1  Arusha   24.00        4  False
2  Mwanza   25.00        2  False
3  Dodoma   27.25        1  False
4     Dar   31.00        0   True

Average rain by city:
city
Arusha    4.0
Dar       0.0
Dodoma    1.0
Mwanza    2.0
Name: rain_mm, dtype: float64
```
