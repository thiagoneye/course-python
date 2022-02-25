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

ANGLESR = list(range(1, 61)) + list(range(300, 360))
ANGLESL = list(range(120, 241))
ANGLESL.remove(180)


# Classes

class Ball(Turtle):
    def __init__(self):
        super().__init__()

        self.penup()
        self.shape('circle')
        self.color('white')
        self.speed('slowest')

        self.direction = 'left'
        self.new_round()

    def move(self):
        self.forward(20)

    def new_round(self):
        self.home()
        if self.direction == 'left':
            self.setheading(rd.choice(ANGLESL))
            self.direction = 'right'
        else:
            self.setheading(rd.choice(ANGLESR))
            self.direction = 'left'
