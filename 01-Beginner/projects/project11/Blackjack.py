"""
The Blackjack
"""

from Deck import Deck
from Player import Player

class Blackjack(object):
    """
    The Blackjack Class.
    """
    def __init__(self):
        """
        Constructor.
        """
        self.stand_round = False
        self.surrender_round = False

        self.my_deck = Deck()
        self.player = Player(self.my_deck)
        self.croupier = Player(self.my_deck, is_dealer=True)

        print("Let the game start!")

    def __del__(self):
        """
        Destructor.
        """
        print("Endgame!")

    def start_round(self):
        """
        Start the round.
        """
        self.stand_round = False
        self.surrender_round = False

        self.my_deck.restart_deck()
        self.player.get_hand(self.my_deck)
        self.croupier.get_hand(self.my_deck)

        print("Your cards:")
        print(*self.player.hand_letter)

        print("The dealer cards:")
        print(*self.croupier.hand_letter)

        option = input("What do you want to do? [1] Stand [2] ")

    def stand(self):
        """
        Not pulling any more cards.
        """
        self.stand_round = True

    def surrender(self):
        """
        Abandon the round.
        """
        self.surrender_round = True

    def verify_scores(self):
        """
        Checks who won the round and took the bets.
        """
