# Basic NumPy — Beginner Cheat Sheet

A concise starter kit covering the essentials you’ll use every day. Each section has:
- What it is (simple words)
- Key functions / syntax
- A short code snippet **with expected output**
- A **Try it** task

> Tip: `import numpy as np` is the standard alias.

---

## 1) Install & Import

```python
import numpy as np
np.__version__
```
**Expected output (example):**
```
'1.26.4'
```

**Try it:** Print the version and confirm it runs.

---

## 2) Create Arrays

An `ndarray` is a fast, typed, multi-dimensional container for numbers.

**Key functions**
- `np.array(seq, dtype=...)` → from Python list/tuple
- `np.zeros(shape)`, `np.ones(shape)`, `np.full(shape, fill)`
- `np.arange(start, stop, step)` → like `range` but array
- `np.linspace(start, stop, num)` → evenly spaced values
- `np.eye(n)` → identity matrix

```python
import numpy as np

a = np.array([1, 2, 3])                  # 1D
b = np.array([[1, 2, 3], [4, 5, 6]])     # 2D
z = np.zeros((2, 3))
o = np.ones((2, 3))
f = np.full((2, 3), 7)
r = np.arange(0, 10, 2)                  # [0 2 4 6 8]
l = np.linspace(0, 1, 5)                 # [0.  0.25 0.5 0.75 1. ]
i = np.eye(3)

print(a, a.ndim, a.shape)
print(b, b.ndim, b.shape)
```
**Expected output:**
```
[1 2 3] 1 (3,)
[[1 2 3]
 [4 5 6]] 2 (2, 3)
```

**Try it:** Make a 3×4 array of fives with `np.full` and check its `ndim` and `shape`.

---

## 3) Dtypes (data types)

Arrays have a single type (for speed): `int64`, `float64`, `bool`, etc.

**Inspect & convert**
- `.dtype` → see type
- `.astype(new_dtype)` → convert

```python
x = np.array([1, 2, 3], dtype=np.float32)
print(x.dtype)          # float32
y = x.astype(np.int64)
print(y.dtype)          # int64
```

**Try it:** Create a boolean array from `[0, 1, 2, 0]` by comparing `> 0`.

---

## 4) Inspecting arrays

**Handy attributes**
- `.ndim`, `.shape`, `.size`, `.dtype`
- `.itemsize` (bytes per element), `.nbytes` (total bytes)

```python
m = np.arange(12).reshape(3,4)
print(m)
print(m.ndim, m.shape, m.size)
print(m.itemsize, m.nbytes)
```
**Expected output (example):**
```
[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]]
2 (3, 4) 12
8 96
```

**Try it:** Build a 2×2 float array and print `itemsize` and `nbytes`.

---

## 5) Indexing & Slicing

Pick elements/rows/columns efficiently.

```python
A = np.array([[10,11,12],
              [20,21,22],
              [30,31,32]])

print(A[0, 1])     # 11
print(A[1])        # [20 21 22]
print(A[:, 0])     # [10 20 30]
print(A[0:2, 1:3]) # [[11 12],[21 22]]
```

**Try it:** From `A`, get the last two rows and the last column using slices.

---

## 6) Boolean Masking (filter by condition)

Select values matching a condition.

```python
v = np.array([3, 6, 1, 9, 2, 8])
mask = v > 4
print(mask)       # [False  True False  True False  True]
print(v[mask])    # [6 9 8]

# combine conditions with & (and), | (or), ~ (not)
print(v[(v > 2) & (v % 2 == 0)])  # [6 8]
```

**Try it:** From `np.arange(1,21)`, select numbers divisible by 3 or 5.

---

## 7) Fancy Indexing (by integer arrays)

Pick arbitrary positions in chosen order.

```python
w = np.array([10, 20, 30, 40, 50])
idx = np.array([4, 0, 3])
print(w[idx])   # [50 10 40]
```

**Try it:** From a 3×3 array, select elements at positions (0,0), (1,2), (2,1) using two index arrays.

---

## 8) Vectorised Operations (element-wise)

Fast math without loops.

Operators: `+ - * / // % **` plus comparisons.

```python
a = np.array([1, 2, 3])
b = np.array([10, 20, 30])
print(a + b)      # [11 22 33]
print(a * b)      # [10 40 90]
print(b / a)      # [10. 10. 10.]
print(a ** 2)     # [1 4 9]
```

**Try it:** Compute `(a*b) + (b//a)` for `a=[2,4,5]`, `b=[9,8,7]`.

---

## 9) Broadcasting

NumPy stretches shapes to match for element-wise ops (trailing dims match or are `1`).

```python
M = np.arange(6).reshape(2,3)   # [[0,1,2],[3,4,5]]
v = np.array([10, 100, 1000])
print(M + v)
# [[ 10 101 1002]
#  [ 13 104 1005]]

col = np.array([[1],[2]])  # shape (2,1)
print(M + col)
# [[1 2 3]
#  [5 6 7]]
```

**Try it:** Add a 1D array of length 4 to a 2×4 matrix and explain why it works.

---

## 10) Universal Functions (ufuncs)

Fast element-wise math functions.

Common: `np.sqrt`, `np.exp`, `np.log`, `np.sin`, `np.cos`, `np.maximum`, …

```python
x = np.array([1, 4, 9, 16], dtype=float)
print(np.sqrt(x))       # [1. 2. 3. 4.]
print(np.log(x))        # [0. 1.386... 2.197... 2.772...]
print(np.maximum(x, 5)) # [5. 5. 9. 16.]
```

**Try it:** Given `x=[-1,0,1]`, compute `np.exp(x) / (1 + np.exp(x))` (sigmoid).

---

## 11) Reductions & Stats (along axes)

Aggregate to a single number per array or per axis.

Key: `sum`, `mean`, `std`, `var`, `min`, `max`, `argmin`, `argmax`

- `axis=None` (default) → entire array  
- `axis=0` → down columns  
- `axis=1` → across rows

```python
A = np.arange(1,7).reshape(2,3)  # [[1,2,3],[4,5,6]]
print(A.sum())           # 21
print(A.sum(axis=0))     # [5 7 9]
print(A.mean(axis=1))    # [2. 5.]
print(A.argmax(axis=1))  # [2 2]
```

**Try it:** For `A` above, compute column-wise standard deviation.

---

## 12) NaN-safe ops

Handle missing values (`np.nan`) safely with `nan*` functions.

```python
x = np.array([1.0, np.nan, 3.0, np.nan, 5.0])
print(np.mean(x))      # nan
print(np.nanmean(x))   # 3.0 (ignores NaN)
```

**Try it:** Replace NaNs with the column means using `np.where(np.isnan(x), fill, x)`.

---

## 13) Reshaping, Ravel/Flatten, Transpose

- `.reshape(new_shape)` (same total size)
- `.ravel()` (view) / `.flatten()` (copy) → 1D
- `.T` → transpose

```python
B = np.arange(12)
C = B.reshape(3,4)
print(C.T)
print(C.ravel())
```
**Expected output:**
```
[[ 0  4  8]
 [ 1  5  9]
 [ 2  6 10]
 [ 3  7 11]]
[ 0  1  2  3  4  5  6  7  8  9 10 11]
```

**Try it:** Create a 2×3 matrix, transpose to 3×2, then flatten to 1D.

---

## 14) Stacking & Splitting

- `np.concatenate([a,b], axis=...)`
- `np.vstack([a,b])`, `np.hstack([a,b])`
- `np.split(arr, indices, axis=...)`

```python
x = np.array([[1,2],[3,4]])
y = np.array([[5,6],[7,8]])

print(np.vstack([x,y]))
print(np.hstack([x,y]))
```
**Expected output:**
```
[[1 2]
 [3 4]
 [5 6]
 [7 8]]
[[1 2 5 6]
 [3 4 7 8]]
```

**Try it:** Concatenate two 1D arrays and then split back into two equal halves.

---

## 15) Sorting & Argsort

- `np.sort(a, axis=-1)` → returns sorted copy
- `a.sort(axis=-1)` → in-place
- `np.argsort(a)` → indices that would sort

```python
t = np.array([3,1,4,1,5])
print(np.sort(t))     # [1 1 3 4 5]
idx = np.argsort(t)
print(idx)            # e.g. [1 3 0 2 4]
print(t[idx])         # sorted view
```

**Try it:** Sort rows of a 2D array by the values in column 1 (use `argsort` on that column, then reorder rows).

---

## 16) Unique & Set Ops

- `np.unique(a)` → sorted unique values
- `np.unique(a, return_counts=True)` → plus counts
- `np.intersect1d`, `np.union1d`, `np.setdiff1d`

```python
u, counts = np.unique([1,2,2,3,3,3], return_counts=True)
print(u)       # [1 2 3]
print(counts)  # [1 2 3]
```

**Try it:** Find elements in `[1,2,3,4]` that are *not* in `[2,4,6]` using `np.setdiff1d`.

---

## 17) Random numbers (Generator API)

Modern API:
- `rng = np.random.default_rng(seed)`
- `rng.integers(low, high, size)`
- `rng.random(size)` → uniform [0,1)
- `rng.normal(loc, scale, size)`

```python
rng = np.random.default_rng(42)
print(rng.integers(0, 10, size=5))    # e.g. [7 4 7 9 3]
print(rng.random(3))                  # e.g. [0.77 0.44 0.86]
print(rng.normal(0, 1, size=(2,3)))   # 2x3 Gaussian
```

**Try it:** Create a 1000-sample normal array (mean 100, sd 15) and print its mean and std.

---

## 18) Linear Algebra (quick taste)

- Matrix multiply: `A @ B` or `np.matmul(A,B)`
- Transpose: `A.T`
- Inverse: `np.linalg.inv(A)` (square, non-singular)
- Solve Ax=b: `np.linalg.solve(A, b)`

```python
A = np.array([[3, 1],
              [2, 4]])
b = np.array([7, 10])
x = np.linalg.solve(A, b)
print(x)   # solution vector
```
**Try it:** Verify that `A @ x` equals `b` (within tiny floating error).

---

## 19) Save / Load

- `np.save('file.npy', arr)` / `np.load('file.npy')`
- `np.savetxt('file.csv', arr, delimiter=',')` / `np.loadtxt('file.csv', delimiter=',')`

```python
arr = np.arange(6).reshape(2,3)
np.save('myarr.npy', arr)
arr2 = np.load('myarr.npy')
print(arr2)
```
**Expected output:**
```
[[0 1 2]
 [3 4 5]]
```

**Try it:** Save a random 3×3 matrix to CSV, load it back, check equality (allow tiny float diffs).

---

## 20) Performance tips (just to know)

- Prefer **vectorized** operations (avoid Python loops).
- Keep arrays in one **dtype**.
- Use **broadcasting** instead of manual loops.
- For huge workloads: later explore `numexpr`, Numba, or CuPy (GPU).

---

### Mini Practice Set (5 quick checks)

1) Create a 4×4 array with values 0..15, then:
   - select the last column,
   - compute the mean of rows,
   - get elements > 7.

2) Use broadcasting to subtract the column means from each column.

3) Generate 10,000 standard normal numbers; report mean and std (should be ~0 and ~1).

4) Given `a=[1,2,3]`, `b=[4,5,6]`, build a 3×3 matrix `a[:,None] * b[None,:]` (outer product).

5) Make an array with NaNs and compute `nanmean`, then fill NaNs with the column means.
