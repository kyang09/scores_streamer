import unittest
import time
from context import scores
from scores.scores_api import ScoresApi
from scores.stream.score_stream_thread import ScoreStreamThread


class TestScoresApi(unittest.TestCase):
    """API tests for ScoresApi."""

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
        self.api.start()
        # Give the thread some time to fully start and collect data.
        time.sleep(5)
        self.api.stop()
        self.assertFalse(self.api._stream_thread.isAlive())

    def test_list_students_streaming(self):
        """
        Test list_students from ScoresApi during streaming.
        Requires internet connection.
        """
        print("WARNING: This test may take a while due to stream connection! ... ", end=' ', flush=True)
        self.assertEqual(self.api.list_students(), [])
        start_time = time.time()
        self.api.start()
        list_is_empty = False
        while len(self.api.list_students()) == 0:
            if time.time() - start_time > 15:
                list_is_empty = True # If it takes too long, fail the test.
        self.assertFalse(list_is_empty) # Check student list is non-empty.

    def test_list_students_streamstop(self):
        """
        Test list_students from ScoresApi after a stop.
        Requires internet connection. 
        """
        print("WARNING: This test may take a while due to stream connection! ... ", end=' ', flush=True)
        self.assertEqual(self.api.list_students(), [])
        start_time = time.time()
        self.api.start()
        list_is_empty = False
        while len(self.api.list_students()) == 0:
            if time.time() - start_time > 15:
                list_is_empty = True # If it takes too long, fail the test.
        self.assertFalse(list_is_empty) # Check student list is non-empty.
        self.api.stop()
        time.sleep(5) #  Give extra time in case api does not stop.
        # Check that list_students still works with stop() executed.
        self.assertTrue(len(self.api.list_students()) > 0)

    def test_list_exams(self):
        pass

    def test_student_results_and_average(self):
        pass

    def test_exam_results_and_average(self):
        pass

    def tearDown(self):
        self.api.stop()