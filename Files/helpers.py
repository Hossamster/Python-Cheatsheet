# Dunder methods
# __method__()
class Toy:
    def __init__(self,color,age):
        self.color = color
        self.age = age 
        self.my_dict = {'name':'yoyo','has_pets':False}

    def __str__(self):
        return f"{self.color}"
    
    def __len__(self):
        return 5

    def __del__(self):
        return ("deleted")
    
    def __call__(self):
        return "yesss???"

    def __getitem__(self,i):
       return self.my_dict[i]

action_figure = Toy('red',0)
# print(action_figure.__str__()) #<__main__.Toy object at 0x000001BB8CB67D60>
# print(str(action_figure)) #<__main__.Toy object at 0x000001BB8CB67D60>

print(str(action_figure))       # red
print(action_figure.__str__())  # red

print(len(action_figure))       # 5
print(action_figure.__len__())  #5


print(action_figure.__del__()) #deleted

print(action_figure.__call__())

print(action_figure.__getitem__('name')) 
print(action_figure['has_pets'])
