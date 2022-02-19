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
numb_figs = 36

# Object
circle = tt.Turtle()
circle.speed(0)


# Functions
def rand_color():
    r = rd.randint(1, 255) / 255
    g = rd.randint(1, 255) / 255
    b = rd.randint(1, 255) / 255
    color = (r, g, b)
    return color


def draw_spirograph(size):
    for _ in range(36):
        circle.color(rand_color())
        circle.circle(size)
        current_heading = circle.heading()
        circle.setheading(current_heading + 10)


# Actions
draw_sizes = [50, 100, 150]
for value in draw_sizes:
    draw_spirograph(value)

# Screen
screen = tt.Screen()
screen.exitonclick()
