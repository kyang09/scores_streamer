import unittest
from context import scores
from scores.datatools.storage.memory_store import MemoryStore
from scores.datatools.student import Student
from scores.datatools.exam import Exam
from scores.datatools.storage.memstoretools import student_tools
from scores.datatools.storage.memstoretools import exam_tools


class TestStudentTools(unittest.TestCase):
    """Tests for Student Tools."""

    def setUp(self):
        self.db = MemoryStore()
        self.db.init([
            (student_tools.ID_FIELD_NAME, Student),
            (exam_tools.ID_FIELD_NAME, Exam)
        ])

    def test_get_students(self):
        self.assertTrue(len(student_tools.get_students()) == 0)
        data = '{"exam" : 999, "studentId": "some_student_id", "score": 0.132}'
        data2 = '{"exam" : 999, "studentId": "some_student_id2", "score": 0.523}'
        self.db.store(data)
        self.db.store(data2)
        self.assertTrue(len(student_tools.get_students()) > 0)
        students = student_tools.get_students()
        students.sort()
        self.assertTrue(["some_student_id", "some_student_id2"] == students)

    def test_get_results_by_studentid(self):
        results = student_tools.get_results_by_studentid("some_student_id")
        self.assertTrue(len(results) == 0)
        data = '{"studentId":"some_student_id","exam":999,"score":0.6488820932488337}'
        self.db.store(data)
        results = student_tools.get_results_by_studentid("some_student_id")
        self.assertTrue(len(results) > 0)

    def test_get_average_by_studentid(self):
        average = student_tools.get_average_by_studentid("some_student_id")
        self.assertTrue(average == -1.0)
        data = '{"studentId":"some_student_id","exam":999,"score":0.123}'
        self.db.store(data)
        average = student_tools.get_average_by_studentid("some_student_id")
        self.assertTrue(average != -1.0)
        self.assertTrue(average == 0.123)
        data2 = '{"studentId":"some_student_id","exam":1000,"score":0.421}'
        self.db.store(data2)
        average = student_tools.get_average_by_studentid("some_student_id")
        self.assertTrue(average != -1.0)
        self.assertTrue(average == (0.123 + 0.421)/2.0)

    def test_get_results_average_by_studentid(self):
        results, average = student_tools.get_results_average_by_studentid("some_student_id")
        self.assertTrue(len(results) == 0)
        self.assertTrue(average == -1.0)
        data = '{"studentId":"some_student_id","exam":999,"score":0.123}'
        data2 = '{"studentId":"some_student_id","exam":1000,"score":0.421}'
        self.db.store(data)
        self.db.store(data2)
        results, average = student_tools.get_results_average_by_studentid("some_student_id")
        self.assertTrue(len(results) > 0)
        self.assertTrue(average != -1.0)
        self.assertTrue(average == (0.123 + 0.421)/2.0)

    def test_is_valid_student(self):
        row_dict = {"" : None}
        is_valid = student_tools.is_valid_student(row_dict)
        self.assertFalse(is_valid)
        row_dict = {student_tools.ID_FIELD_NAME : None}
        is_valid = student_tools.is_valid_student(row_dict)
        self.assertFalse(is_valid)
        row_dict = {student_tools.ID_FIELD_NAME : "some_student_id"}
        is_valid = student_tools.is_valid_student(row_dict)
        self.assertTrue(is_valid)

    def tearDown(self):
        del self.db._storage
        del self.db._lookup_tbl
        del self.db._lookup_classes
        del self.db
