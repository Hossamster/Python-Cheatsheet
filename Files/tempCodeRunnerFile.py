def shout(fn):
    def wrapper(*args,**kwargs):
        args = [val.capitalize() for val in args if islower(args)]
        return fn(*args,**kwargs)
    return wrapper


@shout
def greet(name):
    return f"Hello {name}!"

print(greet("hossam"))
