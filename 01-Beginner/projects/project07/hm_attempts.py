"""
The Hangman Game
"""

import os

class Letter_test:
    """
    Letter Test

    Class to test if the letters belong to the words.
    """

    def __init__(self):

        self.gap = ''
        self.checked_letters = list()
        self.correct_letters = list()
        self.mistakes = 0
        self.continue_game = True

        self.generator_gap()
        self.print_gap()

    def generator_gap(self):
        """
        Generates leading gaps based on word length.
        """

        for i in self.word:
            if (i == ' '):
                self.gap += ' '
            elif (i == '-'):
                self.gap += '-'
            else:
                self.gap += '_'

    def print_gap(self):
        """
        Print the current gap.
        """

        print(self.gap)

    def __modify_gap__(self, test):
        """
        Changes the gap.
        """

        __test_multi = self.word.count(test)
        __idx = 0

        for i in range(__test_multi):
            __idx = self.word.find(test, __idx)

            __new_gap = list(self.gap)
            __new_gap[__idx] = test
            self.gap = "".join(__new_gap)

            __idx += 1

    def check_letter(self):
        """
        It imputs a letter, checks if is correct, notify the hit/miss.
        """

        print('\n')
        __test = input('Input a letter! ')
        __test.lower()

        if __test in self.word:
            os.system('cls')
            self.checked_letters.append(__test)
            self.correct_letters.append(__test)
            print('The category is ' + self.category + '.')
            print('The word contains the letter ' + __test + '.\n')
            self.__modify_gap__(test=__test)
            self.print_draws()
            self.print_gap()
            self.__check_win__()
        else:
            os.system('cls')
            self.mistakes += 1
            self.checked_letters.append(__test)
            print('The category is ' + self.category + '.')
            print('The word does not contain the letter ' + __test + '.\n')
            self.read_draws(draw=(self.mistakes))
            self.print_draws()
            self.print_gap()
            self.__check_defeat__()

    def __check_win__(self):
        """
        Check if there was a win in the game.
        """

        if (self.gap.count('_') == 0):
            print('\nYou win!')
            self.continue_game = False

    def __check_defeat__(self):
        """
        Check if there was a defeat in the game.
        """

        if (self.mistakes == 4):
            print('\nGame over!')
            print('The word was ' + self.word + '.')
            self.continue_game = False
