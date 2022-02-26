class User:
    active_users = 0

    @classmethod
    def display_active_users(cls):
        return f"There are {cls.active_users}"
    
    @classmethod
    def from_string(cls,data_str):
        firset,last,age = data_str.split(",")
        return cls(firset,last,age)
    
    def __init__(self,first,last,age):
        self.first = first
        self.last = last
        self.age = age
        User.active_users += 1
    def birthday(self):
        self.age += 1
        return f"Happy {self.age}th {self.first}"
    # def __repr__(self):
    #     return f"{self.first} has {self.age}"

user1 = User("Hossam","Kamel",22)    
user2 = User("Ahmed","Samy",29)    

print(User.display_active_users())

hoss = User.from_string("Loki,Oden,22")
print(hoss.first)

