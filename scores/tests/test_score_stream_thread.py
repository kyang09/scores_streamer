import unittest
import time
from context import scores
from scores.stream.score_stream_thread import ScoreStreamThread
from scores.datatools.storage.memory_store import MemoryStore
from scores.datatools.student import Student
from scores.datatools.exam import Exam
from scores.datatools.storage.memstoretools import student_tools
from scores.datatools.storage.memstoretools import exam_tools


class TestScoreStreamThread(unittest.TestCase):
    """Tests for ScoreStreamThread."""

    def setUp(self):
        self.db = MemoryStore()
        self.db.init([
            (student_tools.ID_FIELD_NAME, Student),
            (exam_tools.ID_FIELD_NAME, Exam)
        ])
        self.url = "http://live-test-scores.herokuapp.com/scores"
        self.stream_thread = ScoreStreamThread(self.db, self.url)
        self.max_wait_duration = 15  # Duration is in seconds.

    def test_thread_start(self):
        self.assertFalse(self.stream_thread.isAlive())
        self.stream_thread.start()
        self.assertTrue(self.stream_thread.isAlive())

    def test_thread_stop(self):
        self.stream_thread.start()
        self.assertTrue(self.stream_thread.isAlive())

        start_time = time.time()
        self.stream_thread.stop()
        duration_too_long = False
        while self.stream_thread.isAlive() and not duration_too_long:
            if time.time() - start_time > self.max_wait_duration:
                duration_too_long = True  # If it takes too long, fail.
        self.assertFalse(duration_too_long)
        self.assertFalse(self.stream_thread.isAlive())

    def test_thread_is_storing(self):
        start_time = time.time()
        self.stream_thread.start()
        duration_too_long = False
        while len(self.db._storage) == 0 and not duration_too_long:
            if time.time() - start_time > self.max_wait_duration:
                duration_too_long = True  # If it takes too long, fail.
        self.assertFalse(duration_too_long)
        self.assertTrue(len(self.db._storage) > 0)

    def tearDown(self):
        self.stream_thread.stop()
        del self.db
        del self.stream_thread
