
# Seaborn — Beginner Basics (Hands‑On Guide)

This guide gets you productive with **Seaborn** quickly, using tiny, in-notebook datasets. For each concept you get:
- What it is and when to use it
- The key Seaborn function(s) + important arguments
- A minimal example (copy–paste ready)
- A short **Try it** task

> Seaborn sits on top of Matplotlib. You can always fine-tune a Seaborn plot using Matplotlib methods like `ax.set_title(...)` or `ax.set_xlabel(...)`.

---

## 0) Setup

```python
%matplotlib inline  # if you are in Jupyter
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

sns.set_theme(context="notebook", style="whitegrid")  # clean defaults
plt.rcParams.update({'figure.dpi': 120, 'font.size': 12})
```
**What these do**
- `sns.set_theme(...)`: sets a consistent style (grid, fonts, colors).
- `%matplotlib inline`: shows plots in the notebook.
- `plt.rcParams.update(...)`: bigger text and sharper figures.

---

## 1) Data shapes Seaborn likes

Seaborn works best with **DataFrames** in “**long**” form: one row per observation, each column a variable.

```python
# Tiny student dataset
df = pd.DataFrame({
    "name":   ["Alice","Bob","Cara","Dan","Eli","Fay"],
    "gender": ["F","M","F","M","M","F"],
    "study":  [2, 1, 3, 2, 2, 4],   # hours/day
    "math":   [62,55,78,71,66,85],
    "bio":    [58,60,80,68,64,88]
})
df
```
**Why this matters**  
Seaborn functions take `data=df` and then `x="column"`, `y="column"`, `hue="column"`.

**Try it**  
Add a new numeric column:
```python
df["sleep"] = [7,6,8,7,7,8]
```

---

## 2) Countplot — counts of a category

**When**: Count how many rows fall into each category (class balance, frequencies).  
**Function**: `sns.countplot(data=..., x='category_col')`

```python
ax = sns.countplot(data=df, x="gender")
ax.set_title("Count by Gender")
ax.set_xlabel("Gender"); ax.set_ylabel("Count")
plt.show()
```
**Key args**: `hue=` (second category), `order=` (control category order).

**Try it**  
```python
sns.countplot(data=df, x="name", hue="gender")
plt.xticks(rotation=15); plt.show()
```

---

## 3) Barplot — average (or other aggregate) by group

**When**: Show a statistic (mean by default) of a numeric variable for each category.  
**Function**: `sns.barplot(data=..., x='group', y='value', estimator=np.mean)`

```python
ax = sns.barplot(data=df, x="gender", y="math")
ax.set_title("Average Math by Gender")
ax.set_xlabel("Gender"); ax.set_ylabel("Average math")
plt.show()
```
**Key args**: `estimator=` (e.g., `np.mean`, `np.median`), `ci=` (e.g., 95 or `None`), `palette=`, `order=`.

**Try it**  
Median biology by gender, with no CI:
```python
sns.barplot(data=df, x="gender", y="bio", estimator=np.median, ci=None)
plt.show()
```

---

## 4) Boxplot & Violin — distribution by category

**When**: Compare distributions, medians, and spread across groups.  
**Functions**:  
- Box: `sns.boxplot(data=..., x='group', y='value')`  
- Violin: `sns.violinplot(data=..., x='group', y='value', inner='quartile')`

```python
fig, axes = plt.subplots(1, 2, figsize=(9, 3.5))
sns.boxplot(data=df, x="gender", y="math", ax=axes[0])
axes[0].set_title("Math by Gender — Boxplot")

sns.violinplot(data=df, x="gender", y="math", inner="quartile", ax=axes[1])
axes[1].set_title("Math by Gender — Violin")
plt.tight_layout(); plt.show()
```

**Try it**  
```python
sns.boxplot(data=df, x="gender", y="bio")
plt.title("Biology by Gender — Boxplot"); plt.show()
```

---

## 5) Scatterplot — relationship between two numbers

**When**: Visualize relationship / association between two numeric variables.  
**Function**: `sns.scatterplot(data=..., x='X', y='Y', hue='group', style='group', size='num')`

```python
ax = sns.scatterplot(data=df, x="study", y="math", hue="gender", style="gender")
ax.set_title("Study vs Math, colored by Gender")
ax.set_xlabel("Study hours per day"); ax.set_ylabel("Math score")
plt.grid(True); plt.show()
```

**Try it**  
Add point sizes by sleep hours:
```python
sns.scatterplot(data=df, x="study", y="bio", hue="gender", size="sleep", palette="Set2")
plt.show()
```

---

## 6) Lineplot — trends over an order

**When**: Ordered categories or time series.  
**Function**: `sns.lineplot(data=..., x='x', y='y', marker='o')`

```python
days  = ["Mon","Tue","Wed","Thu","Fri"]
steps = [3000, 4200, 3800, 5000, 6100]
df_days = pd.DataFrame({"day": days, "steps": steps})

ax = sns.lineplot(data=df_days, x="day", y="steps", marker="o")
ax.set_title("Steps by Day"); plt.grid(True); plt.show()
```

**Try it**  
Long‑form two‑series trend:
```python
stairs = [200, 150, 300, 250, 400]
df_long = pd.DataFrame({
    "day": days*2,
    "metric": ["steps"]*5 + ["stairs"]*5,
    "value": steps + stairs
})
sns.lineplot(data=df_long, x="day", y="value", hue="metric", marker="o")
plt.show()
```

---

## 7) Histograms and KDE (distributions)

**When**: Understand how values are spread.  
**Functions**:  
- Histogram: `sns.histplot(data=..., x='value', bins=..., kde=True)`  
- KDE: `sns.kdeplot(data=..., x='value', fill=True)`

```python
heights = [150,152,153,155,156,158,160,162,163,165,168,170,172,175,178]
df_h = pd.DataFrame({"height_cm": heights})

fig, axes = plt.subplots(1, 2, figsize=(9, 3.5))
sns.histplot(data=df_h, x="height_cm", bins=6, kde=True, ax=axes[0])
axes[0].set_title("Height — Histogram + KDE")

sns.kdeplot(data=df_h, x="height_cm", fill=True, ax=axes[1])
axes[1].set_title("Height — KDE only")
plt.tight_layout(); plt.show()
```

**Try it**  
Change `bins` to `4` and `10` and compare shapes.

---

## 8) Regression plots

**When**: Scatter plus a fitted regression line (quick trend).  
**Functions**:  
- Simple: `sns.regplot(data=..., x='X', y='Y')`  
- Faceted/with groups: `sns.lmplot(data=..., x='X', y='Y', hue='group', col='group')`

```python
ax = sns.regplot(data=df, x="study", y="math")
ax.set_title("Study vs Math with regression line")
plt.show()
```

**Try it**  
Two regression lines by gender:
```python
sns.lmplot(data=df, x="study", y="math", hue="gender", height=4, aspect=1.2)
plt.show()
```

---

## 9) Heatmap — correlations or matrices

**When**: Show a matrix (like correlations) using color.  
**Function**: `sns.heatmap(data=matrix, annot=True, cmap='coolwarm')`

```python
corr = df[["study","math","bio","sleep"]].corr(numeric_only=True)
ax = sns.heatmap(corr, annot=True, cmap="coolwarm", vmin=-1, vmax=1)
ax.set_title("Correlation heatmap")
plt.show()
```

**Try it**  
Remove `sleep` and see how the correlations change.

---

## 10) Faceting (small multiples) — split by a category

**When**: The same plot repeated per subgroup.  
**Functions** (high‑level faceting helpers):  
- `sns.relplot(kind='scatter'|'line')`  
- `sns.catplot(kind='bar'|'box'|'violin')`  
- `sns.displot(kind='hist'|'kde')`

```python
g = sns.relplot(data=df, x="study", y="math", col="gender", kind="scatter", height=3.5, aspect=1)
g.set_titles("gender = {col_name}")
plt.show()
```

**Try it**  
Boxplots of `math` by `gender`, faceted by study group:
```python
df["study_group"] = np.where(df["study"]<=2, "low","high")
sns.catplot(data=df, x="gender", y="math", col="study_group", kind="box", height=3.5)
plt.show()
```

---

## 11) Styling and themes

**Palette and style**
```python
sns.set_theme(style="whitegrid", palette="Set2")
ax = sns.barplot(data=df, x="gender", y="math")
ax.set_title("Styled barplot")
plt.show()

# Restore default
sns.set_theme(context="notebook", style="whitegrid")
```

**Common adjustments**
```python
ax = sns.scatterplot(data=df, x="study", y="math", hue="gender")
ax.set_title("Title here")
ax.set_xlabel("Study (hours/day)")
ax.set_ylabel("Math score")
ax.legend(title="Gender", loc="lower right")
plt.tight_layout(); plt.show()
```

**Try it**  
Pick any previous plot and change: `palette`, `title`, axis labels, and legend location.

---

## 12) Missing values and category order

```python
# Missing values: Seaborn skips NaNs automatically.
df_nan = df.copy()
df_nan.loc[1, "math"] = np.nan
sns.scatterplot(data=df_nan, x="study", y="math")
plt.title("NaNs are skipped"); plt.show()

# Order of categories
order = ["F","M"]
sns.barplot(data=df, x="gender", y="bio", order=order)
plt.title("Controlled category order"); plt.show()
```

**Try it**  
Create a categorical column with order `["Bronze","Silver","Gold"]`. Plot a countplot with that order enforced (`order=`).

---

## 13) Saving figures

```python
ax = sns.lineplot(data=df, x="study", y="math", marker="o")
ax.set_title("Save me")
plt.savefig("seaborn_save_example.png", dpi=300, bbox_inches="tight")
plt.show()
print("Saved seaborn_save_example.png")
```

**Key args**: `dpi=` resolution, `bbox_inches="tight"` trims whitespace.

---

## 14) Quick “cookbook” of common plots

| Goal | Function | Minimal example |
|---|---|---|
| Counts by category | `sns.countplot` | `sns.countplot(data=df, x="gender")` |
| Mean by category | `sns.barplot` | `sns.barplot(data=df, x="gender", y="math")` |
| Distribution (hist + KDE) | `sns.histplot` | `sns.histplot(data=df, x="math", kde=True)` |
| Distribution (smooth) | `sns.kdeplot` | `sns.kdeplot(data=df, x="math", fill=True)` |
| Distribution by group | `sns.boxplot` / `sns.violinplot` | `sns.boxplot(data=df, x="gender", y="math")` |
| Relationship | `sns.scatterplot` | `sns.scatterplot(data=df, x="study", y="math")` |
| Trend + regression | `sns.regplot` | `sns.regplot(data=df, x="study", y="math")` |
| Correlation heatmap | `sns.heatmap` | `sns.heatmap(df.corr(numeric_only=True), annot=True)` |
| Faceting small multiples | `sns.relplot`/`sns.catplot`/`sns.displot` | `sns.relplot(data=df, x="study", y="math", col="gender")` |

---

## 15) Mini‑exercises (solutions inline)

### A) Class balance and performance
```python
sns.countplot(data=df, x="gender"); plt.title("Class counts"); plt.show()
sns.barplot(data=df, x="gender", y="bio", ci=None); plt.title("Average bio by gender"); plt.show()
```

### B) Distributions by group
```python
sns.histplot(data=df, x="math", bins=6, kde=True); plt.title("Math distribution"); plt.show()
sns.boxplot(data=df, x="gender", y="math"); plt.title("Math by gender"); plt.show()
```

### C) Relationship with a fit
```python
sns.regplot(data=df, x="study", y="math"); plt.title("Regression"); plt.show()
sns.scatterplot(data=df, x="study", y="math", hue="gender"); plt.title("Colored by gender"); plt.show()
```

### D) Correlation overview
```python
corr = df[["study","math","bio"]].corr(numeric_only=True)
sns.heatmap(corr, annot=True, cmap="coolwarm", vmin=-1, vmax=1)
plt.title("Correlation"); plt.show()
```

---

### Final tips
- Start with **Seaborn** for speed and nicer defaults, then call Matplotlib methods to fine‑tune.
- Keep data **long‑form** to unlock `hue`, `col`, `row`, and faceting.
- Use `palette` and `sns.set_theme` for quick, consistent styling.
- Use `ci=None` on barplots for cleaner teaching visuals (add it back when discussing uncertainty).
