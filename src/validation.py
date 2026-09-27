def validate_marks(marks):
    return 0 <= marks <= 100


def validate_attendance(attendance):
    return 0 <= attendance <= 100


def validate_study_hours(hours):
    return hours >= 0


def validate_assessment_load(load):
    return 0 <= load <= 100