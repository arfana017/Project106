import csv
import numpy as np

#Cups of Coffee vs Hours of Sleep

def getDataSource1(data_path):
    cups_of_coffee = []
    hours_of_sleep = []
    
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            cups_of_coffee.append(float(row["Coffee in ml"]))
            hours_of_sleep.append(float(row["sleep in hours"]))

    return {"x": cups_of_coffee, "y": hours_of_sleep}

def findCorrelation1(datasource):
    correlation = np.corrcoef(datasource["x"], datasource["y"])
    print("Correlation between Cups of Coffee vs Hours of Sleep:   \n--->", correlation[0,1])

def setup1():
    data_path = "./cups of coffee vs hours of sleep.csv"

    datasource = getDataSource1(data_path)
    findCorrelation1(datasource)


#Student Marks vs Days Present

def getDataSource2(data_path):
    student_marks = []
    days_present = []
    
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            student_marks.append(float(row["Marks In Percentage"]))
            days_present.append(float(row["Days Present"]))

    return {"x": student_marks, "y": days_present}

def findCorrelation2(datasource):
    correlation = np.corrcoef(datasource["x"], datasource["y"])
    print("Correlation between Student Marks vs Days Present:   \n--->", correlation[0,1])

def setup2():
    data_path = "./Student Marks vs Days Present.csv"

    datasource = getDataSource2(data_path)
    findCorrelation2(datasource)


setup1()
setup2()