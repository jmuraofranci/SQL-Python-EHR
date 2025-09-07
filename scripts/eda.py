import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from scripts.utils import save_plot

def run_eda(df: pd.DataFrame):
    """Perform basic exploratory analysis and save plots."""

    # Tumor size distribution
    sns.histplot(df["Tumor_Size_cm"], bins=30, kde=True)
    plt.title("Tumor Size Distribution")
    fig = plt.gcf()
    save_plot(fig, "tumor_size_distribution.png")

    # Treatment × Response × Survival
    heatmap_data = pd.crosstab(
        df["Treatment"], 
        [df["Response_to_Treatment"], df["Survival_Status"]]
    )
    sns.heatmap(heatmap_data, annot=True, fmt="d", cmap="Blues")
    plt.title("Treatment × Response × Survival")
    fig = plt.gcf()
    save_plot(fig, "treatment_response_survival.png")

    print("EDA complete. Plots saved in outputs/")
