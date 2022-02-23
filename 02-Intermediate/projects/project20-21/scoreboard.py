"""
100 Days of Code
The Complete Python Pro Bootcamp
Dra. Angela Yu

Project 20/21
Snake Game
"""

# Imports

from turtle import Turtle

# Constants

ALIGN = 'center'
FONT = ('Courier', 14, 'bold')


# Class

class Scoreboard(Turtle):
    def __init__(self, screen_height):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.sety((screen_height / 2.) - 40.)
        self.color('white')
        self.write(f'Score = {self.score}', align=ALIGN, font=FONT)

    def refresh(self):
        self.score += 1
        self.clear()
        self.write(f'Score = {self.score}', align=ALIGN, font=FONT)

    def game_over(self):
        self.sety(0)
        self.write('Game Over', align=ALIGN, font=FONT)
