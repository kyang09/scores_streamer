# Scores Package
This is a simple package that provides an API to stream and process data from a specified SSE (Server-Sent Events) stream.

# Contents
* `scores` is a package (not to be confused with the project name `scores`) containing subpackages of `stream` and `datatools` and an API file `scores_api.py` that uses the subpackages.
* `stream` is a subpackage of `scores` containing the module `score_stream_thread`. 
* `datatools` is a subpackage of `scores` containing three modules: `lookup_column`, `student`, `exam` and a subpackage `storage`.
* `storage` is a subpackage of `datatools` containing the module `memory_store` and a subpackage `memstoretools`.
* `memstoretools` is a subpackage of `storage` containing modules: `student_tools` and `exam_tools`.

# Tests
Tests are included in the `tests` directory.  
To run tests, you can run the test suite:  
On Windows:  
`py -3 tests/score_test_suite.py`  
On Mac/Linux:  
`python3 tests/score_test_suite.py`  
  
The tests may take a while to run due to the tests with streaming data.  

# Examples
## Initializing the API
```python
from scores.scores_api import ScoresApi

api = ScoresApi()

```

## API Usage
```python
api.list_students()  # Returns a list of student IDs.

api.list_exams()  # Returns a list of exam IDs.

student_id = "John_Doe"
api.student_results_and_average(student_id)  # Returns a tuple of (results, average)

exam_id = "102"
api.exam_results_and_average(exam_id)  # Returns a tuple of (results, average)
```