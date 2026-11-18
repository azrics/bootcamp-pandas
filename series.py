from main import enrollments
# # Display one column as a Series

student_ids = enrollments[[0]] # you nedd aframe nstead of series. expecitnf 



# print("\nStudent IDs:")
# print(student_ids)

# print("\nData type:")
# print(student_ids)
print(type(student_ids))


# # Display multiple columns as a DataFrame
# selected_columns = enrollments[
#     ["StudentID", "CourseID", "PaymentStatus"]
# ]

# print("\nSelected columns:")
# print(selected_columns.head())

# print("\nData type:")
# print(type(selected_columns))