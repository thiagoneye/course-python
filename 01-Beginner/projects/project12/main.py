"""
Number Guessing Game!
"""

# Imports

import os
import random
from logo import logo

# Main

data_options = {'easy': 10, 'hard': 5}

restart_game = True
while restart_game:
    os.system('cls')

    # Prints
    print(logo)
    print('Welcome to the Number Guessing Game!')
    print('I\'m thinking of a number between 1 and 100.')

    # Choose a difficulty
    option = input('Choose a difficulty. Type \'easy\' or \'hard\': ')
    while option not in ['easy', 'hard']:
        option = input('Invalid option! Please, try again: ')

    # Variables
    number_attempt = data_options[option]
    mistakes = 0
    number = random.randint(1, 100)

    continue_game = True
    while continue_game:
        print(f'\nYou have {number_attempt-mistakes} attempts remaining to guess the number.')

        # Request a number
        attempt = input('Make a guess: ')
        while not attempt.isdigit():
            attempt = input('Invalid option! Please, try again: ')

        attempt = int(attempt)

        # Verify the attempt
        if mistakes == number_attempt:
            print(f'You\'ve run out of guesses, you lose. The answer was {number}')
            continue_game = False
        else:
            if attempt < number:
                print('\nToo low.')
                continue_game = True
                mistakes += 1
            elif attempt > number:
                print('\nToo high.')
                continue_game = True
                mistakes += 1
            else:
                print(f'\nYou got it! The answer was {number}.')
                continue_game = False

    # Verify if you want to play again
    play_again = input('\nDo you want play again? Type \'yes\' or \'no\': ')
    while play_again not in ['yes', 'no']:
        play_again = input('Invalid option! Please, try again: ')

    if play_again == 'yes':
        restart_game = True
    else:
        print('Bye bye!!!')
        restart_game = False
