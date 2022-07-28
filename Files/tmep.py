# import pyfiglet
# class Human(dict):
#     def __repr__(self): 
#         return super().__repr__()
#     def __missing__(self,val):
#         return f"This thing [{val}] is not here"
#     def __setitem__(self,key,val):
#         super().__setitem__(key,val)
#         print (f"{pyfiglet.figlet_format('DONE')}")
#     def __setattr__(self, name, value):
#         self.__dict__[name] = value
#     def __getattr__(self,val):
#         print("ok")
#         return self.__dict__.get(val)
#     def __contains__(self,kv):
#         if kv in self.__dict__.keys() or kv in self.__dict__.values:
#             return True 
#     def __getitem__(self,thing):
#         print( self[thing])
        
# k = Human({"name":'Hossam'})
# k['name'] = 'Hamada'
# print(k)
# # k.sam = 'dsa'
# print(k['sam'])




name = "Hossam"
name = iter(name)
# print(next(name))
# print(next(name))
# print(next(name))
# print(next(name))
# print(next(name))

# while True:
#     try:
#         print(next(name))
#     except StopIteration:
#         break

class custom_iterator(object):
    def __init__(self,low,high):
        self.current = low
        self.high = high
    def __iter__(self):
        return self
    def __next__(self):
        if self.current <= self.high:
            res = self.current
            self.current +=1
            return res
        raise StopIteration
k = custom_iterator(0, 5)
# for i in k:
#     print(i)

# import pickle 
# __import__('146')
# with open('pets.pickle','rb') as file:
#     a,b = pickle.load(file)
#     c,d = pickle.load(file)
# print(a)
# print(b)
# print(c)
# print(d)
import jsonpickle
with open('cat.json','r') as file:
    contents = file.read()
    unfrozen = jsonpickle.decode(contents)

print(unfrozen)























