class ScoresApi:
	# mode=0 is JSON. mode=1 is readable output.
	def __init__(self, mode=0):
		self.mode = mode

	# Starts streaming and processing scores data.
	def start():
		pass

	# Stops streaming and processing scores data.
	def stop():
		pass
	
	# Lists all students that have received at least one test score.
	def list_students():
		pass

	# Lists all the exams that have been recorded.
	def list_exams():
		pass

	# Lists the test results for the specified student, and provides the student's average score across all exams.
	def student_results_and_average():
		pass

	# Lists all the results for the specified exam, and provides the average score across all students.
	def exam_results_and_average():
		pass