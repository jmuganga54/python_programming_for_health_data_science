
# Python Visualisation – Part II (Beginner Version, with Seaborn)

## 0) Setup (what you need every time)

**What it does:**  
- `seaborn` (sns) sits on top of Matplotlib and makes nice plots easily.  
- `sns.set_theme(...)` sets the default style.  
- `%matplotlib inline` (in notebooks) shows plots under the cell.  
- `plt.rcParams.update({...})` changes default figure/text sizes.

**Code**
```python
%matplotlib inline
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

sns.set_theme(context="notebook", style="whitegrid")
plt.rcParams.update({
    'figure.dpi': 120,   # sharper images
    'font.size': 12      # bigger text
})
```

---

## 1) Make tiny DataFrames from lists/dicts

**Why:** Seaborn works best with **DataFrames** (columns = variables).

**Code**
```python
# small student dataset
names   = ["Alice","Bob","Cara","Dan","Eli","Fay"]
gender  = ["F","M","F","M","M","F"]
math    = [62, 55, 78, 71, 66, 85]
bio     = [58, 60, 80, 68, 64, 88]
study_h = [2, 1, 3, 2, 2, 4]

df_students = pd.DataFrame({
    "name": names,
    "gender": gender,
    "math": math,
    "bio": bio,
    "study_hours": study_h
})

# category totals (snacks)
snack_counts = {"Apples": 12, "Bananas": 7, "Carrots": 5, "Dates": 3}
df_snacks = pd.DataFrame({
    "snack": list(snack_counts.keys()),
    "count": list(snack_counts.values())
})

# tiny time-like data
days  = ["Mon","Tue","Wed","Thu","Fri"]
steps = [3000, 4500, 4000, 5000, 6000]
df_daily = pd.DataFrame({"day": days, "steps": steps})

# single numeric column
heights_cm = [150, 152, 153, 155, 156, 158, 160, 162, 163, 165, 168, 170, 172, 175, 178]
df_heights = pd.DataFrame({"height_cm": heights_cm})
```

---

## 2) Countplot — **counts of a category**

**Use when:** You want to count how many rows fall in each category (class balance, frequencies).

**Function:**  
- `sns.countplot(data=..., x='col')`  
  - `data` = DataFrame  
  - `x` = categorical column  
  - `hue='other_cat'` → split bars by another category

**Example**
```python
ax = sns.countplot(data=df_students, x="gender")
ax.set_title("Count by Gender")
ax.set_xlabel("Gender")
ax.set_ylabel("Count")
plt.show()
```

**Exercise (Your turn):** If you had a DataFrame with a column `fruit` containing repeated fruit names, use `sns.countplot` to show counts per fruit.

**Solution (pattern)**
```python
# Example mini data
df_fruit = pd.DataFrame({"fruit": ["Apple","Banana","Apple","Banana","Apple","Dates"]})
sns.countplot(data=df_fruit, x="fruit")
plt.title("Fruit Counts")
plt.show()
```

> ✅ Tip: Our `df_snacks` already stores totals, not repeated rows. For that case, use **barplot** (next section).

---

## 3) Barplot — **average (or other stat) per group**

**Use when:** You want the **mean** (default) of a numeric variable by category. Good for showing average scores by group.

**Function:**  
- `sns.barplot(data=..., x='group', y='value', estimator=np.mean)`  
  - `estimator` can change (e.g., `np.median`)
  - `ci=None` to hide error bars

**Example**
```python
ax = sns.barplot(data=df_students, x="gender", y="math")  # mean math by gender
ax.set_title("Average Math Score by Gender")
plt.show()
```

**Exercise:** Plot average **biology** score by gender.

**Solution**
```python
ax = sns.barplot(data=df_students, x="gender", y="bio")
ax.set_title("Average Biology Score by Gender")
plt.show()
```

**Bar chart of totals (not averages):**  
Use `sns.barplot` with your pre-aggregated data:
```python
ax = sns.barplot(data=df_snacks, x="snack", y="count")
ax.set_title("Snack Counts (Totals)")
plt.xticks(rotation=15)
plt.show()
```

---

## 4) Boxplot & Violin — **distribution by category**

**Use when:** You need to show **spread**, **median**, and **outliers** by group (boxplot), or the **shape** (violinplot).

**Functions:**  
- `sns.boxplot(data=..., x='group', y='value')`  
- `sns.violinplot(data=..., x='group', y='value', inner='quartile')`

**Example**
```python
fig, axes = plt.subplots(1, 2, figsize=(9, 3.5))
sns.boxplot(data=df_students, x="gender", y="math", ax=axes[0])
axes[0].set_title("Math by Gender — Boxplot")

sns.violinplot(data=df_students, x="gender", y="math", inner="quartile", ax=axes[1])
axes[1].set_title("Math by Gender — Violin")
plt.tight_layout()
plt.show()
```

**Exercise:** Make a **boxplot** of **biology** by **gender**.

**Solution**
```python
sns.boxplot(data=df_students, x="gender", y="bio")
plt.title("Biology by Gender — Boxplot")
plt.show()
```

---

## 5) Scatterplot (with `hue`) — **relationship between two numbers**

**Use when:** You want to see the relationship between two numeric variables (e.g., study hours vs score). Add `hue=` to color by a category.

**Function:**  
- `sns.scatterplot(data=..., x='X', y='Y', hue='category')`

**Example**
```python
ax = sns.scatterplot(data=df_students, x="study_hours", y="math", hue="gender")
ax.set_title("Study Hours vs Math (by Gender)")
ax.set_xlabel("Study Hours per Day")
ax.set_ylabel("Math Score")
plt.grid(True)
plt.show()
```

**Exercise:** Scatterplot **study_hours vs bio**, colored by gender.

**Solution**
```python
ax = sns.scatterplot(data=df_students, x="study_hours", y="bio", hue="gender")
ax.set_title("Study Hours vs Biology (by Gender)")
plt.grid(True)
plt.show()
```

---

## 6) Lineplot — **trend over order/time**

**Use when:** The x-axis is ordered (time, days, stages). Shows trend nicely.

**Function:**  
- `sns.lineplot(data=..., x='x', y='y', marker='o')`

**Example**
```python
ax = sns.lineplot(data=df_daily, x="day", y="steps", marker="o")
ax.set_title("Steps by Day")
ax.set_xlabel("Day")
ax.set_ylabel("Steps")
plt.grid(True)
plt.show()
```

---

## 7) Distributions — **histplot** & **KDE**

**Use when:** You want to show how values are distributed (peaks, spread).

**Functions:**  
- `sns.histplot(data=..., x='value', bins=..., kde=True)`  
- `sns.kdeplot(data=..., x='value', fill=True)`

**Example**
```python
fig, axes = plt.subplots(1, 2, figsize=(9, 3.5))

sns.histplot(data=df_heights, x="height_cm", bins=6, kde=True, ax=axes[0])
axes[0].set_title("Height — Histogram + KDE")

sns.kdeplot(data=df_heights, x="height_cm", fill=True, ax=axes[1])
axes[1].set_title("Height — KDE (filled)")

plt.tight_layout()
plt.show()
```

**Exercise:** Change `bins` (e.g., 4, 8, 10) and notice how the histogram shape changes.

**Solution**
```python
sns.histplot(data=df_heights, x="height_cm", bins=8, kde=True)
plt.title("Height — Histogram (bins=8) + KDE")
plt.show()
```

---

## 8) Quick styling (titles, labels, palettes)

**Why:** Make plots clearer and consistent.

**Functions:**  
- `sns.set_theme(style='whitegrid', palette='pastel')` → global look  
- `palette='Set2'` (or `'muted'`, `'coolwarm'`, etc.) → per-plot palette  
- `ax.set_title/ set_xlabel/ set_ylabel` → titles & labels  
- `plt.xticks(rotation=...)` → rotate x-tick labels  
- `plt.grid(True)` → gridlines

**Example**
```python
sns.set_theme(style="whitegrid", palette="Set2")
ax = sns.barplot(data=df_snacks, x="snack", y="count")
ax.set_title("Snack Counts — Styled")
plt.xticks(rotation=15)
plt.show()

# (Optional) reset to defaults later
sns.set_theme(context="notebook", style="whitegrid")
```

---

## 9) Save a figure to file

**Use when:** You need the image in reports/slides.

**Function:**  
- `plt.savefig("filename.png", dpi=300)` **before** `plt.show()`

**Example**
```python
ax = sns.lineplot(data=df_daily, x="day", y="steps", marker="o")
ax.set_title("Steps by Day (Saved)")
plt.grid(True)
plt.savefig("steps_by_day_seaborn.png", dpi=300)
plt.show()
print("Saved file: steps_by_day_seaborn.png")
```

---

## Cheat-sheet: Which chart should I use?

- **countplot** → When your data has **one categorical** column and you want **counts** per category (e.g., how many males vs females).
- **barplot** → When you want the **mean (or median)** of a **numeric** variable for each **category** (e.g., average score by gender). Also works to show **pre-computed totals** (like snack counts).
- **boxplot / violinplot** → When you need the **distribution** of a numeric variable **by group** (spread, median, outliers).
- **scatterplot** → When exploring the **relationship** between **two numeric** variables (optionally color with `hue`).
- **lineplot** → When showing a **trend over time/order** (e.g., days, months).
- **histplot / kdeplot** → When showing the **overall distribution** of a single numeric variable.

---

## Extra beginner tips

- If your plot shows nothing, check column names (typos are common).
- If your x-labels overlap, use `plt.xticks(rotation=15)` or `figsize=(w,h)` in `plt.figure(...)` or `plt.subplots(...)`.
- If points overlap in `scatterplot`, try `alpha=0.7` for transparency.
- Use `hue=` to compare groups (e.g., gender, region) on the same chart.

---

## Mini practice set (with solutions)

1) **Countplot:** How many students per gender?  
**Solution**
```python
sns.countplot(data=df_students, x="gender")
plt.title("Students by Gender")
plt.show()
```

2) **Barplot:** Average **math** by gender, no error bars.  
**Solution**
```python
import numpy as np
sns.barplot(data=df_students, x="gender", y="math", estimator=np.mean, ci=None)
plt.title("Average Math by Gender (No CI)")
plt.show()
```

3) **Boxplot:** Distribution of **bio** by gender.  
**Solution**
```python
sns.boxplot(data=df_students, x="gender", y="bio")
plt.title("Biology by Gender — Boxplot")
plt.show()
```

4) **Scatterplot:** **study_hours vs math**, color by gender.  
**Solution**
```python
sns.scatterplot(data=df_students, x="study_hours", y="math", hue="gender")
plt.title("Study Hours vs Math (by Gender)")
plt.grid(True)
plt.show()
```

5) **Lineplot:** **steps by day** with markers.  
**Solution**
```python
sns.lineplot(data=df_daily, x="day", y="steps", marker="o")
plt.title("Steps by Day")
plt.grid(True)
plt.show()
```

6) **Histogram:** Heights with 8 bins + KDE.  
**Solution**
```python
sns.histplot(data=df_heights, x="height_cm", bins=8, kde=True)
plt.title("Height Distribution (bins=8)")
plt.show()
```

---

## Wrap-up

- You now know how to build **Seaborn** charts from tiny in-notebook data.  
- Start simple: pick the chart that matches your question (counts? averages? relationships? distribution? trend?).  
- Add clear titles, axis labels, and (when helpful) grids and palettes.  
- Save your best figure with `plt.savefig(...)` for reports.
