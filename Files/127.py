# def shout(fn):
#     def wrapper(name):
#         return fn(name).upper()
#     return wrapper

def shout(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs).upper()
    return wrapper

@shout
def greet(name):
    return f"Hi Iam {name}"

print(greet('Hoss'))


@shout 
def order(main,side):
    return f"Hi I'd like the {main} with a side of {side}"
print(order('burger','fries'))

@shout 
def lol():
    return ("lol")

print(lol())



