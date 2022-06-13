# Rock Paper Scissors
print("Play a game of Rock, Paper, Scissors")
import random

while True:
 choices = ["r", "p", "s"]

 computer = random.choice(choices)
 player = None

 player = input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors: ").lower()

 while player not in choices:
     player = input("invalid entry, try again: ").lower()

 if player == computer:
      print("CPU: ",computer)
      print("Player: ",player)
      print("You and the CPU have chosen same option it's a tie, try again")
 elif player == "r":
    if computer == "p":
        print("CPU: ",computer)
        print("Player: ",player)
        print("You lose")
    if computer == "s":
        print("CPU: ",computer)
        print("Player: ",player)
        print("You win")
 elif player == "p":
    if computer == "s":
        print("CPU: ",computer)
        print("Player: ",player)
        print("You lose")
    if computer == "r":
        print("CPU: ",computer)
        print("Player: ",player)
        print("You win")
 elif player == "s":
    if computer == "r":
        print("CPU: ",computer)
        print("Player: ",player)
        print("You lose")
    if computer == "p":
        print("CPU: ",computer)
        print("Player: ",player)
        print("You win")

 play_again = input ("Play again? (y/n): ").lower()

 if play_again != "y":
     break
print("Thanks for playing! Goodbye!")