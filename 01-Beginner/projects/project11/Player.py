"""
The Blackjack
"""

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
        if not self.double:
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
        if self.dealer:
            self.hand_letter = list()

            idx = 0
            for card in self.hand:
                if idx > 0:
                    self.hand_letter.append("?")
                    idx += 1
                else:
                    self.hand_letter.append(str(card))
        else:
            Hand.convert_hand(self)

    def double_bet(self):
        """
        Double Down! Double the bet.
        """
        Chips.double_bet(self)
        self.add_card()
        self.double = True
