"""
100 Days of Code
The Complete Python Pro Bootcamp
Dra. Angela Yu

Day 29

Building a Password Manager GUI with Tkinter
"""

# Imports

import json
from tkinter import *
from tkinter import messagebox
from password import password_generator

# Password Generator

def get_password():
    password_entry.delete(0, END)
    password = password_generator()
    password_entry.insert(0, password)

# Search Website

def search_website():
    website = website_entry.get()
    try:
        with open('my_pass.json', mode='r') as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showerror(title='Error', message='No Data File Found.')
    else:
        data_file.close()

        if website in data:
            email = data[website]['email']
            password = data[website]['password']
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showerror(title='Error', message=f'No details for {website} exists.')

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
    new_data = {
        website: {
            'email': user,
            'password': password
            }
        }

    # Actions
    if len(website) == 0 or len(password) == 0 or user == '@outlook.com':
        messagebox.showerror(title='Error', message='The fields cannot be empty!')
    else:
        try:
            with open('my_pass.json', mode='r') as data_file:
                # Reading old data
                data = json.load(data_file)
                # Updating old data with new data
                data.update(new_data)
        except FileNotFoundError:
            data = new_data

        with open('my_pass.json', mode='w') as data_file:
           # Saving Updating data
            json.dump(data, data_file, indent=4)

        data_file.close()
        website_entry.delete(0, END)
        password_entry.delete(0, END)

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

website_entry = Entry(width=33)
website_entry.grid(row=1, column=1)
website_entry.focus()

user_entry = Entry(width=52)
user_entry.grid(row=2, column=1, columnspan=2)
user_entry.insert(0, '@outlook.com')

password_entry = Entry(width=33)
password_entry.grid(row=3, column=1)

# Buttons

search_button = Button(text='Search', width=15,  command=search_website)
search_button.grid(row=1, column=2)

generate_password_button = Button(text='Generate Password', command=get_password)
generate_password_button.grid(row=3, column=2)

add_button = Button(text='Add', width=44, command=save_data)
add_button.grid(row=5, column=1, columnspan=2)

window.mainloop()
