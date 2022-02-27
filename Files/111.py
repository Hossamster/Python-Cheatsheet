
# Class Methods >> cls not self
# __repr__  method is used to represent a class's objects as a string

class User:
    acive_users = 0

    @classmethod
    def display_active_users(cls):
        return f"There are {cls.acive_users} users"
    
    @classmethod
    def from_string(cls,data_str):
        first,last,age = data_str.split(",")
        return cls(first,last,int(age)) # instance of User


    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age
        User.acive_users += 1

    def birthday(self):
        self.age += 1
        return f"Happy {self.age}th {self.firt}"
        
    def __repr__(self):
        return f"{self.first} has {self.age}"

user1 = User("Joe","Smith",68)
user2 = User("Blanca","Lopez",32)

print(User.display_active_users()) # 2

hoss = (User.from_string("Hossam,Hassan,22"))
print(hoss.first)
print(hoss.last)
print(hoss.age)

print(user1)