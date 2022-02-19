"""
100 Days of Code
The Complete Python Pro Bootcamp
Dra. Angela Yu

Day 18
The Hirst Painting Project
"""

# Imports
import colorgram
import turtle as tt
import random as rd

# Inputs
numb_colors = 23

# Colors
colors = colorgram.extract('painting.jpg', numb_colors)

colors_list = list()
for color in colors:
    r = color.rgb.r/255
    g = color.rgb.g/255
    b = color.rgb.b/255
    colors_list.append((r, g, b))

del colors_list[0]
del colors_list[1]
del colors_list[2]

# Turtle Object
picture = tt.Turtle()
picture.speed(0)
picture.penup()
picture.hideturtle()
position = [-225, -225]

for _ in range(10):
    picture.setpos(position[0], position[1])
    for _ in range(10):
        picture.color(rd.choice(colors_list))
        picture.dot(size=20)
        picture.forward(50)
    position[1] += 50

# Save figure
figure = picture.getscreen()
figure.getcanvas().postscript(file='picture.eps')

# Screen
screen = tt.Screen()
screen.exitonclick()
