"""
The Hangman Game
"""

import random

class word_selection(object):
    """
    Word Selection

    Class to extract, transform and load names and figures for the game.
    """

    category = ''
    __options = {1: 'animal', 2: 'artist', 3: 'body', 4: 'car', 5: 'fruit'}
    __word = ''

    def __init__(self):
        """
        Constructor
        """

        print('Welcome to the Hangman Game!\n')
        self.read_draws()

        __choose = input('\nDo you want to choose a word category? [Y] Yes or [N] No\n')

        # Initial settings: choice of category

        if (__choose == 'Y'):
            __new_choose = input('Choose a option: [1] Animal, [2] Artist, [3] Body Part, [4] Car or [5] Fruit\n')
            if (__new_choose in ['1', '2', '3', '4', '5']):
                self.category = self.__options[int(__new_choose)]
                print('The category will be ' + self.category + '.')
            else:
                self.category = self.__sort_category__()
                print('Invalid option, the category will be ' + self.category + '.')
        elif (__choose == 'N'):
            self.category = self.__sort_category__()
            print('Then the category will be ' + self.category + '.')
        else:
            self.category = self.__sort_category__()
            print('Invalid option, the category will be ' + self.category + '.')

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
        __path_database += self.category + '.txt'
        __word = random.choice([x.rstrip() for x in open(__path_database)])

        return __word

    def read_draws(self, draw=5):
        """
        Read from database and print the selected draw.
        """

        self.draw = draw
        __path_draws = '../project07/gallows_database/'
        __path_draws += 'fig0' + str(self.draw) + '.txt'
        self.fig = [x.rstrip() for x in open(__path_draws)]

        for i in self.fig:
            print(i)
