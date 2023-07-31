import random
import time

LOOP = True
REDO = True
while LOOP is True:
    print("""Welcome to Rock, Paper, Scissors.
        You will have a countdown and then you must choose Rock, Paper or Scissors. 
        See if you win againt the computer.""")

    choices = ['Rock', 'Paper', 'Scissors']

    current_time = time.monotonic()
    computer = random.randint(0,2)
    computer_choice = choices[computer]

    print("""The computer has chosen.
        Please choose one of the following:
        R for Rock
        P for Paper
        S for Scissors""")
    USER_CHOICE = input()

    while REDO is True:
        if ((USER_CHOICE == 'r') or (USER_CHOICE == 'R')):
            USER_CHOICE = 'Rock'
            REDO = False
        elif ((USER_CHOICE == 'p') or (USER_CHOICE == 'P')):
            USER_CHOICE = 'Paper'
            REDO = False
        elif ((USER_CHOICE == 's') or (USER_CHOICE == 'S')):
            USER_CHOICE = 'Scissors'
            REDO = False
        else:
            print ("You have chosen an incorrect option. Please try again.")
            USER_CHOICE = input()
            REDO = True

    print("You have chosen " + USER_CHOICE + ". The computer has chosen " + computer_choice + ".")

    if USER_CHOICE == computer_choice:
        print("Its a Tie.")

    if USER_CHOICE == 'Rock':
        if computer_choice == 'Paper':
            print("You have lost.")

        if computer_choice == 'Scissors':
            print("You have won")

    if USER_CHOICE == 'Paper':
        if computer_choice == 'Scissors':
            print("You have lost.")

        if computer_choice == 'Rock':
            print("You have won")

    if USER_CHOICE == 'Scissors':
        if computer_choice == 'Rock':
            print("You have lost.")

        if computer_choice == 'Paper':
            print("You have won")


    print ("Would you like to try again? Y/N")

    REDO = True
    RETRY = input()
    while REDO is True:
        if ((RETRY == 'y') or (RETRY == 'Y')):
            LOOP = True
            REDO = False
        elif ((RETRY == 'n') or (RETRY == 'N')):
            LOOP = False
            REDO = False
        else:
            print ("You have chosen an incorrect option. Please try again.")
            RETRY = input()
            REDO = True


print("Thank you for playing Rock, Paper, Scissors.")
