#return values from function
def square_of_7 ():
    return 7 ** 2

result = square_of_7()
print(result)

def say_hi():
    return "Hi"

greetings = say_hi()
print(greetings)

# Return exits the function
def mul_by_2():
    print("I am before the return")
    return 2 * 2 
    print("I am after the return") # it will not printed as it is after the return which exits the function 

var = mul_by_2()
print(var) 


"""
def speak_pig():
    return "oink"
    
print(speak_pig())
"""

"""
#Define a function called generate_evens
def generate_evens():
    return [num for num in range(1,50) if num % 2 == 0]
#It should return a list of even numbers between 1 and 50(not including 50)
print(generate_evens())
"""