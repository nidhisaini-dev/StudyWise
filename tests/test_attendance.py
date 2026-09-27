import unittest

from src.attendance import calculate_attendance_risk


class TestAttendance(unittest.TestCase):

    def test_low_attendance(self):
        self.assertEqual(calculate_attendance_risk(65), 10)

    def test_target_attendance(self):
        self.assertEqual(calculate_attendance_risk(75), 0)

    def test_high_attendance(self):
        self.assertEqual(calculate_attendance_risk(85), 0)


if __name__ == "__main__":
    unittest.main()