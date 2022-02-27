"""
100 Days of Code
The Complete Python Pro Bootcamp
Dra. Angela Yu

Project 25
U.S. States Game
"""

# Imports
import turtle
from turtle import Screen, Turtle
import pandas as pd

# Constants

IMAGE = 'blank_states_img.gif'

# Data

df = pd.read_csv('50_states.csv')

# Screen

screen = Screen()
screen.title('U.S. States Game')
# screen.screensize(canvwidth=, canvheight=)
screen.addshape(IMAGE)

turtle.shape(IMAGE)

# Objects

state = Turtle()
state.hideturtle()
state.penup()
state.speed('fastest')

# Actions

correct_answers = 0
states_list = list()

while len(states_list) < 50:
    text_input = f'{correct_answers}/50 States Correct'
    answer_state = screen.textinput(title=text_input, prompt='What\'s another state\'s name?')

    if (answer_state.title() in df.state.values) and (answer_state.title() not in states_list):
        correct_answers += 1
        states_list.append(answer_state.title())

        coord_x = df[df.state == answer_state.title()]['x'].values[0]
        coord_y = df[df.state == answer_state.title()]['y'].values[0]
        coords = (coord_x, coord_y)
        state.goto(coords)

        state.write(answer_state.title(), align='center')

state.goto((0, 0))
state.write('You Win!', align='center', font=('Arial', 18, 'normal'))

# Exit

screen.exitonclick()
