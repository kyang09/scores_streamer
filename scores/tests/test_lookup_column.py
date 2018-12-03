import unittest
from context import scores
from scores.datatools.lookup_column import LookupColumn


class TestLookupColumn(unittest.TestCase):
    """Tests for LookupColumn."""

    def setUp(self):
        self.lookup_col = LookupColumn("test")

    def test_lookup_column_obj(self):
        self.assertTrue(len(self.lookup_col.get_db_indices()) == 0)
        self.lookup_col.add_db_index(1)
        self.assertTrue(len(self.lookup_col.get_db_indices()) == 1)
        self.lookup_col.add_db_index(2)
        self.assertTrue(len(self.lookup_col.get_db_indices()) == 2)

    def tearDown(self):
        del self.lookup_col
