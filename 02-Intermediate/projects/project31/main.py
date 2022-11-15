"""
100 Days of Code
The Complete Python Pro Bootcamp
Dra. Angela Yu

Day 31

Flash Card App Capstone Project
"""

# Imports

import random
import pandas as pd
from tkinter import *

# Contants

BACKGROUND_COLOR = "#B1DDC6"

# Actions

current_card = dict()
to_learn = dict()

try:
    data = pd.read_csv('data/words_to_learn.csv')
except FileNotFoundError:
    data = pd.read_csv('data/french_words.csv')

to_learn = data.to_dict(orient='records')

def next_card():
    global current_card, flip_timer
    current_card = random.choice(to_learn)

    window.after_cancel(flip_timer)

    canvas.itemconfig(card_image, image=card_front_img)
    canvas.itemconfig(card_title, text='French', fill='black')
    canvas.itemconfig(card_word, text=current_card['French'], fill='black')

    flip_timer = window.after(3000, func=flip_card)

def is_known():
    to_learn.remove(current_card)
    data = pd.DataFrame(to_learn)
    data.to_csv('data/words_to_learn.csv', index=False)

    next_card()

def flip_card():
    canvas.itemconfig(card_image, image=card_back_img)
    canvas.itemconfig(card_title, text='English', fill='white')
    canvas.itemconfig(card_word, text=current_card['English'], fill='white')

# UI Setup

window = Tk()
window.title('Flash Card App')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

card_back_img = PhotoImage(file='images/card_back.png')
card_front_img = PhotoImage(file='images/card_front.png')

canvas = Canvas(width=800, height=526)
card_image = canvas.create_image(400, 263, image=card_front_img)

card_title = canvas.create_text(400, 150, text='', font=('Arial', 40, 'italic'))
card_word = canvas.create_text(400, 263, text='', font=('Arial', 60, 'bold'))

canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

# Buttons

button_wrong_img = PhotoImage(file='images/wrong.png')
button_wrong = Button(image=button_wrong_img, highlightthickness=0, command=next_card)
button_wrong.grid(row=1, column=0)

button_right_img = PhotoImage(file='images/right.png')
button_right = Button(image=button_right_img, highlightthickness=0, command=is_known)
button_right.grid(row=1, column=1)

# Execution

next_card()
window.mainloop()
