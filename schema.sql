-- Create database (using MySQL/Postgres)
CREATE DATABASE cancer_db;
SHOW DATABASES;

-- Switch into the database
USE cancer_db;

-- Create patients table
CREATE TABLE patients (
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
