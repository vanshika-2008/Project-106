import csv
import numpy as np
import plotly.express as pxp

def ScatterCreation() :
    file = open("./DataSets/Student Marks_vs_Days Present.csv")
    dataframe = csv.DictReader(file)
    plot = pxp.scatter(dataframe,x= "Marks In Percentage",y="Days Present")
    plot.show()

def getDataSource() :
    DaysOfPresence = []
    Percentage = []
    File = open("./DataSets/Student Marks_vs_Days Present.csv")
    Reader = csv.DictReader(File)
    for i in Reader :
        DaysOfPresence.append(float(i["Days Present"]))
        Percentage.append(float(i["Marks In Percentage"]))
    
    return {"x": Percentage, "y" : DaysOfPresence}

def CorrelationFinder (DataSource) :
    Correlation = np.corrcoef(DataSource["x"],DataSource["y"])
    print(Correlation[0,1])

def Setup () :
    DataSource = getDataSource()
    CorrelationFinder(DataSource)
    ScatterCreation()

Setup()
