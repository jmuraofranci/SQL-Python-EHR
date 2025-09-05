-- 1. Average tumor size by gender
SELECT Gender, AVG(Tumor_Size_cm) AS avg_tumor_size
FROM patients
GROUP BY Gender;

-- 2. Average tumor size by age group
SELECT
    CASE
        WHEN Age < 30 THEN '<30'
        WHEN Age BETWEEN 30 AND 50 THEN '30-50'
        ELSE '50+'
    END AS age_group,
    AVG(Tumor_Size_cm) AS avg_tumor_size
FROM patients
GROUP BY age_group
ORDER BY age_group;

-- 3. Survival rate by treatment type
SELECT Treatment,
       ROUND(SUM(CASE WHEN Survival_Status = 'Survived' THEN 1 ELSE 0 END) * 1.0 / COUNT(*), 3) AS survival_rate
FROM patients
GROUP BY Treatment
ORDER BY survival_rate DESC;

-- 4. Cross-tabulation: tumor type × biopsy result × survival
SELECT Tumor_Type, Biopsy_Result, Survival_Status, COUNT(*) AS patient_count
FROM patients
GROUP BY Tumor_Type, Biopsy_Result, Survival_Status
ORDER BY Tumor_Type, Biopsy_Result, Survival_Status;

-- 5. Patients with malignant tumors > 5 cm who survived
SELECT Patient_ID, Age, Gender, Tumor_Size_cm, Treatment
FROM patients
WHERE Tumor_Type = 'Malignant'
  AND Tumor_Size_cm > 5
  AND Survival_Status = 'Survived'
ORDER BY Tumor_Size_cm DESC;

-- 6. Count of patients by treatment response
SELECT Response_to_Treatment, COUNT(*) AS patient_count
FROM patients
GROUP BY Response_to_Treatment
ORDER BY patient_count DESC;

-- 7. Gender distribution among survivors vs. deceased
SELECT Gender, Survival_Status, COUNT(*) AS count
FROM patients
GROUP BY Gender, Survival_Status
ORDER BY Gender, Survival_Status;
