#fuction to toss a coin
from random import random
def flip_coin():
    r = random()
    if r > 0.5:
        print("Heads")
    else:
        print("Tails")

#slightly improved version
# it will overwrite on the previous version
def flip_coin():
    if random() > 0.5:
        print("HEADS")
    else:
        print("TAILS")

flip_coin() # It will execute the overwriten version

