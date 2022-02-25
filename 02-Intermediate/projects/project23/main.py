"""
100 Days of Code
The Complete Python Pro Bootcamp
Dra. Angela Yu

Project 23
The Turtle Crossing
"""

# Imports

import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# Constants

FINISH_LINE_Y = 280

# Screen

screen = Screen()
screen.setup(width=600, height=600)
screen.title('The Turtle Crossing')
screen.tracer(0)

# Objects

player = Player()
scoreboard = Scoreboard()
cars = CarManager()

# Actions

screen.listen()
screen.onkeypress(fun=player.move, key='Up')

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    cars.new_car()
    cars.move()
    cars.delete_cars()

    # Crossed the street
    if player.ycor() >= FINISH_LINE_Y:
        player.restart_position()
        cars.cars_acceleration()
        scoreboard.refresh()

    # Collision with a car
    for car in cars.cars:
        if player.distance(car) < 20:
            scoreboard.game_over()
            game_is_on = False


# Exit Game

screen.exitonclick()
