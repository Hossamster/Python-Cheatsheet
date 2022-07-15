""" 
todo: Enforce a restrictions on the parameters of the function
"""
from functools import wraps
def ensure_no_kwargs(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        if kwargs:
            raise ValueError('No kwargs are allowed ')
        return fn(*args, **kwargs)
    return wrapper


@ensure_no_kwargs
def greet(name):
    return f"Hi {name}"


# print(greet('Hossam'))
# print(greet(name='Hossam'))



'''
@double_return 
def add(x, y):
    return x + y
    
add(1, 2) # [3, 3]

@double_return
def greet(name):
    return "Hi, I'm " + name

greet("Colt") # ["Hi, I'm Colt", "Hi, I'm Colt"]
'''
from functools import wraps
def double_return(fn):
    @wraps(fn)
    def wrapper(*args,**kwargs):
        return [fn(*args,*kwargs) for val in range(2)]
    return wrapper

@double_return 
def add(x, y):
    return x + y
# print(add(1,2))




'''
@ensure_fewer_than_three_args
def add_all(*nums):
    return sum(nums)

add_all() # 0
add_all(1) # 1
add_all(1,2) # 3
add_all(1,2,3) # "Too many arguments!"
add_all(1,2,3,4,5,6) # "Too many arguments!"
'''

from functools import wraps

def ensure_fewer_than_three_args(fn):
    @wraps(fn)
    def wrapper(*args,**kwargs):
        if len(args) > 2:
            return "Too many arguments!"
        else:
            return fn(*args,**kwargs)
    return wrapper

@ensure_fewer_than_three_args
def add_all(*nums):
    return sum(nums)

# print(add_all(1,2,1))





'''
@only_ints 
def add(x, y):
    return x + y
    
add(1, 2) # 3
add("1", "2") # "Please only invoke with integers."
'''

from functools import wraps

def only_ints(fn):
    @wraps(fn)
    def wrapper(*args,**kwargs):
        if all([isinstance(val,int) for val in args]):
            return fn(*args,**kwargs)
        return "Please only invoke with integers."
    return wrapper

@only_ints 
def add(x, y):
    return x + y

# print(add(1, 2))
# print(add('1','2'))




'''
@ensure_authorized
def show_secrets(*args, **kwargs):
    return "Shh! Don't tell anybody!"

show_secrets(role="admin") # "Shh! Don't tell anybody!"
show_secrets(role="nobody") # "Unauthorized"
show_secrets(a="b") # "Unauthorized"
'''

from functools import wraps

def ensure_authorized(fn):
    @wraps(fn)
    def wrapper(*args,**kwargs):
        if 'role' in kwargs.keys() and 'admin' in kwargs.values():
            return fn(*args,**kwargs)
        return "Unauthorized"
    return wrapper

@ensure_authorized
def show_secrets(*args, **kwargs):
    return "Shh! Don't tell anybody!"

print(show_secrets(role="admin") )
print(show_secrets(role="nobody") )
print(show_secrets(a="b"))