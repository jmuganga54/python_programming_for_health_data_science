# Python Visualisation — Part I (Beginner Version)

This guide shows how to plot using **plain Python data** (lists, dictionaries) and **Matplotlib**.

## 0) Setup
```python
import matplotlib.pyplot as plt
plt.rcParams.update({'figure.dpi': 120, 'font.size': 12})
```

## 1) Tiny datasets
```python
months = ["Jan","Feb","Mar","Apr","May","Jun"]
avg_temps_c = [5,6,9,12,16,19]
snack_counts = {"Apples":12, "Bananas":7, "Carrots":5, "Dates":3}
study_hours = [1,2,2,3,4,4,5,6]
test_scores = [50,55,58,65,70,72,80,88]
heights_cm = [150,152,153,155,156,158,160,162,163,165,168,170,172,175,178]
time_budget = {"Sleep":8,"Study":3,"Exercise":1,"Leisure":4,"Other":8}
```

## 2) Line plot
```python
plt.plot(months, avg_temps_c, marker='o')
plt.title("Average Temperature by Month")
plt.xlabel("Month"); plt.ylabel("Temperature (°C)")
plt.grid(True); plt.show()
```

## 3) Bar chart
```python
items = list(snack_counts.keys()); counts = list(snack_counts.values())
plt.bar(items, counts)
plt.title("Snack Counts"); plt.xlabel("Snack"); plt.ylabel("Count")
plt.xticks(rotation=15); plt.show()
```

## 4) Scatter plot
```python
plt.scatter(study_hours, test_scores)
plt.title("Study Hours vs Test Score")
plt.xlabel("Study Hours"); plt.ylabel("Test Score")
plt.grid(True); plt.show()
```

## 5) Histogram
```python
plt.hist(heights_cm, bins=5)
plt.title("Height Distribution"); plt.xlabel("Height (cm)"); plt.ylabel("Count")
plt.grid(True); plt.show()
```

## 6) Pie chart
```python
labels = list(time_budget.keys()); hours = list(time_budget.values())
plt.pie(hours, labels=labels, autopct='%1.0f%%', startangle=90)
plt.title("Daily Time Budget"); plt.axis('equal'); plt.show()
```

## 7) Subplots
```python
fig, axes = plt.subplots(1, 2, figsize=(9, 3.5))
axes[0].plot(months, avg_temps_c, marker='o')
axes[0].set_title("Avg Temp by Month"); axes[0].grid(True)
items = list(snack_counts.keys()); counts = list(snack_counts.values())
axes[1].bar(items, counts); axes[1].set_title("Snack Counts")
for t in axes[1].get_xticklabels(): t.set_rotation(15)
plt.tight_layout(); plt.show()
```

## 8) Save a figure
```python
plt.plot(months, avg_temps_c, marker='o')
plt.title("Average Temperature by Month (Saved)")
plt.xlabel("Month"); plt.ylabel("°C"); plt.grid(True)
plt.savefig("avg_temp_by_month.png", dpi=300); plt.show()
```
