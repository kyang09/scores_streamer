# Implement a dictionary system using LinkedList pointers to access each values in a table.
import json
class DataStore:
    # Using the Borg design pattern to keep state of database.
    # I thought to use this because we may need to expand on the db, and Borg allows subclassing of shared parent state.
    _shared_data_state = {}

    # Override __new__ to set our _shared_data_state as __dict___ for shared arbitrary attributes.
    # The *args and **kwargs params are for variable length non-keyworded and keyworded argument lists.
    def __new__(cls, *args, **kwargs):
        obj = super(DataStore, cls).__new__(cls)
        obj.__dict__ = DataStore._shared_data_state
        return obj
    
    # lookup_classes contains an array of classes used to query for data.
    def __init__(self, lookup_classes):
        self._storage = []
        self._lookup_classes = lookup_classes
        self._lookup_tbl = {}

        for lookup_class in self._lookup_classes:
            self._lookup_tbl[str(lookup_class.__name__)] = dict()


    def store(self, data):
        pass

    def get(self, lookup_class, id = -1): # id = -1 means to get all results of a lookup_class type.
        pass
