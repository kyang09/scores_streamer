from .stream.score_stream_thread import ScoreStreamThread
from .datatools.storage.memory_store import MemoryStore
from .datatools.student import Student
from .datatools.exam import Exam
from .datatools.storage.memstoretools import student_tools
from .datatools.storage.memstoretools import exam_tools


class ScoresApi:

    def __init__(self):
        self._stream_thread = None
        # Initializing MemoryStore should make it act like a singleton resource.
        self._db = MemoryStore()
        self._url = "http://live-test-scores.herokuapp.com/scores"
        self._db.init([
            (student_tools.ID_FIELD_NAME, Student),
            (exam_tools.ID_FIELD_NAME, Exam)
        ])

    def start(self):
        """Starts streaming and processing scores data."""
        self._stream_thread = ScoreStreamThread(self._db, self._url)
        self._stream_thread.daemon = True
        self._stream_thread.start()

    def stop(self):
        """Stops streaming and processing scores data."""
        if self._stream_thread and self._stream_thread.isAlive():
            self._stream_thread.stop() # Set internal event flag to True to kill thread.
            self._stream_thread.join() # Make sure thread finishes before continuing with main thread.
    
    def list_students(self):
        """
        Lists all students that have received at least one test score.

        Results of [] means there were no results.

        :returns: Result list of all students that have received at least one test score.
        """
        return student_tools.get_students()

    def list_exams(self):
        """
        Lists all the exams that have been recorded.

        Results of [] means there were no results.

        :returns: Result list of all exams.
        """
        return exam_tools.get_exams()

    def student_results_and_average(self, student_id=""):
        """
        Lists the test results for the specified student,
        and provides the student's average score across all exams.

        Results of [] means there were no results.
        An average of -1.0 means there were no scores to average.

        :param student_id: str ID of student (given as a string).
        :returns: Tuple of (results, average)
        """
        return student_tools.get_results_average_by_studentid(student_id)

    def exam_results_and_average(self, exam_id=""):
        """
        Lists all the results for the specified exam, and 
        provides the average score across all students.

        Results of [] means there were no results.
        An average of -1.0 means there were no scores to average.

        :param exam_id: int ID of student (given as a string).
        :returns: Tuple of (results, average)
        """
        return exam_tools.get_results_average_by_examid(exam_id)
