# Python Week One — Exercises & Solutions (Beginner-Friendly)

This README collects the week-one exercises **with** clear solutions, sample outputs, and brief explanations of each built-in used.  
You can paste any code block into a Python file or Jupyter notebook and run it.

---

## Table of Contents
- [Problem 1: Variables and Data Structures](#problem-1-variables-and-data-structures)
- [Problem 2: Operators in Python](#problem-2-operators-in-python)
- [Problem 3: Iteration in Python](#problem-3-iteration-in-python)
- [Problem 4: Iteration in Python](#problem-4-iteration-in-python)
- [Problem 5: Data Structures in Python](#problem-5-data-structures-in-python)
- [Problem 6: Functions in Python](#problem-6-functions-in-python)
- [Problem 7: Testing and Error Handling](#problem-7-testing-and-error-handling)
- [Problem 8: Testing and Handling Errors](#problem-8-testing-and-handling-errors)
- [Built-ins Quick Reference](#built-ins-quick-reference)

---

## Problem 1: Variables and Data Structures

### Question (restated)
Create these variables:
1) `age = 45` (int)  
2) `height = 1.75` (float)  
3) `name = 'John Doe'` (str)  
4) `symptoms = ['fever', 'cough', 'headache']` (list)  
5) `patient_info = {'ID': 1, 'Name': 'John Doe', 'BMI': 23.5}` (dict)

Then:
- Print each variable’s **type** and **value**  
- Add a new key `'age'` to `patient_info` and set it to `45`, and then update it (e.g., to `46`)

### Solution
```python
# Define variables
age = 45                       # int
height = 1.75                  # float
name = 'John Doe'              # str
symptoms = ['fever', 'cough', 'headache']  # list
patient_info = {'ID': 1, 'Name': 'John Doe', 'BMI': 23.5}  # dict

# Print type and value for each
print(type(age), age)
print(type(height), height)
print(type(name), name)
print(type(symptoms), symptoms)
print(type(patient_info), patient_info)

# Add and update a new key 'age' in the dictionary
patient_info['age'] = 45
print("After adding age:", patient_info)

patient_info['age'] = 46
print("After updating age:", patient_info)
```

**Expected Output**
```
<class 'int'> 45
<class 'float'> 1.75
<class 'str'> John Doe
<class 'list'> ['fever', 'cough', 'headache']
<class 'dict'> {'ID': 1, 'Name': 'John Doe', 'BMI': 23.5}
After adding age: {'ID': 1, 'Name': 'John Doe', 'BMI': 23.5, 'age': 45}
After updating age: {'ID': 1, 'Name': 'John Doe', 'BMI': 23.5, 'age': 46}
```

**Built-ins used**
- `type(x)`: returns the type of `x`.
- `print(...)`: prints to the console.
- List & dict literals: `[...]` and `{...}` create collections.
- Dict item set/update: `patient_info['age'] = ...`.

---

## Problem 2: Operators in Python

### Question (restated)
Compute the risk score:
\[
\text{Risk} = \frac{(A + B)\times(C - D) + E}{F \times (G + H)} - I
\]
with: A=120, B=30, C=70, D=20, E=5, F=2, G=1, H=10, I=25.

### Solution
```python
A, B, C, D, E, F, G, H, I = 120, 30, 70, 20, 5, 2, 1, 10, 25

numerator = (A + B) * (C - D) + E
denominator = F * (G + H)
risk_score = numerator / denominator - I

print("Numerator:", numerator)
print("Denominator:", denominator)
print("Risk Score:", risk_score)
```

**Expected Output (approx.)**
```
Numerator: 7505
Denominator: 22
Risk Score: 316.1363636363636
```

**Built-ins used**
- Arithmetic operators `+ - * /` follow standard math; `/` returns float.
- `print(...)` to display results.

---

## Problem 3: Iteration in Python

### Question (restated)
Given pairs `(Age, Glucose)`:
```
(65, 110), (45, 90), (72, 150), (51, 105), (40, 85)
```
1) Average glucose for patients **over 50**  
2) New list of **only those** glucose values  
3) Print glucose values higher than threshold (e.g., 100)

### Solution
```python
data = [(65, 110), (45, 90), (72, 150), (51, 105), (40, 85)]
threshold = 100

# Filter patients over 50 and collect their glucose levels
glucose_over_50 = []
for age, glucose in data:
    if age > 50:
        glucose_over_50.append(glucose)

# Compute the average for the filtered list
avg_glucose_over_50 = sum(glucose_over_50) / len(glucose_over_50)

# Get glucose levels higher than threshold
above_threshold = [g for _, g in data if g > threshold]

print("Glucose (age>50):", glucose_over_50)
print("Average glucose (age>50):", avg_glucose_over_50)
print(f"Glucose > {threshold}:", above_threshold)
```

**Expected Output**
```
Glucose (age>50): [110, 150, 105]
Average glucose (age>50): 121.66666666666667
Glucose > 100: [110, 150, 105]
```

**Built-ins used**
- `for ... in ...`: loop through items.
- Tuple unpacking: `for age, glucose in data`.
- `append(x)`: list method to add items.
- `sum(list)`, `len(list)`: quick numeric helpers.
- List comprehension: `[g for _, g in data if g > threshold]`.

---

## Problem 4: Iteration in Python

### Question (restated)
Count how many glucose readings are **strictly greater than 90** from:
```
[85, 90, 78, 92, 88, 75, 85, 95, 89, 84]
```

### Solution
```python
glucose = [85, 90, 78, 92, 88, 75, 85, 95, 89, 84]
threshold = 90

count = 0
for value in glucose:
    if value > threshold:
        count += 1

print("Count above 90:", count)
```

**Expected Output**
```
Count above 90: 2
```

**Built-ins used**
- `if ...:` inside loop for conditional counting.
- `count += 1`: increment pattern.
- `print(...)` for results.

---

## Problem 5: Data Structures in Python

### Question (restated)
Start with:
```python
patients = [
  {'ID': 1, 'Name': 'Alice',   'BMI': 22.4},
  {'ID': 2, 'Name': 'Bob',     'BMI': 27.1},
  {'ID': 3, 'Name': 'Charlie', 'BMI': 24.0}
]
```
Do:
1) Add a new patient  
2) Remove patient by ID  
3) Update BMI by ID

### Solution
```python
patients = [
    {'ID': 1, 'Name': 'Alice',   'BMI': 22.4},
    {'ID': 2, 'Name': 'Bob',     'BMI': 27.1},
    {'ID': 3, 'Name': 'Charlie', 'BMI': 24.0},
]

# 1) Add new patient
new_patient = {'ID': 4, 'Name': 'Diana', 'BMI': 26.3}
patients.append(new_patient)

# 2) Remove patient with ID=2
patients = [p for p in patients if p['ID'] != 2]

# 3) Update BMI for ID=3 (e.g., to 25.0)
for p in patients:
    if p['ID'] == 3:
        p['BMI'] = 25.0

print(patients)
```

**Expected Output**
```
[{'ID': 1, 'Name': 'Alice', 'BMI': 22.4},
 {'ID': 3, 'Name': 'Charlie', 'BMI': 25.0},
 {'ID': 4, 'Name': 'Diana', 'BMI': 26.3}]
```

**Built-ins used**
- `append(item)` to add to list.
- List comprehension for filtering.
- Dict access/update: `p['BMI'] = ...`.

---

## Problem 6: Functions in Python

### Question (restated)
Create:
- `calculate_bmi(weight, height)` → BMI = weight / (height**2)  
- `categorize_bmi(bmi)` → return one of: `Underweight`, `Normal weight`, `Overweight`, `Obese`

### Solution
```python
def calculate_bmi(weight, height):
    return weight / (height ** 2)

def categorize_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

bmi_value = calculate_bmi(70, 1.75)
print("BMI:", bmi_value)
print("Category:", categorize_bmi(bmi_value))
```

**Expected Output**
```
BMI: 22.857142857142858
Category: Normal weight
```

**Built-ins used**
- Function definition `def ...` and `return` to output values.
- `print(...)` for display.

---

## Problem 7: Testing and Error Handling

### Question (restated)
Define `safe_divide(numerator, denominator)`:
- If denominator is zero, **return `None`** and **print** an error message.
- Otherwise return the result.  
Test with `(10, 2)` and `(10, 0)`.

### Solution
```python
def safe_divide(numerator, denominator):
    try:
        return numerator / denominator
    except ZeroDivisionError:
        print("Error: Denominator cannot be zero.")
        return None

print("10 / 2 =", safe_divide(10, 2))
print("10 / 0 =", safe_divide(10, 0))
```

**Expected Output**
```
10 / 2 = 5.0
Error: Denominator cannot be zero.
10 / 0 = None
```

**Built-ins used**
- `try/except` to catch runtime errors.
- `ZeroDivisionError` is raised on division by zero.
- `print(...)` for a user-friendly message.

---

## Problem 8: Testing and Handling Errors

### Question (restated)
Define `divide_numbers(a, b)`:
- If `b == 0`, return: `"Error: division by zero is not allowed"`
- If either input is not a number, return: `"Error: inputs must be numbers"`
- Otherwise return `a / b`.

### Solution
```python
def divide_numbers(a, b):
    try:
        # Type check: must be int or float
        if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
            raise TypeError("inputs must be numbers")
        # Value check: b cannot be zero
        if b == 0:
            raise ZeroDivisionError("division by zero is not allowed")
        return a / b
    except TypeError:
        return "Error: inputs must be numbers"
    except ZeroDivisionError:
        return "Error: division by zero is not allowed"

print(divide_numbers(10, 2))     # valid
print(divide_numbers(10, 0))     # division by zero
print(divide_numbers("a", 2))    # not numbers
```

**Expected Output**
```
5.0
Error: division by zero is not allowed
Error: inputs must be numbers
```

**Built-ins used**
- `isinstance(x, (int, float))`: safe type checking.
- `raise`: create and handle your own exceptions.
- `try/except`: convert low-level errors to friendly messages.

---

## Built-ins Quick Reference

- **`print(value, ...)`** → display output.
- **`type(x)`** → returns the type of `x`.
- **`isinstance(x, (T1, T2))`** → checks if `x` is an instance of any given types.
- **`len(seq)`** → number of items in a sequence.
- **`sum(iterable)`** → sum of numbers.
- **`list.append(x)`** → add `x` to the end.
- **List comprehension** → concise list creation/filtering.
- **`try/except`** → handle runtime errors gracefully.
- **`raise Error("msg")`** → signal a specific error on purpose.
- **Dictionaries** → key-value pairs: `d['key']`, `d['key']=value`.

---

