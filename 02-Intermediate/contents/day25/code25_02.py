"""
100 Days of Code
The Complete Python Pro Bootcamp
Dra. Angela Yu

Day 25
Working with CSV data and the Pandas library
"""

# Imports

import pandas as pd

# Data Structs

data = pd.read_csv('weather_data.csv')
temp_array = data['temp'].values
print(temp_array)

temp_list = data['temp'].to_list()
print(temp_list)

data_dict = data.to_dict()
print(data_dict)

# Descriptive Statistics

average_temp = data['temp'].mean()
print(f'\nThe average temperature is {round(average_temp, 2)}.')

max_temp = data['temp'].max()
print(f'The maximum temperature is {max_temp}.')

min_temp = data['temp'].min()
print(f'The minimum temperature is {min_temp}.')

# Challenges

row_max = data[data.temp == max_temp]
print('\nChallenge 1:')
print(row_max)

mond_temp = data[data.day == 'Monday'].temp.values[0] * 9/5 + 32
print('\nChallenge 2:')
print(f'The temperature on monday is {mond_temp} °F.')

# Create a Dataframe

new_dict = {
    'students': ['Amy', 'James', 'Angela'],
    'scores': [76, 56, 65]
}

new_df = pd.DataFrame(new_dict)
print('\n')
print(new_df)

new_df.to_csv('new_data.csv')
