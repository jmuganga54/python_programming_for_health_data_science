<img src="./intro_images/logo_excercises.png" width="100%" align="left" />
<table style="float:right;">
    <tr>
        <td>                      
            <div style="text-align: right">Dr Ali Sarrami Foroushani</div>
            <div style="text-align: right">Lecturer in Cardiovascular Biomechanics</div>
            <div style="text-align: right">School of Health Sciences</div>
            <div style="text-align: right">University of Manchester</div>
         </td>
     </tr>
</table>

# Python Week One - Excercises

This notebook contains some exercises to evaluate your knowledge in Python, including variables, operators, iteration, data structures, functions, testing, NumPy, vectorised computation, and pandas. Each problem is followed by a code cell for you to write your solution.

## Problem 1: Variables and Data Structures

Define the following variables and use them in expressions:
1. An integer variable `age` with a value of 45.
2. A floating-point variable `height` with a value of 1.75.
3. A string variable `name` with the value `'John Doe'`.
4. A list `symptoms` containing the strings `['fever', 'cough', 'headache']`.
5. A dictionary `patient_info` with keys `'ID'`, `'Name'`, and `'BMI'`, and corresponding values of 1, `'John Doe'`, and 23.5.

Print the types and values of these variables. Create a new key `'age'` in the dictionary and update its value.

Write your code below.
```python
# Define variables
age = 45
height = 1.75
name = 'John Doe'
symptoms = ['fever', 'cough', 'headache']
patient_info = {'ID': 1, 'Name': 'John Doe', 'BMI': 23.5}

# Print types and values
print('Type of age:', type(age))
print('Value of age:', age)
print('Type of height:', type(height))
print('Value of height:', height)
print('Type of name:', type(name))
print('Value of name:', name)
print('Type of symptoms:', type(symptoms))
print('Value of symptoms:', symptoms)
print('Type of patient_info:', type(patient_info))
print('Value of patient_info:', patient_info)

# Update dictionary
patient_info['age'] = 45
print('Updated patient_info:', patient_info)
```
## Problem 2: Operators in Python

Calculate the following formula related to a patient's risk score:

$$\text{Risk Score} = \frac{(A + B) \times (C - D) + E}{F \times (G + H)} - I$$

Where:

- $A = 120$ (Blood Pressure)
- $B = 30$ (Cholesterol Level)
- $C = 70$ (Heart Rate)
- $D = 20$ (Exercise Minutes per Week)
- $E = 5$ (Medication Score)
- $F = 2$ (Diabetes Score)
- $G = 1$ (Smoker Status: 1 if smoker, 0 otherwise)
- $H = 10$ (Alcohol Consumption Score)
- $I = 25$ (Base Risk)

Substitute the parameters and compute the final risk score.

Write your code below.
```python
# Solution for Problem 2
A = 120
B = 30
C = 70
D = 20
E = 5
F = 2
G = 1
H = 10
I = 25

risk_score = ((A + B) * (C - D) + E) / (F * (G + H)) - I
print("Risk Score:", risk_score)
```
## Problem 3: Iteration in Python

You are given the following patient data (age and glucose level):

| Age | Glucose Level (mg/dL) |
|-----|-----------------------|
| 65  | 110                   |
| 45  | 90                    |
| 72  | 150                   |
| 51  | 105                   |
| 40  | 85                    |

Perform the following tasks:
- Iterate through the list to calculate the average glucose level for patients over the age of 50.
- Create a new list containing only the glucose levels of those patients.
- Identify and print the glucose levels of patients with glucose levels higher than a specified threshold (e.g., 100 mg/dL).

Write your code below.
```python
# Solution for Problem 3
patient_data = [(65, 110), (45, 90), (72, 150), (51, 105), (40, 85)] # (age, glucose level)

# Extract glucose levels for patients over 50
over_50_glucose = [glucose for age, glucose in patient_data if age > 50]

# Calculate the average glucose level
average_glucose = sum(over_50_glucose) / len(over_50_glucose)
print("Average glucose level for patients over 50:", average_glucose)

# Glucose levels over 100
high_glucose = [glucose for age, glucose in patient_data if glucose > 100]
print("Glucose levels over 100:", high_glucose)
```
## Problem 4: Iteration in Python

Given a list of blood glucose levels for different patients, find the number of patients with glucose levels above a certain threshold. The threshold is 90 mg/dL.

Use the following data:
- `[85, 90, 78, 92, 88, 75, 85, 95, 89, 84]`

Write a loop to count how many glucose levels exceed this threshold.

Write your code below.
```python
# Solution for Problem 4
# Blood glucose levels
glucose_levels = [85, 90, 78, 92, 88, 75, 85, 95, 89, 84]

# Threshold
threshold = 90

# Count patients with glucose levels above threshold
count = 0
for level in glucose_levels:
    if level > threshold:
        count += 1
print('Number of patients with glucose levels above the threshold:', count)
```
## Problem 5: Data Structures in Python

Create a list of dictionaries where each dictionary contains patient information. Perform the following operations:

1. Add a new patient record.
2. Remove a patient record based on the patient ID.
3. Update the BMI of an existing patient based on the patient ID.

Use the following initial data:
```python
[{'ID': 1, 'Name': 'Alice', 'BMI': 22.4},
 {'ID': 2, 'Name': 'Bob', 'BMI': 27.1},
 {'ID': 3, 'Name': 'Charlie', 'BMI': 24.0}]
```
Write your code below.
```python
# Solution for Problem 5
# Initial data
patients = [{'ID': 1, 'Name': 'Alice', 'BMI': 22.4},
            {'ID': 2, 'Name': 'Bob', 'BMI': 27.1},
            {'ID': 3, 'Name': 'Charlie', 'BMI': 24.0}]

# Add a new patient
new_patient = {'ID': 4, 'Name': 'David', 'BMI': 26.5}
patients.append(new_patient)

# Remove a patient
patients = [p for p in patients if p['ID'] != 2]

# Update BMI
for p in patients:
    if p['ID'] == 3:
        p['BMI'] = 25.0

print('Updated patient records:', patients)
```
## Problem 6: Functions in Python

Define a function `calculate_bmi(weight, height)` that calculates the Body Mass Index (BMI) given a patient's weight (in kilograms) and height (in meters). The formula for BMI is:

$$\text{BMI} = \frac{\text{weight}}{\text{height}^2}$$

Additionally, write a function `categorize_bmi(bmi)` that categorizes the BMI value into:
- Underweight: BMI < 18.5
- Normal weight: 18.5 <= BMI < 24.9
- Overweight: 25 <= BMI < 29.9
- Obese: BMI >= 30

Write your code below.
```python
# Solution for Problem 6
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

# Example usage
weight = 70
height = 1.75
bmi = calculate_bmi(weight, height)
category = categorize_bmi(bmi)
print(f"BMI: {bmi:.2f}, Category: {category}")
```
## Problem 7: Testing and Error Handling in Python

Write a function `safe_divide(numerator, denominator)` that safely divides two numbers and handles division by zero errors. The function should return `None` if the denominator is zero and print an error message.

Test this function with the following pairs:
- numerator = 10, denominator = 2
- numerator = 10, denominator = 0

Write your code below.
```python
# Solution for Problem 7
# Function to safely divide two numbers
def safe_divide(numerator, denominator):
    try:
        result = numerator / denominator
    except ZeroDivisionError:
        print('Error: Division by zero is not allowed.')
        return None
    return result

# Test cases
print('Result 1:', safe_divide(10, 2))
print('Result 2:', safe_divide(10, 0))
```
## Problem 8: Testing and Handling Errors in Python

Write a function `divide_numbers(a, b)` that takes two numbers `a` and `b` and returns the result of dividing `a` by `b`. Handle the following scenarios using exceptions:
- If `b` is zero, raise an error and return a message saying division by zero is not allowed.
- If either `a` or `b` is not a number, raise an error and return a message saying inputs must be numbers.

Write your code below.
```python
# Solution for Problem 8
def divide_numbers(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."
    except TypeError:
        return "Error: Inputs must be numbers."

# Example usage
result1 = divide_numbers(10, 2)
result2 = divide_numbers(10, 0)
result3 = divide_numbers(10, "five")

print(result1)
print(result2)
print(result3)
```
