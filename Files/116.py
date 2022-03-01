# Inheritance ex
class User:
    active_users  = 0

    @classmethod
    def display_active_users(cls):
        return f"There are currently {cls.active_users}"
    
    @classmethod
    def from_string(cls,data_str):
        first,last,rage = data_str.split(",")
        return cls(first,last,rage)
    
    def __init__(self,first,last,age):
        self.first = first
        self.last = last
        self.age = age
        User.active_users += 1
    
    def logout(self):
        User.active_users -= 1
    
    def full_name(self):
        return f"{self.first} {self.last}"
    
    def initials(self):
        return f"{self.first[0]}.{self.last[0]}"
    
    def likes(self,thing):
        return f"{self.first} likes {thing}"
    
    def is_senior(self):
        return self.age >= 65
    
    def birthday(self):
        self.age += 1
        return f"Happy {self.age}th {self.first}"

class Moderator(User):
    total_mods = 0
    def __init__(self,first,last,age,community):
        super().__init__(first,last,age)
        self.community = community
        Moderator.total_mods += 1

    @classmethod
    def display_total_mods(cls):
        return f"There are currently {cls.total_mods}"

    def remove_post(self):
        return f"{self.full_name()} removed a post from the {self.community} community"

# print(jasmine.full_name())
# print(jasmine.community)

print(User.display_active_users()) # 0

u1 = User("Hossam","Kamel",22)
u1 = User("Hossam","Kamel",22)
u1 = User("Hossam","Kamel",22)

print(User.display_active_users()) # 3

jasmine = Moderator("Jasmine","O' Conner",61,'piano')
jasmine = Moderator("Jasmine","O' Conner",61,'piano')

print(User.display_active_users()) # 5
print(Moderator.display_total_mods()) # 2


