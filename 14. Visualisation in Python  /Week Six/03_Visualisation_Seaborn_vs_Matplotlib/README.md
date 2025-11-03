# Matplotlib vs Seaborn — What’s the difference and when to use each?
A friendly, hands-on comparison for beginners. We’ll build tiny datasets **inside** the notebook/script and compare how to make the **same chart** in Matplotlib and Seaborn — side by side — so you can see where each shines.

> **You will learn**
>
> - The philosophy of **Matplotlib** (low-level control) vs **Seaborn** (statistical, style-first)
> - How defaults and styling differ
> - Categorical and statistical plotting (e.g., regression) — why Seaborn often feels easier
> - Faceting: multi-plot layouts (manual in Matplotlib vs built-in in Seaborn)
> - A practical checklist: **When to choose which?**

No data files are needed. We’ll use tiny lists/dicts and small DataFrames.

---

## 0) Setup
```python
%matplotlib inline                 # in notebooks: show plots inline
import numpy as np                 # numbers and small math (we'll use it for regression)
import pandas as pd               # tables/dataframes (Seaborn loves these)
import matplotlib.pyplot as plt    # core plotting library
import seaborn as sns              # statistical plots and nice defaults

# Make figures crisp and text readable
plt.rcParams.update({'figure.dpi': 120, 'font.size': 12})

# Apply a clean theme (grid, fonts, etc.)
sns.set_theme(context="notebook", style="whitegrid")
```

### Tiny datasets we will reuse
```python
months = ["Jan","Feb","Mar","Apr","May","Jun"]
temps  = [5, 6, 9, 12, 16, 19]

# Aggregated category counts
snack_counts = {"Apples": 12, "Bananas": 7, "Carrots": 5, "Dates": 3}

# Row-wise version (one row per observation) for Seaborn countplot
snack_items = (["Apples"]*6 + ["Bananas"]*4 + ["Carrots"]*3 + ["Dates"]*2
               + ["Apples"]*6 + ["Bananas"]*3)
df_snacks = pd.DataFrame({"snack": snack_items})
df_snacks_agg = pd.DataFrame({"snack": list(snack_counts.keys()),
                              "count": list(snack_counts.values())})

study =  [1, 2, 2, 3, 4, 4, 5, 6]
score =  [50,55,58,65,70,72,80,88]
gender = ["F","M","F","M","M","F","M","F"]
df_students = pd.DataFrame({"study": study, "score": score, "gender": gender})
```

**What the functions do**
- `%matplotlib inline`: in Jupyter, shows plots in the cell output.
- `plt.rcParams.update`: change global style (image clarity, font size).
- `sns.set_theme`: set a nice default look (grid + colors) for all plots.

---

## 1) Philosophy & Defaults (Line chart example)
- **Matplotlib** = low-level, flexible. You style much of it yourself.
- **Seaborn** = higher-level, DataFrame-friendly, great defaults, quick stats.

```python
fig, axes = plt.subplots(1, 2, figsize=(10, 3.5))

# Matplotlib
axes[0].plot(months, temps, marker='o')
axes[0].set_title("Matplotlib line")
axes[0].set_xlabel("Month"); axes[0].set_ylabel("Temp (°C)")
axes[0].grid(True)

# Seaborn
sns.lineplot(x=months, y=temps, marker='o', ax=axes[1])
axes[1].set_title("Seaborn lineplot")
axes[1].set_xlabel("Month"); axes[1].set_ylabel("Temp (°C)")

plt.tight_layout(); plt.show()
```

**Where to use line charts:** trends over ordered categories (time, stages, months).

**Key functions**
- `plt.subplots(r, c, figsize)`: create a figure and a grid of axes.
- `ax.plot(x, y)`: Matplotlib line.
- `sns.lineplot(x=..., y=..., ax=...)`: Seaborn line with nice defaults.
- `ax.set_title/ set_xlabel/ set_ylabel`: annotate axes.

---

## 2) Categorical counts: Bar (Matplotlib) vs Countplot (Seaborn)
Two shapes of data:
- **Aggregated**: dict of totals (good for Matplotlib `bar` or Seaborn `barplot`).
- **Row-wise**: one row per item (good for Seaborn `countplot` — it counts for you).

```python
fig, axes = plt.subplots(1, 2, figsize=(10, 3.5))

# Matplotlib bar (aggregated)
labels = list(snack_counts.keys())
values = list(snack_counts.values())
axes[0].bar(labels, values)
axes[0].set_title("Matplotlib bar (aggregated)")
axes[0].set_xlabel("Snack"); axes[0].set_ylabel("Count")
for t in axes[0].get_xticklabels(): t.set_rotation(15)

# Seaborn countplot (row-wise)
sns.countplot(data=df_snacks, x="snack", ax=axes[1])
axes[1].set_title("Seaborn countplot (auto-count)")
axes[1].set_xlabel("Snack"); axes[1].set_ylabel("Count")
for t in axes[1].get_xticklabels(): t.set_rotation(15)

plt.tight_layout(); plt.show()
```

**Where to use these**
- Bar (aggregated): you already have totals per category.
- Countplot (row-wise): your data is one row per observation and you want quick counts.

**Key functions**
- `ax.bar(x, height)`: Matplotlib bar chart.
- `sns.countplot(data=..., x='col')`: auto-count rows per category.

---

## 3) Summary bars (mean by group) — Seaborn advantage
Seaborn’s `barplot` computes the mean (by default) for each category.

```python
ax = sns.barplot(data=df_students, x="gender", y="score")
ax.set_title("Average Score by Gender")
ax.set_xlabel("Gender"); ax.set_ylabel("Mean Score")
plt.show()
```

**Where to use:** show a statistic (mean/median) per group.  
**Tip:** Change the statistic with `estimator=np.median`.

---

## 4) Distribution by group: Box & Violin
```python
fig, axes = plt.subplots(1, 2, figsize=(10, 3.5))

sns.boxplot(data=df_students, x="gender", y="score", ax=axes[0])
axes[0].set_title("Boxplot: Score by Gender")

sns.violinplot(data=df_students, x="gender", y="score", inner="quartile", ax=axes[1])
axes[1].set_title("Violin: Score by Gender")

plt.tight_layout(); plt.show()
```

**Where to use:** compare spreads and medians per category.  
- **Boxplot**: compact summary (median, quartiles, outliers).
- **Violin**: shows the full shape/density.

**Key functions**
- `sns.boxplot(...)`, `sns.violinplot(..., inner="quartile")`

---

## 5) Relationship (Scatter) + groups (hue)
```python
ax = sns.scatterplot(data=df_students, x="study", y="score", hue="gender")
ax.set_title("Study vs Score (colored by gender)")
ax.set_xlabel("Study hours"); ax.set_ylabel("Score")
plt.grid(True); plt.show()
```

**Where to use:** show relationship between two numeric variables; color by group for comparison.

**Key function**
- `sns.scatterplot(..., hue='group')`

---

## 6) Regression line (trend): manual vs auto
```python
fig, axes = plt.subplots(1, 2, figsize=(10, 3.5))

# Matplotlib: manual regression with numpy.polyfit
axes[0].scatter(df_students["study"], df_students["score"], label="data")
m, b = np.polyfit(df_students["study"], df_students["score"], 1)  # slope & intercept
xline = np.linspace(min(df_students["study"]), max(df_students["study"]), 50)
axes[0].plot(xline, m*xline + b, linestyle="--", label="fit")
axes[0].set_title("Matplotlib: manual regression")
axes[0].legend(); axes[0].grid(True)

# Seaborn: one-liner
sns.regplot(data=df_students, x="study", y="score", ax=axes[1])
axes[1].set_title("Seaborn regplot (auto-fit)")

plt.tight_layout(); plt.show()
```

**Where to use:** show a trend/line of best fit.  
**Key functions**
- `np.polyfit(x, y, 1)`: returns slope & intercept for a straight line.
- `sns.regplot(...)`: scatter + regression line for you.

---

## 7) Faceting (small multiples)
Compare the same plot split by a category (e.g., one panel per gender).

```python
# Matplotlib: manual faceting
fig, axes = plt.subplots(1, 2, figsize=(10, 3.5), sharey=True)
for ax, g in zip(axes, sorted(df_students['gender'].unique())):
    d = df_students[df_students['gender']==g]
    ax.scatter(d['study'], d['score'])
    ax.set_title(f"gender={g}")
    ax.set_xlabel("Study"); ax.set_ylabel("Score"); ax.grid(True)
plt.tight_layout(); plt.show()

# Seaborn: FacetGrid via relplot
g = sns.relplot(data=df_students, x="study", y="score", col="gender",
                kind="scatter", height=3.2, aspect=1.0)
g.set_titles("gender = {col_name}")
plt.show()
```

**Where to use:** compare patterns across subgroups quickly.  
**Key function**
- `sns.relplot(..., col='group')`: auto-layout of multiple panels.

---

## 8) Styling and themes
```python
# Matplotlib: tweak per plot
plt.plot(months, temps, marker='o', linewidth=2)
plt.title("Matplotlib styled")
plt.xlabel("Month"); plt.ylabel("Temp (°C)")
plt.grid(True); plt.show()

# Seaborn: set a palette/theme once, then plot
sns.set_theme(style="whitegrid", palette="Set2")
ax = sns.barplot(data=df_snacks_agg, x="snack", y="count")
ax.set_title("Seaborn styled")
plt.xticks(rotation=15); plt.show()

# Restore default theme if you want
sns.set_theme(context="notebook", style="whitegrid")
```

**Where to use:** whenever you want a clean, professional look quickly.

**Key functions**
- `sns.set_theme(style=..., palette=...)`
- `plt.grid(True)`

---

## 9) Saving figures (same for both)
```python
fig, ax = plt.subplots(figsize=(6, 3.5))
sns.lineplot(x=months, y=temps, marker='o', ax=ax)
ax.set_title("Saved example")
plt.savefig("saved_example.png", dpi=300)   # save BEFORE show()
plt.show()
print("Saved: saved_example.png")
```

**Key function**
- `plt.savefig("file.png", dpi=300)`: export high-quality images.

---

## 10) When to choose which?

### Use **Matplotlib** when…
- You need **low-level control** or very custom layouts (annotations, insets, multiple axes)
- You want to style every detail manually
- You’re building complex, publication-quality figures that require precise tuning

### Use **Seaborn** when…
- You want **good-looking defaults** with minimal code
- Your data is **tabular** (DataFrame) and you want quick **statistical plots** (mean bars, box/violin, regression)
- You need **faceting** (small multiples) fast

### Use **both together** (most common)
- Create with **Seaborn** for speed/polish, then fine‑tune with **Matplotlib** (`ax.set(...)`, annotations, limits).

---

## Mini exercises (with solutions)

**A — Pick the right chart**  
**Q:** You have monthly temperatures. Which chart? Why?  
**A:** **Line chart** — shows change over time (ordered axis).

**B — Bar vs Countplot**  
**Q:** You have a dict of counts per category. Which is simpler?  
**A:** **Matplotlib bar** or **Seaborn barplot** (already aggregated). If you had one row per item, **Seaborn countplot** would auto-count.

**C — Mean by group**  
```python
sns.barplot(data=df_students, x="gender", y="score")
plt.title("Average Score by Gender"); plt.show()
```

**D — Distribution by group**  
```python
sns.boxplot(data=df_students, x="gender", y="score")
plt.title("Score by Gender"); plt.show()
```

**E — Trend line**  
```python
sns.regplot(data=df_students, x="study", y="score")
plt.title("Study vs Score with Trend"); plt.show()
```

---

## Quick reference (functions you’ll use most)

**Matplotlib**
- `plt.subplots(r, c, figsize)`, `ax.plot`, `ax.scatter`, `ax.bar`
- `ax.set_title`, `ax.set_xlabel`, `ax.set_ylabel`, `ax.grid(True)`
- `plt.savefig("file.png", dpi=300)`

**Seaborn**
- `sns.lineplot`, `sns.countplot`, `sns.barplot`, `sns.boxplot`, `sns.violinplot`
- `sns.scatterplot(..., hue=...)`, `sns.regplot`
- `sns.relplot(..., col=...)` (faceting)
- `sns.set_theme(style=..., palette=...)`

**Bottom line:** Start in **Seaborn** for speed and clarity. Use **Matplotlib** to fine-tune details when you need extra control.


>Final tip

Start with Seaborn for speed and nice defaults. When you need extra control, customize with Matplotlib on the same axes. This is the most common and most productive workflow.
