"""
100 Days of Code
The Complete Python Pro Bootcamp
Dra. Angela Yu

Day 35

Automate Check if it Will Rain
"""

# Imports

import requests

# Constants

api = 'https://api.openweathermap.org/data/2.5/weather'
params = {
    'lat': -8.3338176,
    'lon': -36.41849,
    'appid': ''
}

# Main

data = requests.get(url=api, params=params)
data = data.json()

if data['weather'][0]['id'] < 700:
    print('Bring an umbrella.')
else:
    print('Don\'t bring an umbrella.')
