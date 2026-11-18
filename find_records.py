from main import enrollments

# student_records = enrollments.loc[
#     enrollments[1] == "STU001"
# ]

# print("\nRecords belonging to STU001:")
# print(student_records)

# # specific columns retrieval
# student_records = enrollments.loc[
#     enrollments["StudentID"] == "STU001",
#     ["StudentID", "CourseID", "PaymentStatus"]
# ]

# print(student_records)

# # loc allows us to select rows using labels or conditions and columns using their names.
# # syntax: df.loc[row_condition, column_selection]

# # Find empty cells and rows
# # Business requirement: Identify enrolments with incomplete information.
# # Identify missing cells
# missing_cells = enrollments.isna()

# print("\nMissing cell indicators:")
# print(missing_cells.head())

# # Find rows containing at least one missing value
# missing_rows = enrollments[
#     enrollments.isna().any(axis=1)
# ]

# print("\nRows containing missing values:")
# print(missing_rows)

# # Find column containing empty cells
# # Check which columns contain missing values
# columns_with_missing = enrollments.isna().any()

# print("\nColumns containing missing values:")
# print(columns_with_missing)

# # Display only columns with missing values
# print("\nMissing column names:")
# print(columns_with_missing[columns_with_missing].index.tolist())

# """any() checks each column by default (axis=0).
# False means no missing value exists in that column.
# True means at least one missing value exists.
# .index.tolist() extracts the names of columns marked True."""

# # Count empty values
# # Count missing values in each column
# missing_count = enrollments.isna().sum()

# print("\nMissing values per column:")
# print(missing_count)

# # Count all missing cells in the dataset
# total_missing = enrollments.isna().sum().sum()

# print("\nTotal missing cells:", total_missing)

# """isna().sum() counts missing values in each column.

# isna().sum().sum() adds those column counts together to give the total number of missing cells."""

# # Drop rows and columns containing missing values
# # Experiment 1: Drop rows containing any missing value
# dropna_rows = enrollments.dropna(axis=0, how="any")

# print("\nAfter dropping rows:")
# print(dropna_rows.shape)


# # Experiment 2: Drop columns containing any missing value
# dropna_columns = enrollments.dropna(axis=1, how="any")

# print("\nAfter dropping columns:")
# print(dropna_columns.shape)

# # Fill missing values
# fillna_data = enrollments.copy()

# fillna_data["Campaign"] = fillna_data["Campaign"].fillna(
#     "Unattributed"
# )

# fillna_data["PaymentChannel"] = fillna_data["PaymentChannel"].fillna(
#     "Unknown"
# )

# print("\nAfter filling missing values:")
# print(fillna_data.isna().sum())

# """copy() creates a separate DataFrame.



# fillna() replaces missing values with the supplied value.



# We fill different columns with different values because they represent different business information.
# """

