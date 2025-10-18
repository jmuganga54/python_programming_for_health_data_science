# Testing and Error Handling in Python — Beginner-Friendly Guide

This guide makes **error handling** and **testing** clear and practical using small, focused examples. You’ll learn:

- `try / except / else / finally`
- Raising your own errors with `raise`
- Safe type checks with `isinstance()`
- Unit tests with `unittest` (including edge cases)
- Integration testing ideas
- Handy testing tips & patterns

Where helpful, we show the **expected output** so you know what to look for.

---

## 1) Error Handling: `try / except / else / finally`

### Why?
Programs often see unexpected input (e.g., height = 0, or a string where a number is expected). Error handling lets your code **fail gracefully** instead of crashing.

### Anatomy
```python
try:
    # Code that may raise an error (an exception)
except SomeError as e:
    # How to recover/report
else:
    # Runs only if no exception happened in try
finally:
    # Always runs (cleanup, closing files, etc.)
```

### Common Exceptions
- `ZeroDivisionError` — division by zero
- `TypeError` — wrong type (e.g., string instead of number)
- `ValueError` — correct type but bad value (e.g., negative age)
- `IndexError` — index out of range in a list
- `KeyError` — key not found in a dict

### Key Built-in Used
- **`isinstance(obj, types)`** → safe type checking; supports tuples and inheritance.

---

## 2) Example: Safe BMI Calculation

```python
def calculate_bmi_safe(weight, height):
    try:
        if not (isinstance(weight, (int, float)) and isinstance(height, (int, float))):
            raise TypeError("Weight and height must be numbers.")
        bmi = weight / (height ** 2)
    except ZeroDivisionError:
        return "Error: Height cannot be zero."
    except TypeError as e:
        return f"Error: {e}"
    else:
        return bmi
    finally:
        # Always runs — good place to close files, release connections, etc.
        pass

print(calculate_bmi_safe(70, 1.75))
print(calculate_bmi_safe(70, 0))
print(calculate_bmi_safe("seventy", 1.75))
```
**Expected Output**
```
22.857142857142858
Error: Height cannot be zero.
Error: Weight and height must be numbers.
```

---

## 3) `else` and `finally` in Action

```python
def safe_divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        return "Error: cannot divide by zero"
    else:
        return f"Result: {result}"
    finally:
        # Always runs — even if an exception occurred
        pass

print(safe_divide(10, 2))
print(safe_divide(10, 0))
```
**Expected Output**
```
Result: 5.0
Error: cannot divide by zero
```

---

## 4) Raising Your Own Errors with `raise`

```python
def dosage_per_kg(weight, per_kg=0.5):
    if not isinstance(weight, (int, float)) or weight <= 0:
        raise ValueError("weight must be a positive number")
    return weight * per_kg

try:
    print(dosage_per_kg(-10))
except ValueError as e:
    print("Caught:", e)
```
**Expected Output**
```
Caught: weight must be a positive number
```

---

## 5) Unit Testing with `unittest`

### Why Unit Tests?
- Prove your function works now.
- Prevent bugs when you change code later.

### Essentials
- Create a class inheriting from `unittest.TestCase`.
- Write methods that start with `test_...`.
- Use assertions like `assertEqual`, `assertAlmostEqual`, `assertTrue`, `assertRaises`, etc.

### Example: Tests for `calculate_bmi_safe`
```python
import unittest

def calculate_bmi_safe(weight, height):
    try:
        if not (isinstance(weight, (int, float)) and isinstance(height, (int, float))):
            raise TypeError("Weight and height must be numbers.")
        bmi = weight / (height ** 2)
    except ZeroDivisionError:
        return "Error: Height cannot be zero."
    except TypeError as e:
        return f"Error: {e}"
    return bmi

class TestCalculateBmiSafe(unittest.TestCase):
    def test_valid_input(self):
        self.assertAlmostEqual(calculate_bmi_safe(70, 1.75), 22.8571428571, places=4)

    def test_zero_height(self):
        self.assertEqual(calculate_bmi_safe(70, 0), "Error: Height cannot be zero.")

    def test_non_numeric_input(self):
        self.assertEqual(
            calculate_bmi_safe("seventy", 1.75),
            "Error: Weight and height must be numbers."
        )

# In a script:
# if __name__ == "__main__":
#     unittest.main()
```

> **Why `assertAlmostEqual`?** Floating-point math can have tiny rounding differences; this assertion allows tolerance via `places`.

---

## 6) Integration Testing (components working together)

```python
def calculate_health_risk(bmi, age, bp, cholesterol, smoker=False):
    try:
        if not all(isinstance(x, (int, float)) for x in (bmi, age, bp, cholesterol)):
            raise TypeError("BMI, age, blood pressure, and cholesterol must be numbers.")
        if bmi <= 0 or age <= 0 or bp <= 0 or cholesterol <= 0:
            raise ValueError("All inputs must be positive.")
        risk = (bmi * 0.2) + (age * 0.3) + (bp * 0.3) + (cholesterol * 0.2)
        if smoker:
            risk *= 1.5
        return risk
    except (TypeError, ValueError) as e:
        return f"Error: {e}"

import unittest

class TestHealthRiskIntegration(unittest.TestCase):
    def test_valid(self):
        self.assertAlmostEqual(calculate_health_risk(22.5, 45, 120, 200), 60.5, places=1)

    def test_smoker(self):
        self.assertAlmostEqual(calculate_health_risk(22.5, 45, 120, 200, smoker=True), 90.75, places=2)

    def test_bad_types(self):
        self.assertEqual(
            calculate_health_risk("22.5", 45, 120, 200),
            "Error: BMI, age, blood pressure, and cholesterol must be numbers."
        )
```

---

## 7) Edge-Case Testing

Test extremes and boundaries (very small/large values, zero, negatives, empty lists, wrong types).

```python
def calculate_dosage(weight, age, dosage_per_kg=0.5):
    try:
        if not (isinstance(weight, (int, float)) and isinstance(age, (int, float))):
            raise TypeError("Weight and age must be numbers.")
        if weight <= 0 or age <= 0:
            raise ValueError("Weight and age must be positive numbers.")
        dose = weight * dosage_per_kg
        if age < 12:        # child adjustment
            dose *= 0.75
        return dose
    except (TypeError, ValueError) as e:
        return f"Error: {e}"

import unittest

class TestDosageEdgeCases(unittest.TestCase):
    def test_high_dosage(self):
        self.assertAlmostEqual(calculate_dosage(200, 30, dosage_per_kg=10), 2000.0, places=1)

    def test_low_dosage(self):
        # 0.1 * 0.01 = 0.001; child factor 0.75 => 0.00075
        self.assertAlmostEqual(calculate_dosage(0.1, 1, dosage_per_kg=0.01), 0.00075, places=5)

    def test_zero_weight(self):
        self.assertEqual(calculate_dosage(0, 30), "Error: Weight and age must be positive numbers.")

    def test_negative_age(self):
        self.assertEqual(calculate_dosage(70, -1), "Error: Weight and age must be positive numbers.")
```

---

## 8) Helpful Patterns & Tips

- **AAA** (Arrange–Act–Assert): structure tests clearly.
- **One behavior per test**: small, focused, readable.
- **Use specific assertions**: `assertAlmostEqual` for floats, `assertRaises` for expected exceptions.
- **Keep tests independent**: no shared state between tests.
- **Name tests clearly**: e.g., `test_zero_height_returns_error`.
- **Continuous Testing**: run tests often (e.g., `python -m unittest` or `pytest`).

---

## 9) Bonus: Assertions & Custom Exceptions

### Assertions (developer checks)
```python
def age_to_decade(age):
    assert isinstance(age, (int, float)) and age >= 0, "age must be a non-negative number"
    return int(age // 10)
```
> Use assertions for internal sanity checks, not user-facing validation.

### Custom Exceptions
```python
class ClinicalDataError(Exception):
    """Base error for clinical data issues."""

class InvalidBmiError(ClinicalDataError):
    pass

def checked_bmi(weight, height):
    if height == 0:
        raise InvalidBmiError("Height cannot be zero.")
    return weight / (height ** 2)

try:
    checked_bmi(70, 0)
except InvalidBmiError as e:
    print("Caught:", e)
```
**Expected Output**
```
Caught: Height cannot be zero.
```

---

## 10) Final Exercise (with solution pattern)

**Task:** Implement `calculate_health_risk_score` with validation & tests:
- Inputs: `bmi`, `age`, `medical_history` (list), `smoker` flag.
- Validate types/values, return informative errors.
- Write unit tests for valid, invalid, and boundary cases.

**Solution pattern:**
```python
import unittest

def calculate_health_risk_score(bmi, age, medical_history, smoker=False):
    """Calculate a health risk score based on BMI, age, and medical history.

    Parameters:
        bmi (float): BMI (> 0)
        age (int|float): age in years (> 0)
        medical_history (list[str]): conditions, e.g., ["heart disease", "diabetes"]
        smoker (bool): whether the patient smokes

    Returns:
        float | str: risk score (higher = riskier) or an error message.
    """
    try:
        if not isinstance(bmi, (int, float)) or not isinstance(age, (int, float)) or not isinstance(medical_history, list):
            raise TypeError("BMI must be a number, age must be a number, and medical history must be a list.")
        if bmi <= 0 or age <= 0:
            raise ValueError("BMI and age must be positive numbers.")
        risk = (bmi * 0.3) + (age * 0.4)
        if "heart disease" in medical_history:
            risk += 20
        if "diabetes" in medical_history:
            risk += 10
        if smoker:
            risk *= 1.5
        return risk
    except (TypeError, ValueError) as e:
        return f"Error: {e}"

class TestHealthRiskScoreCalculator(unittest.TestCase):
    def test_valid(self):
        self.assertAlmostEqual(calculate_health_risk_score(25, 50, ["high cholesterol"]), 27.5, places=1)

    def test_with_history(self):
        self.assertAlmostEqual(
            calculate_health_risk_score(25, 50, ["heart disease", "diabetes"]),
            (25*0.3 + 50*0.4) + 20 + 10, places=4
        )

    def test_smoker(self):
        base = (25*0.3 + 50*0.4)
        self.assertAlmostEqual(calculate_health_risk_score(25, 50, [], smoker=True), base * 1.5, places=4)

    def test_bad_types(self):
        self.assertEqual(
            calculate_health_risk_score("25", 50, []),
            "Error: BMI must be a number, age must be a number, and medical history must be a list."
        )
        self.assertEqual(
            calculate_health_risk_score(25, 50, "not a list"),
            "Error: BMI must be a number, age must be a number, and medical history must be a list."
        )

    def test_bad_values(self):
        self.assertEqual(calculate_health_risk_score(0, 50, []), "Error: BMI and age must be positive numbers.")
        self.assertEqual(calculate_health_risk_score(25, 0, []), "Error: BMI and age must be positive numbers.")

# In a script:
# if __name__ == "__main__":
#     unittest.main()
```
---

## Quick Reference

- **Error handling:** `try / except / else / finally`
- **Raise error:** `raise ValueError("message")`
- **Type check:** `isinstance(x, (int, float))`
- **Unit tests:** subclass `unittest.TestCase` and write `test_...` methods
- **Float asserts:** `assertAlmostEqual(x, y, places=n)`
- **Run tests:** `python -m unittest` or `pytest`

**One‑line takeaway:**  
Handle errors clearly, validate inputs early, and write small, focused tests—you’ll catch bugs faster and ship more reliable code.



> BONUS ON WHEN TO TEST

# Why Test? When to Test? Where to Use `try/except` — A Beginner’s Guide

This mini‑guide gives you practical rules you can use today: **when to write tests**, **what to test**, and **where (and where not) to write `try/except`**.

---

## 1) Why test at all?
- **Catch bugs early** before they reach users.
- **Document behavior**: tests explain how your code should work.
- **Enable refactoring** safely: if tests still pass, you didn’t break things.
- **Build confidence** to change or add features quickly.

---

## 2) When should you test? (Simple timeline)

1. **As you write each function (Unit tests)**
   - Write 1–3 tests for normal cases + a couple of edge cases.
2. **Before refactoring**
   - Add/extend tests first, then refactor; tests guard behavior.
3. **After fixing a bug (Regression tests)**
   - Add a test that *reproduces* the bug; keep it so it never returns.
4. **When wiring components (Integration tests)**
   - Test how functions/modules work *together*.
5. **On every change (Continuous Integration)**
   - Run tests automatically in CI (e.g., GitHub Actions).

> **Test pyramid**: many **unit** tests, fewer **integration** tests, very few **end‑to‑end** tests.

---

## 3) What types of tests?

- **Unit tests**: one small function/class. Fast, precise feedback.
- **Integration tests**: multiple parts working together (e.g., parse → validate → save).
- **End‑to‑end**: simulate a user flow. Slower; keep these few.
- **Regression tests**: lock in fixed bugs so they don’t come back.

---

## 4) Should you put `try/except` in every function? (No.)

Use `try/except` **strategically**, not everywhere.

### Good places for `try/except`
- **At boundaries** where errors are expected:
  - user input, file I/O, network calls, database operations, parsing external data.
- **Top‑level / entry points** (e.g., `main()` or a web request handler)
  - Catch unhandled exceptions, log, show a friendly message.
- **Where you can recover or add context**
  - Transform a low‑level error into a clear, actionable message.

### Avoid blanket `try/except`
- **Deep inside core logic** (let exceptions bubble up).
- **`except Exception:`** without re‑raising (masks real bugs).
- **Silent excepts** that hide problems.

### Best practices
- Catch **specific** exceptions (e.g., `ValueError`, `ZeroDivisionError`).
- Keep **try blocks small** (wrap only the risky line or two).
- Use **validation** and **meaningful error messages**.
- Prefer **EAFP** (“try it and handle failure”) when it’s clearer than over‑checking.

---

## 5) Tiny examples

### A) Let exceptions bubble; handle near the top‑level
```python
def bmi(weight, height):
    # Core logic stays simple
    return weight / (height ** 2)

def main():
    try:
        print(bmi(70, 1.75))   # OK
        print(bmi(70, 0))      # Raises ZeroDivisionError
    except ZeroDivisionError:
        print("Height can’t be zero.")
    except TypeError:
        print("Weight and height must be numbers.")

# main()
```

### B) Handle errors at the boundary (file I/O + parsing)
```python
def read_floats(path):
    with open(path) as f:
        return [float(line.strip()) for line in f]

def load_data(path):
    try:
        return read_floats(path)
    except FileNotFoundError:
        return "Error: file not found."
    except ValueError:
        return "Error: file contains non‑numeric values."
```

### C) Narrow try/except with small scope
```python
def safe_div(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return None  # or raise ValueError("b must not be zero")
```

### D) EAFP (try) vs LBYL (check)
```python
# EAFP: try first, handle failures
def first_item(seq):
    try:
        return seq[0]
    except (TypeError, IndexError):
        return None

# LBYL: check before acting
def first_item_lbyl(seq):
    if isinstance(seq, (list, tuple)) and len(seq) > 0:
        return seq[0]
    return None
```

---

## 6) Minimal unit testing pattern (`unittest`)
```python
import unittest

def dosage_per_kg(weight, per_kg=0.5):
    if not isinstance(weight, (int, float)) or weight <= 0:
        raise ValueError("weight must be a positive number")
    return weight * per_kg

class TestDosage(unittest.TestCase):
    def test_happy_path(self):
        self.assertAlmostEqual(dosage_per_kg(80), 40.0)

    def test_invalid_weight(self):
        with self.assertRaises(ValueError):
            dosage_per_kg(0)

# if __name__ == "__main__":
#     unittest.main()
```

---

## 7) Quick checklist

- ✅ Write tests:
  - when adding a function,
  - when fixing a bug,
  - before refactoring,
  - when integrating parts,
  - and in CI on every change.
- ✅ Use `try/except`:
  - at I/O & user‑input boundaries,
  - with *specific* exceptions and *small* try blocks,
  - where you can recover or add helpful context.
- ❌ Don’t:
  - wrap everything in `try/except`,
  - swallow errors or use `except Exception:` broadly,
  - hide failures—make them visible and understandable.

**Bottom line:** test early and often; catch errors where they make sense; keep core logic clean.
