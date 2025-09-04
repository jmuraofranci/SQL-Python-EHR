# Cancer Diagnosis & Treatment Outcomes Pipeline

This project demonstrates how to build an end-to-end data pipeline using SQL for database management and Python for analysis, visualization, and machine learning. The dataset contains 20,000 synthetic patient records** with demographic, diagnostic, treatment, and survival information.

---

## Dataset Overview

The dataset comes from Kaggle:
[EHR Dataset – Cancer Diagnosis Data](https://www.kaggle.com/datasets/gauravsrivastav2507/ehr-dataset?resource=download) by **Gaurav Srivastav**.

It includes the following columns:

| Column                  | Description                                          |
| ----------------------- | ---------------------------------------------------- |
| `Patient_ID`            | Unique identifier for each patient                   |
| `Age`                   | Age of the patient                                   |
| `Gender`                | Male / Female                                        |
| `Tumor_Size(cm)`        | Size of the tumor in centimeters                     |
| `Tumor_Type`            | Benign / Malignant                                   |
| `Biopsy_Result`         | Positive / Negative                                  |
| `Treatment`             | Type of treatment (Surgery, Radiation Therapy, etc.) |
| `Response_to_Treatment` | Complete / Partial / No Response                     |
| `Survival_Status`       | Survived / Deceased                                  |

---

## Project Workflow

### **1. Database (SQL)**

* Created a relational database (`patients` table).
* Loaded the dataset into the database.
* Wrote queries for:

  * Average tumor size by gender and age group.
  * Survival rates by treatment type.
  * Cross-tabulations of tumor type × biopsy result × survival.
  * Filtering malignant tumors > 5 cm with survival outcomes.

### **2. Python Integration**

* Connected to the SQL database using **SQLAlchemy + Pandas**.
* Performed **EDA (Exploratory Data Analysis)**:

  * Tumor size distributions.
  * Survival by age groups.
  * Heatmaps of treatment effectiveness.
* Built **ML models** (Logistic Regression, Random Forest) to predict:

  * **Target:** `Survival_Status`
  * **Features:** Age, Gender, Tumor Size, Tumor Type, Treatment
* Evaluated models with **Accuracy, ROC-AUC, Confusion Matrix**.

### **3. Visualization**

* **Matplotlib / Seaborn** for plots:

  * Tumor size histograms
  * Survival by treatment type
  * Response-to-treatment vs. survival heatmaps
* Optional **Streamlit dashboard** for interactive exploration.

---

## Example Insights

* Malignant tumors > 5 cm showed lower survival rates.
* Surgery combined with complete response yielded highest survival.
* Younger patients (<40) had significantly better outcomes compared to 60+.

---

## Repository Structure

```
├── data/
│   └── cancer_diagnosis_data.csv     # dataset (from Kaggle)
├── sql/
│   ├── schema.sql                    # create tables
│   └── queries.sql                   # example SQL queries
├── notebooks/
│   └── eda_and_modeling.ipynb        # Python analysis + ML
├── pipeline.py                        # Python-SQL pipeline script
└── README.md                          # project overview
```

---

## How to Run

### **Requirements**

* Python 3.9+
* MySQL/Postgres/SQLite
* Libraries: `pandas`, `sqlalchemy`, `matplotlib`, `seaborn`, `scikit-learn`, `streamlit`

### **Steps**

1. Clone this repo:

   ```bash
   git clone https://github.com/jmuraofranci/SQL-Python-EHR.git
   cd cancer-sql-python-pipeline
   ```
2. Set up the database:

   ```bash
   mysql -u root -p < sql/schema.sql
   ```
3. Load the dataset into SQL (`patients` table).
4. Run Python pipeline:

   ```bash
   python pipeline.py
   ```
5. (Optional) Launch dashboard:

   ```bash
   streamlit run dashboard.py
   ```

---

## Skills Demonstrated

* SQL: schema design, queries, aggregations, joins
* Python: Pandas, EDA, machine learning (classification)
* Visualization: Matplotlib, Seaborn
* Pipeline building: SQL ↔ Python integration
* Optional: Interactive dashboards with Streamlit

---

## Future Improvements

* Expand ML to multiclass prediction (`Response_to_Treatment`).
* Deploy pipeline in Docker.
* Add CI/CD with GitHub Actions.

