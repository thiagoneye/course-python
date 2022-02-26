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
        self.high_score = 0
        self.hideturtle()
        self.penup()
        self.sety((screen_height / 2.) - 40.)
        self.color('white')
        self.read_score()
        self.refresh()

    def read_score(self):
        with open('data.txt') as data:
            self.high_score = int(data.read())

    def save_score(self):
        with open('data.txt', mode='w') as data:
            data.write(str(self.high_score))

    def refresh(self):
        self.clear()
        self.write(f'Score: {self.score} Record: {self.high_score}', align=ALIGN, font=FONT)

    def increase_score(self):
        self.score += 1
        self.refresh()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.save_score()

        self.score = 0
        self.refresh()

