"""
100 Days of Code
The Complete Python Pro Bootcamp

Constructing Objects and Accessing their Attributes and Methods
"""

# Imports

from prettytable import PrettyTable

# Main

table = PrettyTable()
table.add_column('Pokemon Name', ['Pikachu', 'Squirtle', 'Charmander', 'Bulbasaur'])
table.add_column('Type', ['Electric', 'Water', 'Fire', 'Grass'])

print(table)