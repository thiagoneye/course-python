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

ALIGN = 'center'
FONT = ('Courier', 36, 'bold')


# Class

class Scoreboard(Turtle):
    def __init__(self, screen_height, xcoord):
        super().__init__()

        self.hideturtle()
        self.penup()
        self.setx(xcoord)
        self.sety((screen_height / 2.) - 80.)
        self.color('white')

        self.score = 0
        self.write(f'{self.score}', align=ALIGN, font=FONT)

    def refresh(self):
        self.score += 1
        self.clear()
        self.write(f'{self.score}', align=ALIGN, font=FONT)

