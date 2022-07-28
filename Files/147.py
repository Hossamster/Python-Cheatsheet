import json

#? json.dumps formats a python object as a string of json

# j = json.dumps(['foo',{'bar':('baz',None,1.0,2)}])
# print(type(j)) # class str
# print(j)


class Cat:
    def __init__(self,name,breed):
        self.name = name
        self.breed =breed

c = Cat("meshmesh",'scotlish')

j =  json.dumps(c.__dict__)
# print(j)


import jsonpickle
# new = jsonpickle.encode(c)
# print(new)


with open('cat.json','w') as file:
    frozen = jsonpickle.encode(c)
    file.write(frozen)


# import jsonpickle
# with open('cat.json','r') as file:
#     contents = file.read()
#     unfrozen = jsonpickle.decode(contents)
# print(unfrozen)