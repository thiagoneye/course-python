"""
100 Days of Code
The Complete Python Pro Bootcamp
Dra. Angela Yu

Project 22
Pong Game
"""

# Imports

from turtle import Turtle
import random as rd

# Constants

ANGLES = list(range(1, 61)) + list(range(120, 241)) + list(range(300, 360))
ANGLES.remove(180)


# Classes

class Ball(Turtle):
    def __init__(self):
        super().__init__()

        self.penup()
        self.shape('circle')
        self.color('white')
        self.speed('slowest')

        self.new_round()

    def move(self):
        self.forward(20)

    def new_round(self):
        self.home()
        self.setheading(rd.choice(ANGLES))
