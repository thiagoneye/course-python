"""
100 Days of Code
The Complete Python Pro Bootcamp
Dra. Angela Yu

Project 20/21
Snake Game
"""

# Imports

import random as rd
from turtle import Turtle


# Classes

class Food(Turtle):
    def __init__(self, screen_width, screen_height):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color('white')
        self.speed(0)

        random_x = rd.randint((-screen_width / 2.) + 20., (screen_width / 2.) - 20.)
        random_y = rd.randint((-screen_height / 2.) + 20., (screen_height / 2.) - 20.)
        self.setx(random_x)
        self.sety(random_y)

    def refresh(self, screen_width, screen_height):
        random_x = rd.randint((-screen_width / 2.) + 20., (screen_width / 2.) - 20.)
        random_y = rd.randint((-screen_height / 2.) + 20., (screen_height / 2.) - 20.)
        self.setx(random_x)
        self.sety(random_y)
