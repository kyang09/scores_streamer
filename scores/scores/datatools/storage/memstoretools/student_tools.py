# Module for processing student data.

from ...student import Student
from ..memory_store import MemoryStore
from . import exam_tools


ID_FIELD_NAME = "studentId"


def get_students():
    """
    Get students with at least one exam score.

    :returns: Set of unqiue student IDs.
    """
    student_ids = set()  # unique set of student IDs.
    memstore = MemoryStore()
    results = memstore.get(Student)
    for row_dict in results:
        if is_valid_student(row_dict) and \
          exam_tools.is_valid_exam(row_dict) and \
          exam_tools.is_valid_exam_score(row_dict):
            student_ids.add(row_dict[ID_FIELD_NAME])
    return list(student_ids)


def get_results_by_studentid(lookup_class, id_col_name, student_id):
    return MemoryStore.get(Student, id_col_name, student_id)


def get_average_by_studentid(id_col_name, student_id):
    average = -1.0 # Average of -1.0 means student doesn't have any scores.
    scores = []
    results = MemoryStore.get(Student, id_col_name, student_id)
    for row_dict in results:
        scores.append(row_dict["score"])  # score is a decimal value.
    average = sum(scores)/len(scores)
    return average


def get_results_average_by_studentid(id_col_name, student_id):
    # TODO: Finish implementing.
    return MemoryStore.get(Student)


def is_valid_student(row_dict):
    """
    Checks if a row in the datastore has valid student identifiers.

    :param row_dict: Row in the datastore represented as a dictionary.
    :returns: Boolean True or False.
    """
    if ID_FIELD_NAME not in row_dict and row_dict[ID_FIELD_NAME] == None:
        return False
    if not isinstance(row_dict[ID_FIELD_NAME], str):
        return False
    return True
