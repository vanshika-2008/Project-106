import csv
import numpy as np
import plotly.express as pxp

def ScatterCreation() :
    file = open("./DataSets/cups of coffee vs hours of sleep.csv")
    dataframe = csv.DictReader(file)
    plot = pxp.scatter(dataframe,x= "Coffee in ml",y="sleep in hours")
    plot.show()

def getDataSource() :
    Coffee = []
    Sleep = []
    File = open("./DataSets/cups of coffee vs hours of sleep.csv")
    Reader = csv.DictReader(File)
    for i in Reader :
        Coffee.append(float(i["Coffee in ml"]))
        Sleep.append(float(i["sleep in hours"]))
    
    return {"x": Coffee, "y" : Sleep}

def CorrelationFinder (DataSource) :
    Correlation = np.corrcoef(DataSource["x"],DataSource["y"])
    print(Correlation[0,1])

def Setup () :
    DataSource = getDataSource()
    CorrelationFinder(DataSource)
    ScatterCreation()

Setup()
