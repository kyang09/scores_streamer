import json


class MemoryStore:

    # I'm using the Borg design pattern to keep state of database.
    # I thought to use this because we may need to expand on the db,
    # and Borg allows subclassing of shared parent state.
    _shared_data_state = {}

    # Override __new__ to set our _shared_data_state as __dict___
    # for shared arbitrary attributes. The *args and **kwargs params
    # are for variable length non-keyworded and keyworded argument lists.
    def __new__(cls, *args, **kwargs):
        obj = super(MemoryStore, cls).__new__(cls)
        obj.__dict__ = MemoryStore._shared_data_state
        return obj

    def init(self, lookup_classes=[]):
        """
        Initializes the MemoryStore.

        :param lookup_classes: List of lookup classes for lookup table.
        """
        self._storage = []
        self._lookup_tbl = {}

        # List of tuples of (column name, class).
        self._lookup_classes = lookup_classes

        # Populate storage classes and attributes.
        for lookup_tup in self._lookup_classes:
            col_name = lookup_tup[0]
            class_name = lookup_tup[1].__name__
            if class_name in self._lookup_tbl:
                self._lookup_tbl[class_name][col_name] = dict()
            else:
                self._lookup_tbl[class_name] = {col_name: dict()}

    def store(self, data, data_format="json"):
        """
        Stores data into the MemoryStore storage.

        To avoid RuntimeError when there is an iteration happening
        through _storage or _lookup_tbl size increase, we can possibly
        look into using an Event flag or resource lock to switch between
        storing stream data in buffer arrays and dictionaries. Once the
        flag or lock allows storage into dictionaries again, make sure to
        store all the data in the buffer arrays into the dictionaries.
        For now, this function just copies the current .items() of
        dictionaries into a list for iteration to avoid RuntimeError.

        :param data: String format of data.
        :param data_format: Format option of the data. JSON by default.
        """
        if self._is_initialized():
            if data_format == "json":
                data_dict = json.loads(data)
                self._storage.append(data_dict)  # Store JSON row in storage.
                # colmap is a tuple of (column name, class).
                for lookup_tup in self._lookup_classes:
                    field_name = lookup_tup[0]
                    col_name = field_name
                    if not isinstance(field_name, str):
                        col_name = str(field_name)
                    class_name = lookup_tup[1].__name__
                    if col_name in data_dict:
                        data_identifier = data_dict[col_name]
                        data_class = lookup_tup[1]  # Class of data column.
                        self._update_lookup_tbl(class_name, col_name,
                                                data_identifier, data_class)

    def _update_lookup_tbl(self, class_name, col_name, data_identifier, data_class):
        """
        Updates _lookup_tbl by either creating or updating a lookup object.

        :param class_name: The class name to look up in the _lookup_tbl.
        :param col_name: Name of the field column in the datastore.
        :param data_identifier: Value that represents the object at a column.
        :param data_class: Class of the lookup data.
        """
        if not isinstance(data_identifier, str):
            data_identifier = str(data_identifier)
        # The reason for using data_identifier as the value is because
        # the values of each column can represent unique objects.
        if data_identifier in self._lookup_tbl[class_name][col_name]:
            obj = self._lookup_tbl[class_name][col_name][data_identifier]
            # If -1 index, nothing is in storage.
            obj.add_db_index(len(self._storage) - 1)
        else:
            obj = data_class(data_identifier)
            # If -1 index, nothing is in storage.
            obj.add_db_index(len(self._storage) - 1)
            self._lookup_tbl[class_name][col_name][data_identifier] = obj

    def get(self, lookup_class, col_name="", identifier=""):
        """
        Gets MemoryStore data from storage based on class and class attributes.

        :param lookup_class: The class to look up in the _lookup_tbl.
        :param col_name: Name of the field column in the datastore. Default is "".
        :param identifier: Value that represents the object at a column. Default is "".
        :returns: List of dictionary results.
        """
        if not self._is_initialized():
            return []

        if lookup_class.__name__ not in self._lookup_tbl:
            return []

        if identifier == "":
            if col_name == "":
                return self._get_all(lookup_class)
            else:
                return self._get_all_with_col(lookup_class, col_name)
        elif col_name == "":
            return self._get_all_with_id(lookup_class, identifier)

        # Get specific results based on col_name and identifier.
        return self._get_all_with_col_id(lookup_class, col_name, identifier)

    def _get_all(self, lookup_class):
        """
        Gets all MemoryStore data from storage based on class.

        :param lookup_class: The class to look up in the _lookup_tbl.
        :returns: List of dictionary results.
        """
        result = []
        class_dict = self._lookup_tbl[lookup_class.__name__]

        # We copy .items() to a list in order to avoid RuntimeError
        # when dictionary changes in size during an iteration.
        for col_name, data_id_dict in list(class_dict.items()):
            for data_id, data_obj in list(data_id_dict.items()):
                for ndx in data_obj.get_db_indices():
                    result.append(self._storage[ndx])
        return result

    def _get_all_with_col(self, lookup_class, col_name=""):
        """
        Gets MemoryStore data from storage based on class and column name.

        :param lookup_class: The class to look up in the _lookup_tbl.
        :param col_name: Name of the field column in the datastore. Default is "".
        :returns: List of dictionary results.
        """
        class_dict = self._lookup_tbl[lookup_class.__name__]
        if col_name not in class_dict:
            return []

        result = []
        if col_name != "":
            data_id_dict = class_dict[col_name]

            # We copy .items() to a list in order to avoid RuntimeError
            # when dictionary changes in size during an iteration.
            for data_id, data_obj in list(data_id_dict.items()):
                for ndx in data_obj.get_db_indices():
                    result.append(self._storage[ndx])
        return result

    def _get_all_with_id(self, lookup_class, identifier=""):
        """
        Gets MemoryStore data from storage based on class and column name.

        :param lookup_class: The class to look up in the _lookup_tbl.
        :param identifier: Value that represents the object at a column. Default is "".
        :returns: List of dictionary results.
        """
        result = []
        if identifier != "":
            class_dict = self._lookup_tbl[lookup_class.__name__]

            # We copy .items() to a list in order to avoid RuntimeError
            # when dictionary changes in size during an iteration.
            for col_name, data_id_dict in list(class_dict.items()):
                if identifier in data_id_dict:
                    data_obj = data_id_dict[identifier]
                    for ndx in data_obj.get_db_indices():
                        result.append(self._storage[ndx])
            return result

    def _get_all_with_col_id(self, lookup_class, col_name="", identifier=""):
        """
        Gets MemoryStore data from storage based on class, column name, and identifier.

        :param lookup_class: The class to look up in the _lookup_tbl.
        :param col_name: Name of the field column in the datastore. Default is "".
        :param identifier: Value that represents the object at a column. Default is "".
        :returns: List of dictionary results.
        """
        class_dict = self._lookup_tbl[lookup_class.__name__]
        if col_name not in class_dict or \
           identifier not in class_dict[col_name]:
                return []

        result = []
        if col_name != "" and identifier != "":
            data_obj = class_dict[col_name][identifier]
            for ndx in data_obj.get_db_indices():
                result.append(self._storage[ndx])
        return result

    def _is_initialized(self):
        if hasattr(self, "_storage") and \
           hasattr(self, "_lookup_tbl") and \
           hasattr(self, "_lookup_classes"):
            return True
        return False
