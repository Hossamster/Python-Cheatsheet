#Project 1 part 1
#Rock paper scissors
from random import choice
print("Rock...")
print("Paper...")
print("Scissors...")
print("Shoot...\n")
player1 = input("one of (rock, paper, scissor) ").lower()
player2 = input("one of (rock, paper, scissor) ").lower()

print(f"Player 1 {player1}"); print(f"Player 2 {player2}\n")
if (player1 == player2) :
    print("No one wins, repeat again\n")

elif (player1 == 'rock' and player2 == 'scissor') or (player1 == 'scissor' and player2 == 'paper') or (player1 == 'paper' and player2 == 'rock'):
    print("Player 1 wins \n")
else:
    print("player 2 wins \n")