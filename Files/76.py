#keyword arguments
def full_name(first,last):
    return f"Your name is {first} {last}"

print(full_name(first='Hossam',last='Kamel'))
print(full_name(last='Kamel',first="Hossam"))

def exponent(num,power=2):
    return num ** power

print(exponent(num=4,power=3))
print(exponent(power=3,num=4))

# why use keyword arguments?
# A little more flexibility
# u may not see the value now,but it's useful when passing a dictionary
# to a function and unpacking it's values - we will see that later

def full_name(first="Hamada",last='Ahmed'):
    return f"Your name is {first} {last}"

print(full_name(first='Hossam',last='Kamel'))
print(full_name(last='Kamel',first="Hossam"))