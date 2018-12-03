import unittest
import json
from context import scores
from scores.stream.score_stream_thread import ScoreStreamThread
from scores.datatools.storage.memory_store import MemoryStore
from scores.datatools.student import Student
from scores.datatools.exam import Exam
from scores.datatools.storage.memstoretools import student_tools
from scores.datatools.storage.memstoretools import exam_tools


class TestMemoryStore(unittest.TestCase):
    """Tests for MemoryStore."""

    def setUp(self):
        self.db = MemoryStore()

    def test_db_init(self):
        self.assertFalse(hasattr(self.db, "_storage"))
        self.assertFalse(hasattr(self.db, "_lookup_tbl"))
        self.assertFalse(hasattr(self.db, "_lookup_classes"))
        self.db.init([
            (student_tools.ID_FIELD_NAME, Student),
            (exam_tools.ID_FIELD_NAME, Exam)
        ])
        self.assertTrue(hasattr(self.db, "_storage"))
        self.assertTrue(hasattr(self.db, "_lookup_tbl"))
        self.assertTrue(hasattr(self.db, "_lookup_classes"))

    def test_db_store(self):
        self.db.init([
            (student_tools.ID_FIELD_NAME, Student),
            (exam_tools.ID_FIELD_NAME, Exam)
        ])
        data = '{"exam" : 999, "studentId": "some_student_id", "score": 0.132}'
        self.assertTrue(len(self.db._storage) == 0)
        self.db.store(data)
        self.assertTrue(len(self.db._storage) == 1)
        self.assertTrue(len(self.db._lookup_tbl) > 0)
        data_from_db = self.db._storage[0]
        self.assertTrue(data_from_db == json.loads(data))

    def test_db_get_all(self):
        self.db.init([
            (student_tools.ID_FIELD_NAME, Student),
            (exam_tools.ID_FIELD_NAME, Exam)
        ])
        data = '{"studentId":"some_student_id","exam":999,"score":0.648}'
        self.assertTrue(len(self.db._storage) == 0)
        self.db.store(data)
        self.assertTrue(len(self.db._storage) == 1)
        students_from_db = self.db.get(Student)
        self.assertTrue(len(students_from_db) == 1)
        exams_from_db = self.db.get(Exam)
        self.assertTrue(len(exams_from_db) == 1)
        self.assertTrue(students_from_db[0]["studentId"] == "some_student_id")
        self.assertTrue(exams_from_db[0]["exam"] == 999)
        self.assertTrue(students_from_db[0]["score"] == 0.648)
        self.assertTrue(exams_from_db[0]["score"] == 0.648)

        data2 = '{"studentId":"some_student_id2","exam":123,"score":0.148}'
        self.assertTrue(len(self.db._storage) == 1)
        self.db.store(data2)
        self.assertTrue(len(self.db._storage) == 2)
        students_from_db = self.db.get(Student)
        self.assertTrue(len(students_from_db) == 2)
        exams_from_db = self.db.get(Exam)
        self.assertTrue(len(exams_from_db) == 2)
        self.assertTrue(students_from_db[0]["studentId"] == "some_student_id")
        self.assertTrue(exams_from_db[0]["exam"] == 999)
        self.assertTrue(students_from_db[0]["score"] == 0.648)
        self.assertTrue(exams_from_db[0]["score"] == 0.648)
        self.assertTrue(students_from_db[1]["studentId"] == "some_student_id2")
        self.assertTrue(exams_from_db[1]["exam"] == 123)
        self.assertTrue(students_from_db[1]["score"] == 0.148)
        self.assertTrue(exams_from_db[1]["score"] == 0.148)

    def test_db_get_specific(self):
        self.db.init([
            (student_tools.ID_FIELD_NAME, Student),
            (exam_tools.ID_FIELD_NAME, Exam)
        ])
        data = '{"exam" : 999, "studentId": "some_student_id", "score": 0.132}'
        self.assertTrue(len(self.db._storage) == 0)
        self.db.store(data)
        self.assertTrue(len(self.db._storage) == 1)
        student_results = self.db.get(Student, student_tools.ID_FIELD_NAME,
                                      "some_student_id")
        self.assertTrue(len(student_results) == 1)
        exam_results = self.db.get(Exam, exam_tools.ID_FIELD_NAME, "999")
        self.assertTrue(len(exam_results) == 1)
        self.assertTrue(student_results[0]["studentId"] == "some_student_id")
        self.assertTrue(student_results[0]["exam"] == 999)
        self.assertTrue(student_results[0]["score"] == 0.132)
        self.assertTrue(exam_results[0]["studentId"] == "some_student_id")
        self.assertTrue(exam_results[0]["exam"] == 999)
        self.assertTrue(exam_results[0]["score"] == 0.132)

    def tearDown(self):
        del self.db._storage
        del self.db._lookup_tbl
        del self.db._lookup_classes
        del self.db
