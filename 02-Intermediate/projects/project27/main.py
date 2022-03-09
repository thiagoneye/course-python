"""
100 Days of Code
The Complete Python Pro Bootcamp
Dra. Angela Yu

Day 27
Tkinter, *args, **kwargs and Creating GUI Programs

Mile to Kilometers Converter Project
"""

# Imports

import tkinter as tk

# Window

window = tk.Tk()
window.title('Miles to Kilometers')
# window.minsize(width=300, height=100)
# window.maxsize(width=300, height=100)
window.config(padx=100)

# Entry

value_input = tk.Entry(width=7)
value_input.grid(column=0, row=0)

# Label 1

label1 = tk.Label(text='miles')
label1.grid(column=1, row=0)

# Label 2

label2 = tk.Label(text='is equal to')
label2.grid(column=0, row=1)

# Label 3

label3 = tk.Label(text=f'0 Km')
label3.grid(column=0, row=2)

# Button

def convert_value():
    if not value_input.get().isnumeric():
        value_output = 0
    else:
        value_output = float(value_input.get())
        value_output *= 1.60934
        value_output = int(value_output)
    return value_output

def button_clicked():
    label3.config(text=f'{convert_value()} Km')

button = tk.Button(text='Calculate', command=button_clicked)
button.grid(column=0, row=3)

# Exhibition

window.mainloop()