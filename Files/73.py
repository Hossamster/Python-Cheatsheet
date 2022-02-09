# Takes Parameters inside the function
def square(num):
    return num * num
print(square(4))
print(square(8))

def happy_birthday(name):
    print(f"Happy birthday ya {name}")
    print(f"Sana helwa ya {name}")

happy_birthday("hossam")
# happy_birthday() > type error .. name is required 

def add(a,b):
    return a+b

print(add(5,3)) # 8

def mul(a,b):
    return a*b

print(mul(5,3)) # 15

def your_name(first,second):
    return (f"your full name is {first} {second}")
print(your_name("Hossam","Kamel"))

#parameters vs arguments

#parameter is a variable in a method definition
#parameter is variable in the declearation of function
def add(a,b): # a , b are the parameters 
    return a+b
#arguments are the data you pass into the method's parameters
#argument is the actual value of this variable that gets passed to function
print(add(5,3)) # 5,3 are the arguments

def divide(num1,num2):
    return num1 / num2
print(divide(5,2))

"""
def yell(string):
    return f"{string.upper()}!"
print(yell("go away"))
print(yell("leave me alone"))

"""