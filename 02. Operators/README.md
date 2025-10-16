## Topic

This section we will learn about;

- [1) What is a variable?](#1-what-is-a-variable)
- [2) Create and assign](#2-create-and-assign)
- [3) Naming rules & conventions](#3-naming-rules--conventions)
- [4) Scalar data types you will use](#4-scalar-data-types-you-will-use)
- [5) Dynamic typing (types can change)](#5-dynamic-typing-types-can-change)
- [6) Strings 101](#6-strings-101)
- [7) Converting between strings and numbers](#7-converting-between-strings-and-numbers)
- [8) Encoding and decoding (for names with accents)](#8-encoding-and-decoding-for-names-with-accents)
- [9) Regular expressions (quick pattern find)](#9-regular-expressions-quick-pattern-find)
- [10) String formatting (3 main ways)](#10-string-formatting-3-main-ways)
- [11) Mini real-world report](#11-mini-real-world-report)
- [12) Common pitfalls to avoid](#12-common-pitfalls-to-avoid)

## Keywords and Notes

### Single-Value Variables and Strings

<a id="1-what-is-a-variable"></a>
1) What is a variable?

A `variable` is a name (label) that stores a value. Python figures out the type for you (this is called `dynamic typing`).

```
patient_age = 45          # int
patient_name = "Alice"    # str
bmi = 24.5                # float
has_diabetes = False      # bool

print(patient_age, patient_name, bmi, has_diabetes)
```
Output:
```
45 Alice 24.5 False

```

<a id="2-create-and-assign"></a>
2) Create and assign

Use `=` to store a value in a name. Left is the name, right is the value.

```
x = 1
print(x)

```
Output:
```
1
```

<a id="3-naming-rules--conventions"></a>
3) Naming rules & conventions

* Start with a letter or `_`, then letters, numbers, `_`
* Case sensitive (`age ≠ Age`)
* Do not use Python keywords as names.
* Prefer clear names like `systolic_bp`, not `sbp`
```
patient_id = "P12345"
MAX_BMI_THRESHOLD = 30
print(patient_id, MAX_BMI_THRESHOLD)

```

Output:
```
P12345 30

```

To see reserved words:

```
help('keywords')

```
(Outputs a list like `['False', 'None', 'True', 'and', ...]`)

<a id="4-scalar-data-types-you-will-use"></a>
4) Scalar data types you will use

* `int`: whole numbers
* `float`: decimals
* `bool`: True or False
* `str`: text

```
num_patients = 250      # int
cholesterol = 185.5     # float
is_smoker = True        # bool
diagnosis = "HTN"       # str

print(type(num_patients), type(cholesterol), type(is_smoker), type(diagnosis))

```
Output (types may vary in format):

```
<class 'int'> <class 'float'> <class 'bool'> <class 'str'>

```
<a id="5-dynamic-typing-types-can-change"></a>
5) Dynamic typing (types can change)

```
bp_reading = "120"          # starts as string
bp_reading = int(bp_reading)  # now int
print(bp_reading, type(bp_reading))

```
Output:

```
120 <class 'int'>

```
<a id="6-strings-101"></a>
6) Strings 101

Strings are text in quotes. Useful tools:

**Length**
```
s = "This is a text string."
print(len(s))

```
Output:
```
22

```
**Indexing & slicing**

(Index starts at 0)

```

s = "This is a text string."
print(s[2])       # third character
print(s[0:4])     # 'This'
print(s[-1])      # last character
print(s[3:-5])    # slice middle

```
Output:
```
i
This
.
s a text str

```

**Concatenation**

```
first = "John"; last = "Doe"
full = first + " " + last
print(full)

```
Output:

```
John Doe

```

**Change case**

```
note = "patient requires IMMEDIATE attention"
print(note.lower())
print(note.upper())

```
Output:

```
patient requires immediate attention
PATIENT REQUIRES IMMEDIATE ATTENTION

```

**Membership (`in`, `not in`)**

```
pc = "86 year old female with central chest pain"
print("chest" in pc)
print("kidney pain" not in pc)

```
Output:

```
True
True
```
**Split and join**

```
record = "Alice Smith, 50, Hypertension"
parts = record.split(", ")
print(parts)

address_parts = ["123 Main St", "Apt 4B", "Springfield", "IL"]
address = ", ".join(address_parts)
print(address)

```
Output:

```
['Alice Smith', '50', 'Hypertension']
123 Main St, Apt 4B, Springfield, IL

```

**Escape characters**
```
print("This is \t a tab")
print("This is a \n newline")

```
Output:

```
This is 	 a tab
This is a 
 newline

```

**Multiline strings**

```
medical_note = """
Patient: John Doe
Age: 45
Diagnosis: Hypertension
"""
print(medical_note)

```
Output:
```

Patient: John Doe
Age: 45
Diagnosis: Hypertension


```
<a id="7-converting-between-strings-and-numbers"></a>
7) Converting between strings and numbers

```
# str -> int / float
age = int("45")
bmi = float("24.5")
print(age, type(age))
print(bmi, type(bmi))

```

Output:

```
45 <class 'int'>
24.5 <class 'float'>

```
```
# int / float -> str
count_str = str(120)
bmi_str = str(23.7)
print(count_str, type(count_str))
print(bmi_str, type(bmi_str))

```
Output

```
120 <class 'str'>
23.7 <class 'str'>

```

**Common mistake example**
```
x = "123"
# x + 4   # ❌ TypeError
print(x + str(4))     # "1234"
print(int(x) + 4)     # 127
```
Output
```
1234
127

```

**Safe conversion with error handling**

```
def safe_to_int(s):
    try:
        return int(s)
    except ValueError:
        return None

print(safe_to_int("42"))
print(safe_to_int("forty-two"))

```
Output:

```
42
None

```
<a id="8-encoding-and-decoding-for-names-with-accents"></a>
8) Encoding and decoding (for names with accents)

```
patient = "Dr. Sławomir Bąk - Cardiologist"
encoded = patient.encode("utf-8")
decoded = encoded.decode("utf-8")
print(encoded)
print(decoded)

```
Output (first line shows bytes, will vary):

```
b'Dr. S\xc5\x82awomir B\xc4\x85k - Cardiologist'
Dr. Sławomir Bąk - Cardiologist

```
<a id="9-regular-expressions-quick-pattern-find"></a>
9) Regular expressions (quick pattern find)

```
import re
text = "Patient record: ID P123456, Age 45, Condition: HTN"
m = re.search(r"P\d{6}", text)
if m:
    print(m.group())

```
Output:
```
P123456

```
<a id="10-string-formatting-3-main-ways"></a>
10) String formatting (3 main ways)

a) Percent style (older)

```
name = "Claire"
print("Hi %s, nice to meet you" % name)

```

Output:
```
Hi Claire, nice to meet you

```

b) `str.format()`

```
patient_name, age, bmi = "John Doe", 45, 24.5
print("Patient: {}, Age: {}, BMI: {:.1f}".format(patient_name, age, bmi))

```

Output:

```
Patient: John Doe, Age: 45, BMI: 24.5

```

c) f-strings (recommended)

```
patient_name, age, bmi, has_dm = "Jane Smith", 34, 21.34, False
print(f"Patient: {patient_name}, Age: {age}, BMI: {bmi:.1f}, Diabetes: {has_dm}")

```

Output:

```
Patient: Jane Smith, Age: 34, BMI: 21.3, Diabetes: False

```

**Template strings (safe substitutions)**

```
from string import Template
tpl = Template("Patient: $name, Age: $age, BMI: $bmi")
print(tpl.substitute(name="Bob Brown", age=50, bmi=26.4))

```

Output:

```
Patient: Bob Brown, Age: 50, BMI: 26.4

```
<a id="11-mini-real-world-report"></a>
11) Mini real-world report

```
patient = {
    "name": "Chris Wilson",
    "age": 41,
    "height": 1.75,
    "weight": 80
}
bmi = patient["weight"] / (patient["height"] ** 2)

report = f"""
Patient Report
--------------
Name: {patient['name']}
Age: {patient['age']}
Height: {patient['height']} m
Weight: {patient['weight']} kg
BMI: {bmi:.2f}
"""
print(report)


```

Output:

```
Patient Report
--------------
Name: Chris Wilson
Age: 41
Height: 1.75 m
Weight: 80 kg
BMI: 26.12

```
<a id="12-common-pitfalls-to-avoid"></a>
12) Common pitfalls to avoid

* Do not shadow built-ins: avoid `list = [...]` (use patient_list instead). 
* Mutable aliasing: two names pointing to the same list will both change
```
vital_stats = [120, 80]
patient_vitals = vital_stats
patient_vitals.append(98.6)
print(vital_stats)      # [120, 80, 98.6]

```
* Global mutations: changing globals inside functions can surprise you


