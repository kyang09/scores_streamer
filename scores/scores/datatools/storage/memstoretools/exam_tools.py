# Module for processing exam data.

from ...exam import Exam
from ..memory_store import MemoryStore


ID_FIELD_NAME = "exam"
SCORE_FIELD_NAME = "score"


def get_exams():
    """
    Gets the results of all exams.

    :returns: String List of exam IDs.
    """
    exam_ids = set()
    memstore = MemoryStore()
    results = memstore.get(Exam)
    for row_dict in results:
        if is_valid_exam(row_dict):
            exam_ids.add(str(row_dict[ID_FIELD_NAME]))
    return list(exam_ids)

def get_results_by_examid(exam_id):
    """
    Gets the results of exams of exam_id.

    :param exam_id: ID of exam.
    :returns: String List of results.
    """
    memstore = MemoryStore()
    return memstore.get(Exam, ID_FIELD_NAME, exam_id)


def get_average_by_examid(exam_id):
    """
    Gets the test score average of exams of exam_id.

    :param exam_id: ID of exam.
    :returns: Float value of average.
    """
    average = -1.0 # Average of -1.0 means exam doesn't have any scores.
    scores = []
    memstore = MemoryStore()
    results = memstore.get(Exam, ID_FIELD_NAME, exam_id)
    for row_dict in results:
        scores.append(row_dict["score"])  # score is a decimal value.
    average = sum(scores)/len(scores)
    return average


def get_results_average_by_examid(exam_id):
    """
    Gets results and test score average of exams of exam_id.

    :param exam_id: ID of exam.
    :returns: Tuple of (string results list, float average)
    """
    average = -1.0 # Average of -1.0 means exam doesn't have any scores.
    scores = []
    memstore = MemoryStore()
    results = memstore.get(Exam, ID_FIELD_NAME, exam_id)
    for row_dict in results:
        scores.append(row_dict["score"])  # score is a decimal value.
    if len(scores) > 0:
        average = sum(scores)/len(scores)
    return (results, average)


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
