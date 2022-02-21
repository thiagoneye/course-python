"""
100 Days of Code
The Complete Python Pro Bootcamp
Dra. Angela Yu

Project 19
Turtle Race
"""

# Imports
from turtle import Turtle, Screen
import random as rd


# Functions
def create_turtle(color):
    """Create a new turtle."""
    new_turtle = Turtle(shape='turtle')
    new_turtle.color(color)
    return new_turtle


def set_initial_position(turtle, ycor):
    """Set the turtle's starting position."""
    turtle.hideturtle()
    turtle.penup()
    turtle.setpos(x=-300, y=ycor)
    turtle.pendown()
    turtle.showturtle()


# Objects
turtle_names = ['Leonardo', 'Raphael', 'Donatello', 'Michelangelo']
turtle_colors = ['blue', 'purple', 'red', 'orange']
turtle_coord = [75, 25, -25, -75]

turtles = list()
for idx in range(len(turtle_names)):
    new_turtle = create_turtle(turtle_colors[idx])
    set_initial_position(new_turtle, turtle_coord[idx])
    turtles.append(new_turtle)


# Actions
def run(turtle):
    turtle.forward(rd.randint(0, 10))


def get_xcor(turtle):
    xcor = turtle.xcor()
    return xcor


def start_race():
    continue_race = True
    while continue_race:
        new_positions = list()
        for turtle in turtles:
            run(turtle)
            new_positions.append(get_xcor(turtle))

        if max(new_positions) >= 300.0:
            continue_race = False


# Screen
screen = Screen()
# screen.setup(width=400, height=400) # Window Size
bet = screen.textinput(title='Make your bet', prompt='Who will win the race? Enter a color:')

# Start Game
screen.listen()
screen.onkey(fun=start_race, key='space')

# Exit Window
screen.exitonclick()

# Bet
positions = [get_xcor(turtle) for turtle in turtles]
winner_idx = positions.index(max(positions))
winner_name = turtle_names[winner_idx]
winner_color = turtle_colors[winner_idx]

# Outputs
print(f'The winner is {winner_name}, the {winner_color} turtle.')
if bet == winner_color:
    print('You winn!')
else:
    print('You loser!')
