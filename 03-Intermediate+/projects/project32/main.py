"""
100 Days of Code
The Complete Python Pro Bootcamp
Dra. Angela Yu

Day 32

Automated Birthday Wisher
"""

# Imports

import os
import smtplib
import getpass
import random as rd
import pandas as pd
import datetime as dt

# Constants

PATH = 'letter_templates'

# Functions

def check_date(month: int, day: int) -> bool:
    today = dt.datetime.today()
    today = (today.month, today.day)

    if today == (month, day):
        return True
    else:
        return False

def get_letter(name: str) -> str:
    for (_, _, files) in os.walk(PATH):
        file_path = rd.choice(files)
        file_path = '.\\' + PATH + '\\' + file_path

    with open(file_path, mode='r') as file:
        letter = file.read()

    letter = letter.replace('[NAME]', name)

    return letter

def send_a_email(connection, address_email: str, message: str):
    message = 'Subject:Happy Birthday\n\n' + message

    connection.sendmail(
        from_addr=my_email,
        to_addrs=address_email,
        msg=message
    )

# Read Data

birthdays = pd.read_csv('birthdays.csv')

# Connection

my_email = input('Username: ')
my_password = getpass.getpass()

connection = smtplib.SMTP('smtp.gmail.com')
connection.starttls()
connection.login(user=my_email, password=my_password)

# Execution

for row in range(len(birthdays)):
    month = int(birthdays.loc[row, 'month'])
    day = int(birthdays.loc[row, 'day'])

    if check_date(month, day):
        name = birthdays.loc[row, 'name']
        address_email = birthdays.loc[row, 'email']

        letter = get_letter(name)
        send_a_email(connection, address_email, message=letter)

connection.close()
