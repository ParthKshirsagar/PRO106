import plotly.express as px
import csv
import numpy as np

def getData(data):
    sleep_in_hours = []
    coffee_in_ml = []
    with open(data) as f:
        reader = csv.DictReader(f)
        for row in reader:
            sleep_in_hours.append(float(row['sleep in hours']))
            coffee_in_ml.append(float(row['Coffee in ml']))
    
    return {'x': coffee_in_ml, 'y': sleep_in_hours}

def plotData(file):
    with open(file) as f:
        df = csv.DictReader(f)
        fig = px.scatter(df, x="Coffee in ml", y="sleep in hours", color="week", size_max=60)
        fig.show()

def getCorr(data):
    correlation = np.corrcoef(data['x'], data['y'])
    print("Correlation between Coffee and sleep is: " + str(correlation[0,1]))

def main():
    file='./csv/Coffee_Sleep.csv'

    file_data = getData(file)
    plotData(file)
    getCorr(file_data)

main()