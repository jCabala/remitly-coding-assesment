import sys
import os
from JSONValidator import JSONValidator

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Expected path as an argument")
        exit(1)

    path = str(sys.argv[1])

    if not os.path.isfile(path):
        print("Path provided is not valid")
        exit(1)

    print("The result of validation: ")
    print(JSONValidator.validate_resource(path, isPath=True))

