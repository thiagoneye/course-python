"""
100 Days of Code
The Complete Python Pro Bootcamp
Dra. Angela Yu

Day 25
Working with CSV data and the Pandas library
"""

# Imports

import csv

# Main

temperatures = list()

with open('weather_data.csv') as file:
    data = csv.reader(file)

    for row in data:
        if row[1] != 'temp':
            temperatures.append(int(row[1]))

print(temperatures)
