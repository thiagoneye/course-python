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

ALIGN = 'center'
FONT = ("Courier", 18, "normal")
COORDX = -200
COORDY = 250


# Class

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()

        self.hideturtle()
        self.penup()
        self.setx(COORDX)
        self.sety(COORDY)

        self.level = 1
        self.refresh()

    def refresh(self):
        self.clear()
        self.write(f'Level: {self.level}', align=ALIGN, font=FONT)
        self.level += 1

    def game_over(self):
        self.goto((0, 0))
        self.write('Game Over', align=ALIGN, font=FONT)
