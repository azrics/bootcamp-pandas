import pandas as pd
from remove_duplicates import duplicate_records

# #DecisionMaking

# total_missing = enrollments.isna().sum().sum()

# if total_missing == 0:
#     print("Dataset is clean. Ready for analysis.")

# else:
#     print("Dataset contains missing values.")
#     print("Total missing cells:", total_missing)
#     print("Data cleaning is required.")

# # Write results into a new Excel
output_file = "academy_cleaning_results.xlsx"

with pd.ExcelWriter(output_file, engine="openpyxl") as writer:

#     # Original data
#     enrollments.to_excel(
#         writer,
#         sheet_name="Original_Data",
#         index=False
#     )

#     # Rows containing missing values
#     missing_rows.to_excel(
#         writer,
#         sheet_name="Missing_Rows",
#         index=False
#     )

#     # Drop rows experiment
#     dropna_rows.to_excel(
#         writer,
#         sheet_name="DropNA_Rows",
#         index=False
#     )

#     # Drop columns experiment
#     dropna_columns.to_excel(
#         writer,
#         sheet_name="DropNA_Columns",
#         index=False
#     )

#     # Fill missing values experiment
#     fillna_data.to_excel(
#         writer,
#         sheet_name="FillNA",
#         index=False
#     )

#     # Duplicate records
    duplicate_records.to_excel(
        writer,
        sheet_name="Duplicates",
        index=False
    )

#     # Unique enrolments
#     unique_enrollments.to_excel(
#         writer,
#         sheet_name="Unique_Enrollments",
#         index=False
#     )

# print("Excel results exported successfully!")