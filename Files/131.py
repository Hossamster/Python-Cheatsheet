""" 
? when we write
@decorator
def func(*args, **kwargs):
    pass
# we are really doing 
func = decorator(func)


! when we write
@decorator_with_args(arg)
def func(*args, **kwargs):
    pass
# we are really doing 
func = decorator_with_args(arg)(func) 
"""
from functools import wraps
def ensure_first_arg(arg):
    def inner(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            if   args[0] != arg: # if args >> to avoid error if there is no args !
                return 'first argument needs to be {arg}'
            return fn(*args, **kwargs)
        return wrapper
    return inner

@ensure_first_arg('Hossam')
def fav_persons(*persons):
    return persons

print(fav_persons('Hossam','Manar','Jana'))
print(fav_persons('d','Manar','Jana'))
print(fav_persons())