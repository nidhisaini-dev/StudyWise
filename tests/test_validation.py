import unittest

from src.validation import (
    validate_marks,
    validate_attendance,
    validate_study_hours,
    validate_assessment_load
)


class TestValidation(unittest.TestCase):

    def test_valid_marks(self):
        self.assertTrue(validate_marks(80))

    def test_invalid_marks(self):
        self.assertFalse(validate_marks(120))

    def test_valid_attendance(self):
        self.assertTrue(validate_attendance(75))

    def test_invalid_attendance(self):
        self.assertFalse(validate_attendance(120))

    def test_valid_study_hours(self):
        self.assertTrue(validate_study_hours(10))

    def test_invalid_study_hours(self):
        self.assertFalse(validate_study_hours(-5))

    def test_valid_assessment_load(self):
        self.assertTrue(validate_assessment_load(60))

    def test_invalid_assessment_load(self):
        self.assertFalse(validate_assessment_load(120))


if __name__ == "__main__":
    unittest.main()