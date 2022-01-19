# Rock Paper Scissors

# Imports
from random import randint

# Options (strings)
Rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

Paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

Scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Code
options_names = {0: 'Rock', 1: 'Paper', 2: 'Scissor'}
options_drawings = {0: Rock, 1: Paper, 2: Scissors}

you = int(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n'))
print(options_drawings[you])

computer = randint(0,2)

print('Computer chose ' + options_names[computer])
print(options_drawings[computer])

if ((you < 0) or (you > 2)):
    print('You typed an invalid number, you lose!')
elif (you == computer):
    print('Draw')
else:
    if (you == 0):
        if (computer == 1):
            print('You lose')
        else:
            print('You win')
    if (you == 1):
        if (computer == 0):
            print('You win')
        else:
            print('You lose')
    if (you == 2):
        if (computer == 0):
            print('You lose')
        else:
            print('You win')
