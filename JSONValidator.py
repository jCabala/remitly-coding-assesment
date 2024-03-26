import json
from collections.abc import Iterable

# TODO: Add a possibility to pass already converted JSON as well
# TODO: Write a method to verify the policy

STMT_KEY = "Statement"
DOC_KEY = "PolicyDocument"
RES_KEY = "Resource"

class JSONValidator:

    @staticmethod
    def validate_resource(data, isPath=False):
        """
        Method returns fals eif any of the Resource fields in the given 
        JSON contains an asterix ('*') and true in any other case

        :param data: 
            JSON data either in a string format, already converted to a dictionary
            or a path to a file containing JSON
        :param isPath:
            Set to true if data is a path to a file
        :return: boolean
        """
        json_data = {}

        if isPath:
           with open(data) as f:
                json_data = json.load(f)
        elif type(data) is str:
            json_data = json.loads(data) 
        elif type(data) is dict:
            json_data = data
        else:
            raise Exception(f"Type mismatch. Expected string or dict but got {type(data)}")

        doc = json_data.get(DOC_KEY)
        if not STMT_KEY in doc:
            # TODO: Check if stmt can be empty. For now assume it can
            return True

        # Statement can be an array or a single string  
        stmts = JSONValidator.__get_iterable(doc.get(STMT_KEY)) 

        for stmt in stmts:
            if not RES_KEY in stmt:
                # TODO: Check if resource can be empty. For now assume it can
                continue
            # Resource can be an array or a single string
            res = JSONValidator.__get_iterable(stmt.get(RES_KEY))
            for val in res:
                if '*' in val:
                    return False
                    
        return True

    @staticmethod
    def __get_iterable(x):
        return [x] if not isinstance(x, Iterable) else x

