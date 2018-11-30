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
        self._lookup_tbl = {}
        self._lookup_classes = lookup_classes # List of tuples of (column name, class).

        # Populate storage classes and attributes.
        for lookup_tup in self._lookup_classes:
            col_name = lookup_tup[0]
            class_name = lookup_tup[1].__name__
            if class_name in self._lookup_tbl:
                self._lookup_tbl[class_name][col_name] = dict()
            else:
                self._lookup_tbl[class_name] = {col_name : dict()}

    def store(self, data, data_format="json"):
        """
        Stores data into the DataStore storage.

        :param data: String format of data.
        :param data_format: Format option of the data. JSON by default.
        """
        if data_format == "json":
            data_dict = json.loads(data)
            self._storage.append(data_dict) # Store JSON row in storage.
            for lookup_tup in self._lookup_classes: # colmap is a tuple of (column name, class).
                col_name = lookup_tup[0]
                class_name = lookup_tup[1].__name__
                if col_name in data_dict:
                    data_identifier = data_dict[col_name]
                    data_class = lookup_tup[1] # Class of data column.
                    # The reason for using data_identifier as the value is because
                    # the values of each column can represent unique objects.
                    obj = data_class(data_identifier)
                    obj.add_db_index(len(self._storage) - 1) # If -1 index, nothing is in storage.
                    self._lookup_tbl[class_name][col_name][data_identifier] = data_class(data_identifier)

    def get(self, lookup_class, id=-1):
        """
        Get DataStore data from storage.

        :param lookup_class: The class to look up in the _lookup_tbl.
        :param id: int ID of the object to find. id=-1 to get all lookup_class objects.
        :returns: List of dictionary results.
        """
        pass
