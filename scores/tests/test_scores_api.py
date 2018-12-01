import unittest
from context import scores
from scores.scores_api import ScoresApi
from scores.stream.score_stream_thread import ScoreStreamThread


class TestScoresApi(unittest.TestCase):

    def setUp(self):
      self.api = ScoresApi()

    def test_start(self):
        self.assertEqual(self.api._stream_thread, None)
        self.assertEqual(self.api._db._storage , [])
        self.assertNotEqual(self.api._db._lookup_classes, [])
        self.assertTrue(len(self.api._db._lookup_tbl) > 0)
        self.api.start()
        self.assertNotEqual(self.api._stream_thread, None)
        self.assertTrue(isinstance(self.api._stream_thread, ScoreStreamThread))
        self.assertTrue(self.api._stream_thread.daemon)
        self.assertTrue(self.api._stream_thread.isAlive())

    def test_stop(self):
        pass

    def test_list_students(self):
      pass

    def test_list_exams(self):
      pass

    def test_student_results_and_average(self):
      pass

    def test_exam_results_and_average(self):
      pass

    def tearDown(self):
        self.api.stop()