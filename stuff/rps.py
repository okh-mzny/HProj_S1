"""
This code is a simple program that plays rock-paper-scissors with the user. It first asks the user to choose their 
move and stores it in the 'user_action' variable. Then, it randomly chooses the computer's move. It then prints out 
both moves to the screen and checks if they are equal. If they are, it declares a tie.

If the user's move is not equal to the computer's move, it uses a series of conditional statements to determine who
won the game. It first checks each possible combination of moves that could result in the user winning, such as paper
beating rock and rock beating rock . If none of these combinations match what happened, it declares a win for the
computer.
"""

import random

user_action = input("Enter a choice (rock, paper or scissors): ")
possible_actions = ["rock", "paper", "scissors"]
computer_action = random.choice(possible_actions)
print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")

if user_action == computer_action:
    print("It's a tie")

for e in enumerate(possible_actions):
    if computer_action == e[1]:
        if e[1] == "rock" and user_action == "paper" or \
                e[1] == "paper" and user_action == "scissors" or \
                e[1] == "scissors" and user_action == "rock":
            print("The computer lost, you're a winner!")
        else:
            print("The computer won")
