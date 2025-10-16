# Operators in Python 

Python operators let you **calculate**, **compare**, and **combine conditions**. You will use them every day for data work.

---

## 1) Arithmetic Operators

Do maths.

| Operator | Meaning | Example | Notes |
|---|---|---|---|
| `+` | Addition | `a + b` | add numbers or join strings |
| `-` | Subtraction | `a - b` |  |
| `*` | Multiplication | `a * b` |  |
| `/` | Division | `a / b` | always float (e.g., `5/2 -> 2.5`) |
| `%` | Modulus | `a % b` | remainder |
| `**` | Exponent | `a ** b` | power |
| `//` | Floor division | `a // b` | divide then round **down** (e.g., `5//2 -> 2`) |

### Example: BMI (Body Mass Index)
```python
weight_kg = 70
height_m = 1.75
bmi = weight_kg / (height_m ** 2)
print(bmi)
```
**Output**
```
22.857142857142858
```

**Try it (exercise):** change weight and height.
```python
weight_kg = 85
height_m = 1.80
bmi = weight_kg / (height_m ** 2)
print(bmi)
```
**Output**
```
26.234567901234566
```

---

## 2) Assignment Operators

Update a variable in place.

| Operator | Meaning | Example | Same as |
|---|---|---|---|
| `=` | assign | `a = b` |  |
| `+=` | add then assign | `a += b` | `a = a + b` |
| `-=` | subtract then assign | `a -= b` | `a = a - b` |
| `*=` | multiply then assign | `a *= b` | `a = a * b` |
| `/=` | divide then assign | `a /= b` | `a = a / b` |
| `%=` | modulus then assign | `a %= b` | `a = a % b` |
| `//=` | floor divide then assign | `a //= b` | `a = a // b` |
| `**=` | exponent then assign | `a **= b` | `a = a ** b` |

### Example
```python
weight_kg = 70
weight_kg -= 5
print(weight_kg)
```
**Output**
```
65
```

**Try it (exercise):**  
```python
weight_kg = 85
weight_kg += 3
print(weight_kg)
```
**Output**
```
88
```

---

## 3) Comparison Operators

Return `True` or `False`.

| Operator | Meaning | Example |
|---|---|---|
| `==` | equal | `a == b` |
| `!=` | not equal | `a != b` |
| `>` | greater than | `a > b` |
| `<` | less than | `a < b` |
| `>=` | greater or equal | `a >= b` |
| `<=` | less or equal | `a <= b` |

### Example: Study eligibility by age
```python
patient_age = 45
min_age, max_age = 18, 65
is_eligible = min_age <= patient_age <= max_age
print(is_eligible)
```
**Output**
```
True
```

---

## 4) Logical Operators

Combine conditions.

| Operator | Meaning | Example result |
|---|---|---|
| `and` | both must be True | `True and False -> False` |
| `or` | at least one True | `True or False -> True` |
| `not` | flips truth | `not True -> False` |

### Example: Complex eligibility
```python
min_age, max_age = 18, 65
patient_age = 45
has_diabetes = False
has_heart_disease = True

is_eligible = (min_age <= patient_age <= max_age) and not has_diabetes and not has_heart_disease
print(is_eligible)
```
**Output**
```
False
```

---

## 5) Membership Operators

Check if a value is inside a sequence (list, string, etc.).

| Operator | Meaning | Example |
|---|---|---|
| `in` | is member | `3 in [1,2,3] -> True` |
| `not in` | is not member | `"a" not in "cup" -> True` |

### Example
```python
critical_patients = [101, 202, 303]
patient_id = 202
print(patient_id in critical_patients)
```
**Output**
```
True
```

---

## 6) Identity Operators

Do two variables point to the **same object** in memory?

| Operator | Meaning |
|---|---|
| `is` | same object |
| `is not` | different objects |

### Example
```python
list_a = [101, 202, 303]
list_b = list_a
list_c = [101, 202, 303]

print(list_a is list_b)  # same object
print(list_a is list_c)  # different object, same contents
```
**Output**
```
True
False
```

---

## 7) Operator Precedence (Order of operations)

Python evaluates some operators before others (like maths).  
Use **parentheses** to make intent clear.

> Exponent `**` → multiply/divide `* / // %` → add/subtract `+ -` → comparisons → `not` → `and` → `or`

### Example
```python
age = 30
bmi = 22
smoker = True
health_score = age / 10 + bmi / 2 - (5 if smoker else 0)
print(health_score)
```
**Output**
```
16.0
```

### More examples
```python
age = 50; bmi = 30; cholesterol = 220; smoker = True
risk_score = (age / 10 + bmi / 5 + cholesterol / 100) * (1.5 if smoker else 1)
print(risk_score)
```
**Output**
```
25.8
```

```python
age = 40; bmi = 28; has_diabetes = True; has_heart_disease = False; is_smoker = True
is_eligible = (18 <= age <= 60) and (bmi < 30) and not has_diabetes and (is_smoker or not has_heart_disease)
print(is_eligible)
```
**Output**
```
False
```

---

## 8) Selection with `if / elif / else`

Run different code depending on conditions.

### Example: BMI category
```python
bmi = 28

if bmi < 18.5:
    risk = "Underweight"
elif 18.5 <= bmi < 24.9:
    risk = "Normal weight"
elif 25 <= bmi < 29.9:
    risk = "Overweight"
else:
    risk = "Obesity"

print(risk)
```
**Output**
```
Overweight
```

### Example: Multiple conditions
```python
age = 45
bmi = 32
is_smoker = True

if age >= 18 and age <= 60 and bmi < 30 and not is_smoker:
    print("Eligible")
else:
    print("Not eligible")
```
**Output**
```
Not eligible
```

> Note on `input()`: Interactive input pauses the program to wait for typing. To **show an output here**, we usually avoid `input()` and set a value directly in examples.

---

## 9) `/` vs `//` (very common question)

```python
print(5 / 2)   # division (float)
print(5 // 2)  # floor division (rounded down)
print(-5 // 2) # also rounds down (toward negative infinity)
```
**Output**
```
2.5
2
-3
```

---

## 10) Tiny Practice (with solutions)

### Q1. Is a patient eligible (18–65 inclusive)?
```python
age = 70
eligible = 18 <= age <= 65
print(eligible)
```
**Output**
```
False
```

### Q2. Add five kilograms using `+=` and show the result.
```python
weight = 60
weight += 5
print(weight)
```
**Output**
```
65
```

### Q3. Check if `"AB123"` is in a list of critical IDs.
```python
critical = ["AA111", "AB123", "AC222"]
print("AB123" in critical)
```
**Output**
```
True
```

---

## Best Practices and Common Pitfalls

**Best Practices**
- Use **parentheses** to make complex expressions clear.
- Use **meaningful names** (`systolic_bp`, not `sbp1`).
- Avoid “magic numbers”: store constants in clearly named variables.

**Common Pitfalls**
- Misreading precedence (fix with parentheses).
- Confusing `/` (float division) with `//` (floor division).
- Mixing bitwise `&` `|` with logical `and` `or` (they are different).
- Assuming `is` means equality. Use `==` to compare values; `is` checks identity.

---

### One-line summary
Arithmetic does the maths, comparison checks values, logical combines conditions, membership tests “in lists,” identity tests “same object,” and `if/elif/else` chooses what to run — all governed by operator **precedence**.
