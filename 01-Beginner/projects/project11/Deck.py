"""
The Blackjack
"""

import random

class Deck(object):
    """
    The Deck Class.
    """
    deck = list()
    __cards_options = {1: 'A', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7',
                       8: '8', 9: '9', 10: '10', 11: 'J', 12: 'Q', 13: 'K'}

    def __init__(self):
        """
        Constructor.
        """
        self.deck = list()
        self.restart_deck()

    def restart_deck(self):
        """
        Get(restart) the cards to the game.
        """
        self.deck = 4*list(range(1,14))

    def pull_card(self):
        """
        Pull a card from the deck.
        """
        card = random.choice(self.deck)
        self.deck.remove(card)

        return card

    def convert_card(self, card):
        """
        Converts a card from number to string.
        """
        card_letter = self.__cards_options[card]

        return card_letter
