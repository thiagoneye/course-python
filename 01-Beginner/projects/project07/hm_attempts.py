"""
The Hangman Game
"""

from hm_database import Read_database

class Letter_test(Read_database):
    """
    Letter Test

    Class to test if the letters belong to the words.
    """

    def __init__(self):
        """
        Constructor
        """

        Read_database.__init__(self)

        self.gap = ''
        self.checked_letters = list()
        self.correct_letters = list()
        self.mistakes = 0
        self.__continue = True

        self.__generator_gap__()
        self.__print_gap__()

        while self.__continue:
            self.__check_letter__()

    def __generator_gap__(self):
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

    def __print_gap__(self):
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

    def __check_letter__(self):
        """
        It imputs a letter, checks if is correct, notify the hit/miss.
        """

        print('\n')
        __test = input('Input a letter! ')
        __test.lower()

        if __test in self.word:
            self.checked_letters.append(__test)
            self.correct_letters.append(__test)
            print('The word contains the letter.\n')
            self.__modify_gap__(test=__test)
            self.print_draws()
            self.__print_gap__()
            self.__check_win__()
        else:
            self.mistakes += 1
            self.checked_letters.append(__test)
            print('The word does not contain the letter.\n')
            self.read_draws(draw=(self.mistakes))
            self.print_draws()
            self.__print_gap__()
            self.__check_defeat__()

    def __check_win__(self):
        """
        Check if there was a win in the game.
        """

        if (self.gap.count('_') == 0):
            print('\nYou win!')
            self.__continue = False

    def __check_defeat__(self):
        """
        Check if there was a defeat in the game.
        """

        if (self.mistakes == 4):
            print('\nGame over!')
            print('The word was ' + self.word + '.')
            self.__continue = False
