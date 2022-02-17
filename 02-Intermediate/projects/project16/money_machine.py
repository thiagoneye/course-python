"""
100 Day of Code
The Complete Python Pro Bootcamp
Prof. Dr. Angela Yu

Project 16
Coffee Machine
"""


class MoneyMachine:

    CURRENCY = '$'

    COIN_VALUES = {'penny': 0.01,
                   'nickel': 0.05,
                   'dime': 0.10,
                   'quarter': 0.25}

    def __init__(self):
        self.profit = 0.0
        self.money_received = 0.0

    def report(self):
        """Prints the current profit
        e.g. Money: $0"""
        print(f'Money: {self.profit}')

    def process_coin(self):
        """Returns the total calculated from coins inserted."""
        print('\nPlease insert coins.')

        for coin in self.COIN_VALUES:
            self.money_received += float(input(f'How many {coin}?: ')) * self.COIN_VALUES[coin]

        return self.money_received

    def make_payment(self, cost):
        """Parameter cost: (float) The cost of the drink.
        Returns True when payment is accepted, or False if insufficient.
        e.g. False
        """
        self.process_coin()

        if self.money_received >= cost:
            change = round(self.money_received - cost, 2)

            self.profit += cost
            self.money_received = 0

            print(f'Here is {self.CURRENCY}{change} in change.')

            return True
        else:
            self.money_received = 0

            print('Sorry that\'s not enough money. Money refunded.')

            return False
