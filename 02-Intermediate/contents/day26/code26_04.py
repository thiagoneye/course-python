"""
100 Days of Code
The Complete Python Pro Bootcamp
Dra. Angela Yu

Day 26
List Comprehension
"""

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"

# Don't change code above 👆

string_list = sentence.split()
result = {value: len(value) for value in string_list}

# Write your code below:

print(result)
