#ask for age
#18-21 wristband
#21+ drink,normal entry
#too young, sorry
age = input("How old are u: ")
# age = int(age)
if age and (int(age) >= 18 and int(age) <21):
    print("u can enter, but need a wristband\n")
elif age and (int(age) >= 21):
    print("u are good to enter and can drink\n")
elif age and (int(age) < 18):
    print("u can't come in, little one \n")
else:
    print("please enter an age")
