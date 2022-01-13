"""
The Hangman Game
"""

from hm_database import Read_database
from hm_attempts import Letter_test

class Hangman(Read_database, Letter_test):
    """
    Hangman

    Class to execute the game.
    """

    def __init__(self):
        """
        Constructor
        """

        print('Welcome to the Hangman Game!\n')

        Read_database.__init__(self)
        Letter_test.__init__(self)

        while self.continue_game:
            self.check_letter()
