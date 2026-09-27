from getpass import getpass

from student import Student
from academic import calculate_percentage, calculate_performance_gap
from attendance import calculate_attendance_risk
from priority import calculate_priority_score, classify_priority
from planner import allocate_study_hours
from report import generate_report
from storage import save_data

from validation import (
    validate_marks,
    validate_attendance,
    validate_assessment_load
)


def main():
    # Student details
    name = input("Enter your name: ")
    roll_number = input("Enter your roll number: ")
    password = getpass("Create your password: ")

    student = Student(name, roll_number, password)

    # Study plan details
    number_of_subjects = int(input("How many subjects? "))
    total_study_hours = float(
        input("Enter total study hours available per week: ")
    )

    # Validate study hours
    if total_study_hours < 0:
        print("Invalid study hours. Study hours cannot be negative.")
        return

    subjects = []

    # Take data for each subject
    for i in range(number_of_subjects):
        print(f"\nSubject {i + 1}")

        subject_name = input("Enter subject name: ")

        marks = [
            float(input("Enter marks 1: ")),
            float(input("Enter marks 2: ")),
            float(input("Enter marks 3: "))
        ]

        # Validate marks
        for mark in marks:
            if not validate_marks(mark):
                print("Invalid marks. Marks must be between 0 and 100.")
                return

        attendance = float(
            input("Enter attendance percentage: ")
        )

        # Validate attendance
        if not validate_attendance(attendance):
            print("Invalid attendance. It must be between 0 and 100.")
            return

        assessment_load = float(
            input("Enter assessment load (0-100): ")
        )

        # Validate assessment load
        if not validate_assessment_load(assessment_load):
            print(
                "Invalid assessment load. "
                "It must be between 0 and 100."
            )
            return

        # Academic calculations
        percentage = calculate_percentage(marks)
        performance_gap = calculate_performance_gap(percentage)

        # Attendance calculation
        attendance_risk = calculate_attendance_risk(attendance)

        # Priority calculation
        priority_score = calculate_priority_score(
            performance_gap,
            attendance_risk,
            assessment_load
        )

        priority = classify_priority(priority_score)

        # Store subject information
        subjects.append({
            "name": subject_name,
            "marks": marks,
            "percentage": percentage,
            "attendance": attendance,
            "assessment_load": assessment_load,
            "performance_gap": performance_gap,
            "attendance_risk": attendance_risk,
            "priority_score": priority_score,
            "priority": priority
        })

    # Allocate available study hours
    subjects = allocate_study_hours(
        subjects,
        total_study_hours
    )

    # Save student and study data
    study_data = {
        "student": {
            "name": student.name,
            "roll_number": student.roll_number
        },
        "subjects": subjects,
        "total_study_hours": total_study_hours
    }

    save_data(
        study_data,
        "data/student_data.json"
    )

    print("\nData saved successfully!")

    # Generate final report
    generate_report(student, subjects)


if __name__ == "__main__":
    main()