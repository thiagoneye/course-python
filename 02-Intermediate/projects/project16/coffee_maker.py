"""
100 Day of Code
The Complete Python Pro Bootcamp
Prof. Dr. Angela Yu

Project 16
Coffee Machine
"""


class CoffeeMaker:
    """Models the machine that makes the coffee"""
    def __init__(self):
        self.resources = {'water': 300,
                          'milk': 200,
                          'coffee': 100}

    def report(self):
        """Prints a report of all resources.
        e.g.
        Water: 300ml
        Milk: 200ml
        Coffee: 100g"""

        print(f'\nWater: {self.resources["water"]}ml')
        print(f'Milk: {self.resources["milk"]}ml')
        print(f'Coffee: {self.resources["coffee"]}g')

    def is_resource_sufficient(self, drink):
        """Parameter drink: (MenuItem) The MenuItem object to make.
        Returns True when the drink order can be made, False if ingredients are insufficient.
        e.g. True"""
        can_make = True
        for item in drink.ingredients:
            if drink.ingredients[item] > self.resources[item]:
                print(f'Sorry there is not enough {item}.')
                can_make = False

        return can_make

    def make_coffee(self, order):
        """Parameter order: (MenuItem) The MenuItem object to make.
        Deducts the required ingredients from the resources."""
        for item in order.ingredients:
            self.resources[item] -= order.ingredients[item]

        print(f'\nHere is your {order.name}. Enjoy!')
