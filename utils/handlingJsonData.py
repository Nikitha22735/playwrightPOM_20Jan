import json

def readJsonData(filePath):
    with open(filePath) as jsonVariable:
        data = json.load(jsonVariable)
        return data
