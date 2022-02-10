"""
Coffee Machine
"""

menu = {
    'espresso': {
        'ingredients': {
            'water': 50, # ml
            'milk': 0,   # ml
            'coffee': 18 # g
            },
        'cost': 1.50     # $
    },
    'latte': {
        'ingredients': {
            'water': 200, # ml
            'milk': 150,  # ml
            'coffee': 24  # g
            },
        'cost': 2.50      # $
    },
    'cappuccino': {
        'ingredients': {
            'water': 250, # ml
            'milk': 100,  # ml
            'coffee': 24  # g
            },
        'cost': 3.00      # $
    }
}

resources = {
    'water': 600, # ml
    'milk': 300,  # ml
    'coffee': 100 # g
}

units = {
    'water': 'ml',
    'milk': 'ml',
    'coffee': 'g'
}

coins = [0.01, 0.05, 0.10, 0.25] # [penny, nickel, dime, quarter]
