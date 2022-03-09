"""
100 Days of Code
The Complete Python Pro Bootcamp
Dra. Angela Yu

Day 27
Tkinter, *args, **kwargs and Creating GUI Programs
"""

# Functions

def print_values(a, b=2):
    values = [a,b]
    for value in values:
        print(value)

def add(*args):
    total = 0
    for n in args:
        total += n

    return total

def calculate(n, **kwargs):
    print(f'\n{kwargs}\n')

    for key, value in kwargs.items():
        print(f'{key}: {value}')

    n += kwargs['add']
    # n -= kwargs['subtract']
    n *= kwargs['multiply']

    print(f'\nThe result is {n}.')

# Main

print_values(1)

value = add(1,1,2,3,5,8)
print(f'\n{value}')

calculate(2, add=3, multiply=5)

# Class

class Car:
    def __init__(self, **kwargs):
        self.make = kwargs.get('make')
        self.model = kwargs.get('model')

my_car = Car(make='Nissan')
print(f'\nThe car model is {my_car.model}.')
