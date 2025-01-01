"""This is a game of rock, paper. and scissors, this was the first, main project, I had completed."""

import random as rand

def game():
    options = ["rock", "paper", "scissors"]
    
    print("\nWelcome to the game of rock, paper scissors!")
    y = "y"
    while y == "y":
        valid_input = False
        while not valid_input:
            choice = input("What would you like to play? ").lower()
            if choice in options:
                valid_input = True
            else:
                print("Not a valid input")
        defense = rand.choice(options)
        if choice == defense:
            print("You choose the same as the computer")
            print(f"The computer had choose {defense} as well.")
            return
        elif choice  == "rock":
            if defense == "paper":
                print(f"The computer had chose {defense}, so you had lost.")
            elif defense == "scissors":
                print(f"The computer had choose {defense}, so you had won.")
        elif choice == "scissors":
            if defense == "paper":
                print(f"The computer had chose {defense}, so you had won.")
            elif defense == "rock":
                print(f"The computer had chose {defense}, so you had lost.")
        elif choice == "paper":
            if defense == "rock":
                print(f"The computer had chose {defense}, so you had won.")
            elif defense == "scissors":
                print(f'The computer had chose {defense}, so you had lost.')
        y = input("Would you like to play again? y/n: ")

game()