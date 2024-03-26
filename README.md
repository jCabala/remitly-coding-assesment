# Remitly Home Exercise

## Code overivew
The [`JSONValidator` class](./JSONValidator.py) contains 2 public methods:
1. `validateResource(data)` a method checking for asterix in `Resource` field (the method requested in the task).
The `data` argument might be: a dictionary or string containing json or a path to a json file
2. `check_AWS_IAM_format()` a method checking if the JSON follows a correct format

The [`main.py` file](./main.py) contains the CLI interface for validating files

The [`JSONValidatorTest.py` file](./JSONValidatorTest.py) contains the unit tests for JSON validator.
The files that are being tested are in `./testFiles` directory.

# Run CLI
To run a CLI type a command:
```console
python3 main.py <path-to-a-file>
```

# Run tests
To run the tests type:
```console
python3 JSONValidatorTest.py
```
