# StudyWise

Constraint-Based Academic Performance & Study Planner

## Overview

StudyWise is a Python-based academic planning system that analyzes:

- Student marks
- Attendance
- Assessment workload
- Available weekly study time

The system calculates a priority score for each subject and generates a personalized study plan based on the student's academic needs.

## Features

- Student profile management
- Secure password hashing
- Marks and performance analysis
- Attendance risk analysis
- Assessment workload tracking
- Subject priority calculation
- Personalized weekly study-hour allocation
- JSON-based data storage
- Input validation
- Automated unit testing
- Console-based academic report generation

## Project Structure

```text
StudyWise/
├── data/
│   ├── sample_data.json
│   ├── student_data.json
│   └── test_storage.json
├── src/
│   ├── main.py
│   ├── student.py
│   ├── validation.py
│   ├── academic.py
│   ├── attendance.py
│   ├── priority.py
│   ├── planner.py
│   ├── report.py
│   ├── security.py
│   └── storage.py
├── tests/
│   ├── test_validation.py
│   ├── test_academic.py
│   ├── test_attendance.py
│   ├── test_priority.py
│   └── test_planner.py
├── .gitignore
└── README.md
```

## How It Works

1. The student enters their profile details.
2. The system collects marks, attendance, and assessment workload for each subject.
3. Input values are validated.
4. The system calculates performance percentage and performance gap.
5. Attendance risk is calculated using the target attendance level.
6. A priority score is calculated for each subject.
7. Subjects are classified as Critical, High, Medium, or Low priority.
8. Available weekly study hours are distributed according to priority scores.
9. Student data and the generated study plan are saved in JSON format.
10. A final academic report is displayed in the console.

## Requirements

- Python 3.10 or higher
- VS Code or any Python-compatible editor
- Git (for version control)

No external Python packages are required to run the current version of StudyWise.

## Running the Project

1. Clone the repository.
2. Open the project folder in VS Code.
3. Create and activate a Python virtual environment.
4. Run the main application:

```bash
python src/main.py
```

5. Follow the instructions shown in the terminal.

## Testing

StudyWise uses Python's built-in `unittest` framework for automated testing.

Run all tests using:

```bash
python -m unittest discover -s tests
```

The test suite covers:

- Input validation
- Academic calculations
- Attendance risk calculation
- Priority score and classification
- Study-hour allocation

All automated tests currently pass successfully.

## Security Note

StudyWise uses password hashing so that the original password is not stored directly.

The current implementation uses Python's built-in SHA-256 hashing.

## Repository

The complete source code and project files are available on GitHub:

https://github.com/nidhisaini-dev/StudyWise

## Future Enhancements

Possible future improvements for StudyWise include:

- Graphical user interface (GUI)
- Database integration
- Improved password security using Argon2 or bcrypt



