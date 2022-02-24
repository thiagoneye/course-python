"""
100 Days of Code
The Complete Python Pro Bootcamp
Dra. Angela Yu

Project 22
Pong Game
"""

# Imports

import time
from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

# Inputs

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
COORDS_X = [-SCREEN_WIDTH/2 + 40., SCREEN_WIDTH/2 - 40.]

# Create Screen

screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor('black')
screen.title('Pong Game')
screen.tracer(0)

# Create Line

line = Turtle()
line.color('white')
line.penup()
line.hideturtle()
line.sety(SCREEN_HEIGHT/2 + 10)
line.pendown()
line.sety(-SCREEN_HEIGHT/2 - 10)

# Objects

scoreboard1 = Scoreboard(screen_height=SCREEN_HEIGHT, xcoord=(- SCREEN_WIDTH / 4))
scoreboard2 = Scoreboard(screen_height=SCREEN_HEIGHT, xcoord=(SCREEN_WIDTH / 4))
ball = Ball()
paddle1 = Paddle(coord=COORDS_X[0], screen_height=SCREEN_HEIGHT)
paddle2 = Paddle(coord=COORDS_X[1], screen_height=SCREEN_HEIGHT)


# Actions

def start_game():
    paddle1.sety(0)
    paddle2.sety(0)

    continue_game = True
    while continue_game:
        screen.update()
        time.sleep(0.1)

        # Ball Movement
        ball.move()

        # Collision with the Walls
        if abs(ball.ycor()) >= (SCREEN_HEIGHT - 60)/2:
            new_angle = 360 - ball.heading()
            ball.setheading(new_angle)

        # Collision with the Paddles
        if (abs(ball.xcor()) > (COORDS_X[1] - 30)) and ((ball.distance(paddle2) < 70) or (ball.distance(paddle1) < 70)):
            new_angle = 180 - ball.heading()
            ball.setheading(new_angle)

        # Stop Game
        if ball.xcor() < COORDS_X[0]:
            ball.new_round()
            scoreboard2.refresh()
            continue_game = False

        if ball.xcor() > COORDS_X[1]:
            ball.new_round()
            scoreboard1.refresh()
            continue_game = False


# Screen

screen.listen()
screen.onkey(fun=start_game, key='space')
screen.onkeypress(fun=paddle1.go_up, key='w')
screen.onkeypress(fun=paddle1.go_down, key='s')
screen.onkeypress(fun=paddle2.go_up, key='Up')
screen.onkeypress(fun=paddle2.go_down, key='Down')

# Exit Game

screen.exitonclick()
