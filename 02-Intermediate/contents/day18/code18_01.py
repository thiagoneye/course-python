"""
100 Days of Code
The Complete Python Pro Bootcamp
Dra. Angela Yu

Day 18
Turtle & the Graphical User Interface
"""

# Imports
from turtle import Turtle, Screen

# Object
timmy = Turtle()
timmy.shape('turtle')
timmy.color('green')

# Actions
for _ in range(4):
    timmy.forward(100)
    timmy.left(90)

# Screen
screen = Screen()
screen.exitonclick()
