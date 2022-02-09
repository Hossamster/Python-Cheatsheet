#ask for age
#18-21 wristband
#21+ drink,normal entry
#too young, sorry
age = input("How old are u: ")
if age != "":
    age = int(age)
    if age >= 18 and age < 21:
        print("u can enter, but need a wristband!\n")
    elif age >=21:
        print("u are good to enter and can drink \n")
    else:
        print("u can't come in, little one \n")
else:
    print("Please enter an age")

