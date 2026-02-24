import csv

def readCSV(path):
    with open(path) as csvVariable:
            credentials = []
            data = csv.DictReader(csvVariable)
            
            for row in data:
                credentials.append(row)

            return credentials
