"""
The Blackjack
"""

import os
from logo import logo
from Blackjack import Blackjack

print(logo)
print("Welcome to the Blackjack!")

game = Blackjack()

while game.continue_game:
    game.round()

    exit_game = input("Do you want exit the game? [Y] Yes or [N] No.\n")
    while exit_game not in ['Y', 'N']:
        exit_game = input("Invalid option. Please, type again.\n")

    if exit_game == 'Y':
        game.continue_game = False
        print(f"Your money is R$ {game.player.money}.")
        print("Bye bye!")
    else:
        os.system('cls')
