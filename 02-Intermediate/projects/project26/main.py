"""
100 Days of Code
The Complete Python Pro Bootcamp
Dra. Angela Yu

Project 26
NATO Alphabet Project
"""

# Imports

import pandas as pd

# TODO 1. Create a dictionary in this format:

df = pd.read_csv('nato_phonetic_alphabet.csv')
nato_dict = {row.letter: row.code for (_, row) in df.iterrows()}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.

try_again = True

while try_again:
    new_word = input('Enter a word: ').upper()

    try:
        phonetic_code = [nato_dict[letter] for letter in new_word]
        print(phonetic_code)
    except KeyError:
        print('Sorry, only letters in the alphabet, please.')
    else:
        try_again = False
