"""
The Blackjack
"""

class Chips(object):
    """
    The Chips Class.
    """

    def __init__(self):
        """
        Constructor.
        """
        self.money = 500
        self.bet = 10

    def set_bet(self):
        """
        Sets a bet.
        """
        print(f"You have R$ {self.money}.")
        value = input("What is your bit? Type a value:\nR$ ")
        while ((not value.isdigit()) or (value > self.money)):
            if not value.isdigit():
                value = input("Invalid option. Please type a integer value.\nR$ ")
            else:
                value = input(f"You can bet a maximum R$ {self.money}. Please type another value.\nR$ ")

        if value > self.bet:
            self.bet = int(value)

        print(f"The bet is R$ {self.bet}.")

    def double_bet(self):
        """
        Double Down! Double the bet.
        """
        self.bet *= 2
