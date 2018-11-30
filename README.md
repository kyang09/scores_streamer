First, make sure you install Python 3:
    https://www.python.org/downloads

If successful or present, you should either be able to enter the Python shell in the commandline like this:
    On Windows:
        py -3
    On Mac/Linus:
        python3

Install pip if you haven't done so already:
    On Windows:
        py -3 get_pip.py
    On Mac/Linux:
        python3 get_pip.py

To check if pip is installed correctly, open the Python 3 shell:
    On Windows:
        py -3
    On Mac/Linus:
        python3

Type in:
    import pip

If installed correctly, there should be no error.

Then, make sure to install all module requirements:
    On Windows:
        py -3 -m pip install -r requirements.txt
    On Mac/Linux:
        python3 -m pip install -r requirements.txt
