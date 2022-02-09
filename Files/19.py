age = int(input("please input an age: "))
#2-8 2 dollar ticket
#65 5 dollar ticket
#10 dollars for everyone else
if not((age >= 2 and age <=8) or age >=65):
    print("Price = 10 dollars\n")
elif (age >= 65):
    print("price = 5 dollars\n")
elif(age >= 2 and age <=8):
    print("price = 2 dollars\n")