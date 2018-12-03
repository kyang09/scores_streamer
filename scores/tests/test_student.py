import unittest
from context import scores
from scores.datatools.student import Student


class TestStudent(unittest.TestCase):
    """Tests for Student."""

    def setUp(self):
        self.student = Student("some_student_id")

    def test_student_obj(self):
        self.assertTrue(len(self.student.get_db_indices()) == 0)
        self.student.add_db_index(1)
        self.assertTrue(len(self.student.get_db_indices()) == 1)
        self.student.add_db_index(2)
        self.assertTrue(len(self.student.get_db_indices()) == 2)

    def tearDown(self):
        del self.student
