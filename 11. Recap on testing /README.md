# Testing, Error Handling, and Objects in Python — Recap

> Beginner-friendly cheat sheet with examples you can copy–paste and run.

## Table of Contents
- [1. Quick Python Recap](#1-quick-python-recap)
- [2. Exceptions & Tracebacks](#2-exceptions--tracebacks)
- [3. Handling Errors: try/except/else/finally](#3-handling-errors-tryexceptelsefinally)
- [4. Building Safe Functions Step-by-Step (BMI)](#4-building-safe-functions-step-by-step-bmi)
- [5. Objects & Classes (Patient example)](#5-objects--classes-patient-example)
- [6. Unit Testing with unittest](#6-unit-testing-with-unittest)
- [7. Integration & Edge-Case Thinking](#7-integration--edge-case-thinking)
- [8. Final Practice Function](#8-final-practice-function)
- [9. Glossary of Key Built-ins](#9-glossary-of-key-built-ins)

---

## 1. Quick Python Recap

- **Variable**: `x = 3`
- **Types**: `int`, `float`, `str`, `bool`, `list`, `dict`
- **Function**: takes inputs ➜ returns output

```python
weight = 70              # int
height = 1.75            # float
name = "Alex"            # str
is_smoker = False        # bool

print(type(weight), type(height), type(name), type(is_smoker))
print("Uppercased name:", name.upper())            # str method
print("Count of 2s:", [1, 2, 2, 3].count(2))       # list method
```

**Expected output (example)**
```
<class 'int'> <class 'float'> <class 'str'> <class 'bool'>
Uppercased name: ALEX
Count of 2s: 2
```

---

## 2. Exceptions & Tracebacks

When Python hits a problem, it raises an **exception** and shows a **traceback**.

Common exceptions: `TypeError`, `ValueError`, `ZeroDivisionError`, `IndexError`, `KeyError`.

```python
# 70 / 0  # ZeroDivisionError (commented so it doesn't crash)
print("ZeroDivisionError example is commented out.")
```

---

## 3. Handling Errors: try/except/else/finally

```python
try:
    # code that might fail
except SomeError as e:
    # handle that specific error
else:
    # runs only if no error happened in try
finally:
    # always runs (clean-up)
```

Key tools:
- `except SomeError as e` ➜ capture and inspect the error object (`print(e)`)
- `isinstance(x, T)` ➜ type checks
- `raise TypeError("message")` / `raise ValueError("message")` ➜ intentionally signal problems

**Examples:**

```python
# Catch a specific error
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print("Caught a ZeroDivisionError:", e)

# isinstance checks
print(isinstance(3, int))            # True
print(isinstance(3.0, float))        # True
print(isinstance("3", (int, float))) # False

# raise with clear messages
def safe_square(x):
    if not isinstance(x, (int, float)):
        raise TypeError("x must be a number (int or float)")
    if x < 0:
        raise ValueError("x must not be negative for this demo")
    return x * x

try:
    print(safe_square(3))       # 9
    print(safe_square("three")) # raises TypeError
except (TypeError, ValueError) as e:
    print("Handled error:", e)
```

---

## 4. Building Safe Functions Step-by-Step (BMI)

**v0 — naive (no checks):**

```python
def bmi_v0(weight, height):
    return weight / (height ** 2)

print("v0 OK:", round(bmi_v0(70, 1.75), 2))
try:
    print("v0 bad:", bmi_v0("seventy", 1.75))
except Exception as e:
    print("v0 crashed:", e)
```

**v1 — add type checks (`TypeError`):**

```python
def bmi_v1(weight, height):
    if not isinstance(weight, (int, float)) or not isinstance(height, (int, float)):
        raise TypeError("Weight and height must be numbers.")
    return weight / (height ** 2)

print("v1 OK:", round(bmi_v1(70, 1.75), 2))
```

**v2 — add value checks (`ValueError`):**

```python
def bmi_v2(weight, height):
    if not isinstance(weight, (int, float)) or not isinstance(height, (int, float)):
        raise TypeError("Weight and height must be numbers.")
    if height <= 0:
        raise ValueError("Height must be > 0.")
    return weight / (height ** 2)

for w, h in [(70, 1.75), (70, 0)]:
    try:
        print("v2:", w, h, "=>", bmi_v2(w, h))
    except Exception as e:
        print("v2 error:", e)
```

**v3 — friendly version that returns messages (teaching style):**

```python
def calculate_bmi(weight, height):
    """Return BMI (float) or 'Error: ...' (string)."""
    try:
        if not isinstance(weight, (int, float)) or not isinstance(height, (int, float)):
            raise TypeError("Weight and height must be numbers.")
        if height <= 0:
            raise ValueError("Height must be > 0.")
        return weight / (height ** 2)
    except (TypeError, ValueError, ZeroDivisionError) as e:
        return f"Error: {e}"

print("Valid BMI:", calculate_bmi(70, 1.75))
print("Height 0:", calculate_bmi(70, 0))
print("Non-numeric:", calculate_bmi("seventy", 1.75))
```

---

## 5. Objects & Classes (Patient example)

A **class** is a blueprint; an **object** is an instance. `self` means “this object”.

```python
class Patient:
    def __init__(self, name, weight_kg, height_m):
        self.name = name
        self.weight_kg = weight_kg
        self.height_m = height_m

    def bmi(self):
        if self.height_m <= 0:
            raise ValueError("height_m must be > 0.")
        return self.weight_kg / (self.height_m ** 2)

p1 = Patient("Alex", 70, 1.75)
p2 = Patient("Sam", 60, 1.70)
print(p1.name, "BMI:", round(p1.bmi(), 2))
print(p2.name, "BMI:", round(p2.bmi(), 2))
```

---

## 6. Unit Testing with `unittest`

- `import unittest` — standard testing library
- `class TestX(unittest.TestCase):` — group tests
- Methods named `test_*` are picked up by the runner
- Useful assertions: `assertEqual`, `assertAlmostEqual`

```python
import unittest

class TestCalculateBMI(unittest.TestCase):
    def test_valid_input(self):
        self.assertAlmostEqual(calculate_bmi(70, 1.75), 22.8571, places=4)

    def test_zero_height(self):
        self.assertEqual(calculate_bmi(70, 0), "Error: Height must be > 0.")

    def test_non_numeric(self):
        self.assertEqual(calculate_bmi("seventy", 1.75), "Error: Weight and height must be numbers.")

# In a script, you would usually enable:
# if __name__ == "__main__":
#     unittest.main()
```

> Tip: In notebooks, use a runner like:
> `unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(TestCalculateBMI))`

---

## 7. Integration & Edge-Case Thinking

**Integration example (toy health risk):**

```python
def calculate_health_risk(bmi, age, bp, cholesterol, smoker=False):
    try:
        for label, val in {"bmi": bmi, "age": age, "bp": bp, "cholesterol": cholesterol}.items():
            if not isinstance(val, (int, float)):
                raise TypeError("BMI, age, blood pressure, and cholesterol must be numbers.")
            if val <= 0:
                raise ValueError("BMI, age, blood pressure, and cholesterol must be positive numbers.")
        risk = (bmi * 0.2) + (age * 0.3) + (bp * 0.3) + (cholesterol * 0.2)
        if smoker:
            risk *= 1.5
        return risk
    except (TypeError, ValueError) as e:
        return f"Error: {e}"
```

**Edge-case example (dosage):**

```python
def calculate_dosage(weight, age, dosage_per_kg=0.5):
    try:
        if not isinstance(weight, (int, float)) or not isinstance(age, (int, float)):
            raise TypeError("Weight and age must be numbers.")
        if weight <= 0 or age <= 0:
            raise ValueError("Weight and age must be positive numbers.")
        dose = weight * dosage_per_kg
        if age < 12:
            dose *= 0.75
        return dose
    except (TypeError, ValueError) as e:
        return f"Error: {e}"

print(calculate_dosage(200, 30, dosage_per_kg=10))   # 2000.0
print(calculate_dosage(0.1, 1, dosage_per_kg=0.01))  # 0.00075
print(calculate_dosage(0, 30))                       # Error message
```

---

## 8. Final Practice Function

```python
def calculate_health_risk_score(bmi, age, medical_history, smoker=False):
    """Toy risk score for practice (not clinical)."""
    try:
        if not isinstance(bmi, (int, float)) or not isinstance(age, int) or not isinstance(medical_history, list):
            raise TypeError("BMI must be a number, age must be an integer, and medical history must be a list.")
        if bmi <= 0 or age <= 0:
            raise ValueError("BMI and age must be positive numbers.")

        score = (bmi * 0.3) + (age * 0.4)
        flags = [str(s).lower() for s in medical_history]
        if "heart disease" in flags:
            score += 20
        if "hypertension" in flags:
            score += 10
        if smoker:
            score *= 1.5
        return score
    except (TypeError, ValueError) as e:
        return f"Error: {e}"

# Demos
print(calculate_health_risk_score(25, 50, ["high cholesterol"]))              # 27.5
print(calculate_health_risk_score(25, 50, ["Heart Disease", "Hypertension"])) # 57.5
print(calculate_health_risk_score(25, 50, ["hc"], smoker=True))               # 41.25
print(calculate_health_risk_score(25, "fifty", ["hc"]))                       # Error
```

---

## 9. Glossary of Key Built-ins

- `print(x)` — display `x`
- `type(x)` — the type of `x`
- `isinstance(x, T)` — is `x` an instance of `T` (or tuple of types)?
- `raise SomeError("msg")` — create/throw an exception
- `try/except/else/finally` — error-handling structure
- `unittest` — built-in testing framework
  - `unittest.TestCase` — base class for test cases
  - `self.assertEqual(a, b)` — assert equal
  - `self.assertAlmostEqual(a, b, places=n)` — float comparison
  - `if __name__ == "__main__": unittest.main()` — run tests in scripts

---

### Keep going! 🚀
Write tiny functions, validate inputs, raise clear errors, and add a couple of tests for each new behavior. Your future self will thank you.


### BONUS

# Understanding `assertAlmostEqual(..., places=4)` in Python `unittest`

This short guide explains what `places=4` means in:

```python
self.assertAlmostEqual(a, b, places=4)
```

## What does `places=4` mean?

`places=4` tells the test to pass if **`a` and `b` are equal up to 4 decimal places**.  
Formally, it checks:

```
round(a - b, 4) == 0
```

So the absolute difference must be **< 0.00005** for the assertion to pass (because rounding to 4 decimal places would make the difference zero).

### Why do we need this?

Floating‑point math (division, square roots, etc.) often introduces tiny rounding errors.  
`assertAlmostEqual` prevents tests from failing due to these harmless differences.

## Minimal examples

### Example 1 — PASS (difference is tiny)
```python
import unittest

class Demo(unittest.TestCase):
    def test_pass(self):
        a = 22.8571428571
        b = 22.8571
        # Difference ≈ 0.0000428571 -> rounds to 0 at 4 dp -> PASS
        self.assertAlmostEqual(a, b, places=4)
```

### Example 2 — FAIL (difference is too big)
```python
import unittest

class Demo(unittest.TestCase):
    def test_fail(self):
        a = 22.8576
        b = 22.8571
        # Difference = 0.0005 -> rounds to 0.0005 at 4 dp (not zero) -> FAIL
        self.assertAlmostEqual(a, b, places=4)
```

> Tip: When a test fails, `unittest` raises an `AssertionError` showing the two values.

## Alternatives you should know

Sometimes decimal places aren’t the best way to express tolerance. You can use:

### 1) Absolute tolerance with `delta`
```python
self.assertAlmostEqual(a, b, delta=1e-4)  # passes if abs(a - b) <= 0.0001
```

### 2) General‑purpose closeness checks
Outside of `unittest`, use:

```python
import math
math.isclose(a, b, rel_tol=1e-9, abs_tol=1e-4)
```

Or with NumPy:

```python
import numpy as np
np.isclose(a, b, rtol=1e-9, atol=1e-4)
```

## Rule of thumb

- Use **`places=`** when you care about **decimal precision** (e.g., displaying values to a fixed number of decimal places).
- Use **`delta=`** (or `isclose`) when you prefer an explicit **numerical tolerance**.

---

### Quick reference table

| Parameter              | Meaning                                          | Typical Use Case                          |
|------------------------|--------------------------------------------------|-------------------------------------------|
| `places=4`             | Round `a-b` to 4 dp and compare to zero         | Comparing printed/rounded numbers         |
| `delta=1e-4`           | Require `abs(a-b) <= 1e-4`                       | Explicit absolute error budget            |
| `math.isclose(...)`    | Relative and/or absolute tolerance               | General numeric comparisons               |
| `numpy.isclose(...)`   | Vectorized relative/absolute tolerance           | Arrays and scientific computing           |

