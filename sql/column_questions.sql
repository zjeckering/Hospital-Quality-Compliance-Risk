SELECT TABLE_NAME, COLUMN_NAME, DATA_TYPE
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_SCHEMA = 'dbo'
ORDER BY TABLE_NAME, ORDINAL_POSITION;

SELECT 
    COUNT(*) AS total_rows,
    SUM(CASE WHEN Score = 'Not Available' THEN 1 ELSE 0 END) AS score_na,
    CAST(SUM(CASE WHEN Score = 'Not Available' THEN 1 ELSE 0 END) AS FLOAT) / COUNT(*) * 100 AS pct_score_na
FROM Complications_and_Deaths;

SELECT 
    COUNT(*) AS total_rows,
    SUM(CASE WHEN Score = 'Not Available' THEN 1 ELSE 0 END) AS score_na,
    CAST(SUM(CASE WHEN Score = 'Not Available' THEN 1 ELSE 0 END) AS FLOAT) / COUNT(*) * 100 AS pct_score_na
FROM Unplanned_Hospital_Visits;

SELECT 
    COUNT(*) AS total_rows,
    SUM(CASE WHEN Score = 'Not Available' THEN 1 ELSE 0 END) AS score_na,
    CAST(SUM(CASE WHEN Score = 'Not Available' THEN 1 ELSE 0 END) AS FLOAT) / COUNT(*) * 100 AS pct_score_na
FROM Healthcare_Associated_Infections;

SELECT DISTINCT Compared_to_national
FROM Healthcare_Associated_Infections;

SELECT DISTINCT Compared_to_national
FROM Unplanned_Hospital_Visits;

SELECT DISTINCT Compared_to_national
FROM Complications_and_Deaths;

SELECT DISTINCT Measure_ID, Measure_Name
FROM Unplanned_Hospital_Visits
ORDER BY Measure_ID;

SELECT DISTINCT Measure_ID, Measure_Name
FROM Healthcare_Associated_Infections
ORDER BY Measure_ID;

SELECT DISTINCT Measure_ID, Measure_Name
FROM Complications_and_Deaths
ORDER BY Measure_ID;

SELECT COUNT(*) AS total_rows
FROM Healthcare_Associated_Infections;

SELECT COUNT(*) AS sir_only_rows
FROM Healthcare_Associated_Infections
WHERE Measure_ID LIKE '%_SIR';

SELECT TOP 20 Facility_ID, Measure_ID, Measure_Name, Score, Compared_to_National
FROM Healthcare_Associated_Infections
WHERE Measure_ID LIKE '%_SIR'
ORDER BY Facility_ID, Measure_ID;

