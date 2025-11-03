# Python Visualisation — Part I (Beginner Version)

This lesson teaches you to make charts with:
- **Plain Python data** (lists and dictionaries)
- **Matplotlib** (the standard plotting library)

You will learn:
1) How to store small datasets  
2) How to make **line**, **bar**, **scatter**, **histogram**, **pie** charts  
3) How to add **titles**, **axis labels**, **ticks**, **legends**, **grids**  
4) How to make **subplots** (many charts in one figure)  
5) How to **save** a figure as an image

I also include **Your Turn** mini-exercises with short solutions.

---

## 0) Setup

### What we import and why
- `matplotlib.pyplot as plt` — the plotting functions live here.

```python
# (In Jupyter you can also use: %matplotlib inline)
import matplotlib.pyplot as plt

# Optional: make plots a bit clearer
plt.rcParams.update({
    'figure.dpi': 120,  # pixels per inch (sharpness)
    'font.size': 12     # base font size
})
```

---

## 1) Tiny datasets in Python

Two simple ways to hold data:

- **List**: ordered values, e.g. `["Jan", "Feb"]`
- **Dictionary**: key → value pairs, e.g. `{"Alice": 82}`

We will reuse these:

```python
months        = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
avg_temps_c   = [5, 6, 9, 12, 16, 19]                # y-values per month (x)

snack_counts  = {"Apples": 12, "Bananas": 7, "Carrots": 5, "Dates": 3}

study_hours   = [1, 2, 2, 3, 4, 4, 5, 6]
test_scores   = [50, 55, 58, 65, 70, 72, 80, 88]

heights_cm    = [150, 152, 153, 155, 156, 158, 160, 162,
                 163, 165, 168, 170, 172, 175, 178]

time_budget   = {"Sleep": 8, "Study": 3, "Exercise": 1, "Leisure": 4, "Other": 8}
```

---

## 2) Line plot

**When to use**: show change across an ordered x-axis (months, days, time).

### Functions you will use
- `plt.plot(x, y, marker='o')` — draw a line (optionally add point markers)
- `plt.title("...")` — add a title
- `plt.xlabel("...")`, `plt.ylabel("...")` — label axes
- `plt.grid(True)` — draw a grid
- `plt.show()` — display the figure

```python
plt.plot(months, avg_temps_c, marker='o')
plt.title("Average Temperature by Month")
plt.xlabel("Month")
plt.ylabel("Temperature (°C)")
plt.grid(True)
plt.show()
```

**What you should see**: A line that goes up from Jan to Jun with round dots on each month.

### ✅ Your Turn 1
Make your own mini time series.

**Question**: Plot steps walked per day for Mon–Fri.

```python
# Your code here
```

**Solution**

```python
days  = ["Mon","Tue","Wed","Thu","Fri"]
steps = [3000, 4500, 4000, 5000, 6000]

plt.plot(days, steps, marker='o')
plt.title("Steps per Day")
plt.xlabel("Day")
plt.ylabel("Steps")
plt.grid(True)
plt.show()
```

---

## 3) Bar chart

**When to use**: compare categories (snack types, product types).

### Extra functions
- `plt.bar(labels, values)` — vertical bars
- `plt.barh(labels, values)` — horizontal bars
- `plt.xticks(rotation=15)` — rotate x labels for readability

```python
items  = list(snack_counts.keys())    # ['Apples','Bananas','Carrots','Dates']
counts = list(snack_counts.values())  # [12, 7, 5, 3]

plt.bar(items, counts)
plt.title("Snack Counts")
plt.xlabel("Snack")
plt.ylabel("Count")
plt.xticks(rotation=15)
plt.show()
```

**What you should see**: Bars for Apples (highest), Bananas, Carrots, Dates.

### ✅ Your Turn 2
**Question**: Make a **horizontal** bar chart for grade counts.

```python
# Your code here
```

**Solution**

```python
grades = {"A": 5, "B": 9, "C": 4, "D": 1}
labels = list(grades.keys())
values = list(grades.values())

plt.barh(labels, values)
plt.title("Grade Counts")
plt.xlabel("Count")
plt.ylabel("Grade")
plt.show()
```

---

## 4) Scatter plot

**When to use**: relationship between two numeric variables (x vs y).

```python
plt.scatter(study_hours, test_scores)
plt.title("Study Hours vs Test Score")
plt.xlabel("Study Hours")
plt.ylabel("Test Score")
plt.grid(True)
plt.show()
```

**What you should see**: Points that generally rise as hours increase.

### ✅ Your Turn 3
**Question**: Plot minutes of exercise vs heart rate.

```python
# Your code here
```

**Solution**

```python
exercise_min = [5, 10, 15, 20, 25, 30]
heart_rate   = [80, 90, 100, 110, 115, 120]

plt.scatter(exercise_min, heart_rate)
plt.title("Exercise vs Heart Rate")
plt.xlabel("Exercise (minutes)")
plt.ylabel("Heart Rate (bpm)")
plt.grid(True)
plt.show()
```

---

## 5) Histogram

**When to use**: see the **distribution** (how values spread across ranges).

### Function
- `plt.hist(data, bins=5)` — `bins` controls how many buckets

```python
plt.hist(heights_cm, bins=5)
plt.title("Height Distribution")
plt.xlabel("Height (cm)")
plt.ylabel("Count")
plt.grid(True)
plt.show()
```

**What you should see**: Bars showing how many people fall into each height range.

### ✅ Your Turn 4
**Question**: Create list `weights_kg` and try different `bins`.

```python
# Your code here
```

**Solution**

```python
weights_kg = [50, 52, 55, 58, 60, 61, 63, 65, 68,
              70, 72, 73, 75, 78, 80]
plt.hist(weights_kg, bins=6)
plt.title("Weight Distribution")
plt.xlabel("Weight (kg)")
plt.ylabel("Count")
plt.grid(True)
plt.show()
```

---

## 6) Pie chart

**When to use**: show parts of a whole (few categories only).

### Extra arguments
- `labels=...` — labels for slices
- `autopct='%1.0f%%'` — show percentages on slices
- `startangle=90` — rotate so first slice starts at the top
- `plt.axis('equal')` — make the pie a circle (not oval)

```python
labels = list(time_budget.keys())
hours  = list(time_budget.values())

plt.pie(hours, labels=labels, autopct='%1.0f%%', startangle=90)
plt.title("Daily Time Budget")
plt.axis('equal')  # circle
plt.show()
```

### ✅ Your Turn 5
**Question**: Weekly time budget pie chart with 3–6 categories.

```python
# Your code here
```

**Solution**

```python
labels = ["Study", "Work", "Family", "Leisure", "Sleep"]
hours  = [15, 20, 25, 10, 28]

plt.pie(hours, labels=labels, autopct='%1.0f%%', startangle=90)
plt.title("Weekly Time Budget")
plt.axis('equal')
plt.show()
```

---

## 7) Subplots (many charts in one figure)

**When to use**: compare charts side-by-side or in a grid.

### New function
- `fig, axes = plt.subplots(rows, cols, figsize=(w, h))`  
  - `axes` is an array of “small canvases”
  - On each `axes[i]`, call plotting methods like `axes[i].plot(...)`
- `plt.tight_layout()` — fix spacing

```python
fig, axes = plt.subplots(1, 2, figsize=(9, 3.5))

# Left: line
axes[0].plot(months, avg_temps_c, marker='o')
axes[0].set_title("Avg Temp by Month")
axes[0].set_xlabel("Month")
axes[0].set_ylabel("°C")
axes[0].grid(True)

# Right: bar
items  = list(snack_counts.keys())
counts = list(snack_counts.values())
axes[1].bar(items, counts)
axes[1].set_title("Snack Counts")
axes[1].set_xlabel("Snack")
axes[1].set_ylabel("Count")
for tick in axes[1].get_xticklabels():
    tick.set_rotation(15)

plt.tight_layout()
plt.show()
```

---

## 8) Quick styling tips

- **Markers**: `'o'` (circle), `'s'` (square), `'+'` (plus)
- **Grid**: `plt.grid(True)`
- **Axis limits**: `plt.xlim(min, max)`, `plt.ylim(min, max)`
- **Rotate ticks**: `plt.xticks(rotation=45)`
- **Legend**:
  - Add `label="..."` inside plot call(s)
  - Then call `plt.legend()`

```python
plt.plot(months, avg_temps_c, marker='o', label='Temperature')
plt.title("Styling Demo")
plt.xlabel("Month")
plt.ylabel("°C")
plt.ylim(0, 22)     # force y-axis range
plt.grid(True)
plt.legend()        # show legend for "Temperature"
plt.show()
```

---

## 9) Save a figure to a file

**Important**: call `plt.savefig(...)` **before** `plt.show()`.

```python
plt.plot(months, avg_temps_c, marker='o')
plt.title("Average Temperature by Month (Saved)")
plt.xlabel("Month")
plt.ylabel("°C")
plt.grid(True)

plt.savefig("avg_temp_by_month.png", dpi=300)  # saves to file
plt.show()
print("Saved file: avg_temp_by_month.png")
```

This creates a high-quality PNG in your current folder.

---

## Mini FAQ (quick reminders)

- **Why `plt.show()`?**  
  It tells Matplotlib to draw and display the figure.

- **Why rotate x labels?**  
  Long category names overlap; rotation keeps them readable.

- **What does `figsize=(w, h)` mean?**  
  Size of the whole figure in inches (width, height).

- **Why `plt.axis('equal')` for pie charts?**  
  Without it, the pie can look oval; this makes it a circle.

---

## Practice set (extra)

1) **Make two line plots** on the same axes (temperature vs rainfall). Add a legend.  
2) **Bar chart** of three products’ sales in **Q1–Q4** as grouped bars (hint: use index and offsets).  
3) **Scatter plot** with two series (e.g., two classes’ study hours vs scores) using different markers and a legend.  
4) **Histogram** of random ages; test `bins=5`, `bins=10`. Which shows more detail?  
5) **Save** one of your figures as `my_plot.png`.

---

## Wrap-up

You can now:
- Use lists and dictionaries to store tiny datasets
- Plot **line**, **bar**, **scatter**, **histogram**, **pie** charts
- Add **titles**, **labels**, **grids**, **legends**
- Use **subplots** to compare charts
- **Save** your figures to files

**Next steps**:
- Try the same plots with **NumPy** arrays and **pandas** DataFrames
- Add **data labels** to bars using `plt.text(x, y, value)`
- Explore the Matplotlib gallery for inspiration
