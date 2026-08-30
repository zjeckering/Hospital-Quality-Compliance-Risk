CREATE VIEW vw_All_Measures AS
    -- COMPLICATIONS AND DEATHS
    SELECT 
        Facility_ID,
        CASE 
            WHEN Compared_to_National IN ('No Different Than the National Rate', 'No Different Than the National Value') THEN 'No Different than National'
            WHEN Compared_to_National IN ('Better Than the National Rate', 'Better Than the National Value') THEN 'Better than National'
            WHEN Compared_to_National IN ('Worse Than the National Rate', 'Worse Than the National Value') THEN 'Worse than National'
            ELSE 'Not Available'
        END AS Compared_to_National_Clean,
        Measure_ID,
        Measure_Name,
        Compared_to_National,
        Score,
        CASE
            WHEN Measure_ID = 'PSI_90' THEN 'Composite Ratio'
            WHEN Measure_ID LIKE 'PSI_%' THEN 'Rate per 1,000 Discharges'
            ELSE 'Rate (%)'
        END AS Score_unit,
        'Mortality/Complications' as Category
    FROM Complications_and_Deaths
    UNION ALL

    -- READMISSIONS
    SELECT 
        Facility_ID,
        CASE 
            WHEN Compared_to_National IN ('Better Than the National Rate', 'Fewer Days Than Average per 100 Discharges', 'Better than expected') THEN 'Better than National'
            WHEN Compared_to_National IN ('Worse Than the National Rate', 'More Days Than Average per 100 Discharges', 'Worse than expected') THEN 'Worse than National'
            WHEN Compared_to_National IN ('No Different Than the National Rate', 'Average Days per 100 Discharges', 'No Different than expected') THEN 'No Different than National'
            ELSE 'Not Available'
        END AS Compared_to_National_Clean,
        Measure_ID,
        Measure_Name,
        Compared_to_National,
        Score,
        CASE
            WHEN Measure_ID LIKE 'EDAC%' THEN 'Days per 100 Discharges'
            WHEN Measure_ID LIKE 'OP_%' THEN 'Rate/Ratio (Outpatient Procedure)'
            ELSE 'Rate (%)'
        END AS Score_Unit,
        'Readmissions' AS Category
    FROM Unplanned_Hospital_Visits
    UNION ALL

    -- INFECTIONS
    SELECT 
        Facility_ID,
        CASE 
            WHEN Compared_to_National = 'Better than the National Benchmark' THEN 'Better than National'
            WHEN Compared_to_National = 'Worse than the National Benchmark' THEN 'Worse than National'
            WHEN Compared_to_National = 'No Different than National Benchmark' THEN 'No Different than National'
            ELSE 'Not Available'
        END AS Compared_to_National_Clean,
        Measure_ID,
        Measure_Name,
        Compared_to_National,
        Score,
        'Standardized Infection Ratio' AS Score_Unit,
        'Infections' AS Category
    FROM Healthcare_Associated_Infections
    WHERE Measure_ID LIKE '%_SIR';