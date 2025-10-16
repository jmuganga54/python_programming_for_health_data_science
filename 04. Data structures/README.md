# Data Structures in Python — Beginner Guide

We’ll cover the 4 core, built-in data structures:

- **List** — ordered, **mutable**, allows duplicates.
- **Tuple** — ordered, **immutable**, allows duplicates.
- **Set** — **unordered**, **unique** elements only (no duplicates).
- **Dictionary** — key → value mapping, super fast lookups.

You’ll also see helpful built-ins like **`len()`**, **`range()`**, **`print()`**, plus common **methods** (e.g., `append`, `remove`, `items`, etc.).

---

## Built-in functions used (what they do)

- **`print(*values, sep=' ', end='\n')`**: shows values on screen. `sep` controls separator, `end` controls line ending.
- **`len(obj)`**: number of items in `obj` (works for lists, tuples, sets, dicts, strings, …).
- **`range(start, stop[, step])`**: produces integers from `start` to `stop-1`, step by `step` (default step is 1). Often used for counting in loops.
- **`type(obj)`**: tells you the object’s type.
- **`sorted(iterable, reverse=False)`**: returns a **new** sorted list (doesn’t change the original); for sets/dicts it sorts their elements/keys.

I’ll also explain **methods** (functions on an object), like `list.append()` or `dict.get()` when we use them.

---

## 1) Lists

**What:** Ordered collection, **mutable** (you can change it), allows duplicates.  
**Create:** square brackets `[]`.

### Common list methods
- **`append(x)`**: add `x` to the end.
- **`remove(x)`**: remove the **first** occurrence of `x` (error if not found).
- **`pop([i])`**: remove and return item at index `i` (last item if `i` omitted).
- **`insert(i, x)`**: insert `x` at position `i`.
- **`sort()`**: sort list **in place** (modifies the list).
- **`reverse()`**: reverse list **in place**.
- **Indexing**: `lst[i]` (0-based), **Slicing**: `lst[a:b]`.

### Example — Managing Patient Records
```python
patients = ['John Doe', 'Jane Smith', 'Alice Johnson']

# Show each patient (using len() and range())
for i in range(len(patients)):
    print(f'Patient {i + 1}: {patients[i]}')

# Add a patient (append)
patients.append('Bob Brown')

# Remove a patient (remove)
patients.remove('Jane Smith')

# Show updated list
print('\nUpdated List of Patients:')
for i in range(len(patients)):
    print(f'Patient {i + 1}: {patients[i]}')

# Show type and length
print(type(patients), 'with length', len(patients))
```
**Output**
```
Patient 1: John Doe
Patient 2: Jane Smith
Patient 3: Alice Johnson

Updated List of Patients:
Patient 1: John Doe
Patient 2: Alice Johnson
Patient 3: Bob Brown
<class 'list'> with length 3
```

### Exercise (with solution)
**Task:** Add two names, sort the list alphabetically, then show the last two names.

**Solution**
```python
patients = ['John Doe', 'Alice Johnson', 'Bob Brown']
patients.append('Carol King')
patients.append('Derek Lee')

# Sort in place
patients.sort()

print('Sorted:', patients)
print('Last two:', patients[-2:])
```
**Output**
```
Sorted: ['Alice Johnson', 'Bob Brown', 'Carol King', 'Derek Lee', 'John Doe']
Last two: ['Derek Lee', 'John Doe']
```

---

## 2) Tuples

**What:** Ordered, **immutable** (cannot be changed), allows duplicates.  
**Create:** parentheses `()` or just commas.

**When to use:** fixed data that shouldn’t change; as dictionary keys (because they are immutable).

### Example — (ID, Diagnosis) pairs
```python
patient_diagnoses = [(1, 'Diabetes'), (2, 'Hypertension'), (3, 'Asthma')]

for patient in patient_diagnoses:
    pid, dx = patient  # unpacking the tuple
    print(f'Patient ID: {pid}, Diagnosis: {dx}')

print(type(patient_diagnoses[0]))
```
**Output**
```
Patient ID: 1, Diagnosis: Diabetes
Patient ID: 2, Diagnosis: Hypertension
Patient ID: 3, Diagnosis: Asthma
<class 'tuple'>
```

### Exercise (with solution)
**Task:** Given a list of `(id, diagnosis)` tuples, find the diagnosis for `id == 2`. If not found, print “Not found”.

**Solution**
```python
patient_diagnoses = [(1, 'Diabetes'), (2, 'Hypertension'), (3, 'Asthma')]

target_id = 2
result = None

for pid, dx in patient_diagnoses:
    if pid == target_id:
        result = dx
        break

print(result if result is not None else 'Not found')
```
**Output**
```
Hypertension
```

---

## 3) Sets

**What:** **Unordered**, **unique** elements only (no duplicates).  
**Create:** curly braces `{}` or `set([...])`.  
**Great for:** removing duplicates, membership tests, set math.

### Common set operations
- **`add(x)`**: add an element.
- **`discard(x)`**: remove if present (no error if missing).
- **`remove(x)`**: remove (error if missing).
- **`union`** (`|`), **`intersection`** (`&`), **`difference`** (`-`), **`symmetric_difference`** (`^`).

### Example — Unique Patient Conditions
```python
conditions = {'Diabetes', 'Hypertension', 'Asthma', 'Diabetes'}  # duplicate 'Diabetes' collapses
print('Unique Conditions:', conditions)

other_conditions = {'Diabetes', 'Allergy'}

common = conditions.intersection(other_conditions)
unioned = conditions.union(other_conditions)
only_in_first = conditions.difference(other_conditions)

print('Common:', common)
print('Union:', unioned)
print('Only in first:', only_in_first)
```
**Output** *(order may vary, sets are unordered)*:
```
Unique Conditions: {'Asthma', 'Hypertension', 'Diabetes'}
Common: {'Diabetes'}
Union: {'Asthma', 'Hypertension', 'Diabetes', 'Allergy'}
Only in first: {'Asthma', 'Hypertension'}
```

### Exercise (with solution)
**Task:** Given two condition sets, show conditions present in **exactly one** set (symmetric difference).

**Solution**
```python
a = {'Asthma', 'Diabetes', 'COPD'}
b = {'Diabetes', 'Allergy', 'Flu'}

exactly_one = a.symmetric_difference(b)  # same as (a - b) | (b - a)
print(exactly_one)
```
**Output** *(order may vary)*:
```
{'Flu', 'COPD', 'Allergy', 'Asthma'}
```

---

## 4) Dictionaries

**What:** key → value store (a mapping).  
**Create:** curly braces with `key: value` pairs `{...}`.

**Keys** must be hashable (e.g., strings, numbers, tuples); **values** can be anything.

### Common dict methods
- **`dict[key]`**: get the value (errors if key absent).
- **`get(key, default=None)`**: get value, or `default` if missing (no error).
- **`keys()` / `values()` / `items()`**: views for keys, values, or (key, value) pairs.
- **`update({...})`**: merge another dict.
- **`pop(key[, default])`**: remove key and return value.

### Example — Patient Information
```python
patient_info = {
    1: {'Name': 'John Doe',  'Diagnosis': 'Diabetes'},
    2: {'Name': 'Jane Smith','Diagnosis': 'Hypertension'},
    3: {'Name': 'Alice Johnson', 'Diagnosis': 'Asthma'}
}

# Loop with .items() to get (key, value)
for patient_id, info in patient_info.items():
    print(f"Patient ID: {patient_id}, Name: {info['Name']}, Diagnosis: {info['Diagnosis']}")

# Lookup safely with .get()
pid_to_find = 2
dx = patient_info.get(pid_to_find, {}).get('Diagnosis', 'Not found')
print('Diagnosis for ID 2:', dx)
```
**Output**
```
Patient ID: 1, Name: John Doe, Diagnosis: Diabetes
Patient ID: 2, Name: Jane Smith, Diagnosis: Hypertension
Patient ID: 3, Name: Alice Johnson, Diagnosis: Asthma
Diagnosis for ID 2: Hypertension
```

### Exercise (with solution)
**Task:** Add a new patient with ID 4, update ID 3’s diagnosis to “Recovered”, and print the names sorted by patient ID.

**Solution**
```python
patient_info = {
    1: {'Name': 'John Doe',  'Diagnosis': 'Diabetes'},
    2: {'Name': 'Jane Smith','Diagnosis': 'Hypertension'},
    3: {'Name': 'Alice Johnson', 'Diagnosis': 'Asthma'}
}

# Add ID 4
patient_info[4] = {'Name': 'Bob Brown', 'Diagnosis': 'COPD'}

# Update ID 3
patient_info[3]['Diagnosis'] = 'Recovered'

# Print in order of ID (sorted() returns a sorted list of keys)
for pid in sorted(patient_info.keys()):
    print(pid, '-', patient_info[pid]['Name'], '-', patient_info[pid]['Diagnosis'])
```
**Output**
```
1 - John Doe - Diabetes
2 - Jane Smith - Hypertension
3 - Alice Johnson - Recovered
4 - Bob Brown - COPD
```

---

## Helpful Patterns & Extras

### Looping: items vs. indexes
If you only need **values**, loop directly:
```python
for name in ['John', 'Jane', 'Alice']:
    print(name)
```
**Output**
```
John
Jane
Alice
```

If you also need the **index and value**, use **`enumerate()`**:
```python
for i, name in enumerate(['John', 'Jane', 'Alice'], start=1):
    print(i, name)
```
**Output**
```
1 John
2 Jane
3 Alice
```
> `enumerate(iterable, start=1)` returns `(index, item)` pairs; cleaner than `range(len(...))`.

### Removing duplicates quickly
```python
names = ['John', 'John', 'Alice', 'Jane', 'Alice']
unique_names = list(set(names))  # convert set back to list if you need a list
print(sorted(unique_names))
```
**Output**
```
['Alice', 'Jane', 'John']
```

---

## Common Pitfalls & Best Practices

**Pitfalls**
1) **Mutable vs immutable**  
   - Lists and dicts **changeable**, tuples **not changeable**.  
   - Copy carefully: `b = a` points to the **same** list. Use `a.copy()` for a shallow copy.

2) **KeyError with dicts**  
   - `d['missing']` raises `KeyError`. Prefer `d.get('missing', default)` when unsure.

3) **Set order**  
   - Sets are unordered; don’t rely on element positions. Use `sorted(set_obj)` to view in order.

4) **List index errors**  
   - `my_list[5]` when there are only 3 items → `IndexError`. Check `len()`.

**Best Practices**
- Use **lists** for ordered, changeable sequences.
- Use **tuples** for fixed records and as dict keys when needed.
- Use **sets** for uniqueness and set math (fast membership tests).
- Use **dicts** for fast key→value lookups and structured records.

---

## Quick Reference

- **List**: `[]` — ordered, mutable, duplicates allowed. Methods: `append`, `remove`, `pop`, `sort`, `reverse`.
- **Tuple**: `()` — ordered, immutable, duplicates allowed. Use for fixed data.
- **Set**: `{}` — unordered, **unique** elements. Operations: `|`, `&`, `-`, `^`.
- **Dict**: `{key: value}` — mapping. Methods: `get`, `keys`, `values`, `items`, `update`, `pop`.

---

### One-line takeaway
Choose the **right structure** for your task: list (ordered & editable), tuple (fixed), set (unique), dictionary (key→value). Use `len()`, `range()`, and methods like `append()`, `items()` to work with them efficiently.
