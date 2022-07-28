#underscores 
# _name     >> telling developers that this supposed to be private or for internal use
# __name    >> name mangling >> object._class__name
# __name__  >> something exist in python otherwise not technially wrong but bad idea or used for python specific method

# class Person:
#     def __init__(self):
#         pass
#     def __hello__():
#         pass

class Person:
    def __init__(self):
        self.name = "Tony"
        self._secret = "hi!" # not intended to be used outside of the class
        self.__msg = "I like u"
        
p = Person()

print(p.name)    # Tony
print(p._secret) # hi!
print(dir(p))
print(p._Person__msg) # mangle the variable name 