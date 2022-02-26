"""
Higher or Lower
"""

# Imports
from database import logo, vs
import random
import os

# Inputs
best_score = 0

# Main
restart_game = True
while restart_game:
    # Imports
    from database import data

    # Raffle the options
    optionA = random.choice(data)
    data.remove(optionA)

    optionB = random.choice(data)
    data.remove(optionB)

    # Inputs
    final_score = 0

    continue_game = True
    while continue_game:
        # User Experience
        os.system('cls')

        # Prints
        print(logo)

        if final_score > 0:
            print(f"\nYou're right! Current score: {final_score}.")

        print("\nCompare A:")
        print(optionA["name"] + ", " + optionA["description"] + ", from " + optionA["country"] + ".")
        print(vs)
        print("\nAgainst B:")
        print(optionB["name"] + ", " + optionB["description"] + ", from " + optionB["country"] + ".")

        # Inputs
        who_win = input("\nWho has more followers? Type 'A' or 'B': ")
        while who_win not in ["A", "B"]:
            who_win = input("Invalid inputs, please type again: ")

        # Comparasion
        if (optionA["follower_count"] > optionB["follower_count"]):
            if (who_win == "A"):
                # Score
                final_score += 1

                # New Option
                optionA = optionB.copy()
                optionB = random.choice(data)
                data.remove(optionB)
            else:
                # Action
                continue_game = False

                # Print
                print(f"\nSorry, that's wrong. Final score: {final_score}.")
        else:
            if (who_win == "A"):
                # Action
                continue_game = False

                # Print
                print(f"\nSorry, that's wrong. Final score: {final_score}.")
            else:
                # Score
                final_score += 1

                # New Option
                optionA = optionB.copy()
                optionB = random.choice(data)
                data.remove(optionB)

        if not continue_game:
            if final_score > best_score:
                best_score = final_score

            print(f"The best score is: {best_score}.")

            want_again = input("\nDo you want play again? Type 'Yes' or 'No': ")
            while want_again not in ["Yes", "No"]:
                want_again = input("Invalid inputs, please type again: ")

            if (want_again == "No"):
                restart_game = False
                print("Bye bye!")
