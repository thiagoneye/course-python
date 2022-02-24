"""
100 Days of Code
The Complete Python Pro Bootcamp
Dra. Angela Yu

Project 22
Pong Game
"""

# Imports

from turtle import Turtle

# Constants

WIDTH = 5
HEIGHT = 1


# Classes

class Paddle(Turtle):
    def __init__(self, coord, screen_height):
        super().__init__()

        self.shape('square')
        self.penup()
        self.color('white')
        self.setx(coord)
        self.shapesize(stretch_wid=WIDTH, stretch_len=HEIGHT)

        self.limit = (screen_height - WIDTH*20 - 40.) / 2

    def go_up(self):
        if self.ycor() < self.limit:
            new_y = self.ycor() + 20
            self.sety(new_y)

    def go_down(self):
        if self.ycor() > -self.limit:
            new_y = self.ycor() - 20
            self.sety(new_y)
