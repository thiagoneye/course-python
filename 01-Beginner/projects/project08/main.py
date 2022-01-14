"""
Caesar Cipher
"""

# Imports

import os
from caesar import inputs, encode, decode
from logo import logo

# Software

continue_code = True
while continue_code:
    os.system('cls')

    print(logo)
    print('Welcome to Caesar Cipher!')
    option, text, shift = inputs()

    if option == 'encode':
        text_encode = encode(text, shift)
        print("Here's the encode result:\n" + text_encode)
    else:
        text_decode = decode(text, shift)
        print("Here's the decode result:\n" + text_decode)

    exit_not_ok = True
    while exit_not_ok:
        exit = input("Type 'again' to try again, type 'exit' to exit.\n")
        if (exit != 'again') and (exit != 'exit'):
            print("This option does not exist, please try again.")
        else:
            exit_not_ok = False
            if (exit == 'exit'):
                continue_code = False
