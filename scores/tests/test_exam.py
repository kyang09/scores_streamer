import unittest
from context import scores
from scores.datatools.exam import Exam


class TestExam(unittest.TestCase):
    """Tests for Exam."""

    def setUp(self):
        self.exam = Exam("some_exam_id")

    def test_student_obj(self):
        self.assertTrue(len(self.exam.get_db_indices()) == 0)
        self.exam.add_db_index(1)
        self.assertTrue(len(self.exam.get_db_indices()) == 1)
        self.exam.add_db_index(2)
        self.assertTrue(len(self.exam.get_db_indices()) == 2)

    def tearDown(self):
        del self.exam
