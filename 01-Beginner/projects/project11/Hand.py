"""
The Blackjack
"""

import numpy as np

class Hand(object):
    """
    The Hand Class.
    """

    def __init__(self, my_deck):
        """
        Constructor.
        """
        self.double = False

        self.get_hand(my_deck)

    def get_hand(self, my_deck):
        """
        Generates the starting hand.
        """
        self.hand = list()
        self.hand_letter = list()
        self.score = 0

        self.deck = my_deck

        self.hand.append(self.deck.pull_card())
        self.hand.append(self.deck.pull_card())

        self.convert_hand()
        self.get_score()

    def convert_hand(self):
        """
        Converts the hand cards from numbers to strings.
        """
        self.hand_letter = [self.deck.convert_card(i) for i in self.hand]

    def get_score(self):
        """
        Generates the score of the hand cards.
        """
        hand_array = np.array(self.hand)

        # Verify the J, Q and K cards
        hand_array[hand_array > 10] = 10

        # Verify the A card
        if np.any(hand_array == 1):
            if (np.sum(hand_array)+10 <= 21):
                hand_array[self.hand.index(1)] = 11

        self.score = np.sum(hand_array)

    def add_card(self):
        """
        Hit! Adds a new card to the hand.
        """
        self.hand.append(self.deck.pull_card())
        self.convert_hand()
        self.get_score()

    """
    def split(self):
        \"""
        Splits the hand cards.
        \"""
        if ((len(self.hand) == 2) and (self.hand[0] == self.hand[1])):
            self.hand_split = self.hand[0]
            self.hand = self.hand[0]
        else:
            print("You can't split the cards.")
    """
