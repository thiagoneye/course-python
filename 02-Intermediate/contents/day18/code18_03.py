"""
100 Days of Code
The Complete Python Pro Bootcamp
Dra. Angela Yu

Day 18
Turtle & the Graphical User Interface
"""

# Imports
import turtle as tt
import random as rd

# Inputs
numb_shapes = 10
colors = ['black', 'cornflower blue', 'cyan', 'dark cyan', 'medium spring green', 'dark olive green', 'gold',
          'firebrick', 'orange red', 'rosy brown', 'purple', 'indigo']

# Object
timmy = tt.Turtle()
timmy.shape('turtle')

# Actions
for numb_sides in range(3, numb_shapes+1):
    angle = 360/numb_sides
    timmy.color(rd.choice(colors))

    for _ in range(numb_sides):
        timmy.forward(100)
        timmy.right(angle)

# Screen
screen = tt.Screen()
screen.exitonclick()
