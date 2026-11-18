# Insoect the columns
print(enrollments.columns)
print(students.columns)
print(courses.columns)

# Merge enrollments with students
enrollment_students = pd.merge(
    enrollments,
    students,
    on="StudentID",
    how="inner"
)



print(enrollment_students.head())


"""
enrollments	Left DataFrame
students	Right DataFrame
on="StudentID"	Common column used to match records
how="inner"	Keep only records with matching StudentIDs in both tables"""