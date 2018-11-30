import json


class DataStore:
    # I'm using the Borg design pattern to keep state of database.
    # I thought to use this because we may need to expand on the db,
    # and Borg allows subclassing of shared parent state.
    _shared_data_state = {}

    # Override __new__ to set our _shared_data_state as __dict___
    # for shared arbitrary attributes. The *args and **kwargs params
    # are for variable length non-keyworded and keyworded argument lists.
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

    def store(self, data, data_format="json"):
        """Stores data into the DataStore storage.
        
        Parameters:
        data (str): String format of data.
        data_format (str): Format option of the data. JSON by default.
        """
        if data_format == "json":
            data_dict = json.loads(data)

    def get(self, lookup_class, id=-1):
        """Get DataStore data from storage.
        
        Parameters:
        lookup_class (class): The class to look up in the _lookup_tbl.
        id (int): ID of the object to find.
            Default of -1 gets all lookup_class objects.
        
        Returns:
        tuple: Tuple of the _lookup_tbl result row.
        """
        pass
