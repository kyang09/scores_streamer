# Module for processing exam data.

from ...exam import Exam
from ..memory_store import MemoryStore


ID_FIELD_NAME = "exam"
SCORE_FIELD_NAME = "score"


def get_exams():
    memstore = MemoryStore()
    results = memstore.get(Student)

def get_results_by_examid():
    pass


def get_average_by_examid():
    pass


def get_results_average_by_examid():
    pass


def is_valid_exam(row_dict):
     """
    Checks if a row in the datastore has valid exam identifiers.

    :param row_dict: Row in the datastore represented as a dictionary.
    :returns: Boolean True or False.
    """
    if "exam" not in row_dict or row_dict[ID_FIELD_NAME] == None:
        return False
    if not isinstance(row_dict[ID_FIELD_NAME], int):
        return False
    return True


def is_valid_exam_score(row_dict):
    """
    Checks if a row in the datastore has valid exam score identifiers.

    :param row_dict: Row in the datastore represented as a dictionary.
    :returns: Boolean True or False.
    """
    if "score" not in row_dict or row_dict[SCORE_FIELD_NAME] == None:
        return False
    if not isinstance(row_dict[SCORE_FIELD_NAME], float):
        return False
    return True
