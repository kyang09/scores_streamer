# Module for processing student data.

from .datatools.storage.memory_store import MemoryStore
from .datatools.exampkg import exam_tools


ID_FIELD_NAME = "studentId"

def get_students(self, lookup_class):
    """
    Get students with at least one exam score.

    :param lookup_class: The class to look up in the _lookup_tbl.
    :returns: List of unqiue student IDs.
    """
    student_ids = {}  # unique set of student IDs.
    if lookup_class.__name__ == "Student":
        result = MemoryStore.get(lookup_class)
        for row_dict in result:
            if is_valid_student(row_dict) and \
              exam_tools.is_valid_exam(row_dict) and \
              exam_tools.is_valid_exam_score(row_dict):
                student_ids.add(row_dict[ID_FIELD_NAME])

    return []


def get_results_by_studentid(self, lookup_class, id_col_name, student_id):
    if lookup_class.__name__ == "Student":
        return MemoryStore.get(lookup_class, id_col_name, student_id)
    return []


def get_average_by_studentid(self, lookup_class, id_col_name, student_id):
    average = -1.0 # Average of -1.0 means student doesn't have any scores.
    scores = []
    if lookup_class.__name__ == "Student":
        results = MemoryStore.get(lookup_class, id_col_name, student_id)
        for row_dict in results:
            scores.append(row_dict["score"])  # score is a decimal value.
        average = sum(scores)/len(scores)
    return average


def get_results_average_by_studentid(self, lookup_class, id_col_name, student_id):
    if lookup_class.__name__ == "Student":
        # TODO: Finish implementing.
        return MemoryStore.get(lookup_class)
    return []

def is_valid_student(self, row_dict):
    return ID_FIELD_NAME in row_dict and row_dict[ID_FIELD_NAME] != None