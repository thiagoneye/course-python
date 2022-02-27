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
screen.setup(width=725, height=491)
screen.addshape(IMAGE)
turtle.shape(IMAGE)

# Objects

state = Turtle()
state.hideturtle()
state.penup()
state.speed('fastest')

# Actions

answer_state = ''
correct_answers = 0
listed_states = list()
all_states = df.state.to_list()

while len(listed_states) < 50:
    text_input = f'{correct_answers}/50 States Correct'
    answer_state = screen.textinput(title=text_input, prompt='What\'s another state\'s name?').title()

    if answer_state == 'Exit':
        break

    if (answer_state in df.state.values) and (answer_state not in listed_states):
        correct_answers += 1
        listed_states.append(answer_state)

        coord_x = df[df.state == answer_state]['x'].values[0]
        coord_y = df[df.state == answer_state]['y'].values[0]
        state.goto((coord_x, coord_y))

        state.write(answer_state, align='center')

if answer_state == 'Exit':
    with open('unlisted_states.txt', mode='w') as file:
        for name in all_states:
            if name not in listed_states:
                file.write(name + '\n')
else:
    state.goto((0, 0))
    state.write('YOU WIN', align='center', font=('Arial', 18, 'normal'))

# Exit

screen.exitonclick()
