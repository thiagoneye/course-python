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
numb_steps = 100
directions = [0, 90, 180, 270]

# Object
timmy = tt.Turtle()
timmy.shape('turtle')
timmy.speed(0)
timmy.width(5)

# Actions
for _ in range(numb_steps):
    color = (rd.randint(1, 255)/255, rd.randint(1, 255)/255, rd.randint(1, 255)/255)
    timmy.color(color)
    timmy.forward(10)
    timmy.setheading(rd.choice(directions))

# Screen
screen = tt.Screen()
screen.exitonclick()
