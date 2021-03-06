import unittest
import time
from context import scores
from scores.scores_api import ScoresApi
from scores.stream.score_stream_thread import ScoreStreamThread


class TestScoresApi(unittest.TestCase):
    """API tests for ScoresApi."""

    def setUp(self):
        self.api = ScoresApi()
        self.max_wait_duration = 15  # Duration is in seconds.

    def test_start(self):
        self.assertEqual(self.api._stream_thread, None)
        self.assertEqual(self.api._db._storage, [])
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

    def test_list_students(self):
        """
        Test list_students from ScoresApi during streaming.
        Requires internet connection.
        """
        self.assertEqual(self.api.list_students(), [])
        start_time = time.time()
        self.api.start()
        duration_too_long = False
        while len(self.api.list_students()) == 0 and not duration_too_long:
            if time.time() - start_time > self.max_wait_duration:
                duration_too_long = True  # If it takes too long, fail.
        self.assertFalse(duration_too_long)

    def test_list_exams(self):
        self.assertEqual(self.api.list_exams(), [])
        start_time = time.time()
        self.api.start()
        duration_too_long = False
        while len(self.api.list_exams()) == 0 and not duration_too_long:
            if time.time() - start_time > self.max_wait_duration:
                duration_too_long = True  # If it takes too long, fail.
        self.assertFalse(duration_too_long)

    def test_student_results_and_average(self):
        self.assertEqual(self.api.student_results_and_average(""), ([], -1.0))
        start_time = time.time()
        self.api.start()
        duration_too_long = False
        while len(self.api.list_students()) == 0 and not duration_too_long:
            if time.time() - start_time > self.max_wait_duration:
                duration_too_long = True  # If it takes too long, fail.
        self.assertFalse(duration_too_long)
        students = self.api.list_students()
        for s in students:
            result = self.api.student_results_and_average(s)
            # Check results for the student isn't empty.
            self.assertTrue(len(result[0]) > 0)
            # Check that scores are used to get an average.
            self.assertTrue(result[1] != -1.0)

    def test_exam_results_and_average(self):
        self.assertEqual(self.api.exam_results_and_average(""), ([], -1.0))
        start_time = time.time()
        self.api.start()
        duration_too_long = False
        while len(self.api.list_exams()) == 0 and not duration_too_long:
            if time.time() - start_time > self.max_wait_duration:
                duration_too_long = True  # If it takes too long, fail.
        self.assertFalse(duration_too_long)
        exams = self.api.list_exams()
        for e in exams:
            result = self.api.exam_results_and_average(e)
            # Check results for the student isn't empty.
            self.assertTrue(len(result[0]) > 0)
            # Check that scores are used to get an average.
            self.assertTrue(result[1] != -1.0)

    def test_list_students_streamstop(self):
        """
        Test list_students from ScoresApi after a stop.
        Requires internet connection.
        """
        self.assertEqual(self.api.list_students(), [])
        start_time = time.time()
        self.api.start()
        duration_too_long = False
        while len(self.api.list_students()) == 0 and not duration_too_long:
            if time.time() - start_time > 15:
                duration_too_long = True  # If it takes too long, fail.
        self.assertFalse(duration_too_long)  # Check student list is non-empty.
        self.api.stop()
        self.assertTrue(len(self.api.list_students()) > 0)

    def tearDown(self):
        self.api.stop()
        del self.api
