# Imports

import smtplib
import getpass
import datetime as dt
import random as rd

# Functions

def choice_quote() -> str:
    with open('quotes.txt', mode='r') as file:
        quotes = file.readlines()

    return rd.choice(quotes)

def send_a_email(message: str):
    my_email = input('Username: ')
    my_password = getpass.getpass()

    address_email = input('Address: ')

    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)

        connection.sendmail(
            from_addr=my_email,
            to_addrs=address_email,
            msg=message
        )

# Execution

if __name__ == '__main__':
    weekday = dt.datetime.now().weekday()

    if weekday == 0:
        quote = choice_quote()
        message = 'Subject:Motivational Quote\n\n' + quote

        send_a_email(message)
