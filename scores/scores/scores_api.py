from .stream.score_stream_thread import ScoreStreamThread
from .datatools.storage.memory_store import MemoryStore
from .datatools.studentpkg.student import Student
from .datatools.exampkg.exam import Exam
from .datatools.studentpkg import student_tools
from .datatools.exampkg import exam_tools


class ScoresApi:

    def __init__(self):
        self._stream_thread = None
        # Initializing MemoryStore should make it act like a singleton resource.
        self._db = MemoryStore()
        self._url = "http://live-test-scores.herokuapp.com/scores"
        self._db.init([("studentId", Student), ("exam", Exam)])

    def start(self):
        """Starts streaming and processing scores data."""
        self._stream_thread = ScoreStreamThread(self._db, self._url)
        self._stream_thread.daemon = True
        self._stream_thread.start()
        print("started")

    def stop(self):
        """Stops streaming and processing scores data."""
        if self._stream_thread:
            self._stream_thread.stop() # Set internal event flag to True to kill thread.
            self._stream_thread.join() # Make sure thread finishes before continuing with main thread.
        print("stopped")
    
    def list_students(self):
        """
        Lists all students that have received at least one test score.

        :returns: Result of all students that have received at least one test score.
        """
        return student_tools.get_students()

    def list_exams(self):
        """
        Lists all the exams that have been recorded.

        :returns: Result of all exams.
        """
        pass

    def student_results_and_average(self, student_id):
        """
        Lists the test results for the specified student,
        and provides the student's average score across all exams.

        :param student_id: str ID of student (given as a string).
        :returns: Tuple of (results, average)
        """
        pass

    def exam_results_and_average(self, exam_id):
        """
        Lists all the results for the specified exam, and 
        provides the average score across all students.

        :param exam_id: int ID of student (given as a string).
        :returns: Tuple of (results, average)
        """
        pass
