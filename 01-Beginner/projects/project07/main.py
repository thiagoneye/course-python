"""
The Hangman game
"""

import os
from hm_attempts import Letter_test

restart = True
while restart:
    os.system('cls') or None

    print('Welcome to the Hangman Game!\n')
    initial_game = Letter_test()

    verify_restart = input('Do you want restart the game? [Y] Yes or [N] No\n')

    if (verify_restart != 'Y'):
        restart = False
        print('Bye bye!')
