import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import ttkbootstrap as tb
from ttkbootstrap.constants import *
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.formula.api import ols
import statsmodels.api as sm
from statsmodels.stats.multicomp import pairwise_tukeyhsd
import io

app = tb.Window(themename="cyborg")
app.title("ANOVA & ANCOVA Predictive Analysis Dashboard")
app.geometry("1150x820")

analysis_type = tk.StringVar(value="ANOVA")
dataset_choice = tk.StringVar(value="Education")
current_data = None
model = None

def load_dataset(name):
    np.random.seed(42)
    n = 50

    if name == "Education":
        groups = ['Method_A', 'Method_B', 'Method_C']
        age = np.random.randint(18, 25, n * 3)
        score = np.repeat([70, 75, 80], n) + 0.7 * age + np.random.normal(0, 5, n * 3)
        df = pd.DataFrame({'Method': np.repeat(groups, n), 'Age': age, 'Score': score})
        desc = "🎓 Education Dataset — Compare teaching methods and age impact on student scores."

    elif name == "Medical":
        groups = ['Drug_A', 'Drug_B', 'Drug_C']
        age = np.random.randint(30, 60, n * 3)
        recovery = np.repeat([60, 70, 75], n) + 0.5 * age + np.random.normal(0, 6, n * 3)
        df = pd.DataFrame({'Method': np.repeat(groups, n), 'Age': age, 'Score': recovery})
        desc = "🏥 Medical Dataset — Study treatment efficiency adjusting for patient age."

    elif name == "Agriculture":
        groups = ['Fert_A', 'Fert_B', 'Fert_C']
        rain = np.random.randint(200, 500, n * 3)
        yield_crop = np.repeat([150, 160, 170], n) + 0.2 * rain + np.random.normal(0, 10, n * 3)
        df = pd.DataFrame({'Method': np.repeat(groups, n), 'Age': rain, 'Score': yield_crop})
        desc = "🌾 Agriculture Dataset — Analyze fertilizer performance adjusting for rainfall."

    elif name == "Marketing":
        groups = ['TV_Ads', 'Online_Ads', 'Billboards']
        income = np.random.randint(20000, 70000, n * 3)
        sales = np.repeat([150, 180, 200], n) + 0.001 * income + np.random.normal(0, 8, n * 3)
        df = pd.DataFrame({'Method': np.repeat(groups, n), 'Age': income, 'Score': sales})
        desc = "💼 Marketing Dataset — Compare advertisement types adjusting for consumer income."

    return df, desc

def show_dataset_info(event=None):
    global current_data
    dataset_name = dataset_choice.get()
    df, desc = load_dataset(dataset_name)
    current_data = df

    info_text.delete(1.0, tk.END)
    info_text.insert(tk.END, f"{desc}\n\n")
    info_text.insert(tk.END, f"Shape: {df.shape}\nColumns: {list(df.columns)}\n\n")
    info_text.insert(tk.END, str(df.head(5)))

def run_analysis():
    global model, current_data
    if current_data is None:
        messagebox.showwarning("No Dataset", "Please select a dataset first.")
        return

    try:
        if analysis_type.get() == "ANOVA":
            model = ols('Score ~ C(Method)', data=current_data).fit()
        else:
            model = ols('Score ~ C(Method) + Age', data=current_data).fit()

        table = sm.stats.anova_lm(model, typ=2)

        # Log results
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, f"=== {analysis_type.get()} RESULTS ({dataset_choice.get()}) ===\n\n")
        result_text.insert(tk.END, f"{table}\n\n")
        result_text.insert(tk.END, f"R²: {model.rsquared:.4f}\nAdj R²: {model.rsquared_adj:.4f}\nAIC: {model.aic:.2f}, BIC: {model.bic:.2f}\n\n")

        # Post-hoc test
        tukey = pairwise_tukeyhsd(current_data['Score'], current_data['Method'])
        result_text.insert(tk.END, f"--- Post-hoc Tukey Test ---\n{tukey.summary()}\n")

        plot_results()

    except Exception as e:
        messagebox.showerror("Error", str(e))


def plot_results():
    global model, current_data

    sns.set_theme(style="whitegrid")

    plt.figure(figsize=(9, 4))
    sns.boxplot(x='Method', y='Score', data=current_data, palette='coolwarm')
    plt.title(f"Score Distribution ({dataset_choice.get()})")
    plt.show()

    plt.figure(figsize=(9, 4))
    sns.scatterplot(x='Age', y='Score', hue='Method', data=current_data, s=50)
    plt.title('Covariate vs Dependent Variable')
    plt.show()

    # Comparison: Actual vs Predicted
    current_data['Predicted'] = model.fittedvalues
    plt.figure(figsize=(6, 6))
    sns.scatterplot(x='Score', y='Predicted', hue='Method', data=current_data)
    plt.plot([current_data['Score'].min(), current_data['Score'].max()],
            [current_data['Score'].min(), current_data['Score'].max()],
            'r--')
    plt.title("Predicted vs Actual Scores")
    plt.show()


def compare_models():
    """Compare ANOVA vs ANCOVA visually"""
    df, _ = load_dataset(dataset_choice.get())

    model_a = ols('Score ~ C(Method)', data=df).fit()
    model_c = ols('Score ~ C(Method) + Age', data=df).fit()

    plt.bar(['ANOVA', 'ANCOVA'], [model_a.rsquared, model_c.rsquared], color=['orange', 'green'])
    plt.title(f"Model Comparison (R² Values) — {dataset_choice.get()}")
    plt.ylabel("R² Value")
    plt.show()

    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, f"R² (ANOVA): {model_a.rsquared:.4f}\nR² (ANCOVA): {model_c.rsquared:.4f}\n\n")
    if model_c.rsquared > model_a.rsquared:
        result_text.insert(tk.END, "✅ ANCOVA shows higher predictive accuracy.\n")
    else:
        result_text.insert(tk.END, "ℹ️ ANOVA performs equally or better for this dataset.\n")


def export_results():
    if model is None:
        messagebox.showinfo("Info", "Please run an analysis first.")
        return

    file = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text File", "*.txt")])
    if file:
        with open(file, "w") as f:
            f.write(result_text.get(1.0, tk.END))
        messagebox.showinfo("Exported", f"Results saved to {file}")


def toggle_theme():
    current = app.style.theme_use()
    new_theme = "flatly" if current == "cyborg" else "cyborg"
    app.style.theme_use(new_theme)

tb.Label(app, text="ANOVA & ANCOVA Predictive Analysis Dashboard",
            font=("Segoe UI", 20, "bold"), bootstyle="info").pack(pady=15)

frame = ttk.Frame(app)
frame.pack(pady=10)

tb.Label(frame, text="Select Dataset:", font=("Segoe UI", 12)).grid(row=0, column=0, padx=8)
tb.Combobox(frame, textvariable=dataset_choice,
            values=["Education", "Medical", "Agriculture", "Marketing"],
            width=20, state="readonly").grid(row=0, column=1, padx=8)

tb.Label(frame, text="Select Analysis:", font=("Segoe UI", 12)).grid(row=0, column=2, padx=8)
tb.Radiobutton(frame, text="ANOVA", variable=analysis_type, value="ANOVA", bootstyle="success").grid(row=0, column=3)
tb.Radiobutton(frame, text="ANCOVA", variable=analysis_type, value="ANCOVA", bootstyle="warning").grid(row=0, column=4)

tb.Button(frame, text="🔍 Load Dataset", command=show_dataset_info, bootstyle="primary").grid(row=0, column=5, padx=8)
tb.Button(frame, text="🌗 Toggle Theme", command=toggle_theme, bootstyle="secondary").grid(row=0, column=6, padx=8)

# Text areas
info_text = tk.Text(app, height=12, width=120, wrap="word", font=("Consolas", 10))
info_text.pack(pady=8)

btn_frame = ttk.Frame(app)
btn_frame.pack(pady=5)

tb.Button(btn_frame, text="▶ Run Analysis", command=run_analysis, bootstyle="success-outline").grid(row=0, column=0, padx=10)
tb.Button(btn_frame, text="📊 Compare Models", command=compare_models, bootstyle="info-outline").grid(row=0, column=1, padx=10)
tb.Button(btn_frame, text="💾 Export Results", command=export_results, bootstyle="dark-outline").grid(row=0, column=2, padx=10)

result_text = tk.Text(app, height=18, width=120, wrap="word", font=("Consolas", 10))
result_text.pack(pady=8)
app.mainloop()