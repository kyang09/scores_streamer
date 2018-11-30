from ..lookup_column import LookupColumn


class Student(LookupColumn):
	
    def __init__(self, student_id):
    	# student_id is a string.
        self.id = student_id
        self._db_indices = []
