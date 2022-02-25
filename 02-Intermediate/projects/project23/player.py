"""
100 Days of Code
The Complete Python Pro Bootcamp
Dra. Angela Yu

Project 23
The Turtle Crossing
"""

# Imports

from turtle import Turtle

# Constants

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10


# Class

class Player(Turtle):
    def __init__(self):
        super().__init__()

        self.penup()
        self.setheading(90)
        self.shape('turtle')
        self.color('green')

        self.restart_position()

    def restart_position(self):
        self.goto(STARTING_POSITION)

    def move(self):
        self.forward(MOVE_DISTANCE)
