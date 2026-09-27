def calculate_percentage(marks):
    if not marks:
        return 0

    return sum(marks) / len(marks)


def calculate_performance_gap(percentage):
    return max(0, 100 - percentage)