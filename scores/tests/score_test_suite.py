import unittest

# Test Modules
import test_scores_api

# Init test suite.
loader = unittest.TestLoader()
suite  = unittest.TestSuite()

# Add tests from test modules to the test suite.
suite.addTests(loader.loadTestsFromModule(test_scores_api))

# Init a test runner.
runner = unittest.TextTestRunner(verbosity=2)

# Warning about possible long testing wait time.
print("------------------------------------------------------------")
print("WARNING: These tests may take a while due to data streaming!")
print("------------------------------------------------------------")

# Run the test suite.
result = runner.run(suite)
