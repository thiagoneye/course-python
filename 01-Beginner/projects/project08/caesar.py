"""
Caesar Cipher
"""

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
