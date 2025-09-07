import os
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv

def get_engine():
    """Return a SQLAlchemy engine using .env credentials."""
    load_dotenv()
    db_user = os.getenv("DB_USER")
    db_pass = os.getenv("DB_PASS")
    db_name = os.getenv("DB_NAME", "cancer_db")

    if not db_user or not db_pass:
        raise ValueError("DB_USER and DB_PASS must be set in the .env file")

    return create_engine(f"mysql+mysqlconnector://{db_user}:{db_pass}@localhost/{db_name}")

def load_data(table_name="patients"):
    """Load a table from the database into a pandas DataFrame."""
    engine = get_engine()
    return pd.read_sql(f"SELECT * FROM {table_name}", engine)
