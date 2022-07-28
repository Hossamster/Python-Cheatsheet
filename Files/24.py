#calling in sick 
from random import randint,choice
actually_sick = choice([True,False])
kinda_sick = choice([True,False])
hate_your_job = choice([True,False])
sick_days = randint(0,10)

calling_in_sick = None
print("\n")
print(f"actually sick is {actually_sick}")
print(f"kinda sick is {kinda_sick}")
print(f"hate your job is {hate_your_job}")
print(f"sick days are {sick_days} \n")

if actually_sick and sick_days > 0:
    calling_in_sick = True
elif kinda_sick and hate_your_job and sick_days > 0:
    calling_in_sick = True
else:
    calling_in_sick = False

print(f"calling in sick is {calling_in_sick}\n")