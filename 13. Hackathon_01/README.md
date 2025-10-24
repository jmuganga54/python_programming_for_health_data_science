# Hackathon 01: Analysing Brain Aneurysm Rupture Data — Summary

## What this is about
You will analyze a real dataset of **750 brain aneurysms** to learn which features are linked to **rupture**. You’ll practice a typical data‑science workflow:
**load → explore → clean → analyze → visualize → interpret**.

## What a brain aneurysm is
A **brain (intracranial) aneurysm** is a bulge in a brain blood vessel. If it **ruptures**, it can cause **haemorrhagic stroke** and serious neurological damage.

## Common aneurysm locations
- **ICA** (Internal Carotid Artery): includes ICA Ophthalmic, ICA Cavernous, ICA Tip  
- **MCA** (Middle Cerebral Artery)  
- **VA** (Vertebral Artery)  
- **BA** (Basilar Artery)  
- **AComA** (Anterior Communicating Artery)

## Dataset
- File: `data_aneurysms.csv` (provided; no download needed)  
- Rows: **750 aneurysms**  
- Key columns:
  - **Patient ID** — unique identifier
  - **Status** — *ruptured* or *unruptured*
  - **Location** — anatomical site (e.g., ICA, MCA, etc.)
  - **Side** — *left* or *right*
  - **Gender**
  - **Age**
  - **AR** — Aspect Ratio (shape feature)
  - **NSI** — Non‑Sphericity Index (how non‑round the shape is)
  - **Dmax** — maximum aneurysm diameter (size)
  - **Dn** — neck (normal) diameter
  - **H** — aneurysm height

### Quick glossary (key measurements)
- **AR (Aspect Ratio):** shape descriptor; higher values often indicate more elongated aneurysms.  
- **NSI (Non‑Sphericity Index):** how far from a perfect sphere the aneurysm is (larger → less spherical).  
- **Dmax:** maximum diameter; larger aneurysms generally carry higher rupture risk.  
- **Dn:** neck diameter.  
- **H:** aneurysm height.

## What you’ll do (big picture)
1. **Load** the CSV into pandas.  
2. **Explore**: counts, missing values, and basic stats.  
3. **Subset**: focus on **ICA** aneurysms first (a common type).  
4. **Clean**: handle missing data (e.g., fill numeric with mean; standardize/drop categorical if missing).  
5. **Analyze**:
   - Compare **ruptured vs unruptured** by side, gender, and key measurements (Age, AR, NSI, Dmax, Dn, H).
   - Compute **summary statistics** (mean, median, std, min, max).
6. **Visualize**:
   - Histograms + density plots for Age, AR, NSI, Dmax, Dn, H, split by rupture **Status**.
   - **Correlation heatmaps** (convert categories to numbers first) to see relationships with **Status**.
7. **Extend to all data**:
   - Create simplified site category **Site**:
     - `A` → contains *ICA*  
     - `B` → contains *MCA*  
     - `C` → contains *VA*, *BA*, or *AComA*  
   - Re‑clean and analyze full dataset.
8. **Risk scoring (modified PHASES)**:
   - Build a simplified **PHASES** score from **Site**, **Age**, **Dmax**:  
     - **Site Score:** A=0, B=2, C=4  
     - **Age Score:** <70 → 0, ≥70 → 1  
     - **Size Score (Dmax):** <7 → 0; 7–<10 → 3; 10–<20 → 6; ≥20 → 10  
   - **PHASES = Site Score + Age Score + Size Score**  
   - Compare PHASES by rupture **Status** (e.g., box plots).

## Simple checks you’ll perform
- Count/percentage of **ruptured** vs **unruptured** with:  
  - **Dmax > 10 mm** (known risk factor)  
  - **AR > 2** (shape‑related risk)  
  - **NSI > 0.2** (less spherical shapes may carry risk)

## Goal
Identify **patterns** suggesting which factors (e.g., larger **Dmax**, higher **AR/NSI**, older **Age**, certain **Locations/Sites**) are **associated with rupture**, and assess whether the **modified PHASES** score tends to be **higher** in ruptured cases.

---
#### Task 1: Read the data

Let's start by importing the necessary libraries and reading the CSV file containing the aneurysm data. In this task, we will load the dataset data_aneurysms.csv into a Pandas DataFrame. This will allow us to manipulate and analyse the data effectively. Use the pd.read_csv() function to read the CSV file.

```
import pandas as pd

# Read the data
df = pd.read_csv('./data/data_aneurysms.csv')
df.head()
```