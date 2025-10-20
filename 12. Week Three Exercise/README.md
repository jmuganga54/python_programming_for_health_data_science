# Python Week Three – Exercises (with Solutions & Explanations)

> This file is GitHub-friendly Markdown. Code blocks are fenced with language hints for nice syntax highlighting.  
> You can run these snippets in a Python environment (e.g., Jupyter, VS Code, or a plain `.py` file with slight tweaks).

---

## Common imports

```python
import numpy as np
import pandas as pd
```

---

## Problem 1: Vectorised Computation (NumPy) — Mean Arterial Pressure (MAP)

**Question**  
Compute the Mean Arterial Pressure (MAP) for 5 patients with:
\[
\text{MAP}=\frac{\text{systolic}+2\times \text{diastolic}}{3}
\]

**Solution**

```python
import numpy as np

# data
systolic  = np.array([120, 130, 110, 140, 135])
diastolic = np.array([ 80,  85,  75,  90,  88])

# vectorised MAP formula
map_values = (systolic + 2 * diastolic) / 3
print(map_values)
```

**Functions explained**
- `np.array([...])`: builds a NumPy array (vector).
- Vectorised arithmetic (`+`, `*`, `/`) works element-wise when arrays have the same shape.

**Expected output**

```
[ 93.33333333 100.          86.66666667 106.66666667 103.66666667]
```

---

## Problem 2: Mean & Standard Deviation (NumPy)

**Question**  
For `bmi = np.array([22.5, 24.7, 28.1, 30.2, 27.5, 26.1, 23.0])`, compute the mean and standard deviation. Briefly interpret them.

**Solution**

```python
import numpy as np

bmi = np.array([22.5, 24.7, 28.1, 30.2, 27.5, 26.1, 23.0])

mean_bmi = np.mean(bmi)         # same as bmi.mean()
std_bmi  = np.std(bmi)          # population std (ddof=0 by default)

print("Mean BMI:", mean_bmi)
print("Std Dev (population):", std_bmi)
```

**Functions explained**
- `np.mean(arr)`: average value.
- `np.std(arr)`: standard deviation; spread around the mean.
  - For sample std use `np.std(arr, ddof=1)`.

**Expected output**

```
Mean BMI: 26.014285714285716
Std Dev (population): 2.508040551492787
```

**Interpretation**  
Average BMI is ~26.01 (slightly above “normal” range). A std dev of ~2.51 means most BMIs are within about ±2.5 units of the mean.

---

## Problem 3: Matrix Multiplication (NumPy) — Risk Score

**Question**  
Given:
\[
X=\begin{pmatrix}
60&110&220\\
50&90&180\\
70&130&210\\
40&85&190
\end{pmatrix},\quad
W=\begin{pmatrix}0.5\\0.3\\0.2\end{pmatrix}
\]
Compute `X @ W` to get a risk score for each patient.

**Solution**

```python
import numpy as np

X = np.array([[60, 110, 220],
              [50,  90, 180],
              [70, 130, 210],
              [40,  85, 190]])
W = np.array([[0.5],
              [0.3],
              [0.2]])

risk_scores = X @ W           # matrix multiply
print(risk_scores.ravel())    # ravel to 1D for display
```

**Functions & operators explained**
- `@`: matrix multiplication (same as `np.matmul(X, W)` or `X.dot(W)`).
- `.ravel()`: view as 1D for neat printing.

**Expected output**

```
[103.  89. 111.  84.]
```

---

## Problem 4: Vectorised BMI (NumPy)

**Question**  
Given weights `[70,85,90,60,75]` and heights `[1.75,1.80,1.78,1.60,1.70]`, compute BMI for each with  
\[
\text{BMI}=\frac{\text{weight}}{\text{height}^2}
\]

**Solution**

```python
import numpy as np

weights = np.array([70, 85, 90, 60, 75])
heights = np.array([1.75, 1.80, 1.78, 1.60, 1.70])

bmis = weights / (heights ** 2)
print(np.round(bmis, 2))
```

**Functions explained**
- `** 2`: element-wise power.
- `np.round(arr, 2)`: round to 2 decimals for readability.

**Expected output**

```
[22.86 26.23 28.41 23.44 25.95]
```

---

## Problem 5: Pandas — Create, Save, Load & Average

**Question**  
Create a DataFrame with the table below, save to `patient_data.csv`, read it back, and compute average values for each numeric column (excluding Patient ID). Show the first rows.

**Solution**

```python
import pandas as pd

data = {
    "Patient ID": [1, 2, 3, 4, 5],
    "Age (years)": [65, 50, 45, 60, 55],
    "Glucose Level (mg/dL)": [110, 95, 105, 100, 90],
    "Cholesterol Level (mg/dL)": [180, 170, 190, 200, 160],
    "Blood Pressure (mmHg)": ["120/80", "130/85", "140/90", "150/95", "125/75"]
}

df = pd.DataFrame(data)
df.to_csv("patient_data.csv", index=False)  # save without row index

df_loaded = pd.read_csv("patient_data.csv")
print(df_loaded.head())  # first rows

# Compute means for numeric columns except Patient ID
numeric_cols = ["Age (years)", "Glucose Level (mg/dL)", "Cholesterol Level (mg/dL)"]
means = df_loaded[numeric_cols].mean()
print("\nColumn means (excluding Patient ID):")
print(means)
```

**Functions explained**
- `pd.DataFrame(dict)`: table from dict of columns.
- `.to_csv(path, index=False)`: write CSV, omit row numbers.
- `pd.read_csv(path)`: read CSV into DataFrame.
- `.head()`: show first rows.
- `.mean()`: column-wise mean for numeric columns.

**Expected output (abridged)**

```
   Patient ID  Age (years)  Glucose Level (mg/dL)  Cholesterol Level (mg/dL) Blood Pressure (mmHg)
0           1           65                    110                         180                120/80
1           2           50                     95                         170                130/85
...

Column means (excluding Patient ID):
Age (years)                   55.0
Glucose Level (mg/dL)        100.0
Cholesterol Level (mg/dL)    180.0
dtype: float64
```

---

## Problem 6: Importing & Using a Custom Module

**Question**  
Create `health_utils.py` with:
- `calculate_bmi(weight, height)`  
- `is_healthy_bmi(bmi)` → `True` if 18.5 ≤ BMI ≤ 24.9  
Import it and check if a person (72 kg, 1.78 m) is healthy.

**Solution**

Create **`health_utils.py`**:

```python
# health_utils.py
def calculate_bmi(weight, height):
    return weight / (height ** 2)

def is_healthy_bmi(bmi):
    return 18.5 <= bmi <= 24.9
```

Use it:

```python
import health_utils

bmi_val = health_utils.calculate_bmi(72, 1.78)
print("BMI:", round(bmi_val, 2))
print("Healthy range?", health_utils.is_healthy_bmi(bmi_val))
```

**Expected output**

```
BMI: 22.72
Healthy range? True
```

---

## Problem 7: Descriptive Stats & Thresholding (NumPy)

**Question**  
For heart rates `rates = np.array([72,75,78,70,69,80,77,74,76,73])`  
1) Compute mean, median, std.  
2) Find indices of patients whose rate is **above mean + 1 std**.

**Solution**

```python
import numpy as np

rates = np.array([72, 75, 78, 70, 69, 80, 77, 74, 76, 73])

mean = np.mean(rates)
median = np.median(rates)
std = np.std(rates)        # population std

threshold = mean + std
idx = np.where(rates > threshold)[0]   # indices where condition is True

print("Mean:", mean, "Median:", median, "Std:", std)
print("Threshold (mean+std):", threshold)
print("Indices above threshold:", idx)
print("Values:", rates[idx])
```

**Functions explained**
- `np.median(arr)`: middle value.
- `np.where(condition)`: indices where condition is `True`.

**Expected output**

```
Mean: 74.4 Median: 74.5 Std: 3.3226495451672298
Threshold (mean+std): 77.72264954516723
Indices above threshold: [2 5]
Values: [78 80]
```

---

## Problem 8: Boolean & Fancy Indexing (NumPy)

**Question**  
For `glucose = np.array([90,110,130,95,145,160,125,105])`  
1) Select values > 120 using boolean indexing.  
2) Using fancy indexing, extract readings of patients 1, 3, 5 (0-based → `[0,2,4]`).  
3) Print both results.

**Solution**

```python
import numpy as np

glucose = np.array([90, 110, 130, 95, 145, 160, 125, 105])

# 1) boolean indexing
high = glucose[glucose > 120]

# 2) fancy indexing by specific positions
subset = glucose[[0, 2, 4]]   # patients 1, 3, 5

print("Glucose > 120:", high)
print("Patients 1, 3, 5:", subset)
```

**Expected output**

```
Glucose > 120: [130 145 160 125]
Patients 1, 3, 5: [ 90 130 145]
```

---

## Problem 9: Pandas — Data Cleaning (Missing Values)

**Question**  
Build a DataFrame with cholesterol values containing `NaN`.  
1) Show missing values via `isnull()`  
2) Fill missing cholesterol with the **mean** of the available values  
3) Show the cleaned DataFrame.

**Solution**

```python
import numpy as np
import pandas as pd

df = pd.DataFrame({
    "Patient ID": [1, 2, 3, 4, 5],
    "Age":        [45, 50, 60, 55, 48],
    "Glucose":    [105, 98, 110, 95, 115],
    "Cholesterol":[180, np.nan, 200, np.nan, 190]
})

print("Missing values per column:")
print(df.isnull().sum())

chol_mean = df["Cholesterol"].mean()   # ignores NaNs automatically
df["Cholesterol"] = df["Cholesterol"].fillna(chol_mean)

print("\nCleaned DataFrame:")
print(df)
```

**Functions explained**
- `.isnull()`: boolean mask for missing values. `.sum()` counts them per column.
- `.mean()`: average over non-missing values.
- `.fillna(value)`: replace NaNs with `value`.

**Expected output**

```
Missing values per column:
Patient ID    0
Age           0
Glucose       0
Cholesterol   2
dtype: int64

Cleaned DataFrame:
   Patient ID  Age  Glucose  Cholesterol
0           1   45      105        180.0
1           2   50       98        190.0
2           3   60      110        200.0
3           4   55       95        190.0
4           5   48      115        190.0
```

*(Mean cholesterol here is (180+200+190)/3 = 190.)*

---

## Problem 10: Pandas — Groupby & New Column, Save to CSV

**Question**  
Create the DataFrame below.  
1) Compute **average BMI by Gender** using `groupby()`  
2) Add `High_Cholesterol = Cholesterol > 200`  
3) Save result as `health_summary.csv`.

**Solution**

```python
import pandas as pd

df = pd.DataFrame({
    "Patient ID":    [1, 2, 3, 4, 5],
    "Gender":        ["Male", "Female", "Male", "Female", "Male"],
    "BMI":           [25.3, 22.4, 27.5, 23.1, 29.2],
    "Blood Pressure":[120, 110, 130, 115, 140],
    "Cholesterol":   [180, 170, 210, 190, 220]
})

avg_bmi_by_gender = df.groupby("Gender")["BMI"].mean()
print("Average BMI by Gender:")
print(avg_bmi_by_gender)

df["High_Cholesterol"] = df["Cholesterol"] > 200
print("\nDataFrame with High_Cholesterol column:")
print(df)

df.to_csv("health_summary.csv", index=False)
```

**Functions explained**
- `.groupby("Gender")["BMI"].mean()`: split by gender, compute mean of BMI.
- `df["High_Cholesterol"] = ...`: add a boolean column based on a condition.
- `.to_csv(...)`: save to CSV.

**Expected output**

```
Average BMI by Gender:
Gender
Female    22.75
Male      27.333333
Name: BMI, dtype: float64

DataFrame with High_Cholesterol column:
   Patient ID  Gender   BMI  Blood Pressure  Cholesterol  High_Cholesterol
0           1    Male  25.3             120          180             False
1           2  Female  22.4             110          170             False
2           3    Male  27.5             130          210              True
3           4  Female  23.1             115          190             False
4           5    Male  29.2             140          220              True
```

---

### Quick Recap of Key Tools You Used

- **NumPy**
  - `np.array`, vectorised arithmetic (`+ - * / **`)
  - `np.mean`, `np.std`, `np.median`, `np.where`
  - Boolean indexing (`arr[arr > x]`), fancy indexing (`arr[[i,j,k]]`)
  - Matrix multiply (`@`), `.ravel()`

- **Pandas**
  - `pd.DataFrame`, `.to_csv`, `pd.read_csv`, `.head()`
  - Column selection, `.mean()`, `.groupby(...).mean()`
  - Missing data: `.isnull()`, `.fillna(...)`

Happy practicing! 🎓
