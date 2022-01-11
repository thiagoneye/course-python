"""
The Hangman Game
"""

from hm_database import Word_selection

class Letter_test(Word_selection):
    """
    Letter Test

    Class to test if the letters belong to the words.
    """

    def __init__(self):
        """
        Constructor
        """

        Word_selection.__init__(self)

        self.__gap = ''
        self.__checked_letters = list()
        self.__correct_letters = list()
        self.__mistakes = 0

        print('\n')
        self.__generator_gap__()
        self.__print_gap__()


    def __generator_gap__(self):
        """
        Generates leading gaps based on word length.
        """

        for i in self.__word:
            if (i == ' '):
                self.__gap += ' '
            elif (i == '-'):
                self.__gap += '-'
            else:
                self.__gap += '_'

    def __print_gap__(self):
        """
        Print the current gap.
        """

        print(self.__gap)

    def __modify_gap__(self, test):
        """
        Changes the gap.
        """

        __test_multi = self.__word.count(test)

        __idx = 0

        for i in range(len(__test_multi)):
            __idx = self.__word.find(test, __idx)

            __new_gap = list(self.__gap)
            __new_gap[__idx] = test
            self.__gap = "".join(__new_gap)

            __idx += 1

    def __letter_check__(self):
        """
        It imputs a letter, checks if is correct, notify the hit/miss.
        """

        print('\n')
        __test = input('Input a letter! ')
        __test.lower()

        if __test in self.__word:
            self.__checked_letters.append(__test)
            self.__correct_letters.append(__test)
            print('The word contains the letter.\n')
            self.__modify_gap__(test=__test)
            Word_selection.__print_draws__()
            print('\n')
            self.__print_gap__()
        else:
            self.__mistakes += 1
            self.__checked_letters.append(__test)
            Word_selection.__read_draws__(draw=(self.__mistakes))
            print('The word does not contain the letter.\n')
            Word_selection.__print_draws__()
            print('\n')
            self.__print_gap__()
