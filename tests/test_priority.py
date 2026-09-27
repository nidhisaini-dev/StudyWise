import unittest

from src.priority import (
    calculate_priority_score,
    classify_priority
)


class TestPriority(unittest.TestCase):

    def test_priority_score(self):
        self.assertEqual(
            calculate_priority_score(20, 10, 50),
            27
        )

    def test_critical_priority(self):
        self.assertEqual(classify_priority(90), "Critical")

    def test_high_priority(self):
        self.assertEqual(classify_priority(70), "High")

    def test_medium_priority(self):
        self.assertEqual(classify_priority(50), "Medium")

    def test_low_priority(self):
        self.assertEqual(classify_priority(20), "Low")


if __name__ == "__main__":
    unittest.main()