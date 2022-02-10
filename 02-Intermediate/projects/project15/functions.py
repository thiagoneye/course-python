"""
Coffee Machine
"""

import numpy as np

def report(resources, units, safeBox):
    """
    Print machine report: resources and money.
    """
    for key, value in resources.items():
        print(key.title() + ': ' + str(value) + units[key])

    print(f'Money: ${safeBox:.2f}')

def checkResources(optionCoffee, resources, menu):
    """
    Check resources sufficient.
    """
    resourcesSufficient = True

    for key, value in resources.items():
        if value < menu[optionCoffee]['ingredients'][key]:
            resourcesSufficient = False
            resourcesInsufficient = key

    if not resourcesSufficient:
        print(f'Sorry there is not enough {resourcesInsufficient}.')
        sucessful = False
    else:
        sucessful = True

    return sucessful

def insertCoins():
    """
    Insert coins in machine.
    """
    print('Please insert coins.')

    penny = int(input('How many pennies? '))
    nickel = int(input('How many nickels? '))
    dime = int(input('How many dimes? '))
    quarter = int(input('How many quarters? '))

    return [penny, nickel, dime, quarter]

def processCoins(amountOfCoins, coins):
    """
    Process coins.
    """
    return np.sum(np.array(amountOfCoins)*np.array(coins))

def checkTransaction(amountOfCoins, coins, optionCoffee, menu, resources, safeBox):
    """
    Check transaction successful.
    """
    money = processCoins(amountOfCoins, coins)
    value = menu[optionCoffee]['cost']
    change = money - value

    if (money < value):
        print('Sorry that\'s not enough money. Money refunded.')
        sucessful = False
    else:
        print(f'Here is ${change:.2f} in change.')
        sucessful = True

        for key, value in menu[optionCoffee]['ingredients'].items():
            resources[key] -= value

        safeBox += menu[optionCoffee]['cost']

    return sucessful, safeBox
