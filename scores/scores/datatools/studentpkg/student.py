from ..lookup_column import LookupColumn


class Student(LookupColumn):
	
    def __init__(self, student_id):
    	# student_id is a string.
        super(Student, self).__init__(student_id)
