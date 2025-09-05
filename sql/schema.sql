-- 1. Create database (using MySQL or Postgres)
CREATE DATABASE cancer_db;

-- 2. Show databases
SHOW DATABASES;

-- 3. Create patients table
CREATE TABLE patients(
    Patient_ID VARCHAR(50) PRIMARY KEY,
    Age INT,
    Gender VARCHAR(10),
    Tumor_Size_cm FLOAT,
    Tumor_Type VARCHAR(20),
    Biopsy_Result VARCHAR(10),
    Treatment VARCHAR(50),
    Response_to_Treatment VARCHAR(20),
    Survival_Status VARCHAR(10)
);