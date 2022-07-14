class Human:
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        if age >= 0:
            self._age = age
        else:
            self._age = 0

    # def get_age(self):
    #     return self._age

    # def set_age(self, new):
    #     if new >= 0:
    #         self._age = new
    #     else:
    #         self._age = 0

    @property
    def age(self):
        return self._age
    @age.setter
    def age_set(self,new):
        if new >= 0:
            self._age = new
        else:
            raise ValueError("age can't be negative")
    @property
    def full_name(self):
        return f"{self.first} {self.last}"
    
    @full_name.setter
    def full_name(self,name):
        self.first,self.last = name.split(" ")
        
jane = Human("Samy", "Zarko", 23)
# print(jane.age) # 23
# jane.age_set = -100
# print(jane.age) # -100
# jane = Human("Samy","Zarko",-23)
# print(jane.age) # 0

# jane = Human("Samy", "Zarko", 23)
# print(jane.get_age())  # 23

# jane.set_age(56)
# print(jane.get_age())  # 23

#for property bas >>msh ba3tbra
print(jane.rage) #

jane.rage = 54
print(jane.rage) # 54

print(jane.full_name)
jane.full_name = "Hossam Hassan"
print(jane.full_name)
print(jane.__dict__)

