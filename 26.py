#Project 1 part 2
#Rock paper scissors
from random import choice
print("Rock...")
print("Paper...")
print("Scissors...")
print("Shoot...\n")
player1 = input("one of (rock, paper, scissor) ")
computer = choice(["rock","paper","scissor"])

print(f"Player 1 {player1}"); print(f"computer {computer}\n")
if (player1 == computer) :
    print("No one wins, repeat again\n")

if (player1 == "rock"):
    if computer == "scissor":
        print("player 1 wins")
    elif computer == "paper":
        print("computer wins")

elif player1 == "paper":
    if computer == "scissor":
        print("computer wins")
    elif computer == "rock":
        print("player 1 wins")

elif player1 == "scissor":
    if computer == "paper":
        print("player 1 wins")
    elif computer == "rock":
        print("computer wins")
else:
    print("invalid move!")
print("\n ") 