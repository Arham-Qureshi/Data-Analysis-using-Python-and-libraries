# 🧠 ANOVA–ANCOVA Predictive Analysis Dashboard  
### *Interactive Statistical Modeling & Visualization Toolkit*

<img src="https://img.shields.io/badge/Python-3.10+-blue?logo=python" alt="Python Badge">
<img src="https://img.shields.io/badge/UI-Tkinter%20%7C%20ttkbootstrap-orange" alt="UI Badge">
<img src="https://img.shields.io/badge/Visualization-Seaborn%20%7C%20Matplotlib-green" alt="Viz Badge">
<img src="https://img.shields.io/github/stars/Arham-Qureshi?style=social" alt="GitHub stars">

---

## 🧩 Overview
This project presents a **Graphical Predictive Analysis Dashboard** integrating **ANOVA (Analysis of Variance)** and **ANCOVA (Analysis of Covariance)** methods in a visually appealing **Tkinter GUI** with **ttkbootstrap themes**.  
It enables **dataset selection, statistical computation, visualization, and model comparison** — all in one sleek interface.

---

## 🚀 Key Features
- 🎛️ Interactive Dashboard — Switch between ANOVA & ANCOVA modes instantly.  
- 📚 Preloaded Datasets — Education, Medical, Agriculture, and Marketing case studies.  
- 📊 Dynamic Visualization — Boxplots, scatter plots, and prediction comparisons.  
- ⚙️ Post-hoc Tukey Test Integration — Automatic multiple comparison analysis.  
- 🧾 Model Metrics — Displays R², Adjusted R², AIC, and BIC scores.  
- 💾 Result Export — Save full statistical summaries to `.txt`.  
- 🌗 Theme Toggle — Instantly switch between Cyborg (dark) and Flatly (light) modes.  
- 🔁 Model Comparison — Visually compare ANOVA vs ANCOVA predictive power.  

---

## 🧮 Technologies Used

| Category | Libraries |
|-----------|------------|
| **GUI** | tkinter, ttkbootstrap |
| **Data Handling** | pandas, numpy |
| **Statistical Analysis** | statsmodels, scipy |
| **Visualization** | matplotlib, seaborn |

---

## 📂 Project Structure
```
ANOVA_ANCOVA_Dashboard/
│
├── d664857e-c3e8-43e6-9f17-7acb1f1f7cf0.py   # Main Dashboard Script
├── README.md                                # This file
├── requirements.txt                         # Python dependencies
└── assets/                                  # (optional) icons, screenshots, etc.
```

---

## ⚙️ Installation & Usage

1. **Clone the repository**
   ```bash
   git clone https://github.com/Arham-Qureshi/ANOVA-ANCOVA-Dashboard.git
   cd ANOVA-ANCOVA-Dashboard
   ```

2. **Install dependencies**
   ```bash
   pip install pandas numpy seaborn matplotlib statsmodels ttkbootstrap
   ```

3. **Run the app**
   ```bash
   python d664857e-c3e8-43e6-9f17-7acb1f1f7cf0.py
   ```

4. **Explore**
   - Choose a dataset  
   - Select ANOVA or ANCOVA  
   - Click Run Analysis  
   - Visualize and compare results!

---

## 🧠 Example Datasets

| Dataset | Description |
|----------|-------------|
| 🎓 **Education** | Compare teaching methods with age as covariate |
| 🏥 **Medical** | Study drug effects on recovery adjusting for age |
| 🌾 **Agriculture** | Analyze fertilizers with rainfall adjustment |
| 💼 **Marketing** | Evaluate ad performance considering income |

---

## 📈 Statistical Output Example
```
=== ANOVA RESULTS (Education) ===

                 sum_sq   df         F    PR(>F)
C(Method)      4325.11    2   8.76     0.001
Residual       24310.2   147
R²: 0.2574 | Adj R²: 0.2445
AIC: 402.76 | BIC: 415.21

--- Post-hoc Tukey Test ---
Group1   Group2   Mean Diff   p-adj   Reject
Method_A Method_B  -2.43      0.05     True
...
```

---

## 🧑‍💻 Author
**Arham Qureshi**  
💻 Game Dev | Data Science | AI Enthusiast  
🌐 [GitHub Profile →](https://github.com/Arham-Qureshi)

> “Code. Debug. Repeat.”

---

## 🧩 Future Enhancements
- 📁 Import your own datasets (.csv)  
- 🧠 Include MANOVA / MANCOVA support  
- 🎨 Custom graph export options (PNG / PDF)  
- ☁️ Cloud dataset integration  

---

## 🪶 License
This project is released under the **MIT License** — feel free to fork, use, and improve it!

---

### 💬 Feedback or Contributions?
Open an issue or pull request on [GitHub](https://github.com/Arham-Qureshi).

---

✨ *Data-Driven Decisions Made Beautiful.* ✨
