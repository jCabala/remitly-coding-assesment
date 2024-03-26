import json

# TODO: Add a possibility to pass already converted JSON as well
# TODO: Write a method to verify the policy

STMT_KEY = "Statement"
DOC_KEY = "PolicyDocument"
RES_KEY = "Resource"
NAME_KEY = "PolicyName"

class JSONValidator:

    @staticmethod
    def validate_resource(data, isPath=False):
        """
        Method returns false if the given json is not in the AWS::IAM::Role Policy
        Method returns false if any of the Resource fields in the given 
        JSON contains an asterix ('*') and true in any other case

        :param data: 
            JSON data either in a string format, already converted to a dictionary
            or a path to a file containing JSON.
            It must be in a AWS::IAM::Role format
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

        if (not JSONValidator.check_AWS_IAM_format(json_data)):
            print("ERROR: Given JSON does not follow the AWS::IAM::Role Policy format")
            return False

        # At this point json must contain the DOC_KEY
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
    def check_AWS_IAM_format(json):
        """
        Checks if the document follows the desired format
        """
        return DOC_KEY in json and NAME_KEY in json

    @staticmethod
    def __list_wrap(x):
        """
        Creates a singelton list if an argument is not a list
        """
        return [x] if not isinstance(x, list) else x

