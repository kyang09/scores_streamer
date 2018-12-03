import unittest
from context import scores
from scores.datatools.storage.memory_store import MemoryStore
from scores.datatools.student import Student
from scores.datatools.exam import Exam
from scores.datatools.storage.memstoretools import student_tools
from scores.datatools.storage.memstoretools import exam_tools


class TestExamTools(unittest.TestCase):
    """Tests for Exam Tools."""

    def setUp(self):
        self.db = MemoryStore()
        self.db.init([
            (student_tools.ID_FIELD_NAME, Student),
            (exam_tools.ID_FIELD_NAME, Exam)
        ])

    def test_get_exams(self):
        self.assertTrue(len(exam_tools.get_exams()) == 0)
        data = '{"exam" : 999, "studentId": "id1", "score": 0.132}'
        data2 = '{"exam" : 1000, "studentId": "id2", "score": 0.523}'
        self.db.store(data)
        self.db.store(data2)
        self.assertTrue(len(exam_tools.get_exams()) > 0)
        exams = exam_tools.get_exams()
        exams.sort()
        self.assertTrue(['1000', '999'] == exams)

    def test_get_results_by_examid(self):
        results = exam_tools.get_results_by_examid("999")
        self.assertTrue(len(results) == 0)
        data = '{"studentId":"some_student_id","exam":999,"score":0.648}'
        self.db.store(data)
        results = exam_tools.get_results_by_examid("999")
        self.assertTrue(len(results) > 0)

    def test_get_average_by_examid(self):
        average = exam_tools.get_average_by_examid("999")
        self.assertTrue(average == -1.0)
        data = '{"studentId":"some_student_id","exam":999,"score":0.123}'
        self.db.store(data)
        average = exam_tools.get_average_by_examid("999")
        self.assertTrue(average != -1.0)
        self.assertTrue(average == 0.123)
        data2 = '{"studentId":"some_student_id2","exam":999,"score":0.421}'
        self.db.store(data2)
        average = exam_tools.get_average_by_examid("999")
        self.assertTrue(average != -1.0)
        self.assertTrue(average == (0.123 + 0.421)/2.0)

    def test_get_results_average_by_examid(self):
        results, average = exam_tools.get_results_average_by_examid("999")
        self.assertTrue(len(results) == 0)
        self.assertTrue(average == -1.0)
        data = '{"studentId":"some_student_id","exam":999,"score":0.123}'
        data2 = '{"studentId":"some_student_id2","exam":999,"score":0.421}'
        self.db.store(data)
        self.db.store(data2)
        results, average = exam_tools.get_results_average_by_examid("999")
        self.assertTrue(len(results) > 0)
        self.assertTrue(average != -1.0)
        self.assertTrue(average == (0.123 + 0.421)/2.0)

    def test_is_valid_exam(self):
        row_dict = {"": None}
        is_valid = exam_tools.is_valid_exam(row_dict)
        self.assertFalse(is_valid)
        row_dict = {exam_tools.ID_FIELD_NAME: None}
        is_valid = exam_tools.is_valid_exam(row_dict)
        self.assertFalse(is_valid)
        row_dict = {exam_tools.ID_FIELD_NAME: 999}
        is_valid = exam_tools.is_valid_exam(row_dict)
        self.assertTrue(is_valid)

    def test_is_valid_exam_score(self):
        row_dict = {"": None}
        is_valid = exam_tools.is_valid_exam_score(row_dict)
        self.assertFalse(is_valid)
        row_dict = {exam_tools.SCORE_FIELD_NAME: None}
        is_valid = exam_tools.is_valid_exam_score(row_dict)
        self.assertFalse(is_valid)
        row_dict = {exam_tools.SCORE_FIELD_NAME: 0.123}
        is_valid = exam_tools.is_valid_exam_score(row_dict)
        self.assertTrue(is_valid)

    def tearDown(self):
        del self.db._storage
        del self.db._lookup_tbl
        del self.db._lookup_classes
        del self.db
