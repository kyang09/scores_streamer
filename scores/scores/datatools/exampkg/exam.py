from ..lookup_column import LookupColumn


class Exam(LookupColumn):
	
	def __init__(self, exam_id):
		self.id = exam_id
		self._db_indices = []
	