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

MOVE_DISTANCE = 20
START_COORDS = [-20, 0, 20]
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270


# Functions

def new_segment(xcoord, ycoord=0):
    segment = Turtle(shape='square')
    segment.penup()
    segment.color('white')
    segment.setx(xcoord)
    segment.sety(ycoord)
    return segment


# Classes

class Snake:
    def __init__(self):
        self.body = list()
        for coord in START_COORDS:
            self.body.append(new_segment(xcoord=coord))

        self.head = self.body[0]

    def move(self):
        for idx in range(len(self.body)-1, 0, -1):
            self.body[idx].setx(self.body[idx-1].xcor())
            self.body[idx].sety(self.body[idx-1].ycor())

        self.head.forward(MOVE_DISTANCE)

    def go_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def go_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def go_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def go_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
