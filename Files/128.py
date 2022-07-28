""" Metadata : a set of data that describes and gives an information about other data"""
from functools import wraps
def log_function_data(fn):
    @wraps(fn)
    def wrapper(*args,**kwargs):
        """I am in the wrapper function """
        print(f'u are about to call {fn.__name__}')
        print(f"Here is the documentation: {fn.__doc__}")
        return fn(*args,**kwargs)
    return wrapper

@log_function_data
def add(a,b):
    """FUNCION TO ADD TWO NUMBERS """    
    return a + b
print(add(3,3))

print("*"*88)

print(add.__name__)
print(add.__doc__)
# (help(add))
