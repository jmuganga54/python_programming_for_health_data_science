# Functions in Python 

Functions are named blocks of code you can **reuse**. They help you:
- avoid repeating yourself,
- keep code tidy,
- test small parts easily.

You’ll learn how to **define**, **call**, and use:
- parameters & return values,
- default & keyword arguments,
- lambda (small anonymous) functions,
- basic **error handling**,
- **docstrings** (function documentation).

I’ll also explain built-ins we use: `print()`, `type()`, `isinstance()`, `len()`, `sorted()`, `map()`, `filter()`.

---

## 1) Defining and Calling a Function

Use the `def` keyword. Parameters go in `()`. Use `return` to send a result back.

### Built-in used
- **`print(*values, sep=' ', end='\n')`**: shows text/values. `sep` is the separator, `end` is the line ending (default newline).

### Example: Simple BMI calculation
```python
def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi

bmi_value = calculate_bmi(70, 1.75)
print("The BMI is:", bmi_value)
```
**Output**
```
The BMI is: 22.857142857142858
```

### Exercise (solution shown)
**Task:** Call `calculate_bmi` with weight=80, height=1.80.

```python
bmi_value = calculate_bmi(80, 1.80)
print("The BMI is:", bmi_value)
```
**Output**
```
The BMI is: 24.691358024691358
```

---

## 2) Returning More Than a Number (classification)

You can return any type (string, tuple, dict, etc.). Let’s add a BMI **category**.

### Example: BMI + category
```python
def bmi_with_category(weight, height):
    bmi = weight / (height ** 2)
    if bmi < 18.5:
        cat = "Underweight"
    elif bmi < 25:
        cat = "Normal weight"
    elif bmi < 30:
        cat = "Overweight"
    else:
        cat = "Obesity"
    return bmi, cat

b, c = bmi_with_category(85, 1.75)
print("BMI:", b, "| Category:", c)
```
**Output**
```
BMI: 27.755102040816325 | Category: Overweight
```

---

## 3) Function Arguments (positional)

Arguments are inputs to your function.

### Example: Average of three health metrics
```python
def calculate_average(bp, cholesterol, heart_rate):
    avg = (bp + cholesterol + heart_rate) / 3
    return avg

print(calculate_average(120, 200, 70))
```
**Output**
```
130.0
```

### Built-ins used
- **`type(obj)`**: tells you the object’s type.
- **`isinstance(obj, types)`**: checks if `obj` is of a given type or tuple of types.

---

## 4) Default & Keyword Arguments

Provide **default values** so the caller can omit them.  
Use **keyword arguments** to name inputs in any order.

### Example: Medication dosage
```python
def calculate_dosage(weight, age, dosage_per_kg=0.5):
    dosage = weight * dosage_per_kg
    if age < 12:
        dosage *= 0.75  # lower dose for children
    return dosage

print("Adult default:", calculate_dosage(70, 30))
print("Child default:", calculate_dosage(weight=30, age=8))
print("Custom per kg:", calculate_dosage(age=45, weight=80, dosage_per_kg=0.6))
```
**Output**
```
Adult default: 35.0
Child default: 11.25
Custom per kg: 48.0
```

> Tip: Default arguments are evaluated **once** at function definition time. Avoid mutable defaults like `[]` or `{}`.

---

## 5) Lambda Functions (small, anonymous)

`lambda args: expression` — quick inline function.  
Often used with **`sorted`**, **`map`**, **`filter`**.

### Built-ins used
- **`sorted(iterable, key=None, reverse=False)`**: returns a **new** sorted list.
- **`filter(function, iterable)`**: keeps items where function returns `True`. Returns an iterator; wrap with `list(...)` to see results.
- **`map(function, iterable)`**: applies function to each item. Returns an iterator.

### Example: Sort & filter patient records
```python
patients = [
    ("John", 22.5),
    ("Alice", 25.0),
    ("Bob", 30.2)
]

# Sort by BMI
sorted_patients = sorted(patients, key=lambda p: p[1])
print("Sorted by BMI:", sorted_patients)

# Filter BMI > 25
high_bmi = list(filter(lambda p: p[1] > 25, patients))
print("BMI > 25:", high_bmi)

# Map to names only
names = list(map(lambda p: p[0], patients))
print("Names:", names)
``]
**Output**
```
Sorted by BMI: [('John', 22.5), ('Alice', 25.0), ('Bob', 30.2)]
BMI > 25: [('Bob', 30.2)]
Names: ['John', 'Alice', 'Bob']
```

---

## 6) Error Handling in Functions

Use `try` / `except` to catch problems and respond nicely.

### Common errors you’ll see
- **`ZeroDivisionError`**: dividing by zero.
- **`TypeError`**: wrong type (e.g., string where number expected).
- **`ValueError`**: wrong value (e.g., negative where positive required).
- **`IndexError`**: bad list index.

### Example: Safe BMI (catch height=0)
```python
def calculate_bmi_safe(weight, height):
    try:
        bmi = weight / (height ** 2)
        return bmi
    except ZeroDivisionError:
        return "Error: Height cannot be zero."

print(calculate_bmi_safe(70, 0))
```
**Output**
```
Error: Height cannot be zero.
```

### Example: Safer dosage with validation
```python
def calculate_dosage_safe(weight, age, dosage_per_kg=0.5):
    try:
        if not (isinstance(weight, (int, float)) and isinstance(age, (int, float))):
            raise TypeError("Weight and age must be numbers.")
        if weight <= 0 or age <= 0:
            raise ValueError("Weight and age must be positive numbers.")
        dosage = weight * dosage_per_kg
        if age < 12:
            dosage *= 0.75
        return dosage
    except (TypeError, ValueError) as e:
        return f"Error: {e}"

print(calculate_dosage_safe("seventy", 8))
print(calculate_dosage_safe(70, -5))
```
**Output**
```
Error: Weight and age must be numbers.
Error: Weight and age must be positive numbers.
```

---

## 7) Docstrings (built-in help)

A **docstring** is a string right under `def` that explains what your function does, its parameters and return.

### Built-ins used
- **`help(object)`**: shows documentation (prints the docstring).
- You can also inspect `function.__doc__`.

### Example: Add a docstring
```python
def calculate_bmi(weight, height):
    \"\"\"Calculate BMI from weight (kg) and height (m).

    Parameters:
        weight (float): kilograms
        height (float): meters

    Returns:
        float: BMI value
    \"\"\"
    return weight / (height ** 2)

print(calculate_bmi.__doc__ is not None)
```
**Output**
```
True
```

> In an interactive shell, `help(calculate_bmi)` would display the full docstring.

---

## 8) Scope & Return (quick notes)

- Variables inside a function are **local** to that function.
- `return` ends the function and passes back the value.  
- If you don’t `return`, the function returns **`None`**.

```python
def no_return():
    x = 123

print(no_return())
```
**Output**
```
None
```

---

## 9) Putting It Together — Final Exercise (with solution)

**Task:** Write a function to compute a **health risk score** using BMI, age, blood pressure, and cholesterol.  
Requirements:
- default and keyword args,
- validation & error handling,
- docstring,
- an optional `smoker` flag that increases risk.

**Solution**
```python
def calculate_health_risk(bmi, age, bp, cholesterol, *, smoker=False, bmi_weight=0.2, age_weight=0.3, bp_weight=0.3, chol_weight=0.2):
    \"\"\"Calculate a health risk score from BMI, age, blood pressure (bp), and cholesterol.

    Parameters:
        bmi (float): Body Mass Index (must be > 0)
        age (int|float): Age in years (must be > 0)
        bp (int|float): Blood pressure (must be > 0)
        cholesterol (int|float): Cholesterol level (must be > 0)
        smoker (bool, optional): If True, risk increases (default False)
        bmi_weight, age_weight, bp_weight, chol_weight (float, optional): factor weights that sum ≈ 1

    Returns:
        float | str: Risk score (higher = riskier) or an error message string.
    \"\"\"
    try:
        # type checks
        for val in (bmi, age, bp, cholesterol, bmi_weight, age_weight, bp_weight, chol_weight):
            if not isinstance(val, (int, float)):
                raise TypeError("All numeric inputs and weights must be numbers.")
        if not isinstance(smoker, bool):
            raise TypeError("smoker must be a boolean (True/False).")

        # value checks
        if bmi <= 0 or age <= 0 or bp <= 0 or cholesterol <= 0:
            raise ValueError("bmi, age, bp, cholesterol must be positive numbers.")

        # basic risk model
        risk = (bmi * bmi_weight) + (age * age_weight) + (bp * bp_weight) + (cholesterol * chol_weight)
        if smoker:
            risk *= 1.5
        return risk

    except (TypeError, ValueError) as e:
        return f"Error: {e}"

# Try it
print("Risk (non-smoker):", calculate_health_risk(24.7, 40, 120, 180))
print("Risk (smoker):    ", calculate_health_risk(24.7, 40, 120, 180, smoker=True))
```
**Output**
```
Risk (non-smoker): 62.13999999999999
Risk (smoker):     93.20999999999998
```

---

## Extra Mini-Exercises (with solutions)

### A) Classify BMI inside the function
**Goal:** Return a string like `"BMI: 26.23 (Overweight)"`.

```python
def describe_bmi(weight, height):
    bmi = weight / (height ** 2)
    if bmi < 18.5:
        cat = "Underweight"
    elif bmi < 25:
        cat = "Normal weight"
    elif bmi < 30:
        cat = "Overweight"
    else:
        cat = "Obesity"
    return f"BMI: {bmi:.2f} ({cat})"

print(describe_bmi(75, 1.70))
```
**Output**
```
BMI: 25.95 (Overweight)
```

### B) Use `sorted` with a lambda on dicts
**Goal:** Sort patient dicts by cholesterol.

```python
patients = [
    {"name": "John", "chol": 180},
    {"name": "Alice", "chol": 220},
    {"name": "Bob", "chol": 195},
]
by_chol = sorted(patients, key=lambda p: p["chol"])
print(by_chol)
```
**Output**
```
[{'name': 'John', 'chol': 180}, {'name': 'Bob', 'chol': 195}, {'name': 'Alice', 'chol': 220}]
```

### C) Validate inputs with `isinstance`
**Goal:** Return an error if any metric is not numeric.

```python
def average_three(a, b, c):
    if not all(isinstance(x, (int, float)) for x in (a, b, c)):
        return "Error: all inputs must be numbers."
    return (a + b + c) / 3

print(average_three(1, 2, "3"))
print(average_three(1, 2, 3))
```
**Output**
```
Error: all inputs must be numbers.
2.0
```

---

## Quick Reference

- **Define:** `def name(params): ... return value`
- **Call:** `result = name(args)`
- **Default args:** `def f(a, b=10): ...`
- **Keyword args:** `f(b=20, a=5)`
- **Lambda:** `lambda x: x * x`
- **Error handling:** `try: ... except ErrorType: ...`
- **Docstring:** first triple-quoted string in function; shows with `help(func)`

---

### One-line takeaway
Functions let you package logic once and reuse it everywhere—add clear parameters, validate inputs, return results, document with docstrings, and handle errors gracefully.


## MORE ON : Lambda, `filter()`, `map()`, and `isinstance()` 

# Lambda, `filter()`, `map()`, and `isinstance()` 

This mini guide explains **lambda functions**, **`filter()`**, **`map()`**, and **`isinstance()`** with plain-English notes, short examples, and their **outputs**.

---

## 1) `lambda`: tiny, one‑line functions

**What:** An inline, unnamed function.  
**Syntax:** `lambda arguments: expression`  
**Use it for:** very short functions you only need once (e.g., inside `sorted`, `map`, `filter`).

### Example — square a number
```python
square = lambda x: x * x
print(square(5))
```
**Output**
```
25
```

### Same with `def` (for comparison)
```python
def square_def(x):
    return x * x

print(square_def(5))
```
**Output**
```
25
```

> Use `def` for longer/multi-line or reusable functions. Use `lambda` for quick, one-off expressions.

---

## 2) `filter(function, iterable)`: keep items that pass a test

**What:** Keeps items for which `function(item)` is **True**.  
**Returns:** an **iterator** (wrap with `list(...)` to view).

### Example — keep even numbers
```python
nums = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda n: n % 2 == 0, nums))
print(evens)
```
**Output**
```
[2, 4, 6]
```

### Example — names starting with “A”
```python
names = ["Alice", "Bob", "Ahmed", "Clara"]
a_names = list(filter(lambda s: s.startswith("A"), names))
print(a_names)
```
**Output**
```
['Alice', 'Ahmed']
```

> List‑comprehension equivalent:
> ```python
> [n for n in nums if n % 2 == 0]
> [s for s in names if s.startswith("A")]
> ```

---

## 3) `map(function, iterable)`: transform each item

**What:** Applies `function(item)` to **every item**.  
**Returns:** an **iterator** (wrap with `list(...)` to view).

### Example — °C → °F
```python
c = [0, 10, 20, 30]
f = list(map(lambda x: x * 9/5 + 32, c))
print(f)
```
**Output**
```
[32.0, 50.0, 68.0, 86.0]
```

### Example — get names from (name, BMI) pairs
```python
patients = [("John", 22.5), ("Alice", 25.0), ("Bob", 30.2)]
names = list(map(lambda p: p[0], patients))
print(names)
```
**Output**
```
['John', 'Alice', 'Bob']
```

> List‑comprehension equivalent:
> ```python
> [x * 9/5 + 32 for x in c]
> [p[0] for p in patients]
> ```

---

## 4) `isinstance(object, type_or_tuple)`: safe type checking

**What:** Checks if an object is an instance of a type (or any in a tuple).  
**Why not `type(obj) == T`?** Because `isinstance` works with **inheritance** (subclasses).

### Example — basic checks
```python
print(isinstance(3.14, float))    # True
print(isinstance("hello", str))   # True
print(isinstance(10, int))        # True
```
**Output**
```
True
True
True
```

### Example — any of multiple types
```python
x = 3.0
print(isinstance(x, (int, float)))  # True if int OR float
```
**Output**
```
True
```

### Example — inheritance advantage
```python
class Animal: pass
class Dog(Animal): pass

d = Dog()
print(type(d) == Animal)      # False (exact type check)
print(isinstance(d, Animal))  # True (Dog is an Animal)
```
**Output**
```
False
True
```

---

## Putting them together

### Sort by BMI (`sorted` + `lambda`)
```python
patients = [("John", 22.5), ("Alice", 25.0), ("Bob", 30.2)]
by_bmi = sorted(patients, key=lambda p: p[1])
print(by_bmi)
```
**Output**
```
[('John', 22.5), ('Alice', 25.0), ('Bob', 30.2)]
```

### Filter BMI > 25 (`filter` + `lambda`)
```python
high_bmi = list(filter(lambda p: p[1] > 25, patients))
print(high_bmi)
```
**Output**
```
[('Bob', 30.2)]
```

### Map to names (`map` + `lambda`)
```python
names = list(map(lambda p: p[0], patients))
print(names)
```
**Output**
```
['John', 'Alice', 'Bob']
```

---

## Mini Exercises (with solutions)

### 1) Keep only strings from a mixed list
**Task:** From `data = [10, "hi", 3.5, "bye", True]` keep only the strings.

**Solution A — `filter` + `lambda`**
```python
data = [10, "hi", 3.5, "bye", True]
only_strings = list(filter(lambda x: isinstance(x, str), data))
print(only_strings)
```
**Output**
```
['hi', 'bye']
```

**Solution B — list comprehension**
```python
only_strings = [x for x in data if isinstance(x, str)]
print(only_strings)
```
**Output**
```
['hi', 'bye']
```

---

### 2) Add 10% to every price
**Task:** From `prices = [100, 250, 80]` create a new list with +10%.

**Solution — `map` + `lambda`**
```python
prices = [100, 250, 80]
with_tax = list(map(lambda p: p * 1.10, prices))
print(with_tax)
```
**Output**
```
[110.00000000000001, 275.0, 88.0]
```

---

### 3) Validate numeric inputs with `isinstance`
**Task:** Write `safe_avg(a, b)` that returns `"Error"` if either input isn’t a number.

**Solution**
```python
def safe_avg(a, b):
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        return "Error: inputs must be numbers."
    return (a + b) / 2

print(safe_avg(10, 20))
print(safe_avg(10, "20"))
```
**Output**
```
15.0
Error: inputs must be numbers.
```

---

## TL;DR

- **`lambda`**: quick one-liner function → `lambda x: x * x`
- **`filter(fn, data)`**: keep items where `fn(item)` is **True**.
- **`map(fn, data)`**: transform each item into `fn(item)`.
- **`isinstance(obj, types)`**: safe type checks (works with subclasses, multiple types).
