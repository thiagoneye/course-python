"""
The Hangman Game
"""

import random

class Word_selection(object):
    """
    Word Selection

    Class to extract, transform and load names and figures for the game.
    """

    __options = {1: 'animal', 2: 'artist', 3: 'body', 4: 'car', 5: 'fruit'}

    def __init__(self):
        """
        Constructor
        """

        self.__category = ''
        self.__draw = 4
        self.__fig = ''
        self.__word = ''

        print('Welcome to the Hangman Game!\n')
        self.__read_draws__()
        self.__print_draws__()
        self.__read_draws__(draw=0)

        __choose = input('\nDo you want to choose a word category? [Y] Yes or [N] No\n')

        # Initial settings: choice of category

        if (__choose == 'Y'):
            __new_choose = input('Choose a option: [1] Animal, [2] Artist, [3] Body Part, [4] Car or [5] Fruit\n')
            if (__new_choose in ['1', '2', '3', '4', '5']):
                self.__category = self.__options[int(__new_choose)]
                print('The category will be ' + self.__category + '.')
            else:
                self.__category = self.__sort_category__()
                print('Invalid option, the category will be ' + self.__category + '.')
        elif (__choose == 'N'):
            self.__category = self.__sort_category__()
            print('Then the category will be ' + self.__category + '.')
        else:
            self.__category = self.__sort_category__()
            print('Invalid option, the category will be ' + self.__category + '.')

        # Initial settings: choice of word

        self.__word = self.__read_database__()

    def __sort_category__(self):
        """
        Randomly choose a category.
        """

        __category = random.choice(list(self.__options.values()))

        return __category

    def __read_database__(self):
        """
        Reads the database of the chosen category.
        """

        __path_database = '../project07/category_database/'
        __path_database += self.__category + '.txt'
        __word = random.choice([x.rstrip() for x in open(__path_database)])

        return __word

    def __read_draws__(self, draw=4):
        """
        Read from database.
        """

        self.__draw = draw
        __path_draws = '../project07/gallows_database/'
        __path_draws += 'fig0' + str(self.__draw) + '.txt'
        self.__fig = [x.rstrip() for x in open(__path_draws)]

    def __print_draws__(self):
        """
        Print the selected draw.
        """

        for i in self.__fig:
            print(i)
