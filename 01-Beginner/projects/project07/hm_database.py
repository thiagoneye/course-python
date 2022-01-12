"""
The Hangman Game
"""

import random

class Read_database:
    """
    Read Database

    Class to extract, transform and load names and/or figures for the game.
    """

    __options = {1: 'animal', 2: 'artist', 3: 'body', 4: 'car', 5: 'fruit'}

    def __init__(self):
        """
        Constructor
        """

        self.category = ''
        self.draw = 4
        self.fig = ''
        self.word = ''

        self.read_draws()
        self.print_draws()
        self.read_draws(draw=0)
        self.__choose_category__()
        self.__choose_word__()

    def __choose_category__(self):
        """
        Chooses the category of the game.
        """

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

    def __sort_category__(self):
        """
        Randomly choose a category.
        """

        __category = random.choice(list(self.__options.values()))

        return __category

    def __choose_word__(self):
        """
        Reads the database of the chosen category and chooses the word.
        """

        __path_database = '../project07/category_database/'
        __path_database += self.category + '.txt'
        self.word = random.choice([x.rstrip() for x in open(__path_database)])

    def read_draws(self, draw=4):
        """
        Read from database.
        """

        self.draw = draw
        __path_draws = '../project07/gallows_database/'
        __path_draws += 'fig0' + str(self.draw) + '.txt'
        self.fig = [x.rstrip() for x in open(__path_draws)]

    def print_draws(self):
        """
        Print the selected draw.
        """

        for i in self.fig:
            print(i)
