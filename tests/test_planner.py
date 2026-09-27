import unittest

from src.planner import allocate_study_hours


class TestPlanner(unittest.TestCase):

    def test_study_hour_allocation(self):
        subjects = [
            {"name": "Python", "priority_score": 60},
            {"name": "Maths", "priority_score": 30},
            {"name": "English", "priority_score": 10}
        ]

        result = allocate_study_hours(subjects, 10)

        self.assertEqual(result[0]["study_hours"], 6.0)
        self.assertEqual(result[1]["study_hours"], 3.0)
        self.assertEqual(result[2]["study_hours"], 1.0)


if __name__ == "__main__":
    unittest.main()