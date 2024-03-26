import unittest
import glob
import json
from JSONValidator import JSONValidator

VALID_TEST_PATH = "./testFiles/testTrue"
INVALID_TEST_PATH = "./testFiles/testFalse"

class JSONValidatorTest(unittest.TestCase):

    def get_paths(self, path):
       return glob.glob(path + "/*.json") 

    def run_test_with_path(self, dir_path, expected):
        """
        In validateResource(data) passes a path to a file
        """
        paths = self.get_paths(dir_path)
        for path in paths:
            res = JSONValidator.validate_resource(path, isPath=True)
            self.assertEqual(res, expected)
    
    def run_test_with_string(self, dir_path, expected):
        """
        In validateResource(data) passes a string containing the contents of the file
        """
        paths = self.get_paths(dir_path)
        for path in paths:
            with open(path) as f:
                res = JSONValidator.validate_resource(f.read())
                self.assertEqual(res, expected)
    
    def run_test_with_json(self, dir_path, expected):
        """
        In validateResource(data) passes an object containing json from the file
        """
        paths = self.get_paths(dir_path)
        for path in paths:
            with open(path) as f:
                res = JSONValidator.validate_resource(json.load(f))
                self.assertEqual(res, expected)

    def test_true_with_path(self):
        self.run_test_with_path(VALID_TEST_PATH, True)

    def test_false_with_path(self):
        self.run_test_with_path(INVALID_TEST_PATH, False)
    
    def test_true_with_string(self):
        self.run_test_with_string(VALID_TEST_PATH, True)

    def test_false_with_string(self):
        self.run_test_with_string(INVALID_TEST_PATH, False)
    
    def test_true_with_json(self):
        self.run_test_with_json(VALID_TEST_PATH, True)

    def test_false_with_json(self):
        self.run_test_with_json(INVALID_TEST_PATH, False)

if __name__ == '__main__':
    unittest.main()