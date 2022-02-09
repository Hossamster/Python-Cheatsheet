# rock paper scissor with while loop
from random import randint
player_wins = 0
computer_wins = 0
while True:
    rand_num = randint(0, 2)
    if rand_num == 0:
        computer = "rock"
    elif rand_num == 1:
        computer = "paper"
    else:
        computer = "scissor"

    player1 = input("one of (rock, paper, scissor) ").lower()

    print(f"Player 1 {player1}")
    print(f"computer {computer}\n")
    if (player1 == computer):
        print("No one wins, repeat again\n")

    if (player1 == "rock"):
        if computer == "scissor":
            print("player 1 wins")
            player_wins += 1
        elif computer == "paper":
            print("computer wins :(")
            computer_wins += 1

    elif player1 == "paper":
        if computer == "scissor":
            print("computer wins :(")
            computer_wins += 1
        elif computer == "rock":
            print("player 1 wins")
            player_wins += 1

    elif player1 == "scissor":
        if computer == "paper":
            print("player 1 wins")
            player_wins += 1
        elif computer == "rock":
            print("computer wins :(")
            computer_wins += 1
    else:
        print("invalid move!")
    cont = input("Do u want to continue? ")
    if cont == 'n':
        break
    else:
        player1 = None
print(f"Score of player is {player_wins}")
print(f"Score of computer is {computer_wins}")
if player_wins > computer_wins:
    print("Congratulations to u !!! ")
elif player_wins < computer_wins:
    print("Computer wins !!!!!")
else:
    print("no one wins")
print("Good Luck")
