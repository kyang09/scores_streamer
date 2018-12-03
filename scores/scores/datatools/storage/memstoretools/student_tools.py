# Module for processing student data.

from ...student import Student
from ..memory_store import MemoryStore
from . import exam_tools


ID_FIELD_NAME = "studentId"


def get_students():
    """
    Gets the results of students with at least one exam score.

    :returns: String List of student IDs.
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


def get_results_by_studentid(student_id):
    """
    Gets the results of student of student_id.

    :param student_id: ID of student.
    :returns: String List of results.
    """
    memstore = MemoryStore()
    return memstore.get(Student, ID_FIELD_NAME, student_id)


def get_average_by_studentid(student_id):
    """
    Gets the test score average of student of student_id.

    :param student_id: ID of student.
    :returns: Float value of average.
    """
    average = -1.0 # Average of -1.0 means student doesn't have any scores.
    scores = []
    memstore = MemoryStore()
    results = memstore.get(Student, ID_FIELD_NAME, student_id)
    for row_dict in results:
        scores.append(row_dict["score"])  # score is a decimal value.
    if len(scores) > 0:
        average = sum(scores)/len(scores)
    return average


def get_results_average_by_studentid(student_id):
    """
    Gets test results and test score average of student of student_id.

    :param student_id: ID of student.
    :returns: Tuple of (string results list, float average)
    """
    average = -1.0 # Average of -1.0 means student doesn't have any scores.
    scores = []
    memstore = MemoryStore()
    results = memstore.get(Student, ID_FIELD_NAME, student_id)
    for row_dict in results:
        scores.append(row_dict["score"])  # score is a decimal value.
    if len(scores) > 0:
        average = sum(scores)/len(scores)
    return (results, average)


def is_valid_student(row_dict):
    """
    Checks if a row in the datastore has valid student identifiers.

    :param row_dict: Row in the datastore represented as a dictionary.
    :returns: Boolean True or False.
    """
    if ID_FIELD_NAME not in row_dict or row_dict[ID_FIELD_NAME] == None:
        return False
    if not isinstance(row_dict[ID_FIELD_NAME], str):
        return False
    return True
