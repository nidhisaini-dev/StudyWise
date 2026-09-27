import unittest

from src.academic import (
    calculate_percentage,
    calculate_performance_gap
)


class TestAcademic(unittest.TestCase):

    def test_percentage(self):
        marks = [80, 70, 90]
        self.assertEqual(calculate_percentage(marks), 80)

    def test_empty_marks(self):
        self.assertEqual(calculate_percentage([]), 0)

    def test_performance_gap(self):
        self.assertEqual(calculate_performance_gap(80), 20)

    def test_no_performance_gap(self):
        self.assertEqual(calculate_performance_gap(100), 0)


if __name__ == "__main__":
    unittest.main()