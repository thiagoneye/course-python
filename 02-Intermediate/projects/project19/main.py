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
leonardo = create_turtle('blue')
raphael = create_turtle('purple')
donatello = create_turtle('red')
michelangelo = create_turtle('orange')

# Positions
set_initial_position(leonardo, 75)
set_initial_position(raphael, 25)
set_initial_position(donatello, -25)
set_initial_position(michelangelo, -75)


# Actions
def start_race():
    continue_race = True
    while continue_race:
        leonardo.forward(rd.randint(0, 10))
        raphael.forward(rd.randint(0, 10))
        donatello.forward(rd.randint(0, 10))
        michelangelo.forward(rd.randint(0, 10))

        if (leonardo.xcor() >= 300.0) or (raphael.xcor() >= 300.0) or (donatello.xcor() >= 300.0) \
                or (michelangelo.xcor() >= 300.0):
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
positions = [leonardo.xcor(), raphael.xcor(), donatello.xcor(), michelangelo.xcor()]
winner_idx = positions.index(max(positions))
winner_name = ['Leonardo', 'Raphael', 'Donatello', 'Michelangelo'][winner_idx]
winner_color = {'Leonardo': 'blue', 'Raphael': 'purple', 'Donatello': 'red', 'Michelangelo': 'orange'}[winner_name]
print(f'The winner is {winner_name}, the {winner_color} turtle.')
if bet == winner_color:
    print('You winn!')
else:
    print('You loser!')
