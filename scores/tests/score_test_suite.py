import unittest

# Test Modules
import test_scores_api
import test_score_stream_thread
import test_memory_store
import test_lookup_column
import test_student
import test_exam
import test_student_tools
import test_exam_tools

# Init test suite.
loader = unittest.TestLoader()
suite = unittest.TestSuite()

# Add tests from test modules to the test suite.
suite.addTests(loader.loadTestsFromModule(test_scores_api))
suite.addTests(loader.loadTestsFromModule(test_score_stream_thread))
suite.addTests(loader.loadTestsFromModule(test_memory_store))
suite.addTests(loader.loadTestsFromModule(test_lookup_column))
suite.addTests(loader.loadTestsFromModule(test_student))
suite.addTests(loader.loadTestsFromModule(test_exam))
suite.addTests(loader.loadTestsFromModule(test_student_tools))
suite.addTests(loader.loadTestsFromModule(test_exam_tools))

# Init a test runner.
runner = unittest.TextTestRunner(verbosity=2)

# Warning about possible long testing wait time.
print("\n======================================================================")
print("WARNING: These tests may take a while due to data streaming!")
print("----------------------------------------------------------------------\n")

# Run the test suite.
result = runner.run(suite)
