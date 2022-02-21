"""
100 Days of Code
The Complete Python Pro Bootcamp
Dra. Angela Yu

Day 19
Instances, State and Higher Order Functions
"""

# Imports
from turtle import Turtle, Screen

# Objects
timmy = Turtle()


# Functions
def move_forwards():
    timmy.forward(10)


# Screen
screen = Screen()
screen.listen()
screen.onkey(key='space', fun=move_forwards)
screen.exitonclick()

"""
- Ouvinte de Eventos: Ato ao qual o computador aguarda uma ação para executar outra.
- Funções de Ordem Superior: Ao utilizar uma função como entrada para outra, não é necessário o uso dos parênteses ao
final da mesma.
"""
