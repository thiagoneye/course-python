"""
100 Days of Code
The Complete Python Pro Bootcamp
Dra. Angela Yu

Day 29

Building a Password Manager GUI with Tkinter
"""

# Imports

from tkinter import *
from tkinter import messagebox
from password import password_generator

# Password Generator

def get_password():
    password_entry.delete(0, END)
    password = password_generator()
    password_entry.insert(0, password)

# Save Password

def clear_entries():
    website_entry.delete(0, END)
    user_entry.delete(0, END)
    user_entry.insert(0, '@outlook.com')
    password_entry.delete(0, END)

def save_data():
    # Entries values
    website = website_entry.get()
    user = user_entry.get()
    password = password_entry.get()

    # Actions
    if (len(website) != 0) or (len(user) != 0) or (len(password) != 0):
        is_ok = messagebox.askokcancel(title=website,
                                       message=f'These are the details entered: \n\nUser: {user} \nPassword: {password}'
                                               f'\n\nIs it ok to save?')

        if is_ok:
            with open('my_pass.txt', mode='a') as file:
                file.writelines(f'{website} | {user} | {password}\n')

            messagebox.showinfo(title='Success', message='Data has been saved successfully!')
            clear_entries()
    else:
        messagebox.showerror(title='Error', message='The fields cannot be empty!')

# UI Setup

window = Tk()
window.title('Password Manager')
window.config(padx=50, pady=50)

lock_img = PhotoImage(file='logo.png')
canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=lock_img)
canvas.grid(row=0, column=1)

# Labels

website_label = Label(text='Website:')
website_label.grid(row=1, column=0)

user_label = Label(text='Email/Username:')
user_label.grid(row=2, column=0)

password_label = Label(text='Password:')
password_label.grid(row=3, column=0)

# Entries

website_entry = Entry(width=52)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()

user_entry = Entry(width=52)
user_entry.grid(row=2, column=1, columnspan=2)
user_entry.insert(0, '@outlook.com')

password_entry = Entry(width=33)
password_entry.grid(row=3, column=1)

# Buttons

generate_password_button = Button(text='Generate Password', command=get_password)
generate_password_button.grid(row=3, column=2)

add_button = Button(text='Add', width=44, command=save_data)
add_button.grid(row=5, column=1, columnspan=2)

window.mainloop()
