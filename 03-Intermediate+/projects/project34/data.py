"""
100 Days of Code
The Complete Python Pro Bootcamp
Dra. Angela Yu

Day 34

GUI Quiz App
"""

# Imports

import requests

# Parameters

parameters = {
    'amount': 10,
    'type': 'boolean'
}

# Main

data = requests.get(url='https://opentdb.com/api.php', params=parameters)
data = data.json()
question_data = data['results']
