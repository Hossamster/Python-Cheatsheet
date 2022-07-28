#Lamdas and builtin functions
def square(num): 
    """just a function makes a square of number passed"""
    return num * num
print(square(9))

square2 = lambda num: num * num
print(square2(8))

add = lambda a,b:a+b
print(add(3,4))

print(square.__name__)
print(square2.__name__)
print(add.__name__)

print(square.__doc__)

#lambda is used when u want to pass function to another fuction as a parameter and that function will not
# be used again 

#####
# Ex 
# cube the value
cube = lambda num :num **3
print(cube(2))
print(cube(3))
print(cube(8))
