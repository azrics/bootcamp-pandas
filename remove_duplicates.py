# Business requirement: Find students enrolled in the same course more than once.
from main import enrollments

print(enrollments.duplicated(
        subset=["StudentID", "CourseID"],
        keep=False
    ))

duplicate_records = enrollments[
    enrollments.duplicated(
        subset=["StudentID", "CourseID"],
        keep=False
    )
]

print("\nDuplicate student-course combinations:")
print(duplicate_records)

