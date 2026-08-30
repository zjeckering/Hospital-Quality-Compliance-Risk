CREATE VIEW vw_Hospital_Dimension AS
SELECT 
    Facility_ID,
    Facility_Name,
    State,
    City_Town,
    Hospital_Type,
    Hospital_Ownership,
    Hospital_Overall_Rating,
    Emergency_Services
FROM Hospital_General_Information;