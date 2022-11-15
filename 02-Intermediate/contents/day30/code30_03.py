"""
100 Days of Code
The Complete Python Pro Bootcamp
Dra. Angela Yu

Day 30
Errors, Exceptions and JSON Data
"""

fruits = ["Apple", "Pear", "Orange"]

#TODO: Catch the exception and make sure the code runs without crashing.
def make_pie(index):
    try:
        fruit = fruits[index]
    except IndexError:
        print('Fruit pie')
    else:
        print(fruit + " pie")

make_pie(4)
make_pie(1)
