from ..lookup_column import LookupColumn


class Exam(LookupColumn):
	
	def __init__(self, exam_id):
		# exam_id is a string.
		self.id = exam_id
		self._db_indices = []
	