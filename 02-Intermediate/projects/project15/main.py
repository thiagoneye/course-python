"""
Coffee Machine
"""

# Imports

from functions import report, insertCoins, checkResources, processCoins, checkTransaction
from data import menu, resources, units, coins
import os

# Inputs

safeBox = 0

# Main

continueMachine = True

while continueMachine:
    os.system('cls')
    continueOption = True
    sucessfulTransaction = False

    while continueOption:
        optionCoffee = input('What would you like? (espresso/latte/cappuccino): ')

        while (optionCoffee not in ['espresso', 'latte', 'cappuccino', 'report']):
            optionCoffee = input('Invalid option, type again: ')

        if (optionCoffee == 'report'):
            report(resources, units, safeBox)
        else:
            continueOption = False

    sucessfulResources = checkResources(optionCoffee, resources, menu)

    if sucessfulResources:
        amountOfCoins = insertCoins()
        sucessfulTransaction, safeBox = checkTransaction(amountOfCoins, coins, optionCoffee, menu, resources, safeBox)

    if sucessfulTransaction:
        print('Here is your ' + optionCoffee + '. Enjoy!')

    anotherCoffee = input('Do you want another coffee? (yes/no): ')

    while (anotherCoffee not in ['yes', 'no']):
         anotherCoffee = input('Invalid option, type again: ')

    if (anotherCoffee == 'no'):
        continueMachine = False
