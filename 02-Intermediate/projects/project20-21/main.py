"""
100 Days of Code
The Complete Python Pro Bootcamp
Dra. Angela Yu

Project 20/21
Snake Game
"""

# Imports

import time
from turtle import Screen
from snake import Snake

# Inputs

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

# Create Screen

screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)

# Objects

snake = Snake()


# Actions

def start_game():
    continue_game = True
    while continue_game:
        screen.update()
        time.sleep(0.1)
        snake.move()

        if (abs(snake.head.xcor()) >= SCREEN_WIDTH / 2) or (abs(snake.head.ycor()) >= SCREEN_HEIGHT / 2):
            continue_game = False


# Screen

screen.listen()
screen.onkey(fun=start_game, key='space')
screen.onkey(fun=snake.go_right, key='Right')
screen.onkey(fun=snake.go_up, key='Up')
screen.onkey(fun=snake.go_left, key='Left')
screen.onkey(fun=snake.go_down, key='Down')

screen.exitonclick()
