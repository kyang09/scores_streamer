class LookupColumn:

    def __init__(self, identifier):
        self.id = identifier  # String identifier of the lookup column.
        self._db_indices = []  # Indices to the datastore.

    def add_db_index(self, index):
        """
        Add an index to the _db_indices for datastore locations.

        :param index: Index to a location in the datastore.
        """
        self._db_indices.append(index)

    def get_db_indices(self):
        """Gets indices of LookupColumn object locations in the datastore."""
        return self._db_indices
