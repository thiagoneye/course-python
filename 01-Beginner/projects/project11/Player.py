"""
The Blackjack
"""

import numpy as np
from Hand import Hand
from Chips import Chips

class Player(Hand, Chips):
    """
    The Player Class.
    """

    def __init__(self, my_deck, is_dealer=False):
        """
        Constructor.
        """
        self.dealer = is_dealer

        Hand.__init__(self, my_deck)
        Chips.__init__(self)

    def add_card(self):
        """
        Adds a new card to the hand.
        """
        if (self.score < 21):
            if self.dealer:
                if (len(self.hand) < 5):
                    Hand.add_card(self)
                else:
                    print("You have reached the limit of cards in your hand.")
            else:
                Hand.add_card(self)

    def convert_hand(self):
        """
        Converts the hand cards from numbers to strings.
        """
        Hand.convert_hand(self)
        if self.dealer:
            self.hand_dealer = np.array(self.hand_letter)
            self.hand_dealer[1:] = '?'
            self.hand_dealer = list(self.hand_dealer)

    def double_bet(self):
        """
        Double Down! Double the bet.
        """
        Chips.double_bet(self)
        self.add_card()
