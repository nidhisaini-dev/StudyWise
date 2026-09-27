def allocate_study_hours(subjects, total_hours):
    total_priority = sum(subject["priority_score"] for subject in subjects)

    if total_priority == 0:
        return subjects

    for subject in subjects:
        subject["study_hours"] = round(
            (subject["priority_score"] / total_priority) * total_hours,
            2
        )

    return subjects