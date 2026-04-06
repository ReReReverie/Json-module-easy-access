import json

default="Default.json"
def loadjson(jsonfilename=default):
    """Using an external json file open up into a variable list/dictionary or open an empty list"""
    try:
        with open(jsonfilename, "r") as f:
            return json.load(f)
    except:
        return []


def updatejson(dataname,jsonfilename=default):
    """Dump the updated data into the json file to update json file"""
    with open(jsonfilename, "w") as f:
        json.dump(dataname, f ,indent=4)

def greet():
    print("hello")