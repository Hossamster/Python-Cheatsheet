#Scope
#variables created in functions are scoped in that function
instructor = 'Hossam' # global variable
def say_hello():
    return f"Hello {instructor}"
print(say_hello())

def say_hi():
    new_instructor = 'Ahmed' # new_instructor is local variable for say_hi()
    return f'Hi {new_instructor}'
print(say_hi())
# print(new_instructor) # new_instructor is defined inside a function

# total = 0
# def increment():
#     total += 1     # u can't use global variables inside a function
#     return total
# print(increment()) # error 

# So the solution to use global variable inside a function
total = 0
def increment():
    global total
    total +=1     
    return total
print(increment())

#################
name = "Hossam"
def greet():
    # name += " Kamel"     # error for same problem(global variabke)
    print(name) 

greet()

#############
def greet():
    name = "Hamada Ahmed"
    print(name) 

greet()
print(name)

############

def outer():
    count = 0 # local variable in outer()
    def inner():
        nonlocal count # nonlocal to get the count variable from outer()
        count += 1
        return count
    return inner()
print(outer())

###
#Documenting functions 
#to see what comment inside the function > function-name.__doc__
def say_hello():
    """A simple function that returns the string hello"""
    return "Hello!"
print(say_hello())
print(say_hello.__doc__)