import plotly.express as px
import csv
import numpy as np

def getData(data):
    marks_in_percentage = []
    days_present = []
    with open(data) as f:
        reader = csv.DictReader(f)
        for row in reader:
            marks_in_percentage.append(float(row['Marks In Percentage']))
            days_present.append(float(row['Days Present']))
    
    return {'x': marks_in_percentage, 'y': days_present}

def plotData(file):
    with open(file) as f:
        df = csv.DictReader(f)
        fig = px.scatter(df, x="Days Present", y="Marks In Percentage")
        fig.show()

def getCorr(data):
    correlation = np.corrcoef(data['x'], data['y'])
    print("Correlation between Coffee and sleep is: " + str(correlation[0,1]))

def main():
    file='./csv/Marks_Days.csv'

    file_data = getData(file)
    plotData(file)
    getCorr(file_data)

main()