"""
100 Days of Code
The Complete Python Pro Bootcamp
Dra. Angela Yu

Day 25
Working with CSV data and the Pandas library
"""

# Imports

import pandas as pd
from collections import Counter

# Read Data

df = pd.read_csv('Squirrel_Data.csv')
# print(df)
# print(df.info())
# print(df.describe())

# Challenge

data = dict(Counter(df['Primary Fur Color'].dropna()))
output = pd.DataFrame(data.items(), columns=['Fur Color', 'Count'])
output.to_csv('squirrel_count.csv')
