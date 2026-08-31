import pandas as pd
from sqlalchemy import create_engine

# connect to sql server
engine = create_engine(
    "mssql+pyodbc://localhost\\SQLEXPRESS/TJC_Compliance"
    "?driver=ODBC+Driver+17+for+SQL+Server"
    "&trusted_connection=yes"
    "&TrustServerCertificate=yes"
)

# rename headers using custom mapping for renaming with pd

hospital_general_info_columns = {
    "Facility ID": "Facility_ID",
    "Facility Name": "Facility_Name",
    "Address": "Address",
    "City/Town": "City_Town",
    "State": "State",
    "ZIP Code": "ZIP_Code",
    "County/Parish": "County_Parish",
    "Telephone Number": "Telephone_Number",
    "Hospital Type": "Hospital_Type",
    "Hospital Ownership": "Hospital_Ownership",
    "Emergency Services": "Emergency_Services",
    "Meets criteria for birthing friendly designation": "Birthing_Friendly",
    "Hospital overall rating": "Hospital_Overall_Rating",
    "Hospital overall rating footnote": "Hospital_Overall_Rating_Footnote",
    "MORT Group Measure Count": "MORT_Group_Measure_Count",
    "Count of Facility MORT Measures": "Count_Facility_MORT_Measures",
    "Count of MORT Measures Better": "Count_MORT_Measures_Better",
    "Count of MORT Measures No Different": "Count_MORT_Measures_No_Different",
    "Count of MORT Measures Worse": "Count_MORT_Measures_Worse",
    "MORT Group Footnote": "MORT_Group_Footnote",
    "Safety Group Measure Count": "Safety_Group_Measure_Count",
    "Count of Facility Safety Measures": "Count_Facility_Safety_Measures",
    "Count of Safety Measures Better": "Count_Safety_Measures_Better",
    "Count of Safety Measures No Different": "Count_Safety_Measures_No_Different",
    "Count of Safety Measures Worse": "Count_Safety_Measures_Worse",
    "Safety Group Footnote": "Safety_Group_Footnote",
    "READM Group Measure Count": "READM_Group_Measure_Count",
    "Count of Facility READM Measures": "Count_Facility_READM_Measures",
    "Count of READM Measures Better": "Count_READM_Measures_Better",
    "Count of READM Measures No Different": "Count_READM_Measures_No_Different",
    "Count of READM Measures Worse": "Count_READM_Measures_Worse",
    "READM Group Footnote": "READM_Group_Footnote",
    "Pt Exp Group Measure Count": "Pt_Exp_Group_Measure_Count",
    "Count of Facility Pt Exp Measures": "Count_Facility_Pt_Exp_Measures",
    "Pt Exp Group Footnote": "Pt_Exp_Group_Footnote",
    "TE Group Measure Count": "TE_Group_Measure_Count",
    "Count of Facility TE Measures": "Count_Facility_TE_Measures",
    "TE Group Footnote": "TE_Group_Footnote",
}

complications_and_deaths_columns = {
    "Facility ID": "Facility_ID",
    "Facility Name": "Facility_Name",
    "Address": "Address",
    "City/Town": "City_Town",
    "State": "State",
    "ZIP Code": "ZIP_Code",
    "County/Parish": "County_Parish",
    "Telephone Number": "Telephone_Number",
    "Measure ID": "Measure_ID",
    "Measure Name": "Measure_Name",
    "Compared to National": "Compared_to_National",
    "Denominator": "Denominator",
    "Score": "Score",
    "Lower Estimate": "Lower_Estimate",
    "Higher Estimate": "Higher_Estimate",
    "Footnote": "Footnote",
    "Start Date": "Start_Date",
    "End Date": "End_Date",
}

unplanned_hospital_visits_columns = {
    "Facility ID": "Facility_ID",
    "Facility Name": "Facility_Name",
    "Address": "Address",
    "City/Town": "City_Town",
    "State": "State",
    "ZIP Code": "ZIP_Code",
    "County/Parish": "County_Parish",
    "Telephone Number": "Telephone_Number",
    "Measure ID": "Measure_ID",
    "Measure Name": "Measure_Name",
    "Compared to National": "Compared_to_National",
    "Denominator": "Denominator",
    "Score": "Score",
    "Lower Estimate": "Lower_Estimate",
    "Higher Estimate": "Higher_Estimate",
    "Number of Patients": "Number_of_Patients",
    "Number of Patients Returned": "Number_of_Patients_Returned",
    "Footnote": "Footnote",
    "Start Date": "Start_Date",
    "End Date": "End_Date",
}

healthcare_associated_infections_columns = {
    "Facility ID": "Facility_ID",
    "Facility Name": "Facility_Name",
    "Address": "Address",
    "City/Town": "City_Town",
    "State": "State",
    "ZIP Code": "ZIP_Code",
    "County/Parish": "County_Parish",
    "Telephone Number": "Telephone_Number",
    "Measure ID": "Measure_ID",
    "Measure Name": "Measure_Name",
    "Compared to National": "Compared_to_National",
    "Score": "Score",
    "Footnote": "Footnote",
    "Start Date": "Start_Date",
    "End Date": "End_Date",
}


load_plan = [
    {
        "csv": "data/Hospital_General_Information.csv",
        "table": "Hospital_General_Information",
        "rename_map": hospital_general_info_columns,
    },
    {
        "csv": "data/Complications_and_Deaths-Hospital.csv",
        "table": "Complications_and_Deaths",
        "rename_map": complications_and_deaths_columns,
    },
    {
        "csv": "data/Unplanned_Hospital_Visits-Hospital.csv",
        "table": "Unplanned_Hospital_Visits",
        "rename_map": unplanned_hospital_visits_columns,
    },
    {
        "csv": "data/Healthcare_Associated_Infections-Hospital.csv",
        "table": "Healthcare_Associated_Infections",
        "rename_map": healthcare_associated_infections_columns,
    },
]

# write to tables
for item in load_plan:
    csv_file = item["csv"]
    table_name = item["table"]
    rename_map = item["rename_map"]

    print(f"Loading {csv_file} -> {table_name} ...")

    # read everything as text
    df = pd.read_csv(csv_file, dtype=str)  

    # strip whitespace
    df.columns = df.columns.str.strip()

    # applyt renmaing
    df = df.rename(columns=rename_map)

    # flag columns that didnt get renamed
    unmapped = [c for c in df.columns if c not in rename_map.values()]
    if unmapped:
        print(f"unmapped columns found : {unmapped}")

    df.to_sql(table_name, engine, if_exists="append", index=False)

    print(f"Loaded {len(df)} rows into {table_name}")

print("All files loaded")