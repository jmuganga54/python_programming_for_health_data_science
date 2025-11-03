# Week 6 — Visualisation in Python (3–7 Nov 2025)

**Goal:** Build strong foundations for plotting in Python using **Matplotlib** and **Seaborn**. Work in **eLabs** (no installs needed).

---

## Key Dates (Europe/London)
- **Mon 3 Nov, 10:00–12:00** — In-person session: intro, hands-on exercises, Q&A.
- **Thu 6 Nov** — Exercise **solutions** will be posted on **Canvas**.
- **All week** — Self-paced study on eLabs notebooks.

---

## Learning Outcomes
By the end of the week you will be able to:
1. **Create** clear, well-labelled plots (Matplotlib & Seaborn).
2. **Choose** the right chart type for your data:
   - **Line** — changes over time/order
   - **Bar** — compare categories
   - **Scatter** — relationship between two numeric variables
   - **Histogram** — distribution (spread of values)
   - **Box plot** — distribution + outliers across groups
3. **Customize & export** figures:
   - Titles, axis labels (with units), legends, ticks
   - Colours, markers, styles
   - Save images to PNG/PDF for reports

---

## How the Week Runs
1. **Log in to eLabs** → open **Week 6** notebooks.
2. **Work through notebooks**: run cells top-to-bottom, read notes, try practice tasks.
3. **Use the in-person session** (Mon) to ask questions and get unstuck.
4. **Complete the exercise notebook** (not graded but essential).
5. **Check Canvas on Thu** for official solutions; compare with your answers.

> New to eLabs? See **“2.2 Introduction to eLabs.”**  
> Prefer local work? The same notebooks are in **“6.1 Week 6 Jupyter notebooks.”**

---

## Quick Cheat-Sheet

### Matplotlib (core plotting)
```python
import matplotlib.pyplot as plt

plt.figure(figsize=(6, 4))
plt.plot(x, y)                      # line plot
plt.title("My Plot")
plt.xlabel("X label (units)")
plt.ylabel("Y label (units)")
plt.grid(True)
plt.tight_layout()
plt.savefig("figure.png", dpi=300)  # export
plt.show()
```

### Seaborn (quick stats plots & nicer defaults)
```python
import seaborn as sns

sns.set_theme()  # nicer defaults
sns.scatterplot(data=df, x="age", y="bmi", hue="gender")
sns.boxplot(data=df, x="group", y="value")
sns.histplot(data=df, x="bmi", bins=30, kde=True)
```

---

## Good Plotting Habits
- **Label everything**: title, axes, units, and legends.
- **Keep it simple**: avoid clutter; pick readable fonts and sensible colours.
- **Match the chart to the question**: explain what the plot shows in one sentence.
- **Re-use styles**: make your figures consistent across a report.
- **Save your best plots**: you can drop them straight into your coursework reports.

---

## Troubleshooting Tips
- If a cell fails, **run the setup/import cells first**.
- If plots look squashed, use `plt.figure(figsize=(w, h))` and `plt.tight_layout()`.
- If labels overlap, rotate ticks: `plt.xticks(rotation=45)`.

---

## What to Hand In?
- The exercise notebook is **not submitted**, but **do it** to check your understanding.
- Solutions on **Thu 6 Nov** (Canvas) will help you self-assess.
