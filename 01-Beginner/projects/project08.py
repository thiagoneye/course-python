"""
Caesar Cipher
"""

# Imports

import os

logo = """
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88
            88             88
           ""             88
                          88
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8
8b         88 88       d8 88       88 8PP""""""" 88
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88
              88
              88
"""

# Functions

def inputs():
    option_not_ok = True
    while option_not_ok:
        option = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
        if (option != 'encode') and (option != 'decode'):
            print("This option does not exist, please try again.")
        else:
            option_not_ok = False

    text = input("Type your message:\n")

    shift_not_ok = True
    while shift_not_ok:
        shift = input("Type the shift number:\n")
        if shift.isnumeric():
            shift = int(shift)
            shift_not_ok = False
        else:
            print("This option does not is a number, please try again.")

    return option, text, shift

def encode(text, shift):
    text_encode = ''

    for i in text:
        char = ord(i.lower())

        if char in range(97,123):
            shift = shift % 25

            if (char + shift > 122):
                char = 96 + (char + shift - 122)
            else:
                char += shift

        text_encode += chr(char)

    return text_encode

def decode(text, shift):
    text_decode = ''

    for i in text:
        char = ord(i.lower())

        if char in range(97,123):
            shift = shift % 25

            if (char - shift < 97):
                char = 123 + (char - 97 - shift)
            else:
                char -= shift

        text_decode += chr(char)

    return text_decode

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
