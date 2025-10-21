# Getting Started with pandas — Beginner Guide (with Examples & Exercises)

> Quick setup used throughout:
```python
import numpy as np        # numerical arrays & math
import pandas as pd       # tables (Series, DataFrame)
```
All code examples are pure Python; you can run them in Jupyter, VS Code, or any Python REPL.

---

## 1) Two core objects: `Series` and `DataFrame`

### 1.1 `pd.Series`
A **Series** is a one-dimensional, labeled array.

```python
s = pd.Series([4, 7, -5, 3])      # values only → default index 0..N-1
print(s)
print("values as a numpy array:", s.to_numpy())
print("index labels:", s.index)
```
**What we used**
- `pd.Series(seq)`: builds a Series.
- `.to_numpy()`: returns underlying NumPy array.
- `.index`: the index (labels) of the Series.

**Typical output**
```
0    4
1    7
2   -5
3    3
dtype: int64
values as a numpy array: [ 4  7 -5  3]
index labels: RangeIndex(start=0, stop=4, step=1)
```

You can give your own labels:
```python
s2 = pd.Series([4, 7, -5, 3], index=["d", "b", "a", "c"])
print(s2["a"])             # label lookup → -5
s2["d"] = 6                # assignment by label
print(s2[["c", "a", "d"]]) # list of labels
```

**What we used**
- `[]` with a **label** or list of labels to select.
- Assignment to a label to change a value.

---

### 1.2 `pd.DataFrame`
A **DataFrame** is a 2D table of columns (each column is a Series).

```python
data = {
    "state": ["Ohio", "Ohio", "Nevada"],
    "year":  [2000,   2001,   2002   ],
    "pop":   [1.5,    1.7,    2.4    ],
}
df = pd.DataFrame(data)
print(df)
print(df.head())  # first 5 rows
print(df.tail())  # last 5 rows
```
**What we used**
- `pd.DataFrame(dict_of_equal_length_lists)`: builds a DataFrame.
- `.head()`, `.tail()`: first/last rows (default 5).

**Typical output**
```
    state  year  pop
0    Ohio  2000  1.5
1    Ohio  2001  1.7
2  Nevada  2002  2.4
```

Select a **column** (as Series) or **row** (as Series) or a **block**:
```python
print(df["state"])      # column by name → Series
print(df.year)          # dot-access if name is a valid identifier
print(df.loc[1])        # row by label (index label 1 here)
print(df.iloc[2])       # row by integer position
```
**What we used**
- `df["col"]` or `df.col`
- `.loc[row_label]` (label-based)
- `.iloc[row_pos]` (integer position)

---

## 2) Missing data & checking membership

```python
sdata = {"Ohio": 35000, "Texas": 71000, "Oregon": 16000}
states = ["California", "Ohio", "Oregon", "Texas"]
s3 = pd.Series(sdata, index=states)  # custom order; missing → NaN
print(s3)
print(pd.isna(s3))    # True where missing
print(pd.notna(s3))   # inverse
```
**What we used**
- `pd.isna(obj)`, `pd.notna(obj)`: detect missing values (NaNs).

**Typical output**
```
California        NaN
Ohio          35000.0
Oregon        16000.0
Texas         71000.0
dtype: float64
California     True
Ohio          False
Oregon        False
Texas         False
dtype: bool
```

---

## 3) Alignment & arithmetic (labels matter!)

Series and DataFrames **align by labels** during arithmetic.

```python
s1 = pd.Series([7.3, -2.5, 3.4, 1.5], index=["a", "c", "d", "e"])
s2 = pd.Series([-2.1, 3.6, -1.5, 4, 3.1], index=["a", "c", "e", "f", "g"])
print(s1 + s2)   # aligns on labels; non-overlaps → NaN
```
**Typical output**
```
a    5.2
c    1.1
d    NaN
e    0.0
f    NaN
g    NaN
dtype: float64
```

**Fill missing during arithmetic**:
```python
df1 = pd.DataFrame(np.arange(12.).reshape(3,4), columns=list("abcd"))
df2 = pd.DataFrame(np.arange(20.).reshape(4,5), columns=list("abcde"))
df2.loc[1, "b"] = np.nan

print(df1.add(df2, fill_value=0))      # treats missing as 0 for the operation
```
**What we used**
- `.add(other, fill_value=…)`: arithmetic with fill; also `sub`, `mul`, `div`, etc.

---

## 4) Reindexing & dropping

**Reindex** = reorder rows/cols by new labels (inserting missing if needed):
```python
s = pd.Series([4.5, 7.2, -5.3, 3.6], index=["d", "b", "a", "c"])
print(s.reindex(["a", "b", "c", "d", "e"]))  # 'e' → NaN
```

**Forward-fill** when reindexing ordered data:
```python
s2 = pd.Series(["blue", "purple", "yellow"], index=[0, 2, 4])
print(s2.reindex(range(6), method="ffill"))
```

**Drop** rows/columns:
```python
df = pd.DataFrame(np.arange(16).reshape(4,4),
                  index=["Ohio", "Colorado", "Utah", "New York"],
                  columns=["one", "two", "three", "four"])
print(df.drop(index=["Colorado", "Ohio"]))
print(df.drop(columns=["two"]))
```
**What we used**
- `.reindex(new_index, method=…)`
- `.drop(index=[...])`, `.drop(columns=[...])`

---

## 5) Selection: `loc` and `iloc` (avoid confusion)

- `df.loc[rows, cols]` uses **labels**
- `df.iloc[rows, cols]` uses **integer positions**

```python
data = pd.DataFrame(np.arange(16).reshape(4,4),
                    index=["Ohio","Colorado","Utah","New York"],
                    columns=["one","two","three","four"])
print(data.loc["Colorado", ["two", "three"]])
print(data.iloc[[1, 2], [3, 0, 1]])
```

**Boolean filtering**:
```python
print(data[data["three"] > 5])      # rows where column 'three' > 5
mask = data < 5
data2 = data.copy()
data2[mask] = 0                     # set those entries to 0
print(data2)
```

> **Tip:** Avoid *chained indexing* like `df[df.cond]["col"] = ...`. Prefer a single `.loc[...]`:
```python
# Good:
data.loc[data["three"] == 5, "three"] = 6
```

---

## 6) Apply functions column-wise or row-wise

```python
frame = pd.DataFrame(np.random.standard_normal((4,3)),
                     columns=list("bde"),
                     index=["Utah", "Ohio", "Texas", "Oregon"])

def spread(x):               # x is a Series (a column if axis=0)
    return x.max() - x.min()

print(frame.apply(spread))                 # default axis=0 (by column)
print(frame.apply(spread, axis="columns")) # by row
print(np.abs(frame))                       # NumPy ufunc works element-wise
```

**Element-wise formatting**
```python
def fmt(x): return f"{x:.2f}"
print(frame.applymap(fmt))         # DataFrame element-wise
print(frame["e"].map(fmt))         # Series element-wise
```
**What we used**
- `.apply(func, axis=...)`: apply a function per column/row.
- `.applymap(func)`: DataFrame element-wise.
- `.map(func)`: Series element-wise.
- `np.abs(df)`: NumPy ufunc works on pandas objects.

---

## 7) Sorting & ranking

```python
obj = pd.Series([4, 7, -3, 2, np.nan])
print(obj.sort_values(na_position="first"))  # NaNs first

frame = pd.DataFrame({"b": [4, 7, -3, 2], "a": [0, 1, 0, 1]})
print(frame.sort_values(["a", "b"]))        # multi-column sort

print(obj.rank())                           # average ranks by default
print(obj.rank(method="first"))           # tie-break by order of appearance
```

**What we used**
- `.sort_values(by=..., ascending=..., na_position=...)`
- `.rank(method=...)`

---

## 8) Descriptive statistics & summaries

```python
df = pd.DataFrame([[1.4, np.nan],
                   [7.1, -4.5],
                   [np.nan, np.nan],
                   [0.75, -1.3]],
                  index=list("abcd"),
                  columns=["one", "two"])

print(df.sum())                          # column-wise sum
print(df.sum(axis="columns"))            # row-wise sum
print(df.mean())                         # mean (skipna=True by default)
print(df.mean(axis="columns"))
print(df.idxmax())                       # index of max per column
print(df.cumsum())                       # cumulative sums
print(df.describe())                     # summary table
```
**What we used**
- `.sum()`, `.mean()`, `.idxmax()`, `.cumsum()`, `.describe()`
- `axis="columns"` (rows) vs default `axis="index"` (columns)
- `skipna=False` if you want NaNs to propagate

---

## 9) Correlation, covariance

```python
# Small example: make up prices → returns
prices = pd.DataFrame({
    "AAA": [10.0, 10.5, 10.2, 10.4, 10.3],
    "BBB": [20.0, 19.7, 20.2, 20.4, 20.1],
})
returns = prices.pct_change()              # percent change row-wise

print(returns.corr())                      # correlation matrix
print(returns.cov())                       # covariance matrix
print(returns["AAA"].corr(returns["BBB"])) # correlation of 2 Series
```
**What we used**
- `.pct_change()`: percent change
- `.corr()`, `.cov()` on DataFrame/Series

---

## 10) Unique values, counts, membership

```python
obj = pd.Series(["c","a","d","a","a","b","b","c","c"])
print(obj.unique())              # unique values (array)
print(obj.value_counts())        # frequencies (Series, sorted desc)
print(obj.isin(["b","c"]))       # Boolean membership per element
print(obj[obj.isin(["b","c"])])  # filter by membership
```
**What we used**
- `.unique()`, `.value_counts()`, `.isin(iterable)`

---

## Mini-Exercises (with solutions)

### Exercise A — Build a Series and select by labels
**Question:** Create a Series `s = [4, 7, -5, 3]` with index `["d","b","a","c"]`.
1) Select the value for label `"a"`.
2) Double all positive values using boolean filtering.

**Solution**
```python
s = pd.Series([4, 7, -5, 3], index=["d","b","a","c"])
print("a →", s["a"])                 # selection by label
s2 = s.copy()
s2[s2 > 0] = s2[s2 > 0] * 2          # boolean filtering + assignment
print(s2)
```
**Expected output (typical)**
```
a → -5
d     8
b    14
a    -5
c     6
dtype: int64
```

---

### Exercise B — DataFrame selection and assignment with `loc`
**Question:** From the DataFrame below, set column `"three"` to `0` for rows where `"two" < 5` **using one `.loc[...]`** (no chained indexing):
```python
df = pd.DataFrame(np.arange(16).reshape(4,4),
                  index=["Ohio","Colorado","Utah","New York"],
                  columns=["one","two","three","four"])
```
**Solution**
```python
df2 = df.copy()
df2.loc[df2["two"] < 5, "three"] = 0
print(df2.head())
```

---

### Exercise C — Reindex with forward-fill
**Question:** Create `s = ["blue","purple","yellow"]` at indices `[0,2,4]`. Reindex to `0..5` and **forward-fill** the gaps.

**Solution**
```python
s = pd.Series(["blue","purple","yellow"], index=[0,2,4])
print(s.reindex(range(6), method="ffill"))
```
**Expected output**
```
0      blue
1      blue
2    purple
3    purple
4    yellow
5    yellow
dtype: object
```

---

### Exercise D — Apply column-wise function
**Question:** On a random 4×3 DataFrame, compute (max − min) for each column using `.apply`.

**Solution**
```python
np.random.seed(0)
frame = pd.DataFrame(np.random.standard_normal((4,3)),
                     columns=list("bde"))

def spread(x): return x.max() - x.min()
print(frame.apply(spread))
```

---

### Exercise E — Value counts across columns
**Question:** For
```python
data = pd.DataFrame({"Qu1": [1,3,4,3,4],
                     "Qu2": [2,3,1,2,3],
                     "Qu3": [1,5,2,4,4]})
```
Compute value counts for **each column** and combine into one table (missing → 0).

**Solution**
```python
result = data.apply(pd.value_counts).fillna(0)
print(result.sort_index())
```

**What we used**
- `DataFrame.apply(pd.value_counts)`: apply per column
- `.fillna(0)`: replace NaN with 0
- `.sort_index()`: sort by row index

---

## Common gotchas (and fixes)

- **Chained indexing** warning:  Do **not** write `df[df.cond]["col"] = ...`. Use one `.loc[row_cond, "col"] = ...`.
- **Integer labels** vs positions:  Always use `.loc` (labels) and `.iloc` (positions) to avoid ambiguity.
- **Alignment surprises**:  When adding/multiplying items with different labels, unmatched labels → NaN.  Use `.add(..., fill_value=0)` if you want “treat missing as 0”.

---

## Tiny “Why/when” recap of functions we used

- **`pd.Series`, `pd.DataFrame`**: create 1D/2D labeled data.
- **`.head()`, `.tail()`**: quick peek at top/bottom rows.
- **`.index`, `.columns`**: labels.
- **`pd.isna`, `pd.notna`**: check missing.
- **`.reindex()`**: reorder to new labels (can `ffill`).
- **`.drop(index=..., columns=...)`**: remove labels.
- **`.loc`, `.iloc`**: robust selection by label / by position.
- **Boolean masks**: `df[df["col"] > 0]`.
- **`.apply`, `.applymap`, `.map`**: apply functions by column/row / element-wise.
- **`.sort_values`, `.sort_index`**: sort by values / labels.
- **`.rank()`**: ranking with tie strategies (`method="first"`, `"min"`, etc.).
- **`.sum`, `.mean`, `.idxmax`, `.cumsum`, `.describe`**: descriptive stats.
- **`.corr`, `.cov`, `.pct_change`**: relationships and returns.
- **`.unique`, `.value_counts`, `.isin`**: unique values, counts, membership.
- **Arithmetic with fill**: `.add(other, fill_value=0)`.
