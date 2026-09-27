def calculate_attendance_risk(attendance, target=75):
    return max(0, target - attendance)