#Project 1 part 3
#Rock paper scissors
from random import randint
rand_num = randint(0,2)
if rand_num == 0:
    computer = "rock"
elif rand_num == 1:
    computer = "paper"
else:
    computer = "scissor"

player1 = input("one of (rock, paper, scissor) ").lower()

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