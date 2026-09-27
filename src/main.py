from student import Student
from academic import calculate_percentage, calculate_performance_gap
from attendance import calculate_attendance_risk
from priority import calculate_priority_score, classify_priority
from planner import allocate_study_hours
from report import generate_report


def main():
    student = Student("Nidhi", "101", "hello123")

    marks = [65, 70, 60]
    attendance = 68
    assessment_load = 50
    total_study_hours = 10

    percentage = calculate_percentage(marks)
    performance_gap = calculate_performance_gap(percentage)
    attendance_risk = calculate_attendance_risk(attendance)

    priority_score = calculate_priority_score(
        performance_gap,
        attendance_risk,
        assessment_load
    )

    priority = classify_priority(priority_score)

    subjects = [
        {
            "name": "Python",
            "priority_score": priority_score
        }
    ]

    subjects = allocate_study_hours(subjects, total_study_hours)

    subjects[0]["priority"] = priority

    generate_report(student, subjects)


if __name__ == "__main__":
    main()