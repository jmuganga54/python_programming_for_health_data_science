# Matplotlib Basics (Beginner Guide)

This guide gives you the **must-know** pieces to start plotting with Matplotlib.  
For each concept you get: a short explanation, a **code snippet**, notes on the **functions used**, and a small **Try it** task.

> Install (if needed): `pip install matplotlib`

```python
import matplotlib.pyplot as plt
import numpy as np
```

---

## 0) Two ways to use Matplotlib (Pyplot vs. OO)

### Pyplot (quick & simple)
```python
import matplotlib.pyplot as plt

plt.plot([1, 2, 3], [2, 4, 3])      # line
plt.title("Quick Line")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)
plt.show()
```
**What functions do:**
- `plt.plot(x, y)`: draw a line.
- `plt.title/plt.xlabel/plt.ylabel`: add text.
- `plt.grid(True)`: show grid.
- `plt.show()`: render the figure.

### Object-Oriented (clean & scalable)
```python
fig, ax = plt.subplots()            # fig: whole canvas, ax: one plot area
ax.plot([1, 2, 3], [2, 4, 3])
ax.set_title("OO Line")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.grid(True)
plt.show()
```
**Key idea:** You work with a **Figure** and one or more **Axes**. You call plotting/styling methods on `ax`.

**Try it:** Make a line of `x=[0,1,2,3]`, `y=[0,1,4,9]` with title **"Squares"** using the OO style.

---

## 1) Line plots — trends over an ordered x-axis
Use for time, steps, months, etc.

```python
x = [1,2,3,4]
y = [2,3,5,8]
plt.plot(x, y, marker='o', linestyle='-', linewidth=2)
plt.title("Line with Markers")
plt.xlabel("Step")
plt.ylabel("Value")
plt.grid(True)
plt.show()
```
**Common args:**
- `marker='o'|'s'|'+'`, `linestyle='-'|'--'|':'`, `linewidth=2`

**Try it:** Plot days `["Mon","Tue","Wed","Thu","Fri"]` vs steps `[3000,4200,3800,5000,6100]` with circle markers and a grid.

---

## 2) Scatter plots — relationship between two numbers
```python
x = [1,2,3,4,5]
y = [1.2,1.9,3.1,3.9,5.2]
plt.scatter(x, y, s=60, alpha=0.9)   # s = marker size, alpha = transparency
plt.title("Scatter")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)
plt.show()
```
**Function:** `plt.scatter(x, y, s=..., alpha=...)`

**Try it:** `study_hours=[1,2,2,3,4,5]` vs `scores=[50,55,58,65,72,80]` as a scatter plot.

---

## 3) Bar charts — compare categories
```python
items  = ["A","B","C"]
counts = [5,  8,  3]
plt.bar(items, counts)
plt.title("Bar Chart")
plt.xlabel("Item")
plt.ylabel("Count")
plt.show()
```

### Horizontal bars
```python
plt.barh(items, counts)
plt.title("Horizontal Bars")
plt.xlabel("Count")
plt.ylabel("Item")
plt.show()
```
**Functions:** `plt.bar(x, height)`, `plt.barh(y, width)`.

**Try it:** Show snack counts for `{"Apples":12, "Bananas":7, "Carrots":5}` as vertical, then horizontal bars.

---

## 4) Histograms — distributions
```python
data = [50,52,55,58,60,61,63,65,68,70,72,75,78,80]
plt.hist(data, bins=5)   # try 5, 8, 10
plt.title("Histogram")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.grid(True)
plt.show()
```
**Function:** `plt.hist(values, bins=n)` groups values into bins.

**Try it:** Make ~12 heights and draw with `bins=4` and `bins=8`; compare shapes.

---

## 5) Box plots — spread & outliers
```python
group_a = [52,55,57,60,62,63,65]
group_b = [48,50,51,53,54,55]
plt.boxplot([group_a, group_b], labels=["A","B"])
plt.title("Boxplot A vs B")
plt.ylabel("Score")
plt.show()
```
**Function:** `plt.boxplot(list_of_arrays, labels=...)`

**Try it:** Create **three** groups and compare all three in one boxplot.

---

## 6) Pie charts — parts of a whole (use sparingly)
```python
labels = ["Sleep","Work","Study","Leisure"]
hours  = [8, 8, 3, 5]
plt.pie(hours, labels=labels, autopct="%1.0f%%", startangle=90)
plt.title("Daily Time")
plt.axis("equal")   # make it a circle
plt.show()
```
**Function:** `plt.pie(sizes, labels=..., autopct=...)`

**Try it:** Weekly time budget with 4–6 categories.

---

## 7) Titles, labels, limits, ticks, legends
```python
x = [1,2,3,4]
y1 = [1,4,9,16]
y2 = [1,3,5,7]

plt.plot(x, y1, marker='o', label="Squares")
plt.plot(x, y2, marker='s', label="Odds")

plt.title("Two Lines")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()             # uses label=...
plt.xlim(0, 5)           # axis limits
plt.ylim(0, 17)
plt.xticks([1,2,3,4])    # custom ticks
plt.grid(True)
plt.show()
```
**Functions:** `plt.legend()`, `plt.xlim/ylim`, `plt.xticks/yticks(seq, labels=...)`

**Try it:** Add custom tick labels for months `["Jan","Feb","Mar","Apr"]`.

---

## 8) Subplots — multiple charts in one figure
```python
fig, axes = plt.subplots(1, 2, figsize=(10, 4))  # 1 row, 2 columns

axes[0].plot([1,2,3], [2,4,3])
axes[0].set_title("Left")

axes[1].bar(["A","B","C"], [5,2,7])
axes[1].set_title("Right")

plt.tight_layout()
plt.show()
```
**Function:** `plt.subplots(rows, cols, figsize=(w,h))` returns a grid of axes.

**Try it:** Make a 2×2 grid: line, scatter, hist, and bar.

---

## 9) Styles & rcParams — quick look changes
```python
print(plt.style.available)  # list styles
plt.style.use("ggplot")

plt.plot([1,2,3,4], [1,4,2,5], marker='o')
plt.title("Styled Plot (ggplot)")
plt.show()

plt.style.use("default")    # back to default
```
Or tweak defaults globally:
```python
plt.rcParams.update({"figure.dpi": 120, "font.size": 12})
```

**Try it:** List styles, pick one, plot a bar chart with it.

---

## 10) Annotations — callouts & arrows
```python
x = [1,2,3,4,5]
y = [1,4,2,6,3]
fig, ax = plt.subplots()
ax.plot(x, y, marker='o')
ax.annotate("Peak here", xy=(4,6), xytext=(2.5,6.5),
            arrowprops=dict(arrowstyle="->", linewidth=1.5))
ax.set_title("Annotation Demo")
plt.show()
```
**Function:** `ax.annotate(text, xy=(x,y), xytext=(xtext,ytext), arrowprops={...})`

**Try it:** Annotate the max point in your scatter/line plot.

---

## 11) Twin axes — a second y-axis
```python
x = np.arange(1, 6)
temp_c = np.array([10,12,15,18,20])
rain_mm = np.array([5, 20, 10, 30, 15])

fig, ax1 = plt.subplots()
ax1.plot(x, temp_c, marker='o', label="Temp (°C)")
ax1.set_xlabel("Day")
ax1.set_ylabel("Temp (°C)")

ax2 = ax1.twinx()
ax2.bar(x, rain_mm, alpha=0.3, label="Rain (mm)")
ax2.set_ylabel("Rain (mm)")

fig.suptitle("Twin Axes Demo")
fig.tight_layout()
plt.show()
```
**Function:** `ax.twinx()` shares x-axis but gives you a second y-axis.

**Try it:** Plot steps as a line + calories as bars.

---

## 12) Dates on the x-axis
```python
import datetime as dt

dates = [dt.date(2025, 11, d) for d in [1,2,3,4,5]]
values = [3,4,2,5,6]

fig, ax = plt.subplots()
ax.plot(dates, values, marker='o')
ax.set_title("Dates on X-axis")
fig.autofmt_xdate()   # pretty rotate
plt.show()
```
**Try it:** Make 7 days starting today and plot a simple metric.

---

## 13) Images / heatmaps (quick view)
```python
img = np.random.rand(10, 10)   # pretend grayscale image
plt.imshow(img, cmap="viridis")  # choose a colormap
plt.colorbar(label="Intensity")
plt.title("Image Demo")
plt.show()
```
**Functions:** `plt.imshow(array, cmap=...)`, `plt.colorbar()`

**Try it:** Create a 20×20 random array and show with `"magma"`.

---

## 14) Save your figure
Save **before** `plt.show()` (or use `fig.savefig`).

```python
fig, ax = plt.subplots()
ax.plot([1,2,3], [1,4,9], marker='o')
ax.set_title("Saved Figure")
fig.savefig("saved_figure.png", dpi=300, bbox_inches="tight")
plt.show()
```
**Function:** `savefig(path, dpi=..., bbox_inches="tight")`

**Try it:** Save any plot as `"my_plot.png"` at 300 dpi.

---

## Mini Practice (everything together)
Create a 2×2 figure:
1) Line plot of months vs temperatures with markers.  
2) Bar chart of snack counts (rotate x-tick labels).  
3) Histogram of 15 weights (bins=5).  
4) Scatter of study hours vs score with a grid and an annotation at the highest score.  
Add titles to each subplot and finish with `plt.tight_layout()`.

---

### Cheat Sheet (common functions)
- **Creating**: `plt.plot`, `plt.scatter`, `plt.bar`, `plt.barh`, `plt.hist`, `plt.boxplot`, `plt.pie`, `plt.imshow`
- **Layout**: `plt.subplots`, `plt.tight_layout`
- **Labels**: `set_title`, `set_xlabel`, `set_ylabel`, `plt.title`, `plt.xlabel`, `plt.ylabel`
- **Scales & ticks**: `plt.xlim`, `plt.ylim`, `plt.xticks`, `plt.yticks`
- **Styling**: `plt.style.use`, `plt.rcParams.update`, `plt.grid`
- **Legends**: `plt.legend()` (use `label=` when plotting)
- **Save**: `plt.savefig("name.png", dpi=300)`

Happy plotting! 🎉
