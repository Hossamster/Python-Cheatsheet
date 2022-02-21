# debugging with pdb
import pdb
# first = 10
# second = 2
# pdb.set_trace()
# res = first + second
# third = 4
# res += third
# print(res)

"""
common pdb commands 
l (list)
n (next line)
p (print)
c (continue-finishes debugging)
q (quiting)
"""


def add_numbers(a, b, c, d):
    pdb.set_trace()
    return a+b+c+d
print(add_numbers(1,2,3,4))



"""
# Write a function called divide, which accepts two parameters (you can call them num1 and num2). The function should return the result of num1 divided by num2. If you do not pass the correct type of arguments to the function, it should return the string "Please provide two integers or floats". If you pass as the second argument a 0, Python will raise a ZeroDivisionError, so if this function is invoked with a 0 as the value of num2, return the string "Please do not divide by zero"

    # Examples
    
    # divide(4,2)  2
    # divide([],"1")  "Please provide two integers or floats"
    # divide(1,0)  "Please do not divide by zero"
def divide(a,b):
    try:    
        return a / b
    except TypeError:
        return "Please provide two integers or floats"
    except ZeroDivisionError:
        return "Please do not divide by zero"
print(divide('ds',"1"))
print(divide(1,0))
print(divide(4,2))


"""