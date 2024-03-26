import json

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
            # I assume that if Statement is empty than the Resource cannot contain an asterix
            return True

        # Statement can be an array or a single string  
        stmts = JSONValidator.__list_wrap(doc.get(STMT_KEY)) 

        for stmt in stmts:
            if not RES_KEY in stmt:
                # I assume that if a Resource is empty it cannot contain an asterix
                continue
            # Resource can be an array or a single string
            res = JSONValidator.__list_wrap(stmt.get(RES_KEY))
            for val in res:
                if '*' in val:
                    return False
                    
        return True

    @staticmethod
    def __list_wrap(x):
        """
        Creates a singelton list if an argument is not a list
        """
        return [x] if not isinstance(x, list) else x

