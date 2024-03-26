import unittest
import glob
import json
from JSONValidator import JSONValidator

VALID_TEST_PATH = "./testFiles/testTrue"
INVALID_TEST_PATH = "./testFiles/testFalse"
BAD_FORMAT_TEST_PATH = "./testFiles/testInvalidFormat"

class JSONValidatorTest(unittest.TestCase):

    def assertValidationWithPath(self, path, expected, fn):
        try:
            res = fn(path)
            self.assertEqual(res, expected)
        except AssertionError as e:
            print(f"Error occured when testing {path}. Error message is: ")
            print(e)

    def get_paths(self, path):
       return glob.glob(path + "/*.json") 

    def run_test(self, dir_path, expected, fn):
        paths = self.get_paths(dir_path)
        for path in paths:
            self.assertValidationWithPath(path, expected, fn)

    def path_helper(self, path):
        """
        In validateResource(data) passes a path to a file
        """
        return JSONValidator.validate_resource(path, isPath=True)
    
    def string_helper(self, path):
        with open(path) as f:
            return JSONValidator.validate_resource(f.read())
    
    def json_helper(self, path):
        """
        In validateResource(data) passes an object containing json from the file
        """
        with open(path) as f:
            return JSONValidator.validate_resource(json.load(f))

    def check_format_helper(self, path):
        with open(path) as f:
            return JSONValidator.check_AWS_IAM_format(json.load(f))

    def test_validate_resource_true_with_path(self):
        self.run_test(VALID_TEST_PATH, True, self.path_helper)

    def test_validate_resource_false_with_path(self):
        self.run_test(INVALID_TEST_PATH, False, self.path_helper)
    
    def test_validate_resource_true_with_string(self):
        self.run_test(VALID_TEST_PATH, True, self.string_helper)

    def test_validate_resource_false_with_string(self):
        self.run_test(INVALID_TEST_PATH, False, self.string_helper)
    
    def test_validate_resource_true_with_json(self):
        self.run_test(VALID_TEST_PATH, True, self.json_helper)

    def test_validate_resource_false_with_json(self):
        self.run_test(INVALID_TEST_PATH, False, self.json_helper)

    def test_check_AWS_IAM_format_false(self):
        self.run_test(BAD_FORMAT_TEST_PATH, False, self.check_format_helper)

    def test_check_AWS_IAM_format_true(self):
        self.run_test(VALID_TEST_PATH, True, self.check_format_helper)

if __name__ == '__main__':
    unittest.main()