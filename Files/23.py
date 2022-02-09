#positive and negative checking 
from random import randint

x = randint(-100,100)

while(x == 0):
    x=randint(-100,100)

y=randint(-100,100)

while(y == 0):
    y=randint(-100,100)

print(f"x is {x} \n"); print(f"y is {y} \n")

if x > 0 and y > 0:
    print('x and y are positive\n')
elif x > 0 and y < 0:
    print("x is positive but y is negative\n")
elif x < 0 and y > 0:
    print("x is negative and y is positive\n")
else:
    print("x and y are negative\n")