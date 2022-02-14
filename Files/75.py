#Default parameters
def exponent(num, power=2): # default value for power is 2 if power is not
                            #defined by the user 
    return num ** power
print(exponent(3,3))
print(exponent(2,5))
print(exponent(5,3))
print(exponent(6,2))
print(exponent(3))
print(exponent(2))
print(exponent(4))


def add(a=10,b=20):
    return a+b
print(add()) # 30
print(add(1,10)) # 11'

def show_information(first_name= "Hossam", is_instructor = False):
    if first_name == "Hossam" and is_instructor:
        return "Welcome back instructor Hossam"
    elif first_name == 'Hossam':
        return "I really though you were the instructor"
    return f"Hello {first_name}"

print(show_information())
print(show_information("Hossam",True))
print(show_information("Hamada",False))

#why have default parameters
#allows you to be more defensive
#avoid errors with incorrect parameters
#default parameters could be anything
#functions,lists,dictionaries,strings,booleans

def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def math(a,b,fn=add):
    return fn(a,b)
print(math(5,6))
print(math(5,6,sub))


"""
def speak(string="dog"):
    if string == 'pig':
        return 'oink'
    elif string == 'duck':
        return 'quack'
    elif string == 'cat':
        return 'meow'
    elif string == 'dog':
        return 'woof'
    return '?'

print(speak())
print(speak("pig"))
print(speak("duck"))
print(speak("cat"))
print(speak("dog"))
print(speak("lion"))
"""