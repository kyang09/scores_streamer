import os
import sys

# Set the absolute path to be the scores project directory.
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Import the scores package to give tests some context of where to look.
import scores