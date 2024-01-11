""""
import csv 
ABSOLUTE_PATH = "/Users/lovely/Documents/100_DaysOfProgramming/025_Day/ExampleFolder/weather_data.csv"
with open(ABSOLUTE_PATH) as file:
    data = csv.reader(file)
    tempratures = []

    for row in data:
       if row[1] != "temp":
           tempratures.append(int(row[1])) 
    
"""
ABSOLUTE_PATH = "/Users/lovely/Documents/100_DaysOfProgramming/025_Day/ExampleFolder/weather_data.csv"

import pandas

data = pandas.read_csv(ABSOLUTE_PATH)
print(data["temp"])