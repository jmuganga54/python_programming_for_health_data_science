# Iterations in Python 

Iteration means **repeating** an action several times. In Python, you’ll mostly use:
- `for` loops — repeat over each item in a sequence (list, string, range, etc.).
- `while` loops — repeat **while** a condition is true.
- Helpful built-ins: **`range()`** (make number sequences) and **`len()`** (count items).

---

## Built-in functions used (explained first)

### 1) `print(value, ...)`
Shows information on the screen. You can pass many values, or control the end of the line with `end=`.

```python
print("Hello", 123)
print("A", end=" "); print("B")  # end=" " keeps same line, puts a space
```
**Output**
```
Hello 123
A B
```

### 2) `range(start, stop, step)`
Creates a sequence of integers. Often used in `for` loops.
- `range(stop)` → 0, 1, 2, …, stop-1  
- `range(start, stop)` → start, …, stop-1  
- `range(start, stop, step)` → uses a step (can be negative)

```python
print(list(range(5)))          # 0..4
print(list(range(2, 7)))       # 2..6
print(list(range(10, 0, -3)))  # 10, 7, 4, 1
```
**Output**
```
[0, 1, 2, 3, 4]
[2, 3, 4, 5, 6]
[10, 7, 4, 1]
```

### 3) `len(object)`
Returns the **number of items** in an object (list, string, tuple, dict, etc.).

```python
patients = ["John", "Jane", "Alice"]
print(len(patients))
print(len("Manchester"))
```
**Output**
```
3
10
```

> Tip: `range(len(seq))` is common when you need **indexes**. If you only need items, loop over the sequence directly.  

---

## Example 1 — For loops (looping over items)

The `for` loop goes through each element in a sequence.

```python
# List of patients
patients = ['John Doe', 'Jane Smith', 'Alice Johnson']

# Loop directly over items
for patient in patients:
    print(patient)
```
**Output**
```
John Doe
Jane Smith
Alice Johnson
```

### With indexes (using `range(len(...))`)
```python
patients = ['John Doe', 'Jane Smith', 'Alice Johnson']
for i in range(len(patients)):
    print(f"Patient {i + 1}: {patients[i]}")
```
**Output**
```
Patient 1: John Doe
Patient 2: Jane Smith
Patient 3: Alice Johnson
```

> Pro tip (optional): `enumerate(seq)` gives index **and** item in one go:
```python
for i, patient in enumerate(patients, start=1):
    print(f"Patient {i}: {patient}")
```
**Output**
```
Patient 1: John Doe
Patient 2: Jane Smith
Patient 3: Alice Johnson
```

---

## Example 2 — Using `range()` in loops

Count or generate positions with `range()`.

```python
# Numbers 0 to 9 on one line
for number in range(10):
    print(number, end=' ')
```
**Output**
```
0 1 2 3 4 5 6 7 8 9 
```

**More `range()` patterns**
```python
# Custom start/stop/step
for n in range(2, 11, 2):
    print(n, end=' ')
```
**Output**
```
2 4 6 8 10 
```

```python
# Reverse counting
for n in range(5, 0, -1):
    print(n, end=' ')
```
**Output**
```
5 4 3 2 1 
```

---

## Example 3 — Using `len()` with loops

Use `len()` to decide how many times to loop or to get valid indexes.

```python
patients = ['John Doe', 'Jane Smith', 'Alice Johnson']
num_patients = len(patients)

for i in range(num_patients):
    print(f"Patient {i + 1}: {patients[i]}")
```
**Output**
```
Patient 1: John Doe
Patient 2: Jane Smith
Patient 3: Alice Johnson
```

---

## Example 4 — While loops (loop while a condition is true)

`while` repeats **until** the condition becomes `False`.  
Be sure to **update** something inside the loop, so it eventually stops.

```python
patients = ['John Doe', 'Jane Smith', 'Alice Johnson']
i = 0

while i < len(patients):
    print(f"Patient {i + 1}: {patients[i]}")
    i += 1  # if you forget this, it will loop forever
```
**Output**
```
Patient 1: John Doe
Patient 2: Jane Smith
Patient 3: Alice Johnson
```

> Tip:  
> - `break` stops the loop immediately.  
> - `continue` skips to the **next** iteration.

```python
# Stop when you find "Jane Smith"
for p in patients:
    if p == "Jane Smith":
        print("Found Jane; stopping.")
        break
    print("Checking:", p)
```
**Output**
```
Checking: John Doe
Found Jane; stopping.
```

---

## Example 5 — Nested loops (loops inside loops)

Useful for grids, tables, pairs of data, etc.

```python
patients = ['John Doe', 'Jane Smith', 'Alice Johnson']
readings = ['120/80', '130/85', '125/82']

for i in range(len(patients)):     # outer loop over rows
    for j in range(1):             # inner loop (here trivial)
        print(f"Patient {i + 1}: {patients[i]} | BP: {readings[i]}")
```
**Output**
```
Patient 1: John Doe | BP: 120/80
Patient 2: Jane Smith | BP: 130/85
Patient 3: Alice Johnson | BP: 125/82
```

A more realistic nested structure (table of multiple measurements):
```python
patients = ["John", "Jane", "Alice"]
measurements = [
    ["BP:120/80", "HR:72",  "BMI:22.8"],  # John
    ["BP:130/85", "HR:80",  "BMI:26.2"],  # Jane
    ["BP:125/82", "HR:76",  "BMI:23.5"]   # Alice
]

for i, name in enumerate(patients, start=1):
    print(f"Patient {i}: {name}")
    for m in measurements[i-1]:
        print("  -", m)
```
**Output**
```
Patient 1: John
  - BP:120/80
  - HR:72
  - BMI:22.8
Patient 2: Jane
  - BP:130/85
  - HR:80
  - BMI:26.2
Patient 3: Alice
  - BP:125/82
  - HR:76
  - BMI:23.5
```

---

## Mini Exercises (with solutions)

### Exercise 1 — Print names in reverse order  
**Goal:** Use `range()` with a negative step.

**Solution**
```python
patients = ['John Doe', 'Jane Smith', 'Alice Johnson']

for i in range(len(patients) - 1, -1, -1):
    print(patients[i])
```
**Output**
```
Alice Johnson
Jane Smith
John Doe
```

---

### Exercise 2 — Only even numbers (0–20)
**Goal:** Use `range(start, stop, step)` to skip odds.

**Solution**
```python
for n in range(0, 21, 2):
    print(n, end=" ")
```
**Output**
```
0 2 4 6 8 10 12 14 16 18 20 
```

---

### Exercise 3 — Guard against empty lists  
**Goal:** Use `len()` to check before looping.

**Solution**
```python
patients = []

if len(patients) == 0:
    print("No patients to process.")
else:
    for p in patients:
        print(p)
```
**Output**
```
No patients to process.
```

---

### Exercise 4 — Sum a list using a `for` loop  
**Goal:** Compute a total manually.

**Solution**
```python
values = [3, 5, 7, 2]
total = 0
for v in values:
    total += v
print(total)
```
**Output**
```
17
```

---

## Common Pitfalls & Best Practices

**Pitfalls**
1) **Infinite loops:** In `while` loops, make sure something changes (e.g., `i += 1`).  
2) **Off-by-one errors:** Remember `range(stop)` excludes `stop`.  
3) **Looping when not needed:** Sometimes you can use built-ins like `sum(values)` or slicing instead of writing a loop.

**Best Practices**
1) Prefer looping **over items** (e.g., `for patient in patients`) unless you truly need indexes.  
2) Use `enumerate()` to get **both** index and item cleanly.  
3) Keep loop bodies short; move complex logic into helper functions.  
4) Use **clear names** and comments for readability.

---

## Quick Reference (what to use when)

- Need to loop a fixed number of times → `for i in range(n):`
- Need to loop over items in a list → `for item in items:`
- Need index **and** item → `for i, item in enumerate(items):`
- Need to repeat until a condition stops → `while condition:`

---

### One-line takeaway
Use `for` to iterate over sequences, `while` to repeat until a condition changes, `range()` to generate counting sequences, and `len()` to measure how many items to loop through.
