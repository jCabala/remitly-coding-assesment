import json
import io

def validateJSON(data):
    json_data = {}

    if type(data) is str:
        json_data = json.loads(data) 
    else:
        raise Exception(f"Type mismatch. Expected string or file but got {type(data)}")

    print(json_data) 
    return True


def is_json(value):
    try:
        json.loads(value)
    except ValueError:
        return False
    return True 