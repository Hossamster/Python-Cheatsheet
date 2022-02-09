from random import choice
food = choice(['apple','grape','bacon','steak','worm'])
print(food)
if food == 'apple' or food == 'grape':
    print("fruit\n")
elif food == 'bacon' or food == 'steak':
    print("meat")
else:
    print("Yuck")