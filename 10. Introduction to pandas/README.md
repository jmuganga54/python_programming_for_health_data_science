# Introduction to Pandas in Python

Pandas is a powerful library for **data manipulation and analysis**, especially when working with **tabular data** (spreadsheets, CSVs, SQL tables). This guide is beginner‑friendly and explains every step with code and comments. We’ll use the **Diabetes dataset** from `scikit-learn` to practice.

---

## Contents
- [Setup & Load the Diabetes Dataset](#setup--load-the-diabetes-dataset)
- [Series vs DataFrame](#series-vs-dataframe)
- [Input/Output (CSV/Excel)](#inputoutput-csvexcel)
- [Selecting Rows & Columns (`.loc` and `.iloc`)](#selecting-rows--columns-loc-and-iloc)
- [Handling Missing Data](#handling-missing-data)
- [Cleaning: Duplicates & Data Types](#cleaning-duplicates--data-types)
- [Grouping & Aggregation](#grouping--aggregation)
- [Merge / Join / Concatenate](#merge--join--concatenate)
- [Transformations (`assign`, `apply`, boolean logic)](#transformations-assign-apply-boolean-logic)
- [Time Series (Simulated)](#time-series-simulated)
- [Quick EDA (Plots)](#quick-eda-plots)
- [Exercises (with solutions)](#exercises-with-solutions)
- [Common Pitfalls & Best Practices](#common-pitfalls--best-practices)
- [Function Reference Used Here](#function-reference-used-here)

---

## Setup & Load the Diabetes Dataset

```python
import pandas as pd          # pandas: data tables and tools
import numpy as np           # numpy: fast numeric utilities
from sklearn.datasets import load_diabetes  # sample dataset

# Load dataset from scikit-learn
diabetes = load_diabetes()

# Make a DataFrame from the feature matrix
df = pd.DataFrame(diabetes.data, columns=diabetes.feature_names)

# The dataset is standardized; rescale 'age' so it looks more realistic.
df['age'] = df['age'] * 100

# Turn 'sex' into a readable label for demo:
# this column is standardized; we’ll label >= 0 as 'Male' else 'Female'
df['sex'] = np.where(df['sex'] >= 0, 'Male', 'Female')

# Add the target (disease progression)
df['target'] = diabetes.target

# Peek at the first 5 rows
df.head()
```

**What these do**
- `load_diabetes()`: returns a small dataset with `.data`, `.target`, `.feature_names`.
- `pd.DataFrame(data, columns=...)`: build a table from array-like data.
- `np.where(cond, a, b)`: vectorized if/else.
- `df.head()`: show the first 5 rows.

---

## Series vs DataFrame

A **Series** is one column (1‑D) and a **DataFrame** is a full table (2‑D).

```python
# DataFrame info summary
df.info()
```

- `df.info()`: prints column names, non-null counts, dtypes, memory usage.

```python
# Extract a single column as a Series
bmi_series = df['bmi']
type(bmi_series), bmi_series.head(3)
```

- `df['col']`: select a column (Series).
- `.head(n)`: first n rows.

---

## Input/Output (CSV/Excel)

```python
# Write to CSV
df.to_csv('diabetes.csv', index=False)

# Read back from CSV
df_csv = pd.read_csv('diabetes.csv')
df_csv.head()
```

- `df.to_csv(path, index=False)`: save as CSV (no row index).
- `pd.read_csv(path)`: load CSV into DataFrame.

> Excel (requires `openpyxl` installed):
```python
df.to_excel('diabetes.xlsx', index=False)
df_xlsx = pd.read_excel('diabetes.xlsx')
```

---

## Selecting Rows & Columns (`.loc` and `.iloc`)

- `.loc[row_labels, column_labels]` uses **labels** (names, booleans).
- `.iloc[row_positions, col_positions]` uses **integer positions**.

```python
# Example: patients with age > 50, show bmi and bp
subset = df.loc[df['age'] > 50, ['bmi', 'bp']]
subset.head()
```

```python
# First 10 rows, BMI and BP by integer positions
pos_bmi = df.columns.get_loc('bmi')
pos_bp  = df.columns.get_loc('bp')
first10_iloc = df.iloc[:10, [pos_bmi, pos_bp]]
first10_iloc
```

- `df.columns.get_loc('name')`: find column index by name.

---

## Handling Missing Data

```python
# Count missing values per column
df.isnull().sum()
```

- `.isnull()` / `.isna()`: True where values are missing; `.sum()` counts them.

```python
# Fill missing numeric columns with column means
numeric = df.select_dtypes(include=[np.number])   # only numeric cols
df_filled = df.copy()
df_filled[numeric.columns] = numeric.fillna(numeric.mean())
```

- `select_dtypes(include=[np.number])`: pick numeric columns.
- `.fillna(value)`: replace NaN with value.
- `.copy()`: make a safe copy you can modify.

```python
# Drop rows with any missing values (use with care)
df_dropna = df.dropna()
```

- `.dropna()`: remove rows with NaNs by default.

---

## Cleaning: Duplicates & Data Types

```python
# Count duplicates
df.duplicated().sum()

# Remove duplicates
df_nodup = df.drop_duplicates()
```

- `.duplicated()`: marks rows equal to an earlier row.
- `.drop_duplicates()`: keeps first occurrence.

> Change dtype example:
```python
# df['some_col'] = df['some_col'].astype('int64')
```

---

## Grouping & Aggregation

```python
# Mean values per sex (numeric columns only)
df.groupby('sex').mean(numeric_only=True)
```

- `.groupby('col')`: split; `.mean()/.median()/.agg()` summarize.
- `numeric_only=True`: ignore non-numeric columns.

Age groups example with `pd.cut`:

```python
bins = [-np.inf, 0, 25, 50, 75, np.inf]
labels = ['very young','young','adult','older','very old']
df['age_group'] = pd.cut(df['age'], bins=bins, labels=labels)

df.groupby('age_group').median(numeric_only=True)
```

- `pd.cut`: bucket continuous values into categories.

---

## Merge / Join / Concatenate

```python
# Concatenate top 5 and bottom 5
df_concat = pd.concat([df.head(), df.tail()], ignore_index=True)
```

- `pd.concat([df1, df2], ...)`: stack along rows (default).

```python
# Merge example: add a sex_code via lookup table
lookup = pd.DataFrame({'sex': ['Male','Female'], 'sex_code': [1, 0]})
df_merged = df.merge(lookup, on='sex', how='left')
df_merged[['sex','sex_code']].head()
```

- `.merge(right, on=..., how='left')`: SQL-like join.

---

## Transformations (`assign`, `apply`, boolean logic)

```python
# Add a boolean flag: is age above the mean?
mean_age = df['age'].mean()
df = df.assign(age_above_mean = df['age'] > mean_age)
df[['age', 'age_above_mean']].head()
```

- `.assign(new_col=...)`: add a column (returns a new DataFrame).

```python
# BMI category via apply (toy example on standardized BMI)
def bmi_category(b):
    if b < -0.05: return 'low'
    elif b < 0.05: return 'mid'
    else: return 'high'

df['bmi_cat'] = df['bmi'].apply(bmi_category)
df[['bmi','bmi_cat']].head()
```

- `.apply(func)`: apply a Python function across a Series (or DataFrame rows with `axis=1`).

---

## Time Series (Simulated)

```python
# Simulate a date column
N = len(df)
dates = pd.date_range('2000-01-01', periods=N, freq='D')
df['date'] = dates

# Monthly average of target
monthly = df.set_index('date')['target'].resample('M').mean()
monthly.head()
```

- `pd.date_range`: make date range.
- `.set_index('date')`: set date as index.
- `.resample('M').mean()`: group by calendar month then average.

---

## Quick EDA (Plots)

```python
import matplotlib.pyplot as plt

# Scatter: BMI vs target
plt.scatter(df['bmi'], df['target'])
plt.xlabel('BMI (standardized)')
plt.ylabel('Disease Progression')
plt.title('BMI vs Disease Progression')
plt.show()
```

Other quick plots:

```python
# Histogram
df['bmi'].hist(bins=30)
plt.title('BMI Distribution')
plt.xlabel('BMI (standardized)')
plt.ylabel('Count')
plt.show()

# Boxplot by sex
df.boxplot(column='target', by='sex')
plt.title('Target by Sex')
plt.suptitle('')
plt.show()
```

---

## Exercises (with solutions)

### Exercise A — Create a Series
**Task:** Extract the `bmi` column as a Series and print its type and first 3 values.

**Solution:**
```python
bmi = df['bmi']
print(type(bmi))
print(bmi.head(3))
```

---

### Exercise B — Save to Excel and Read Back
**Task:** Save `df` to `diabetes.xlsx` and read it back.

**Solution:**
```python
df.to_excel('diabetes.xlsx', index=False)      # requires openpyxl
df_xlsx = pd.read_excel('diabetes.xlsx')
df_xlsx.head()
```

---

### Exercise C — `.loc[]` and `.iloc[]`
**Task:** Using both `.loc[]` and `.iloc[]`, select BMI and BP of the first 10 patients.

**Solution:**
```python
# iloc by positions
pos_bmi = df.columns.get_loc('bmi')
pos_bp  = df.columns.get_loc('bp')
first10_iloc = df.iloc[:10, [pos_bmi, pos_bp]]

# loc by labels
first10_loc = df.loc[:9, ['bmi', 'bp']]
first10_iloc, first10_loc
```

---

### Exercise D — Missing Data
**Task:** Count missing values per column; fill numeric NaNs with the column mean.

**Solution:**
```python
print(df.isnull().sum())

numeric = df.select_dtypes(include=[np.number])
df_filled = df.copy()
df_filled[numeric.columns] = numeric.fillna(numeric.mean())
df_filled.isnull().sum()
```

---

### Exercise E — Duplicates
**Task:** Check for duplicates and remove them.

**Solution:**
```python
print('Duplicates:', df.duplicated().sum())
df_no_dupes = df.drop_duplicates()
print('After drop:', df_no_dupes.duplicated().sum())
```

---

### Exercise F — Grouping
**Task:** Group by `sex` and compute the **median** for numeric columns.

**Solution:**
```python
df.groupby('sex').median(numeric_only=True)
```

---

### Exercise G — Concatenation
**Task:** Concatenate the first 10 and last 10 rows.

**Solution:**
```python
df_concat = pd.concat([df.head(10), df.tail(10)], ignore_index=True)
df_concat.head(), df_concat.tail()
```

---

### Exercise H — New Column
**Task:** Create a binary column `bmi_above_mean` indicating whether BMI is above the mean.

**Solution:**
```python
mean_bmi = df['bmi'].mean()
df['bmi_above_mean'] = df['bmi'] > mean_bmi
df[['bmi','bmi_above_mean']].head()
```

---

## Common Pitfalls & Best Practices

**Pitfalls**
- Chained indexing (`df[col][row]`) → use `.loc`/`.iloc` instead.
- Ignoring NaNs/duplicates → can skew results.
- Wrong data types (numbers stored as strings) → fix with `.astype(...)`.
- Joining on wrong keys → double-check join columns before `merge`.

**Best Practices**
- Start with `df.info()` and `df.describe()`.
- Prefer vectorized operations over loops.
- Use `.loc`/`.iloc` explicitly and clearly.
- Keep intermediate copies when trying risky transforms (`df.copy()`).
- Give clear, consistent column names.
- Document your steps in markdown/comments.

---

## Function Reference Used Here

- **Core**: `pd.DataFrame`, `df.head`, `df.info`, `df.describe`, `df.copy`
- **Selection**: `df['col']`, `.loc[rows, cols]`, `.iloc[rpos, cpos]`, `df.columns.get_loc`
- **Missing data**: `df.isnull()`, `.sum()`, `.dropna()`, `.fillna()`, `select_dtypes`
- **Cleaning**: `df.duplicated()`, `.drop_duplicates()`, `.astype(...)`
- **Grouping**: `df.groupby('col').mean()/median()/agg(...)`, `pd.cut`
- **Combine**: `pd.concat([...])`, `df.merge(...)`
- **Transform**: `.assign(...)`, `.apply(...)`
- **I/O**: `pd.read_csv`, `df.to_csv`, `pd.read_excel`, `df.to_excel`
- **Dates**: `pd.date_range`, `.set_index`, `.resample`
- **Plotting**: `plt.scatter`, `Series.hist`, `df.boxplot`

---

**Tip:** You can run the code blocks in any Python environment (VS Code, Jupyter, Colab). If you don’t have `scikit-learn` or `openpyxl`, install them with:

```bash
pip install scikit-learn openpyxl
```
