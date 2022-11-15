"""
100 Days of Code
The Complete Python Pro Bootcamp
Dra. Angela Yu

Day 30
Errors, Exceptions and JSON Data
"""

height = float(input('Height: '))
weight = int(input('Weight: '))

if height > 3:
    raise ValueError('Human height should not be over 3 meters.')

bmi = round(weight / height**2, 3)

print(bmi)
