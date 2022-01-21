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
        self.continue_game = True

        self.my_deck = Deck()
        self.player = Player(self.my_deck)
        self.croupier = Player(self.my_deck, is_dealer=True)

        print("Let the game start!")

    def round_game(self):
        """
        Start the round.
        """
        self.hit_round = True
        self.result_round = 0   # [0] Draw, [1] Player Win or [2] Dealer Win

        self.my_deck.restart_deck()
        self.player.get_hand(self.my_deck)
        self.croupier.get_hand(self.my_deck)

        # Player Hit

        print(f"\nThe dealer have R$ {self.croupier.money}.")
        self.player.set_bet()
        self.croupier.bet = self.player.bet

        while self.hit_round:
            self.print_cards()

            option = input("\nWhat do you want to do? [1] Hit, [2] Stand, [3] Double Down or [4] Surrender.\n")
            while option not in ['1', '2', '3', '4']:
                option = input("Invalid option. Please, type again.\n")

            if (option == '1'):
                self.hit()
            elif (option == '2'):
                self.stand()
            elif (option == '3'):
                self.double()
            else:
                self.surrender()

        # Dealer Hit

        if (self.player.score > 21):
            dealer_hit = False
        else:
            if (self.player.score > self.croupier.score):
                dealer_hit = True
            elif (self.player.score == self.croupier.score):
                if (self.croupier.score < 16):
                    dealer_hit = True
                else:
                    dealer_hit = False
            else:
                dealer_hit = False

        while dealer_hit:
            self.croupier.add_card()
            if (self.croupier.score >= 21):
                dealer_hit = False
            else:
                if (self.player.score < self.croupier.score):
                    dealer_hit = False
                elif (self.player.score == self.croupier.score):
                    if (self.croupier.score >= 16):
                        dealer_hit = False

        # Winner

        if (option != '4'):
            self.verify_scores()

        if (option == '3'):
            self.player.bet = self.croupier.bet

    def print_cards(self):
        """
        Prints the cards on the hands.
        """
        print("\nYour cards:")
        print(*self.player.hand_letter)

        print("\nThe dealer's cards:")
        print(*self.croupier.hand_dealer)

    def verify_scores(self):
        """
        Checks who won the round and took the bets.
        """
        if (self.player.score > 21):
            if (self.croupier.score > 21):
                self.result_round = 0
            else:
                self.result_round = 2
        else:
            if ((self.croupier.score > 21) or (self.player.score > self.croupier.score)):
                self.result_round = 1
            elif (self.player.score == self.croupier.score):
                self.result_round = 0
            else:
                self.result_round = 2

        print("\nThe dealer's cards:")
        print(*self.croupier.hand_letter)

        if (self.result_round == 1):
            print("\nYou win the round!")
            self.player.money += self.player.bet
            self.croupier.money -= self.player.bet
        elif (self.result_round == 2):
            print("\nYou defeat the round!")
            self.player.money -= self.player.bet
            self.croupier.money += self.player.bet
        else:
            print("\nThe result was draw!")

    def verify_money(self):
        """
        Verifys the endgame.
        """
        if (self.player.money == 0):
            print("Your money is zero. You defeat!")
            self.continue_game = False
        elif (self.croupier.money == 0):
            print("The dealer's money is zero. You win!")
            self.continue_game = False

    def hit(self):
        """
        Pull a card.
        """
        self.player.add_card()
        if (self.player.score >= 21):
            print("\nYour cards:")
            print(*self.player.hand_letter)
            self.hit_round = False

    def stand(self):
        """
        Not pulling any more cards.
        """
        self.hit_round = False

    def double(self):
        """
        Double the bet.
        """
        self.player.double_bet()
        print("\nYour cards:")
        print(*self.player.hand_letter)
        self.hit_round = False

    def surrender(self):
        """
        Abandon the round.
        """
        self.hit_round = False
        self.player.money -= int(self.player.bet/2)
        self.croupier.money += int(self.player.bet/2)
