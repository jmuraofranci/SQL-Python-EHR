import logging
import datetime
import os
from scripts.connect_db import load_data
from scripts.eda import run_eda
from scripts.modeling import run_model
from scripts.utils import summarize_dataframe

# Ensure outputs folder exists
os.makedirs("outputs", exist_ok=True)

# Create a unique log filename with timestamp
timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
log_filename = f"outputs/pipeline_log_{timestamp}.log"

# Configure logging
logging.basicConfig(
    filename=log_filename,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

def log_and_print(message: str, level: str = "info"):
    """Helper to log and print messages consistently."""
    if level == "info":
        logging.info(message)
    elif level == "error":
        logging.error(message)
    print(message)

def main():
    header = "=== Cancer Diagnosis & Treatment Outcomes Pipeline ==="
    log_and_print(header)
    log_and_print(f"Pipeline started at: {datetime.datetime.now()}")
    log_and_print(f"Logs are being saved to: {log_filename}")

    # Step 1: Load data
    log_and_print("\n=== Step 1: Loading data from MySQL ===")
    try:
        df = load_data()
        log_and_print(f"Data loaded successfully: {df.shape}")
        log_and_print("\nPreview of data:")
        summarize_dataframe(df)
    except Exception as e:
        log_and_print(f"Error loading data: {e}", level="error")
        return

    # Step 2: Run EDA
    log_and_print("\n=== Step 2: Running EDA ===")
    try:
        run_eda(df)
        log_and_print("EDA completed successfully.")
    except Exception as e:
        log_and_print(f"Error during EDA: {e}", level="error")
        return

    # Step 3: Run ML modeling
    log_and_print("\n=== Step 3: Running ML Modeling ===")
    try:
        run_model(df)
        log_and_print("Modeling completed successfully.")
    except Exception as e:
        log_and_print(f"Error during modeling: {e}", level="error")
        return

    footer = "=== Pipeline Completed Successfully ==="
    log_and_print(footer)
    log_and_print(f"Pipeline finished at: {datetime.datetime.now()}")

if __name__ == "__main__":
    main()
