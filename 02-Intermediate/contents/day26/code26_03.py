"""
100 Days of Code
The Complete Python Pro Bootcamp
Dra. Angela Yu

Day 26
List Comprehension
"""

# Read Data

with open('file1.txt') as file1:
    values1 = file1.readlines()

with open('file2.txt') as file2:
    values2 = file2.readlines()

# Transform Data

values1 = [int(element.replace('\n', '')) for element in values1]
values2 = [int(element.replace('\n', '')) for element in values2]

# Create Dictionary

result = [element for element in values1 if (element in values2)]

# Write your code above 👆

print(result)
