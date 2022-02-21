"""
100 Days of Code
The Complete Python Pro Bootcamp
Dra. Angela Yu

Day 19
Instances, State and Higher Order Functions

Challenge
Etch-A-Sketch App
"""

# Imports
from turtle import Turtle, Screen

# Objects
timmy = Turtle()


# Functions
def move_forwards():
    timmy.forward(10)


def move_backwards():
    timmy.backward(10)


def turn_left():  # Clockwise
    timmy.left(15)


def turn_right():  # Counter-clockwise
    timmy.right(15)


def restart_screen():
    timmy.reset()


# Screen
screen = Screen()

screen.listen()
screen.onkey(fun=move_forwards, key='w')
screen.onkey(fun=move_backwards, key='s')
screen.onkey(fun=turn_left, key='a')
screen.onkey(fun=turn_right, key='d')
screen.onkey(fun=restart_screen, key='c')

screen.exitonclick()
