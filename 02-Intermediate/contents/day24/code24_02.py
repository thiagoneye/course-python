"""
100 Days of Code
The Complete Python Pro Bootcamp
Dra. Angela Yu

Day 24
Files, Directories and Paths
"""

with open('my_file.txt') as file:
    contents = file.read()
    print(contents)

with open('new_file.txt', mode='a') as file:
    file.write('Text.')
