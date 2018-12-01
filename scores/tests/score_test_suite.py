import unittest

# Test Modules
import test_scores_api

# Init test suite.
loader = unittest.TestLoader()
suite  = unittest.TestSuite()

# Add tests from test modules to the test suite.
suite.addTests(loader.loadTestsFromModule(test_scores_api))

# Init a test runner and run the test suite.
runner = unittest.TextTestRunner(verbosity=2)
result = runner.run(suite)
