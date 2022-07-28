# Special Methods 
from copy import copy

class Human:
    def __init__(self,first,last,age):
        self.first = first
        self.last = last
        self.age = age
    def __repr__(self):
        return f"Human named {self.first} {self.last} aged {self.age}"
        
    def __len__(self):
        return self.age

    def __add__(self,other):
        if isinstance(other,Human):
            return Human(first= 'Newborn',last=self.last,age=0)
        return 'u can\'t add that'

    def __mul__(self,other):
        if isinstance(other,int):
            # return [self for i in range(other)]
            return [copy(self) for i in range(other)]
        return 'can\'t multiply'

j = Human("Jenny",'Larsen',56)
k = Human("Kevin",'Jones',87)
# print(j) # Jenny Larsen aged 56
# print(len(j)) # 56

print(j + k) # k isinstance(Human) >> True ... returning Human named Newborn Larsen aged 0
print(j * 3) # [Human named Jenny Larsen aged 56, Human named Jenny Larsen aged 56, Human named Jenny Larsen aged 56]
triplets = j * 3
triplets[1].first = 'Ahmed'
# These are all the exact same object
print(triplets) # [Human named Ahmed Larsen aged 56, Human named Ahmed Larsen aged 56, Human named Ahmed Larsen aged 56]
print(triplets) 