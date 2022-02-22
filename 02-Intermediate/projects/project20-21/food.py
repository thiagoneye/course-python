"""
100 Days of Code
The Complete Python Pro Bootcamp
Dra. Angela Yu

Project 20/21
Snake Game
"""

# Imports

import random as rd
from snake import new_segment


# Classes

class Food:
    def __init__(self, screen_width, screen_height):
        self.food = None
        self.new_food(screen_width, screen_height)

    def new_food(self, screen_width, screen_height):
        xvalue = rd.randint((-screen_width / 2.) + 20., (screen_width / 2.) - 20.)
        yvalue = rd.randint((-screen_height / 2.) + 20., (screen_height / 2.) - 20.)
        self.food = new_segment(xcoord=xvalue, ycoord=yvalue)
