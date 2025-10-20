# Introduction to NumPy 

NumPy is the foundational library for fast numerical computing in Python. It gives you:
- The ndarray (N-dimensional array) for efficient storage and vectorized operations
- A large toolbox of math functions that work on whole arrays
- Random number utilities
- Tools for reshaping, indexing, boolean filtering, and more

We will use the standard alias:

```python
import numpy as np
print('NumPy version:', np.__version__)
```
**What these do**
- `import numpy as np`: imports NumPy with the common short alias `np`.
- `np.__version__`: string with the installed NumPy version.
- `print(...)`: prints to the console.

Example output:
```
NumPy version: 1.26.4
```

---

## 1) Creating Arrays (ndarray)

The core data structure is the ndarray: a typed, multi-dimensional grid.

```python
import numpy as np

array1 = np.array([1, 2, 3, 4, 5])          # 1D array
array2 = np.array([[1, 2, 3], [4, 5, 6]])   # 2D array (2 rows, 3 cols)
zeros  = np.zeros((3, 3))                   # 3x3 zeros
ones   = np.ones((2, 4))                    # 2x4 ones
empty  = np.empty((2, 2))                   # 2x2 uninitialized (fast, contents may vary)

print('1D Array:', array1)
print('2D Array:\n', array2)
print('3x3 Zeros Array:\n', zeros)
print('2x4 Ones Array:\n', ones)
print('2x2 Empty Array:\n', empty)
```
**Functions used**
- `np.array(iterable)`: create an array from a Python list or list-of-lists.
- `np.zeros(shape)`, `np.ones(shape)`: arrays filled with 0 or 1.
- `np.empty(shape)`: allocates memory without setting values (contents arbitrary).

Example output (abridged):
```
1D Array: [1 2 3 4 5]
2D Array:
 [[1 2 3]
  [4 5 6]]
3x3 Zeros Array:
 [[0. 0. 0.]
  [0. 0. 0.]
  [0. 0. 0.]]
...
```

More creators you will use often:
- `np.full(shape, fill_value)`
- `np.arange(start, stop, step)`
- `np.linspace(start, stop, num)`
- `np.random.random(shape)`

### Exercise 1 (with solution)
**Question**
1) Make a 5x5 array filled with 7.  
2) Make a 3x3 array with random values in [0,1).  
3) Create arrays with `np.full`, `np.arange`, and `np.linspace`.

**Solution**
```python
import numpy as np

# 1) 5x5 of 7
a = np.full((5, 5), 7)
print(a)

# 2) 3x3 random
r = np.random.random((3, 3))
print(r)

# 3a) full
b = np.full((2, 3), 10)
print(b)

# 3b) arange (10..40 step 10) -> [10 20 30 40]
c = np.arange(10, 50, 10)
print(c)

# 3c) linspace (3 points 0..1) -> [0.  0.5 1. ]
d = np.linspace(0, 1, 3)
print(d)
```

---

## 2) Array Arithmetic and Data Types

NumPy does element-wise arithmetic (vectorization).

```python
a = np.array([10, 20, 30, 40])
b = np.array([ 1,  2,  3,  4])

print('Addition:       ', a + b)
print('Subtraction:    ', a - b)
print('Multiplication: ', a * b)
print('Division:       ', a / b)
```

Data types (dtypes) affect precision and behavior:

```python
print('dtype of a:', a.dtype)
print('dtype float array:', np.array([1.5]).dtype)
```

Convert dtypes with `astype`:
```python
arr_float = np.array([1.5, 2.5, 3.5], dtype=float)
arr_int   = arr_float.astype(int)  # truncates toward 0
print(arr_int)  # [1 2 3]
```

### Exercise 2 (with solution)
**Question**  
Create an int array and a float array, add them, check result dtype, then cast floats to ints.

**Solution**
```python
array_int   = np.array([1, 2, 3, 4], dtype=int)
array_float = np.array([1.5, 2.5, 3.5, 4.5], dtype=float)

res = array_int + array_float
print(res)        # [2.5 4.5 6.5 8.5]
print(res.dtype)  # float64 (upcast)

print(array_float.astype(int))  # [1 2 3 4]
```

---

## 3) Array Attributes

Key attributes:
- `shape`: dimensions, e.g. (3,4)
- `size`: total number of elements
- `ndim`: number of axes
- `itemsize`: bytes per element
- `nbytes`: total bytes in the array

```python
arr = np.array([[1,2,3],[4,5,6],[7,8,9]])
print('shape:', arr.shape)
print('size:', arr.size)
print('ndim:', arr.ndim)
print('itemsize:', arr.itemsize)
print('nbytes:', arr.nbytes)
```

### Exercise 3 (with solution)
**Question**  
Make a 1D array with 10 elements. Print attributes. Reshape to (2,5) and print attributes again.

**Solution**
```python
x = np.arange(1, 11)
print(x.shape, x.size, x.ndim, x.itemsize, x.nbytes)

x = x.reshape((2, 5))
print(x.shape, x.size, x.ndim, x.itemsize, x.nbytes)
```

---

## 4) Indexing and Slicing

Access single items, rows, columns, and sub-arrays:

```python
arr = np.array([[1,2,3,4],
                [5,6,7,8],
                [9,10,11,12]])

print('Element (1,2):', arr[1, 2])  # zero-based
print('First row:',     arr[0, :])
print('Last column:',   arr[:, -1])
print('Subarray:',      arr[1:, 1:3])
```

### Exercise 4 (with solution)
**Question**  
Make a 5x5 array of 1..25. Print: element (2,3), first row, last column, subarray rows 2..3 and cols 1..2, and the full array reversed.

**Solution**
```python
A = np.arange(1, 26).reshape(5, 5)
print('A:\\n', A)
print('A[2,3]:', A[2, 3])
print('First row:', A[0, :])
print('Last column:', A[:, -1])
print('Subarray (2:4, 1:3):\\n', A[2:4, 1:3])
print('Reversed:\\n', A[::-1, ::-1])
```

---

## 5) Boolean Indexing (Filtering)

Select elements by condition:
```python
arr = np.array([10, 20, 30, 40, 50])
mask = arr > 25
print('mask:', mask)          # [False False  True  True  True]
print(arr[mask])              # [30 40 50]

# combine conditions: & (and), | (or), ~ (not)
print(arr[(arr > 15) & (arr < 45)])  # [20 30 40]
```

### Exercise 5 (with solution)
**Question**  
From [5, 12, 15, 20, 25, 30, 35], pick elements divisible by 5 and greater than 20.

**Solution**
```python
x = np.array([5, 12, 15, 20, 25, 30, 35])
print(x[(x % 5 == 0) & (x > 20)])  # [25 30 35]
```

---

## 6) Fancy Indexing

Pick specific positions, not just slices:
```python
arr = np.array([10, 20, 30, 40, 50])
idx = [0, 2, 4]
print(arr[idx])  # [10 30 50]

# Modify multiple positions
arr[[1, 3]] = [200, 400]
print(arr)      # [10 200 30 400 50]
```

---

## 7) Transposing and Swapping Axes

- `.T` or `np.transpose` flips axes (2D: rows <-> cols)
- `np.swapaxes(a, axis1, axis2)` swaps two axes in N-D

```python
A = np.array([[1,2,3],[4,5,6]])
print('A:\\n', A)
print('A.T:\\n', A.T)

A3 = np.array([[[1, 2], [3, 4]],
               [[5, 6], [7, 8]]])
B = np.swapaxes(A3, 1, 2)
print('swapaxes(1,2):\\n', B)
```

---

## 8) Vectorized Math (Universal Functions)

NumPy math functions operate element-wise and return arrays:

```python
arr = np.array([1, 2, 3, 4, 5])
print('sqrt: ', np.sqrt(arr))
print('exp:  ', np.exp(arr))
print('log:  ', np.log(arr))    # natural log

# trig examples
print('sin(pi/2):', np.sin(np.pi/2))  # ~1.0
print('cos(pi/2):', np.cos(np.pi/2))  # ~0.0
```

Other useful ones:
- `np.square(x)`, `np.power(x, p)`, `np.log10(x)`

### Exercise 6 (with solution)
**Question**  
For [10, 20, 30, 40, 50]: show square, base-10 log, and power 2. Also compute sin of [0, pi/4, pi/2, pi].

**Solution**
```python
x = np.array([10, 20, 30, 40, 50])
print('square:', np.square(x))
print('log10 :', np.log10(x))
print('pow2  :', np.power(x, 2))

angles = np.array([0, np.pi/4, np.pi/2, np.pi])
print('sin   :', np.sin(angles))
```

---

## 9) Reshaping

Change the shape without changing data order:
```python
x = np.array([1, 2, 3, 4, 5, 6])
print('2x3:\\n', x.reshape((2, 3)))
print('2x1x3:\\n', x.reshape((2, 1, 3)))
```

### Exercise 7 (with solution)
**Question**  
Create `np.arange(1, 13)` and reshape it to 3x4, then 2x3x2.

**Solution**
```python
x = np.arange(1, 13)
print(x.reshape((3, 4)))
print(x.reshape((2, 3, 2)))
```

---

## 10) Pseudorandom Numbers

Random integers, floats, and normal distributions:
```python
# Integers 0..9
ri = np.random.randint(0, 10, size=(3, 3))
print('randint:\\n', ri)

# Uniform floats in [0,1)
rf = np.random.rand(3, 3)
print('rand:\\n', rf)

# Normal distribution (mean 0, std 1)
rn = np.random.normal(0, 1, size=(3, 3))
print('normal:\\n', rn)
```

Reproducibility with a fixed seed:
```python
np.random.seed(42)
print(np.random.randint(10, size=5))
```

**Functions used**
- `np.random.randint(low, high, size)`: random integers in [low, high)
- `np.random.rand(*shape)`: uniform floats in [0,1)
- `np.random.normal(mean, std, size)`: normal distribution
- `np.random.seed(n)`: fix RNG seed

### Exercise 8 (with solution)
**Question**  
1) Generate a 3x3 array of integers 10..19,  
2) A 3x3 array of uniform floats in [0,5),  
3) A 3x3 normal array with mean 5 and std 2. Use `np.random.seed(7)` first.

**Solution**
```python
np.random.seed(7)
print(np.random.randint(10, 20, size=(3, 3)))
print(np.random.rand(3, 3) * 5)
print(np.random.normal(5, 2, size=(3, 3)))
```

---

## Quick Reference (Built-ins and NumPy functions)

- Import / Basics: `import numpy as np`, `np.__version__`, `print(...)`
- Array creation: `np.array`, `np.zeros`, `np.ones`, `np.empty`, `np.full`
- Ranges: `np.arange`, `np.linspace`
- Random: `np.random.seed`, `np.random.random`, `np.random.rand`, `np.random.randint`, `np.random.normal`
- Attributes: `.shape`, `.size`, `.ndim`, `.itemsize`, `.nbytes`, `.dtype`
- Dtype: `.astype(new_dtype)`
- Indexing / slicing: `arr[i, j]`, `arr[i, :]`, `arr[:, j]`, `arr[r1:r2, c1:c2]`
- Boolean masks: `(arr > 0)`, combine with `& | ~`
- Fancy indexing: `arr[[i1, i2, ...]]`
- Reshape / axes: `.reshape(...)`, `.T`, `np.transpose`, `np.swapaxes`
- Math (ufuncs): `np.sqrt`, `np.exp`, `np.log`, `np.log10`, `np.square`, `np.power`, `np.sin`, `np.cos`, `np.pi`

---

## Final Mini-Exercise (with solution)

**Question**  
Create a 10x10 array with values 1..100.  
1) Reshape to 10x10,  
2) Select all numbers divisible by both 3 and 5,  
3) Replace them with -1,  
4) Compute the mean of the resulting array.

**Solution**
```python
x = np.arange(1, 101).reshape(10, 10)

mask = (x % 3 == 0) & (x % 5 == 0)  # divisible by 15
x[mask] = -1

print('Modified array:\\n', x)
print('Mean:', x.mean())
```
**What these do**
- `%` is modulo (remainder)
- `&` combines boolean conditions element-wise
- `x[mask] = -1` assigns to filtered positions
- `.mean()` computes the average of all values


# BONUS : NumPy Array Slicing


# NumPy Array Slicing — Beginner Guide

This file explains how slicing works in NumPy arrays, with clear examples and outputs.  
It is designed to be GitHub-friendly and easy to read.

---

## 1. Create an Array

```python
import numpy as np

array = np.array([[1, 2, 3, 4],
                  [5, 6, 7, 8],
                  [9, 10, 11, 12]])
```

### Output (visual view)

| Row | Values         |
|-----|----------------|
| 0   | [1, 2, 3, 4]   |
| 1   | [5, 6, 7, 8]   |
| 2   | [9, 10, 11, 12] |

---

## 2. Understanding `.ndim`, `.shape`, `.size`

```python
print(array.ndim)   # Number of dimensions
print(array.shape)  # (rows, columns)
print(array.size)   # Total number of elements
```

**Output:**
```
2
(3, 4)
12
```

---

## 3. Basic Slicing

```python
print('Subarray:', array[1:, 1:3])
```

**Explanation:**
- `1:` → rows from index 1 to end → rows 1 and 2
- `1:3` → columns 1 to 2 (3 not included)
- Selected elements:
  - (1,1)=6, (1,2)=7
  - (2,1)=10, (2,2)=11

**Output:**
```
Subarray: [[ 6  7]
           [10 11]]
```

---

## 4. More Examples

```python
# 1) First row (all columns)
print(array[0, :])  # [1 2 3 4]

# 2) Last column (all rows)
print(array[:, -1]) # [ 4  8 12]

# 3) Block of middle elements
print(array[0:2, 1:3])  # [[2 3], [6 7]]

# 4) Every second row and column
print(array[::2, ::2])  # [[ 1  3], [ 9 11]]

# 5) Single element
print(array[2, 3])      # 12
```

---

## 5. Practice Exercises

### Exercise 1
Get the second row.
```python
print(array[1, :])
```
**Output:**
```
[5 6 7 8]
```

### Exercise 2
Get the first two columns of all rows.
```python
print(array[:, :2])
```
**Output:**
```
[[ 1  2]
 [ 5  6]
 [ 9 10]]
```

### Exercise 3
Get rows 0–1 and columns 2–3.
```python
print(array[0:2, 2:])
```
**Output:**
```
[[3 4]
 [7 8]]
```

### Exercise 4
Get the last two rows and last two columns.
```python
print(array[-2:, -2:])
```
**Output:**
```
[[ 7  8]
 [11 12]]
```

---

## 6. Summary

| Attribute | Meaning |
|------------|----------|
| `.ndim` | Number of dimensions |
| `.shape` | Shape (rows, columns) |
| `.size` | Total number of elements |
| `array[start:stop:step]` | Slice rows or columns |

---

✅ **Tip:** Stop value in slicing is *exclusive* (it is not included).  
✅ **Tip:** You can use negative indices to count from the end.

---


