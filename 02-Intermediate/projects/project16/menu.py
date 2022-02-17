"""
100 Day of Code
The Complete Python Pro Bootcamp
Prof. Dr. Angela Yu

Project 16
Coffee Machine
"""


class MenuItem:
    """Models each Menu Item."""
    def __init__(self, name, cost, water, milk, coffee):
        self.name = name
        self.cost = cost
        self.ingredients = {'water': water, 'milk': milk, 'coffee': coffee}


class Menu:
    """Models the Menu with drinks."""
    def __init__(self):
        self.menu = [MenuItem(name='espresso', cost=1.5, water=50, milk=0, coffee=18),
                     MenuItem(name='latte', cost=2.5, water=200, milk=150, coffee=24),
                     MenuItem(name='cappuccino', cost=3.0, water=250, milk=100, coffee=24)]

    def get_items(self):
        """Returns all the names of the available menu items as a concatenated string.
        e.g. “latte/espresso/cappuccino”"""
        options = ''

        for items in self.menu:
            options += f'{items.name}/'

        return options

    def find_drinks(self, order_name):
        """Parameter order_name: (str) The name of the drinks order.
        Searches the menu for a particular drink by name.
        Returns a MenuItem object if it exists, otherwise returns None."""
        for item in self.menu:
            if item.name == order_name:
                return item

        print('Sorry that item is not available.')
