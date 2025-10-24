# NumPy Basics: Arrays & Vectorized Computation 

A friendly, example‑driven guide to NumPy. Every section includes **clear code snippets**, **typical outputs**, and **mini‑exercises with solutions**. Perfect for beginners and GitHub‑friendly.

---

## Table of Contents
- [1) Creating arrays](#1-creating-arrays)
- [2) Data types & casting](#2-data-types--casting)
- [3) Vectorized arithmetic & comparisons](#3-vectorized-arithmetic--comparisons)
- [4) Indexing & slicing (views!)](#4-indexing--slicing-views)
- [5) Boolean indexing (filters)](#5-boolean-indexing-filters)
- [6) Fancy indexing (integer arrays)](#6-fancy-indexing-integer-arrays)
- [7) Transpose & swap axes](#7-transpose--swap-axes)
- [8) Random numbers (Generator API)](#8-random-numbers-generator-api)
- [9) Universal functions (ufuncs)](#9-universal-functions-ufuncs)
- [10) Conditional logic with `np.where`](#10-conditional-logic-with-npwhere)
- [11) Stats & reductions](#11-stats--reductions)
- [12) Sorting & set logic](#12-sorting--set-logic)
- [13) File I/O for arrays](#13-file-io-for-arrays)
- [14) Linear algebra (matrix math)](#14-linear-algebra-matrix-math)
- [15) Example: random walk (vectorized)](#15-example-random-walk-vectorized)
- [Cheat-sheet: shapes & axes](#cheat-sheet-shapes--axes)
- [Function glossary (what we used)](#function-glossary-what-we-used)

> **Import convention** (used throughout):
>
> ```python
> import numpy as np
> ```

---

## 1) Creating arrays

```python
import numpy as np

# From a Python list
arr1 = np.array([6, 7.5, 8, 0, 1])
print(arr1)       # [6.  7.5 8.  0.  1. ]
print(arr1.dtype) # float64 (NumPy picked a float dtype)

# From nested lists (2D array)
arr2 = np.array([[1, 2, 3, 4],
                 [5, 6, 7, 8]])
print(arr2)
# [[1 2 3 4]
#  [5 6 7 8]]

print(arr2.ndim, arr2.shape)  # 2 (dims), (2, 4) (rows, columns)

# Zeros/ones/empty
np.zeros(5)             # [0. 0. 0. 0. 0.]
np.ones((2, 3))         # [[1. 1. 1.],[1. 1. 1.]]
np.empty((2, 2))        # uninitialized (don’t rely on values)

# Ranges
np.arange(6)            # [0 1 2 3 4 5]
```

**What those functions mean**  
- `np.array(seq)` converts a (nested) sequence to an ndarray.  
- `.dtype` = data type (e.g., `int32`, `float64`).  
- `.ndim` = number of dimensions; `.shape` = size per dimension.  
- `np.zeros/ones/empty(shape)` create arrays.  
- `np.arange(n)` like `range` but returns an array.

**Exercise 1** — *Create & reshape*  
**Task**: Make an array of 9 zeros, reshape to 3×3, set center to 5.  
**Solution**:
```python
a = np.zeros(9).reshape(3, 3)
a[1, 1] = 5
print(a)
# [[0. 0. 0.]
#  [0. 5. 0.]
#  [0. 0. 0.]]
```

---

## 2) Data types & casting

```python
arr = np.array([1, 2, 3], dtype=np.float64)
print(arr.dtype)          # float64

arr_i = arr.astype(np.int32)  # cast (copy) to int32
print(arr_i, arr_i.dtype)     # [1 2 3] int32

s = np.array(["1.25", "-9.6", "42"])
print(s.astype(float))    # [ 1.25  -9.6  42.  ]
```

**Meaning**  
- `dtype=` sets the type; `astype(new_dtype)` converts (and copies).

**Exercise 2** — *Casting*  
**Task**: Convert `np.array([3.7, -1.2, 0.0])` to integers.  
**Solution**:
```python
x = np.array([3.7, -1.2, 0.0]).astype(np.int32)
print(x)   # [ 3 -1  0]  (decimals truncated)
```

---

## 3) Vectorized arithmetic & comparisons

```python
arr = np.array([[1., 2., 3.],
                [4., 5., 6.]])

print(arr * arr)
# [[ 1.  4.  9.]
#  [16. 25. 36.]]

print(1 / arr)
# [[1.     0.5    0.3333]
#  [0.25   0.2    0.1667]]

arr2 = np.array([[0., 4., 1.],
                 [7., 2., 12.]])
print(arr2 > arr)
# [[False  True False]
#  [ True False  True]]
```

No loops. NumPy applies operations **element-wise**.

**Exercise 3** — *BMI*  
**Task**: `w=[60,70,80]` kg, `h=[1.7,1.75,1.8]` m → BMI = w / h**2.  
**Solution**:
```python
w = np.array([60,70,80])
h = np.array([1.7,1.75,1.8])
bmi = w / (h ** 2)
print(np.round(bmi, 2))  # [20.76 22.86 24.69]
```

---

## 4) Indexing & slicing (views!)

```python
arr = np.arange(10)
print(arr[5])       # 5
print(arr[5:8])     # [5 6 7]

sl = arr[5:8]
#The colon [:] means “select the whole array”
sl[:] = 99          # modifies the original (slices are VIEWS)
print(arr)          # [0 1 2 3 4 99 99 99 8 9]
```

2D indexing:

```python
arr2d = np.array([[1,2,3],
                  [4,5,6],
                  [7,8,9]])

print(arr2d[0, 2])     # 3
print(arr2d[:2, 1:])   # [[2 3],[5 6]]
```

> **Tip**: Slices don’t copy. Use `.copy()` if you need an independent copy.

**Exercise 4** — *Slice & assign*  
**Task**: Zero out the top-right 2×2 block of `arr2d`.  
**Solution**:
```python
arr2d[:2, 1:] = 0
print(arr2d)
# [[1 0 0]
#  [4 0 0]
#  [7 8 9]]
```

---

## 5) Boolean indexing (filters)

```python
names = np.array(["Bob","Joe","Will","Bob","Will","Joe","Joe"])
data  = np.array([[ 4,  7],
                  [ 0,  2],
                  [-5,  6],
                  [ 0,  0],
                  [ 1,  2],
                  [-12,-4],
                  [ 3,  4]])

mask = (names == "Bob")          # [ True False False  True False False False]
print(data[mask])
# [[4 7]
#  [0 0]]

print(data[(names=="Bob") | (names=="Will")])
```
Use `&` (and), `|` (or), `~` (not) with Boolean arrays.

**Exercise 5** — *Clamp negatives*  
**Task**: Set all negative entries in `data` to 0.  
**Solution**:
```python
data[data < 0] = 0
print(data)
```

---

## 6) Fancy indexing (integer arrays)

```python
arr = np.arange(32).reshape(8, 4)
print(arr[[1, 5, 7, 2]])         # pick rows by order

print(arr[[1,5,7,2], [0,3,1,2]]) # elements (1,0), (5,3), (7,1), (2,2)
# [ 4 23 29 10]

# Rectangular subset in new order:
arr[[1,5,7,2]][:, [0,3,1,2]]

#arr[[1, 5, 7, 2]] → row fancy indexing: picks rows 1, 5, 7, and 2 in that order (reorders the rows).
#[:, [0, 3, 1, 2]] → from that result, picks columns 0, 3, 1, 2 (reorders the columns).
# So you end up with a 4×4 array formed by those four rows and four columns, both reordered.
# The space between ]] and [ is fine—this is just two consecutive indexing operations.
```




> **Note**: Fancy indexing returns a **copy**, unlike slices.

**Exercise 6** — *Pick rows+cols*  
**Task**: 3×2 array from rows `[0,3,5]`, cols `[1,3]`.  
**Solution**:
```python
subset = arr[[0,3,5]][:, [1,3]]
print(subset)
```

---

## 7) Transpose & swap axes

```python
m = np.arange(15).reshape(3,5)
print(m.T.shape)   # (5, 3)
```

- `.T` returns a (usually) zero‑copy **view**.
- `swapaxes(a, b)` swaps two axes (great for >2D arrays).

**Exercise 7** — *AᵀA*  
**Task**: `A = [[0,1,0],[1,2,-2]]`, compute `A.T @ A`.  
**Solution**:
```python
A = np.array([[0,1,0],[1,2,-2]])
print(A.T @ A)
# [[ 1  2 -2]
#  [ 2  5 -4]
#  [-2 -4  4]]
```

---

## 8) Random numbers (Generator API)

```python
rng = np.random.default_rng(seed=12345)
rng.integers(0, 10, size=5)
rng.standard_normal((2,3))
rng.uniform(0, 1, size=4)
```

**Exercise 8** — *Column means*  
**Task**: 4×4 standard normal → compute column means.  
**Solution**:
```python
rng = np.random.default_rng(0)
X = rng.standard_normal((4,4))
print(X.mean(axis=0))
```

---

## 9) Universal functions (ufuncs)

```python
arr = np.arange(10)
np.sqrt(arr)         # element-wise sqrt
np.exp(arr)          # element-wise e**x

x = rng.standard_normal(5)
y = rng.standard_normal(5)
np.maximum(x, y)     # element-wise max

a = rng.standard_normal(5) * 5
frac, whole = np.modf(a)  # fractional & integer parts
```

You can also use the `out=` parameter to avoid extra allocations:
```python
out = np.empty_like(arr, dtype=float)
np.add(arr, 1, out=out)
```

**Exercise 9** — *abs & sign*  
**Task**: For `x=[-1.5,0,2.3]`, return `abs(x)` and `sign(x)`.  
**Solution**:
```python
x = np.array([-1.5, 0, 2.3])
print(np.abs(x))   # [1.5 0.  2.3]
print(np.sign(x))  # [-1  0  1]
```

---

## 10) Conditional logic with `np.where`

```python
x = np.array([1.1,1.2,1.3,1.4,1.5])
y = np.array([2.1,2.2,2.3,2.4,2.5])
cond = np.array([True, False, True, True, False])

np.where(cond, x, y)   # [1.1 2.2 1.3 1.4 2.5]
```

Replace only positives with 2:
```python
A = rng.standard_normal((3,3))
np.where(A > 0, 2, A)
```

**Exercise 10** — *Clamp negatives to -1*  
**Task**: `z=[-2,-0.1,0.0,3.5]` → negatives to `-1`, others unchanged.  
**Solution**:
```python
z = np.array([-2, -0.1, 0.0, 3.5])
print(np.where(z < 0, -1, z))  # [-1.  -1.   0.   3.5]
```

---

## 11) Stats & reductions

```python
A = rng.standard_normal((5,4))
A.mean()              # scalar mean
A.sum(axis=0)         # column sums
A.mean(axis=1)        # row means

v = np.arange(8)
v.cumsum()            # [0 1 3 6 10 15 21 28]
```

Booleans:
```python
x = rng.standard_normal(100)
(x > 0).sum()   # count positives
```

**Exercise 11** — *Count positives*  
**Task**: Count how many positive numbers in 100 N(0,1) samples.  
**Solution**:
```python
x = rng.standard_normal(100)
print((x > 0).sum())
```

---

## 12) Sorting & set logic

```python
a = rng.standard_normal(6)
a.sort()                 # in place

b = np.array([5, -10, 7, 1])
np.sort(b)               # sorted copy

names = np.array(["Bob","Will","Joe","Bob"])
np.unique(names)         # ['Bob' 'Joe' 'Will']

vals = np.array([6,0,0,3,2,5,6])
np.in1d(vals, [2,3,6])   # [ True False False  True  True False  True]
```

**Exercise 12** — *Unique counts*  
**Task**: For `x=[3,3,2,1,2,3,1]` show sorted unique values and their counts.  
**Solution**:
```python
x = np.array([3,3,2,1,2,3,1])
u, counts = np.unique(x, return_counts=True)
print(u)       # [1 2 3]
print(counts)  # [2 2 3]
```

---

## 13) File I/O for arrays

```python
arr = np.arange(5)
np.save("my_array.npy", arr)           # save binary .npy
loaded = np.load("my_array.npy")

np.savez("stack.npz", a=arr, b=arr*2)  # multiple arrays
arch = np.load("stack.npz")
print(arch["b"])                       # [0 2 4 6 8]
```

**Exercise 13** — *Identity save/load*  
**Task**: Save a 2×2 identity matrix and load it back.  
**Solution**:
```python
I = np.eye(2)                 # [[1. 0.],[0. 1.]]
np.save("I.npy", I)
print(np.load("I.npy"))
```

---

## 14) Linear algebra (matrix math)

```python
X = np.array([[1., 2., 3.],
              [4., 5., 6.]])
Y = np.array([[ 6., 23.],
              [-1.,  7.],
              [ 8.,  9.]])
print(X @ Y)
# [[ 28.  64.]
#  [ 67. 181.]]

from numpy.linalg import inv, qr
M = np.array([[2., 0.],
              [0., 2.]])
print(inv(M))       # [[0.5 0. ]
                    #  [0.  0.5]]
Q, R = qr(np.random.default_rng(0).standard_normal((3,3)))
```

**Exercise 14** — *Inverse check*  
**Task**: Verify `A @ inv(A)` ≈ identity for random 3×3 `A`.  
**Solution**:
```python
rng = np.random.default_rng(0)
A = rng.standard_normal((3,3))
Ai = np.linalg.inv(A)
print(np.round(A @ Ai, 6))   # close to identity
```

---

## 15) Example: random walk (vectorized)

**Single walk**
```python
nsteps = 1000
rng = np.random.default_rng(123)
draws = rng.integers(0, 2, size=nsteps)     # 0/1 coin flips
steps = np.where(draws == 0, 1, -1)         # map to +1/-1
walk  = steps.cumsum()
print(walk.min(), walk.max())               # e.g., -8 50
```

**Many walks at once**
```python
nwalks, nsteps = 5000, 1000
draws = rng.integers(0, 2, size=(nwalks, nsteps))
steps = np.where(draws == 0, 1, -1)
walks = steps.cumsum(axis=1)

hits30 = (np.abs(walks) >= 30).any(axis=1)
crossing_times = (np.abs(walks[hits30]) >= 30).argmax(axis=1)
print(hits30.sum(), crossing_times.mean())
```

**Exercise 15** — *Threshold fraction*  
**Task**: Simulate 100 walks of 500 steps; fraction that ever exceed +20.  
**Solution**:
```python
rng = np.random.default_rng(1)
draws = rng.integers(0, 2, size=(100, 500))
steps = np.where(draws==0, 1, -1)
walks = steps.cumsum(axis=1)
frac = (walks.max(axis=1) >= 20).mean()
print(frac)   # e.g., 0.34 (depends on seed)
```

---

## Cheat-sheet: shapes & axes

- Shape `(rows, cols)` for 2D arrays.
- `axis=0` → **down** rows (operate per column).
- `axis=1` → **across** columns (operate per row).

Examples: `A.mean(axis=0)` = mean for each column; `A.sum(axis=1)` = sum for each row.

---

## Function glossary (what we used)

**Array creation**: `np.array`, `np.zeros`, `np.ones`, `np.empty`, `np.arange`, `np.eye`  
**Inspect**: `.dtype`, `.ndim`, `.shape`  
**Casting**: `astype`  
**Indexing**: `arr[r, c]`, `arr[r1:r2, c1:c2]`, fancy integer lists, Boolean masks  
**Reshape/transpose**: `.reshape`, `.T`, `swapaxes`  
**Random**: `np.random.default_rng`, `.integers`, `.standard_normal`, `.uniform`  
**Ufuncs**: `np.abs`, `np.sqrt`, `np.exp`, `np.maximum`, `np.modf`, `np.add` (`out=`)  
**Conditionals**: `np.where`  
**Reductions**: `.sum`, `.mean`, `.std`, `.var`, `.min`, `.max`, `.argmin`, `.argmax`, `.cumsum`, `.cumprod`, `.any`, `.all`  
**Sorting & sets**: `.sort`, `np.sort`, `np.unique`, `np.in1d`  
**I/O**: `np.save`, `np.load`, `np.savez`, `np.savez_compressed`  
**Linear algebra**: `@`, `np.dot`, `np.linalg.inv`, `np.linalg.qr`, `np.linalg.eig`, `np.linalg.svd`, `np.linalg.solve`

---

**Happy NumPy-ing!** If you want this extended with matplotlib plots or pandas bridges, say the word.