from random import randint
random_number = randint(1, 10)
guess = None

while True:
    guess = int(input("pick a number from 1 to 10: "))
    if guess < random_number:
        print("Too Low")
    elif guess > random_number:
        print("Too High")
    else:
        print("You Won! ")
        play_again = input("Do u want to play again? ").lower()
        if play_again == 'y':
            random_number = randint(1, 10)
            guess = None
        else:
            print("Thank u for playing!\n")
            break
print(f"The random number is really {random_number}")
