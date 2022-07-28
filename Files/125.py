# from random import choice 
# def greet(person):
#     def get_modd():
#         msg = choice(["Hello there ",'go away ','I love u '])
#         return msg
#     result = get_modd() + person
#     return result

# print(greet('Hossam'))

from random import choice
def make_laugh_func():
    def get_laugh():
        l = choice(('HAHAHAH', 'lol', 'tehehe'))
        return l 
    return get_laugh
laugh = make_laugh_func()
print(laugh)

""" When you want to execute the function, then you add the parentheses () to call/invoke it. In this scenario, we are creating a function (make_laugh_func) that returns an inner function (get_laugh).

When returning the inner get_laugh function from the outer make_laugh_func, we don't want to call it immediately at that point, and therefore we don't add parentheses to return get_laugh

That allows us to return the get_laugh function reference from make_laugh_func, which we can then call at a later point.

Then, we call the make_laugh_func here and save its return value to the laugh variable: laugh = make_laugh_func()

That will store the return get_laugh function reference to the laugh variable (but not call the inner function immediately). Then, later we can add () to the laugh variable in order to call the get_laugh function which was saved to it: laugh()

So, adding parentheses depends if you want to call and execute the function immediately, or if you are just referencing it so you can call it at a later point. """
