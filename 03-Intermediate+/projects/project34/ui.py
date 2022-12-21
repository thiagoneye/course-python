"""
100 Days of Code
The Complete Python Pro Bootcamp
Dra. Angela Yu

Day 34

GUI Quiz App
"""

# Imports

from tkinter import *


# Constants

THEME_COLOR = "#375362"


# Classes

class QuizInterface:
    def __init__(self):
        self.window = Tk()
        self.window.title('Quizzler')

        self.window.mainloop()
