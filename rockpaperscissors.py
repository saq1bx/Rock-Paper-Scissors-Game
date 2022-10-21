# This is a beginner friendly Rock Paper Scissors game made in Python
# Feel free to use this code in your own projects
# By: https://github.com/saq1bx

from os import system, name
import random
import time
import sys


def clear():
    if name == 'nt':
        _ = system("cls")
    else:
        _ = system("clear")


def player_choice():
    return input("Rock, Paper or Scissors? (or type 'q' to quit)\n> ").lower()


def computer_choice():
    return random.choice(["rock", "paper", "scissors"])


player_points = 0
computer_points = 0

while True:

    clear()

    print("Welcome to Rock, Paper, Scissors!")
    print()
    print(f"Player Points: [{player_points}] | Computer Points: [{computer_points}]")
    print("\n")

    player = player_choice()
    print()
    computer = computer_choice()

    # Check if player entered a valid choice
    if player == "q":
        sys.exit()
    elif not player.startswith("r") and not player.startswith("p") and not player.startswith("s"):
        print("Invalid choice!")
        time.sleep(2)
        continue
    # Rock
    if player.startswith("r") and computer.startswith("r"):
        print("The computer chose ROCK!\n")
        print("It's a TIE!")
        time.sleep(2)
        continue
    elif player.startswith("r") and computer.startswith("p"):
        print("The computer chose PAPER!\n")
        print("You LOSE!")
        computer_points += 1
        time.sleep(2)
        continue
    elif player.startswith("r") and computer.startswith("s"):
        print("The computer chose SCISSORS!\n")
        print("You WIN!")
        player_points += 1
        time.sleep(2)
        continue

    # Paper
    if player.startswith("p") and computer.startswith("r"):
        print("The computer chose ROCK!\n")
        print("You WIN!")
        player_points += 1
        time.sleep(2)
        continue
    elif player.startswith("p") and computer.startswith("p"):
        print("The computer chose PAPER!\n")
        print("It's a TIE!")
        time.sleep(2)
        continue
    elif player.startswith("p") and computer.startswith("s"):
        print("The computer chose SCISSORS!\n")
        print("You LOSE!")
        computer_points += 1
        time.sleep(2)
        continue

    # Scissors
    if player.startswith("s") and computer.startswith("r"):
        print("The computer chose ROCK!\n")
        print("You LOSE!")
        computer_points += 1
        time.sleep(2)
        continue
    elif player.startswith("s") and computer.startswith("p"):
        print("The computer chose PAPER!\n")
        print("You WIN!")
        player_points += 1
        time.sleep(2)
        continue
    elif player.startswith("s") and computer.startswith("s"):
        print("The computer chose SCISSORS!\n")
        print("It's a TIE!")
        time.sleep(2)
        continue
