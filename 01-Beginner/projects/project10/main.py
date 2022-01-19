"""
Calculator
"""

import os
from operations import get_result
from logo import logo

cont_soft = True

while cont_soft:

    os.system('cls')
    print(logo)
    print("\nWelcome to the Calculator!")

    x = input("\nInput a value:\n")
    while not x.isnumeric():
        x = input("This option is invalid, please type a number.\n")

    operat = input("\nWhat operation do you want? Type a option:\n[+] Addition [-] Subtration [*] Multiplication [/] Division \n[%] Module [^] Potential [!] Root\n")
    while operat not in ['+', '-', '*', '/', '%', '^', '!']:
        operat = input("This option is invalid, please type a valid operation.\n")

    y = input("\nInput another value:\n")
    while not y.isnumeric():
        y = input("This option is invalid, please type a number.\n")

    result = get_result(operat, float(x), float(y))
    if type(result) == str:
        print(result)
    else:
        if result.is_integer():
            print(f"\n{x} {operat} {y} = {int(result)}")
        else:
            print(f"\n{x} {operat} {y} = {result}")

    exit_soft = input("\nDo you want to do another calculation? [Y] Yes or [N] No.\n")
    while exit_soft not in ['Y', 'N']:
        exit_soft = input("This option don't exist, try again. [Y] Yes or [N] No.\n")

    if (exit_soft == 'N'):
        cont_soft = False
