## Errors
# first understand them 

# 1 ### syntax error
# occurs when python encounters incorrect Syntax
# def first: >> where is the ()
# None = 1 >>> ????
# return >>> return what?

# 2
# Name error
# This occurs when a variable is not defined
# print(test) > NameError: name 'test' is not defined

# 3
#type error
#an operation or function is applied to the wrong type
# len(5) > TypeError: object of type 'int' has no len()
# print("awesome"+[]) >can;t concatenate 'str' and 'list' objects

# 4
# index error
# occurs when u try to access an element in a list using an invalid index
# lst = ['hello']
# print(lst[2]) >> IndexError: list index out of range

# 5
# value error
# This occurs when a built-in operation or function receives an argument that has the right type but an inappropriate value
# int('foo') >> ValueError: invalid literal for int() with base 10: 'foo'

# print(int('2')) >> This is right


# 6 
# key errror
# this occurs when a dictionary doesn't have a specific key:
# d={}
# d['ffo'] >> key error

# 7 
# Attribute error
# This occurs when a variable does not have an attribute
# "awesome".hello() > AttributeError: 'str' object has no attribute 'hello'
