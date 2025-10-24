# Importing Modules in Python — Beginner Guide + Worked Exercises

> Learn what modules are, how to import them (several ways), how to explore them, create your own module, and handle import errors. Every exercise states the **question**, then shows a **solution** with code and expected **output**. Built-ins are explained along the way. This file renders well on GitHub.

---

## What is a Module?

- A **module** is a Python file (`.py`) that contains functions, classes, and variables.
- Python ships with a **Standard Library** (e.g., `math`, `statistics`, `pathlib`).
- You can install **third-party** modules (e.g., `numpy`, `pandas`, `matplotlib`) via `pip`.
- You can **create your own** module and import it into other scripts.

## Why Use Modules?

- **Reusability**: reuse code across projects.
- **Organization**: split logic into separate files for clarity.
- **Efficiency**: leverage well-tested library code instead of reinventing the wheel.

---

## 1) Importing Standard Library Modules

### Example — Using `math` for health calculations
```python
import math

# Calculate the square root of the average BMI of a population
average_bmi = 25.7
sqrt_bmi = math.sqrt(average_bmi)
print(f"The square root of the average BMI is {sqrt_bmi:.2f}")
```
**Expected output**
```
The square root of the average BMI is 5.07
```

**Built-ins & functions**
- `import math` — loads the whole module; call functions as `math.sqrt`, `math.pow`, etc.
- `math.sqrt(x)` — square root of `x`.
- `print(...)` — display values.
- f-strings `f"... {value:.2f}"` — format numbers to 2 decimal places.

#### Exercise 1 — Your Turn (with solution)
**Question:**  
1) Use `math.pow` to compute **BMI squared**.  
2) Use `math.log` to compute the **natural logarithm** of a blood pressure value (e.g., `bp = 120`).

**Solution:**
```python
import math

average_bmi = 25.7
bmi_squared = math.pow(average_bmi, 2)   # or: average_bmi ** 2
print(f"BMI squared: {bmi_squared:.2f}")

bp = 120
bp_log = math.log(bp)  # natural log
print(f"ln(120) ≈ {bp_log:.4f}")
```
**Expected output (approx.)**
```
BMI squared: 660.49
ln(120) ≈ 4.7875
```

---

## 2) Importing *Specific* Functions or Classes

Import only what you need to keep code concise and avoid long qualifiers.

```python
from statistics import mean, median

bmi_values = [22.5, 25.7, 28.9, 23.4, 26.8]
mean_bmi = mean(bmi_values)
median_bmi = median(bmi_values)

print(f"The mean BMI is {mean_bmi:.2f}")
print(f"The median BMI is {median_bmi:.2f}")
```
**Expected output**
```
The mean BMI is 25.46
The median BMI is 25.70
```

**Built-ins & functions**
- `from statistics import mean, median` — imports just the named functions.
- `statistics.mean(iterable)` — arithmetic mean.
- `statistics.median(iterable)` — median value.

#### Exercise 2 — Your Turn (with solution)
**Question:**  
1) Import and compute the **standard deviation** of `bmi_values` using `stdev`.  
2) Compute the **mode** (most common value) of a list of `ages`.

**Solution:**
```python
from statistics import stdev, mode

bmi_values = [22.5, 25.7, 28.9, 23.4, 26.8]
bmi_stdev = stdev(bmi_values)
print(f"Standard deviation of BMI: {bmi_stdev:.2f}")

ages = [30, 34, 30, 41, 30, 34]
ages_mode = mode(ages)
print(f"Mode age: {ages_mode}")
```
**Expected output**
```
Standard deviation of BMI: 2.31
Mode age: 30
```

---

## 3) Importing Modules with **Aliases**

Aliases keep code readable and avoid name clashes.

### Example — Plot with `matplotlib.pyplot` as `plt`
```python
import matplotlib.pyplot as plt

bmi_values = [22.5, 25.7, 28.9, 23.4, 26.8]

plt.plot(bmi_values)
plt.title('BMI Values Over Time')
plt.xlabel('Time')
plt.ylabel('BMI')
plt.show()
```
**What happens?** A simple line plot is displayed.

**Built-ins & functions**
- `import ... as ...` — alias for shorter calls (here `plt`).
- `plt.plot(...)`, `plt.bar(...)` — basic charts.
- `plt.title/xlabel/ylabel`, `plt.show()` — annotate and render the figure.

#### Exercise 3 — Your Turn (with solution)
**Question:**  
1) Create a **bar chart** of `bmi_values` using `plt.bar`.  
2) Import `numpy` as `np`, create a NumPy array from `bmi_values`, and print it.

**Solution:**
```python
import matplotlib.pyplot as plt
import numpy as np

bmi_values = [22.5, 25.7, 28.9, 23.4, 26.8]

# 1) Bar chart
plt.bar(range(len(bmi_values)), bmi_values)
plt.title('BMI Values (Bar)')
plt.xlabel('Patient Index')
plt.ylabel('BMI')
plt.show()

# 2) NumPy array
arr = np.array(bmi_values)
print("NumPy array:", arr)
```
**Expected output**
```
NumPy array: [22.5 25.7 28.9 23.4 26.8]
```

> Note: `matplotlib` and `numpy` are third-party; install via `pip install matplotlib numpy` if needed.

---

## 4) Exploring Modules with `dir()` and `help()`

Find out what a module contains and how to use it.

```python
import math
print(dir(math))      # list names inside math
help(math.sqrt)       # show docs for math.sqrt
```

**Built-ins**
- `dir(obj_or_module)` — returns a list of attribute names.
- `help(obj_or_module)` — prints documentation (docstrings).

#### Exercise 4 — Your Turn (with solution)
**Question:**  
1) Use `dir(statistics)` to list available names.  
2) Use `help(math.log)` to view documentation.

**Solution:**
```python
import statistics, math
print(dir(statistics))
help(math.log)
```

---

## 5) Creating and Importing **Custom Modules**

Write your own module as a `.py` file and import it.

### Example — `health_utils.py`
```python
# --- in a file named health_utils.py ---

def calculate_bmi(weight, height):
    """Calculate BMI using weight (kg) and height (m)."""
    return weight / (height ** 2)

def is_healthy_bmi(bmi):
    """True if BMI is in the healthy range (18.5-24.9)."""
    return 18.5 <= bmi <= 24.9
```

**Use the module:**
```python
import health_utils

weight = 70
height = 1.75
bmi = health_utils.calculate_bmi(weight, height)
print(f"BMI: {bmi:.2f}")
print("Healthy range?", "Yes" if health_utils.is_healthy_bmi(bmi) else "No")
```
**Expected output**
```
BMI: 22.86
Healthy range? Yes
```

> Put `health_utils.py` in the same directory as your script/notebook (or on your PYTHONPATH) so `import health_utils` works.

#### Exercise 5 — Your Turn (with solution)
**Question:**  
Add `calculate_bmr` (Mifflin-St Jeor) to `health_utils.py` and then import it to compute BMR:
- Male: `10*w + 6.25*h - 5*a + 5`
- Female: `10*w + 6.25*h - 5*a - 161`

**Solution (add to module):**
```python
# --- add inside health_utils.py ---
def calculate_bmr(weight, height_cm, age, gender):
    """BMR via Mifflin-St Jeor (height in cm)."""
    g = gender.lower()
    if g == 'male':
        return 10*weight + 6.25*height_cm - 5*age + 5
    elif g == 'female':
        return 10*weight + 6.25*height_cm - 5*age - 161
    else:
        raise ValueError("gender must be 'male' or 'female'")
```

**Solution (use it):**
```python
import health_utils

bmr = health_utils.calculate_bmr(weight=70, height_cm=175, age=30, gender='male')
print(f"BMR: {bmr:.2f} kcal/day")
```
**Expected output**
```
BMR: 1648.75 kcal/day
```

---

## 6) Handling Import Errors

Handle missing or misspelled modules gracefully.

```python
try:
    import non_existent_module
except ImportError as e:
    print(f"Error: {e}. Please ensure the module is installed and the name is correct.")
```

**Built-ins**
- `try/except` — handle runtime errors gracefully.
- `ImportError` — raised when Python can’t import a module.

#### Exercise 6 — Your Turn (with solution)
**Question:**  
Try to import a clearly missing module and fall back so your script continues.

**Solution:**
```python
try:
    import imaginary_module
except ImportError:
    print("imaginary_module is not installed; continuing without it.")
    imaginary_module = None  # fallback placeholder

print("Script continues here.")
```
**Expected output**
```
imaginary_module is not installed; continuing without it.
Script continues here.
```

---

## Quick Reference: Built-ins Used

- `import module` / `from module import name` / `import module as alias` — import styles.
- `print(value, ...)` — display output.
- **Math**: `math.sqrt`, `math.pow`, `math.log`
- **Statistics**: `statistics.mean`, `median`, `stdev`, `mode`
- **Plotting**: `matplotlib.pyplot` (`plt`) — `plot`, `bar`, `title`, `xlabel`, `ylabel`, `show`
- `dir(obj_or_module)` — list attributes/names
- `help(obj_or_module)` — show docs
- `try/except ImportError` — handle missing modules
- Custom module — save functions in `health_utils.py` and `import health_utils`

---

**Tip:** Keep your custom modules in the same folder as the script/notebook (or configure PYTHONPATH). Use aliases (`as`) for readability (`import numpy as np`, `import matplotlib.pyplot as plt`). And when you’re unsure, check `dir()` and `help()`!

