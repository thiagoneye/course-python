"""
Secret Auction
"""

import os
from logo import logo

print(logo)
print("Welcome to the secret auction program.")

exit_program = False
data = dict()

while not exit_program:
    name = input("What is your name?\n")
    bid = input("What is your bit?\nR$ ")

    while not bid.isnumeric():
        bid = input("Invalid option, please enter a numeric value.\nR$ ")

    data[name] = float(bid)

    other_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n")

    while other_bidders not in ['yes', 'no']:
        other_bidders = input("Invalid option, please type 'yes' or 'no'.\n")

    if other_bidders == 'no':
        exit_program = True

    os.system('cls')

winner = list(data.keys())[0]

for key in data:
    if (data[key] > data[winner]):
        winner = key

print(f"The winner is {winner} with a bit of R$ {data[winner]:.2f}.")
