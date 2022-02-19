"""
100 Days of Code
The Complete Python Pro Bootcamp
Dra. Angela Yu

Day 18
Turtle & the Graphical User Interface
"""

# Imports
import turtle as tt

# Object
timmy = tt.Turtle()
timmy.shape('turtle')
timmy.color('green')

# Actions
for _ in range(15):
    timmy.forward(10)
    timmy.penup()
    timmy.forward(5)
    timmy.pendown()

# Screen
screen = tt.Screen()
screen.exitonclick()
