# Modules
# keep python files small
# reuse code across multiple files by importing

# Built-in modules example
import random
print(random.choice(['apple','banana','cheery','durian']))

import random as omg
print(omg.choice(['apple','banana','cheery','durian']))

# importing parts of a module
# from keyword
from random import randint
print(randint(1,10)) 

###
from random import choice as blah
print(blah(['apple',1,2]))

###
from random import * #imports everything into the current namespace
# u don't have to >> random.choice for ex
# u can make it   >> choice

#########
# Ex
def contains_keyword(*arg):
    # from keyword import kwlist
    # for i in arg:
    #     if i in kwlist:
    #         return True
    import keyword
    for item in arg:
        return keyword.iskeyword(item)
    return False
print(contains_keyword('hello','goodbye'))
print(contains_keyword('def','goodbye'))