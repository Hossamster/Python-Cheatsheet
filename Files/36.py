#guessing game part 1
n =int(input("Guess the number! "))
while n != 9 or n != 1:
    print("Wrong Guess ")
    n = int(input ("Try again:"))
    if n == 9 or n == 1:
        print("u guessed it! u won! ")
        k = input("Do u want to continue? (y/n)").lower()
        if k == 'n':
            break
        else:
            n =int(input("Guess the number! "))
