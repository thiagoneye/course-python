# PyPassword Generator

# Imports

import random

# Code ASCII (Unicode)

letters = list(range(65, 91)) + list(range(97, 123))
symbols = [33, 35, 36, 37, 38, 40, 41, 42, 43]
numbers = list(range(48, 58))

# Inputs

print('Welcome to the PyPassword Generator!')
len1 = int(input('How many letters would you like in your password? '))
len2 = int(input('How many symbols would you like? '))
len3 = int(input('How many numbers would you like? '))

# Code

password = list()

for i in range(len1):
    password.append(random.choice(letters))
for i in range(len2):
    password.append(random.choice(symbols))
for i in range(len3):
    password.append(random.choice(numbers))

random.shuffle(password)

password_code = ''
for i in password:
    password_code += chr(i)

# Outputs

print('Here is your password:', password_code)
