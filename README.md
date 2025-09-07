# Cancer Diagnosis & Treatment Outcomes Pipeline

This project demonstrates how to build an end-to-end data pipeline using SQL for database management and Python for analysis, visualization, and machine learning. The dataset contains 20,000 synthetic patient records with demographic, diagnostic, treatment, and survival information.

---

## Dataset Overview

The dataset comes from Kaggle:
[EHR Dataset – Cancer Diagnosis Data](https://www.kaggle.com/datasets/gauravsrivastav2507/ehr-dataset?resource=download) by **Gaurav Srivastav**.

> **Note:** Download the dataset directly from Kaggle and place it inside the `data/` folder before running the pipeline.

It includes the following columns:

| Column                  | Description                                          |
| ----------------------- | ---------------------------------------------------- |
| `Patient_ID`            | Unique identifier for each patient (UUID string)     |
| `Age`                   | Age of the patient                                   |
| `Gender`                | Male / Female                                        |
| `Tumor_Size_cm`         | Size of the tumor in centimeters                     |
| `Tumor_Type`            | Benign / Malignant                                   |
| `Biopsy_Result`         | Positive / Negative                                  |
| `Treatment`             | Type of treatment (Surgery, Radiation Therapy, etc.) |
| `Response_to_Treatment` | Complete / Partial / No Response                     |
| `Survival_Status`       | Survived / Deceased                                  |

> The original dataset uses `Tumor_Size(cm)`. In this project, it was renamed to `Tumor_Size_cm` for compatibility with SQL databases.

---

## Project Workflow

### 1. Database (SQL)

* Created a relational database (`patients` table).
* Loaded the dataset into the database using Python (`scripts/import_data.py`).
* Wrote example queries (`queries.sql`) for:

  * Average tumor size by gender and age group
  * Survival rates by treatment type
  * Cross-tabulations of tumor type × biopsy result × survival
  * Filtering malignant tumors > 5 cm who survived

### 2. Python Integration

* Connected to the SQL database using **SQLAlchemy + Pandas**.
* Performed **EDA (Exploratory Data Analysis)**:

  * Tumor size distributions
  * Treatment × Response × Survival heatmaps
* Built **ML models** (Random Forest, Logistic Regression) to predict:

  * **Target:** `Survival_Status`
  * **Features:** Age, Gender, Tumor Size, Tumor Type, Treatment
* Evaluated with **Accuracy, ROC-AUC, Confusion Matrix**.

### 3. Visualization

* **Matplotlib / Seaborn** for plots:

  * Tumor size histograms
  * Treatment response × survival heatmaps

### 4. Dashboard

* Built a **Streamlit dashboard (`dashboard.py`)** to interactively explore survival outcomes with filters.

---

## Example Insights

* Malignant tumors > 5 cm showed lower survival rates.
* Surgery combined with complete response yielded highest survival.
* Younger patients (<40) had significantly better outcomes compared to 60+.

---

## Repository Structure

```
SQL-Python-EHR/
├── data/
│   └── .gitkeep                      # placeholder (dataset downloaded separately)
├── sql/
│   ├── schema.sql                    # create tables
│   └── queries.sql                   # example SQL queries
├── scripts/
│   ├── connect_db.py                 # SQL connection + data loading
│   ├── import_data.py                # load dataset into patients table
│   ├── eda.py                        # exploratory plots & descriptive analysis
│   ├── modeling.py                   # ML model training & evaluation
│   └── utils.py                      # helper functions
├── outputs/
│   ├── tumor_size_distribution.png   # histogram of tumor sizes
│   ├── treatment_response_survival.png # heatmap of treatment × response × survival
│   └── model_metrics.txt             # saved model results
├── .gitignore                        # ignores data, envs, caches
├── requirements.txt                  # Python dependencies
├── pipeline.py                       # orchestrates workflow
├── dashboard.py                      # Streamlit dashboard
└── README.md                         # project overview
```

---

## How to Run

### Requirements

* Python 3.9+
* MySQL (or Postgres/SQLite with small edits)
* Python libraries listed in `requirements.txt`

---

### 1. Create and Activate a Virtual Environment

```bash
# Create virtual environment
python -m venv .venv

# Activate (Mac/Linux)
source .venv/bin/activate

# Activate (Windows PowerShell)
.\.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

### 2. Create a `.env` File

Inside the project root, create a file called `.env`:

```env
DB_USER=root
DB_PASSWORD=yourpassword
DB_HOST=localhost
DB_NAME=cancer_db
```

This keeps sensitive credentials out of your code.
The scripts use `python-dotenv` to load these values automatically.

---

### 3. Steps to Run the Pipeline

1. **Clone this repo**

   ```bash
   git clone git@github.com:jmuraofranci/SQL-Python-EHR.git
   cd SQL-Python-EHR
   ```

2. **Download the dataset from Kaggle**
   [EHR Dataset – Cancer Diagnosis Data](https://www.kaggle.com/datasets/gauravsrivastav2507/ehr-dataset?resource=download)
   Place the file `cancer_diagnosis_data.csv` inside the `data/` folder.

3. **Set up the database**

   ```bash
   mysql -u root -p < sql/schema.sql
   ```

4. **Load the dataset into SQL**

   ```bash
   python scripts/import_data.py
   ```

5. **Run the example SQL queries**

   ```bash
   mysql -u root -p cancer_db < sql/queries.sql
   ```

6. **Run the Python pipeline**

   ```bash
   python pipeline.py
   ```

7. **Launch the Streamlit dashboard to visualize results**

   ```bash
   streamlit run dashboard.py
   ```

---

## Skills Demonstrated

* SQL: schema design, queries, aggregations, joins
* Python: Pandas, EDA, machine learning (classification)
* Visualization: Matplotlib, Seaborn
* Pipeline building: SQL ↔ Python integration
* Logging & reproducibility with `pipeline.py`
* Interactive dashboards with Streamlit
* Project reproducibility with `requirements.txt`, `.gitignore`, `.env`

---

## Future Improvements

* Add column sanitization step to handle special characters automatically.
* Expand ML to multiclass prediction (`Response_to_Treatment`).
* Deploy pipeline in Docker.
* Add CI/CD with GitHub Actions.
* Use Airflow/Prefect for orchestration.

---

## Troubleshooting

* **Error: `Unknown column 'Tumor_Size(cm)'`**
  → Ensure you’re using the renamed column `Tumor_Size_cm` in both SQL schema and Python code.

* **Error: `Access denied for user 'root'@'localhost'`**
  → Check your `.env` file (`DB_USER`, `DB_PASSWORD`, `DB_HOST`, `DB_NAME`) and ensure MySQL is running.

* **Error: `FileNotFoundError: data/cancer_diagnosis_data.csv`**
  → Make sure you downloaded the Kaggle dataset and placed it in the `data/` folder.

