"""
100 Days of Code
The Complete Python Pro Bootcamp

Constructing Objects and Accessing their Attributes and Methods

Turtle Documentation: https://docs.python.org/3/library/turtle.html
"""

# Imports
from turtle import Turtle, Screen

# Instantiation
timmy = Turtle()

# Object Settings
timmy.shape('turtle')
timmy.color('chartreuse4')

# Actions
timmy.forward(100)

# Viewer
my_screen = Screen()
my_screen.exitonclick()
# print(my_screen.canvheight) # Print an attribute
