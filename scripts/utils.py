import os
import matplotlib.pyplot as plt
import pandas as pd

def ensure_output_dir(folder: str = "outputs") -> None:
    """Ensure the output directory exists."""
    os.makedirs(folder, exist_ok=True)

def save_plot(fig, filename: str, folder: str = "outputs") -> str:
    """
    Save a matplotlib figure to the outputs folder.

    Parameters:
        fig (matplotlib.figure.Figure): The figure object to save.
        filename (str): Name of the file (e.g., 'plot.png').
        folder (str): Output directory.
    
    Returns:
        str: Path to the saved plot.
    """
    ensure_output_dir(folder)
    path = os.path.join(folder, filename)
    fig.savefig(path)
    plt.close(fig)
    return path

def save_metrics(metrics: dict, filename: str = "model_metrics.txt", folder: str = "outputs") -> str:
    """
    Save model metrics to a text file.

    Parameters:
        metrics (dict): Dictionary of metric name → value.
        filename (str): Output file name.
        folder (str): Output directory.
    
    Returns:
        str: Path to the saved metrics file.
    """
    ensure_output_dir(folder)
    path = os.path.join(folder, filename)
    with open(path, "w") as f:
        for k, v in metrics.items():
            f.write(f"{k}: {v}\n")
    return path

def summarize_dataframe(df: pd.DataFrame, n: int = 5) -> None:
    """Print a quick summary of a DataFrame for debugging."""
    print("Shape:", df.shape)
    print("Columns:", df.columns.tolist())
    print(df.head(n))
