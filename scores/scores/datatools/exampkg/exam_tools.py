"""

Module for processing exam data.

"""


ID_FIELD_NAME = "exam"
SCORE_FIELD_NAME = "score"


def get_exams():
    pass


def get_results_by_examid():
    pass


def get_average_by_examid():
    pass


def get_results_average_by_examid():
    pass


def is_valid_exam(row_dict):
    if "exam" not in row_dict or row_dict[ID_FIELD_NAME] == None:
        return False
    if not instanceof(row_dict[ID_FIELD_NAME], int):
        return False
    return True


def is_valid_exam_score(row_dict):
    if "score" not in row_dict or row_dict[SCORE_FIELD_NAME] == None:
        return False
    if not instanceof(row_dict[SCORE_FIELD_NAME], float):
        return False
    return True
