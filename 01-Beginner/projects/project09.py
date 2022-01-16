"""
Secret Auction
"""

import os

print("Welcome to the secret auction program.")

exit_program = False
data = dict()

while not exit_program:
    name = input("What is your name?\n")
    bid = input("What is your bit?\nR$ ")

    while not bid.isnumeric():
        bid = input("Invalid option, please enter a numeric value.\nR$ ")

    data[float(bid)] = name

    other_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n")

    while other_bidders not in ['yes', 'no']:
        other_bidders = input("Invalid option, please type 'yes' or 'no'.\n")

    if other_bidders == 'no':
        exit_program = True

    os.system('cls')

winner = data[max(data.keys())]
print(f"The winner is {winner} with a bit of R$ {max(data.keys()):.2f}.")
