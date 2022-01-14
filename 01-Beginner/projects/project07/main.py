"""
The Hangman game
"""

import os
from hm_game import Hangman

restart = True
while restart:
    os.system('cls')
    initial_game = Hangman()
    verify_restart = input('Do you want restart the game? [Y] Yes or [N] No\n')

    if (verify_restart != 'Y'):
        restart = False
        print('Bye bye!')
