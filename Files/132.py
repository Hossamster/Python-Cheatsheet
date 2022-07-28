from functools import wraps
def enforce(*types):
    def inner(fn):
        @wraps(fn)
        def wrapper(*args,**kwargs):
            argslst = []
            for (a,t) in zip(args,types):
                argslst.append(t(a))
            return fn(*argslst,**kwargs)
        return wrapper
    return inner

@enforce(str,int)
def what(msg,times):
    for time  in range(times):
        print(msg)

# what('I love u',6)
# what('I love u',"6")




'''
@delay(3)
def say_hi():
    return "hi"

say_hi()
# should print the message "Waiting 3s before running say_hi" to the console
# should then wait 3 seconds
# finally, should invoke say_hi and return "hi"
'''

from functools import wraps
from time import sleep

def delay(val):
    def inner(fn):
        @wraps(fn)
        def wrapper(*args,**kwargs):
            print(f"Waiting {val}s before running say_hi")
            sleep(val)
            return fn(*args,**kwargs)
        return wrapper
    return inner

@delay(3)
def say_hi():
    return 'hi'

print(say_hi())

