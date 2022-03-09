"""
100 Days of Code
The Complete Python Pro Bootcamp
Dra. Angela Yu

Day 27
Tkinter, *args, **kwargs and Creating GUI Programs
"""

# Imports

import tkinter

# Window

window = tkinter.Tk()
window.title('My First GUI Program')
# window.minsize(width=500, height=300)

# Label

my_label = tkinter.Label(text='I am a label', font=('Arial', 24, 'bold', 'italic'))
my_label.grid(column=0, row=0)
# my_label.place(x=0, y=0)
# my_label.pack(side='left')
# my_label['text'] = 'New Text'
my_label.config(text='New Text')
my_label.config(padx=50, pady=50)

# Entry

my_input = tkinter.Entry()
my_input.grid(column=0, row=1)
# my_input.pack()

# Button

def button_clicked():
    my_label.config(text=my_input.get())

button = tkinter.Button(text='Submit', command=button_clicked)
button.grid(column=1, row=1)

# Main

window.mainloop()