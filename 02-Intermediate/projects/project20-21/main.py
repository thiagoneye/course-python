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
from food import Food
from scoreboard import Scoreboard

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
food = Food(screen_width=SCREEN_WIDTH, screen_height=SCREEN_HEIGHT)
scoreboard = Scoreboard(screen_height=SCREEN_HEIGHT)


# Actions

def start_game():
    continue_game = True
    while continue_game:
        screen.update()
        time.sleep(0.1)
        snake.move()

        # Detect collision with food
        if snake.head.distance(food) < 15:
            food.refresh(screen_width=SCREEN_WIDTH, screen_height=SCREEN_HEIGHT)
            scoreboard.increase_score()
            snake.grow()

        # Detect collision with wall
        if (abs(snake.head.xcor()) > (SCREEN_WIDTH / 2.) - 10.) or (abs(snake.head.ycor()) > (SCREEN_WIDTH / 2.) - 10.):
            scoreboard.reset()
            snake.reset()

        # Detect collision with own tail
        for segment in snake.body[1:]:
            if snake.head.distance(segment) < 10:
                scoreboard.reset()
                snake.reset()


# Screen

screen.listen()
screen.onkey(fun=start_game, key='space')
screen.onkey(fun=snake.go_right, key='Right')
screen.onkey(fun=snake.go_up, key='Up')
screen.onkey(fun=snake.go_left, key='Left')
screen.onkey(fun=snake.go_down, key='Down')

screen.exitonclick()
