from .stream.score_stream_thread import ScoreStreamThread

class ScoresApi:
    # mode=0 is JSON. mode=1 is readable output.
    def __init__(self, mode=0):
        self._mode = mode
        self._stream_thread = None

    # Starts streaming and processing scores data.
    def start(self):
        if self._stream_thread:
            print(self._stream_thread._i)
        self._stream_thread = ScoreStreamThread()
        self._stream_thread.daemon = True
        self._stream_thread.start()

    # Stops streaming and processing scores data.
    def stop(self):
        self._stream_thread.stop() # Set internal event flag to True to kill thread.
        self._stream_thread.join() # Make sure thread finishes before continuing with main thread.
        if self._stream_thread:
            print(self._stream_thread._i)
    
    # Lists all students that have received at least one test score.
    def list_students(self):
        pass

    # Lists all the exams that have been recorded.
    def list_exams(self):
        pass

    # Lists the test results for the specified student, and provides the student's average score across all exams.
    def student_results_and_average(self, student_id):
        pass

    # Lists all the results for the specified exam, and provides the average score across all students.
    def exam_results_and_average(self, exam_id):
        pass