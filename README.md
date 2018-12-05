# Scores Streamer
This project contains a package project `scores` and a CLI tool that uses the `scores` package.

## Setup
First, make sure you install Python 3:  
    https://www.python.org/downloads  

**If successful or present, you should either be able to enter the Python shell in the command-line like this:**  
    On Windows:  
        `py -3`.  
    On Mac/Linux:  
        `python3`  

**Install pip if you haven't done so already:**  
    On Windows:  
        `py -3 get_pip.py`  
    On Mac/Linux:\
        `python3 get_pip.py`  

**To check if pip is installed correctly, open the Python 3 shell:**  
    On Windows:  
        `py -3`  
    On Mac/Linux:  
        `python3`  

Type in:  
    `import pip`  

If installed correctly, there should be no error.  

**Then, make sure to install all module requirements:**  
    On Windows:  
        `py -3 -m pip install -r requirements.txt`  
    On Mac/Linux:  
        `python3 -m pip install -r requirements.txt`  

## Starting the CLI
**To start the command-line tool to play with the Scores API, in the project root, run:**  
    On Windows:  
        `py -3 scores_cli.py`  
    On Mac/Linux:  
        `python3 scores_cli.py`  
**You may also run the tool with the option to start collecting data right away:**  
    On Windows:  
        `py -3 scores_cli.py start`  
    On Mac/Linux:  
        `python3 scores_cli.py start`

**Follow the instructions from the tool's menu. It should look something like this:**  
```
start : Start collecting scores data.

stop : Stop collecting scores data.  

list : Show list options.

list students : Lists all students that have received at 
least one test score.  

list student <student_id> : Lists the test results for the
student specified by student_id and provides the student's 
average score across all exams.  

list exams : Lists all the exams that have been recorded.  

list exam <exam_id> : Lists all the results for the exam 
specified by exam_id and provides the average score across 
all students.  

menu : Show the commands menu.  

quit : Exit the program.  
```
## Testing
The `scores` package project contains a `tests` directory.  
It contains API tests and module tests.  
For convenience, there is a provided test suite in the `tests` directory.  
**To run the test suite from the package project root:**  
On Windows:  
`py -3 tests/score_test_suite.py`  
On Mac/Linux:  
`python3 tests/score_test_suite.py`  
  
The tests may take a while to run due to the tests with streaming data.  

## Version
v0.1.0
