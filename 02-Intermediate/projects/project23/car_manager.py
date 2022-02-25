"""
100 Days of Code
The Complete Python Pro Bootcamp
Dra. Angela Yu

Project 23
The Turtle Crossing
"""

# Imports

from turtle import Turtle
import random as rd

# Constants

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 2
COORD_X = 320
COORD_Y = list(range(-250, 250, 20))


# Class

class CarManager:
    def __init__(self):
        self.cars = list()
        self.speed_car = STARTING_MOVE_DISTANCE

    def new_car(self):
        random_chance = rd.randint(1, 6)
        if random_chance == 6:
            car = Turtle()
            car.penup()
            car.setx(320)
            car.sety(rd.choice(COORD_Y))
            car.setheading(180)
            car.shape('square')
            car.color(rd.choice(COLORS))
            car.shapesize(stretch_wid=1, stretch_len=2)
            self.cars.append(car)

    def delete_cars(self):
        for car in self.cars:
            if car.xcor() < -COORD_X:
                car.hideturtle()
                self.cars.remove(car)

    def move(self):
        for car in self.cars:
            car.forward(self.speed_car)

    def cars_acceleration(self):
        self.speed_car += MOVE_INCREMENT
