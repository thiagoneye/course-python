"""
100 Day of Code
The Complete Python Pro Bootcamp
Prof. Dr. Angela Yu

Project 16
Coffee Machine
"""


# Imports

from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

import os

# Objects

menu_coffee = Menu()
coffee_maker = CoffeeMaker()
money_coffee = MoneyMachine()

# Main

options = menu_coffee.get_items()

more_coffee = True
while more_coffee:
    os.system('cls')

    order_name = input(f'What would you like? ({options}): ')
    while order_name not in options:
        if order_name == 'report':
            coffee_maker.report()
            money_coffee.report()

        order_name = input(f'\nWhat would you like? ({options}): ')

    drink = menu_coffee.find_drinks(order_name)

    if coffee_maker.is_resource_sufficient(drink) and money_coffee.make_payment(drink.cost):
        coffee_maker.make_coffee(drink)

    option_continue = input('\nDo you like more coffee? Type "yes" or "no". ')
    if option_continue not in ['yes', 'no']:
        option_continue = input('Invalid option, try again.')

    if option_continue == 'no':
        more_coffee = False
