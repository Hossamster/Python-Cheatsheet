# *args >> special operator we can pass to functions
#Gathers remaining arguments as a tuple

def sum_all_nums(num1,num2,num3,num4,num5,num6): # What if we want more than these numbers to get their sum ?
    return num1+num2+num3+num4+num5+num6
print(sum_all_nums(1,2,3,4,5,6))

def sum_all_nums(*args):
    print(args)

sum_all_nums(1,2,3,4)

def sum_all_nums(*args):
    total = 0
    for i in args:
        total += i
    return total
    
print(sum_all_nums(1,2,3,4))

def sum_all_nums(num1,*args):
    print(num1)
    total = 0
    for i in args:
        total += i
    return total
    
print(sum_all_nums(1,2,3,4))

def ensure_correct_info(*args):
    if "Hossam" in args and "Kamel" in args:
        return "Welcome back Hossam"
    return "Not sure who u are"
print(ensure_correct_info())
print(ensure_correct_info("Hossam","Kamel"))

###############
#Ex
def contains_purple(*args):
    return "purple" in args
    
print(contains_purple("purple"))
print(contains_purple("PURPLE",12))

