import pandas as pd

file_path = "academy_analytics_training_dataset.xlsx"

# Read the Excel workbook
excel_file = pd.ExcelFile(file_path)

print(excel_file.sheet_names)

# # Display available sheets
# print("Available sheets:")
# print(excel_file.sheet_names)

# # Read individual sheets
enrollments = pd.read_excel(
    file_path,
    sheet_name="Raw_Enrollments"
)

students = pd.read_excel(
    file_path,
    sheet_name="Students"
)

# print(type(students))

# students = pd.read_excel(
#     file_path,
#     sheet_name="Students"
# )

# courses = pd.read_excel(
#     file_path,
#     sheet_name="Courses"
# )

# engagement = pd.read_excel(
#     file_path,
#     sheet_name="Engagement"
# )

# print("\nEnrollment Data:")
# print(enrollments.head())