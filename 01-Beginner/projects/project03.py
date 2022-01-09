# Treasure Island

print('Welcome to Treasure Island.')
print('Your mission is to find the treasure.')

action = input('You\'re at a cross road. Where do you wa go? Type "left" or "right"\n')

if (action == 'left'):
    action = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.\n')
    if (action == 'wait'):
        action = input('You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. What colour do you choose?\n')
        if (action == 'red'):
            print('It\'s a room full of fire. Game over.')
        elif (action == 'yellow'):
            print('You found the treasure! You Win!')
        elif (action == 'blue'):
            print('You enter a room of beasts. Game over.')
        else:
            print('You chose a door the don\'t exist. Game over.')
    else:
        print('You get attacked by an angry trout. Game over.')
else:
    print('You fell into a hole. Game over.')
