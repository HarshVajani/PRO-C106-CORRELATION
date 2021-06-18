import csv
import numpy as np


def getDataSource(data_path):
    cups_of_coffee = []
    hours_of_sleep = []
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            cups_of_coffee.append(float(row["Cups Of Coffee"]))
            hours_of_sleep.append(float(row["Hours Of Sleep"]))

    return {"x" : cups_of_coffee, "y" : hours_of_sleep}

def findCorrelation(datasource):
    correlation = np.corrcoef(datasource["x"], datasource["y"])
    print("Correlation between Cups Of Coffee and Hours Of Sleep :- \n--->",correlation[0,1])

def setup():
    data_path = "C:\Users\hitesh\Desktop\Whitehat.Jr\Project 106\cups of coffee vs hours of sleep.csv"

    datasource = getDataSource(data_path)
    findCorrelation(datasource)

setup()