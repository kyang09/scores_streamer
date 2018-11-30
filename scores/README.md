# Scores Package
This is a simple package that provides an API to stream and process data from a specified SSE (Server-Sent Events) stream.

# Contents
* `scores` is a package (not to be confused with the project name `scores`) containing subpackages of `stream` and `datatools` and an API file `scores_api.py` that uses the subpackages.
* `stream` is a subpackage of `scores` containing the module `score_stream_thread`. 
* `datatools` is a subpackage of `scores` containing three subpackages: `studentpkg`, `exampkg`, `storage`.
* `studentpkg`is a subpackage of `datatools` containing modules: `student_tools`, `student`.
* `exampkg` is a subpackage of `datatools` containing modules: `exam_tools`, `exam`.
* `storage` is a subpackage of `datatools` containing the module `memory_store`.