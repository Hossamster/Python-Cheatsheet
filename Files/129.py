from functools import wraps
from time import time

def speed_test(fn):
    @wraps(fn)
    def wrapper(*args,**kwargs):
        start_time = time()
        res = fn(*args,**kwargs)
        end_time = time()
        print(f"The {fn.__name__} function takes time {end_time - start_time} seconds")
        return res
    return wrapper


# @speed_test
# def gen():
#     return sum(num for num in range(100000000))

# print(gen())


# @speed_test
# def lst():
#     return sum([num for num in range(100000000)])

# print(lst())





'''
@show_args
def do_nothing(*args, **kwargs):
    pass

do_nothing(1, 2, 3,a="hi",b="bye")

# Should print (on two lines):
# Here are the args: (1, 2, 3)
# Here are the kwargs: {"a": "hi", "b": "bye"}
'''

from functools import wraps

def show_args(fn):
    @wraps(fn)
    def wrapper(*args,**kwargs):
        print("Here are the args: {}".format(args))
        print("Here are the kwargs: {}".format(kwargs))
    return wrapper

@show_args
def do_nothing(*args, **kwargs):
    pass
do_nothing(1, 2, 3,a="hi",b="bye")