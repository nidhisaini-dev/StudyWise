def calculate_priority_score(performance_gap, attendance_risk, assessment_load):
    score = (
        0.50 * performance_gap
        + 0.20 * attendance_risk
        + 0.30 * assessment_load
    )

    return round(score, 2)

def classify_priority(score):
    if score >= 80:
        return "Critical"
    elif score >= 60:
        return "High"
    elif score >= 40:
        return "Medium"
    else:
        return "Low"