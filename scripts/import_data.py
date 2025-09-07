import os
import pandas as pd
from connect_db import get_engine

def import_data():
    """Import patients.csv into the patients table in MySQL."""
    # Build path relative to project root
    base_dir = os.path.dirname(os.path.dirname(__file__))  # go up from scripts/
    data_path = os.path.join(base_dir, "data", "cancer_diagnosis_data.csv")

    # Load dataset
    df = pd.read_csv(data_path)

    # 🔹 Fix column names to match MySQL schema
    df.rename(columns={"Tumor_Size(cm)": "Tumor_Size_cm"}, inplace=True)

    # Get DB engine
    engine = get_engine()

    # Insert into patients table
    df.to_sql("patients", con=engine, if_exists="replace", index=False)
    print("✅ Data imported successfully into patients table!")

if __name__ == "__main__":
    import_data()
