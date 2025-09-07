import os
import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv

# Load DB credentials from .env
load_dotenv()
DB_USER = os.getenv("DB_USER", "root")
DB_PASS = os.getenv("DB_PASS", "yourpassword")
DB_NAME = os.getenv("DB_NAME", "cancer_db")

# Connect to MySQL
@st.cache_data
def load_data():
    engine = create_engine(f"mysql+mysqlconnector://{DB_USER}:{DB_PASS}@localhost/{DB_NAME}")
    df = pd.read_sql("SELECT * FROM patients", engine)
    return df

df = load_data()

st.title(" Cancer Diagnosis & Treatment Outcomes Dashboard")

# Sidebar Filters
st.sidebar.header("Filters")

treatment_filter = st.sidebar.multiselect(
    "Select Treatment(s)",
    options=df["Treatment"].unique(),
    default=list(df["Treatment"].unique())
)

gender_filter = st.sidebar.multiselect(
    "Select Gender(s)",
    options=df["Gender"].unique(),
    default=list(df["Gender"].unique())
)

age_min, age_max = int(df["Age"].min()), int(df["Age"].max())
age_range = st.sidebar.slider(
    "Select Age Range",
    min_value=age_min,
    max_value=age_max,
    value=(age_min, age_max)
)

# Apply filters
filtered_df = df[
    (df["Treatment"].isin(treatment_filter)) &
    (df["Gender"].isin(gender_filter)) &
    (df["Age"].between(age_range[0], age_range[1]))
]

st.write(f"Showing **{len(filtered_df)}** patients after filters.")

# --- Survival Rate by Treatment ---
st.subheader("Survival Rate by Treatment")
survival_rate = (
    filtered_df.groupby("Treatment")["Survival_Status"]
    .apply(lambda x: (x == "Survived").mean())
    .reset_index(name="Survival Rate")
)
st.bar_chart(survival_rate.set_index("Treatment"))

# --- Tumor Size Distribution ---
st.subheader("Tumor Size Distribution")
st.histogram = st.bar_chart(filtered_df["Tumor_Size_cm"])

# --- Survival by Gender ---
st.subheader("Survival by Gender")
gender_survival = (
    filtered_df.groupby("Gender")["Survival_Status"]
    .apply(lambda x: (x == "Survived").mean())
    .reset_index(name="Survival Rate")
)
st.bar_chart(gender_survival.set_index("Gender"))
