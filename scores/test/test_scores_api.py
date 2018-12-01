import unittest
from .scores.scores_api import ScoresApi
from .scores.stream.score_stream_thread import ScoreStreamThread


class TestScoresApi(unittest.TestCase):

    def setUp(self):
    	self.api = ScoresApi()

    def test_start(self):
        self.assertEqual(api._stream_thread, None)
        self.assertEqual(api._db._storage , [])
        self.assertNotEqual(api._db._lookup_classes, [])
        self.assertTrue(len(api._db._lookup_tbl) > 0)
        self.api.start()
        self.assertNotEqual(api._stream_thread, None)
        self.assertTrue(isinstance(api._stream_thread, ScoreStreamThread))
        self.assertTrue(api._stream_thread.daemon)
        self.assertTrue(api._stream_thread.isAlive())

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