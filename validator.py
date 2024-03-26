import json
from collections.abc import Iterable

# TODO: Add a possibility to pass already converted JSON as well
# TODO: Write a method to verify the policy
STMT_KEY = "Statement"
DOC_KEY = "PolicyDocument"
RES_KEY = "Resource"

def validateJSON(data):
    json_data = {}

    if type(data) is str:
        json_data = json.loads(data) 
    else:
        raise Exception(f"Type mismatch. Expected string but got {type(data)}")

    doc = json_data.get(DOC_KEY)
    if not STMT_KEY in doc:
        # TODO: Check if stmt can be empty. For now assume it can
        print("No Stmt")
        return True

    # Statement can be an array or a single string  
    stmts = __getIterable(doc.get(STMT_KEY)) 

    for stmt in stmts:
         print(stmt)
         if not RES_KEY in stmt:
            # TODO: Check if resource can be empty. For now assume it can
             continue
         # Resource can be an array or a single string
         res = __getIterable(stmt.get(RES_KEY))
         for val in res:
             if '*' in val:
                 return False
                  
    return True

def __getIterable(x):
    return [x] if not isinstance(x, Iterable) else x