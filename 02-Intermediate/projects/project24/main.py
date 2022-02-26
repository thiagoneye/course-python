"""
100 Days of Code
The Complete Python Pro Bootcamp
Dra. Angela Yu

Project 24
Mail Merge
"""

PATH1 = '../project24/inputs/invited_names.txt'
PATH2 = '../project24/inputs/starting_letter.txt'
PATH3 = '../project24/outputs/'

with open(PATH1) as file1:
    names = file1.readlines()

with open(PATH2) as file2:
    letter = file2.read()

for name in names:
    name = name.replace('\n', '')
    new_letter = letter.replace('[name]', name)

    PATH = PATH3 + 'letter_for_' + name + '.txt'
    with open(PATH, mode='w') as output:
        output.write(new_letter)
