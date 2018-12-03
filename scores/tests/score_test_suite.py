import unittest

# Test Modules
import test_scores_api
import test_score_stream_thread
import test_memory_store

# Init test suite.
loader = unittest.TestLoader()
suite  = unittest.TestSuite()

# Add tests from test modules to the test suite.
#suite.addTest(test_scores_api.TestScoresApi('test_exam_results_and_average'))
suite.addTests(loader.loadTestsFromModule(test_scores_api))
suite.addTests(loader.loadTestsFromModule(test_score_stream_thread))
suite.addTests(loader.loadTestsFromModule(test_memory_store))

# Init a test runner.
runner = unittest.TextTestRunner(verbosity=2)

# Warning about possible long testing wait time.
print("\n======================================================================")
print("WARNING: These tests may take a while due to data streaming!")
print("----------------------------------------------------------------------\n")

# Run the test suite.
result = runner.run(suite)
