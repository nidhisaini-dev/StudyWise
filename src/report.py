def generate_report(student, subjects):
    print("\n===== StudyWise Report =====")
    print(f"Student: {student.name}")
    print(f"Roll Number: {student.roll_number}")

    print("\nStudy Plan:")

    for subject in subjects:
        print(f"\nSubject: {subject['name']}")
        print(f"Performance: {subject['percentage']:.2f}%")
        print(f"Attendance: {subject['attendance']:.2f}%")
        print(f"Assessment Load: {subject['assessment_load']:.2f}")
        print(f"Priority Score: {subject['priority_score']:.2f}")
        print(f"Priority Level: {subject['priority']}")
        print(f"Recommended Study Hours: {subject['study_hours']:.2f}")

    print("\n============================")