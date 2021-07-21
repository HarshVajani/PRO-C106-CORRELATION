import plotly.express as px
import csv
import numpy as np

def plotFigure(data_path):
    with open(data_path) as csv_file:
        df = csv.DictReader(csv_file)
        fig = px.scatter(df,x="Cups Of Coffee", y="Hours Of Sleep")
        fig.show()
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
    data_path  = "C:\Users\Harsh\Desktop\WhiteHat.Jr\Class\106\PRO-C106-CORRELATION-main\cups of coffee vs hours of sleep.csv"

    datasource = getDataSource(data_path)
    findCorrelation(datasource)
    plotFigure(data_path)

setup()