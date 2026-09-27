def generate_report(student, subjects):
    print("\n===== StudyWise Report =====")
    print(f"Student: {student.name}")
    print(f"Roll Number: {student.roll_number}")

    print("\nStudy Plan:")
    for subject in subjects:
        print(
            f"{subject['name']} - "
            f"Priority: {subject['priority_score']} - "
            f"Study Hours: {subject['study_hours']}"
        )

    print("============================")