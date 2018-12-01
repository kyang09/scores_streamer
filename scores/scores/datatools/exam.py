from .lookup_column import LookupColumn


class Exam(LookupColumn):
	
	def __init__(self, exam_id):
		# exam_id is a string.
		super(Exam, self).__init__(exam_id)
	