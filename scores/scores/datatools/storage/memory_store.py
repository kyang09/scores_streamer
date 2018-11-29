# Implement a dictionary system using LinkedList pointers to access each values in a table.
import json
class DataStore:
	# Using the Borg design pattern to keep state of database.
	# I thought to use this because we may need to expand on the db, and Borg allows subclassing of shared parent state.
    _shared_data_state = {}

    def __new__(cls):
        obj = super(Borg, cls).__new__(cls)
        obj.__dict__ = Borg._shared_data_state
        return obj
	
	def __init__(self):
		self.db = []
		self.lookup_tbl = []

	def store(self, data):
		pass

	def get(self, ...):
		pass

