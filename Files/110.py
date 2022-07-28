# Class Attributes

class User:
    acive_users = 0

    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age
        User.acive_users += 1

    def logout(self):
        User.acive_users -= 1
        return f"{self.first} has logged out "

# user1 = User("Hossam", 'Kamel', 22)
# user2 = User("Samy", 'Ahmed', 30)
# user3 = User("aboelshoq", 'saad', 32)
# print(User.acive_users) # 3


# print(user3.logout()) # aboelshoq has logged out
# print(User.acive_users) # 2

class Pet:
    allowed = ['cat','dog','fish','rat']
    def __init__(self,name,species):
        if species not in Pet.allowed:
            raise ValueError(f"u can't have a {species} pet!")
        self.name = name
        self.species = species
    def set_species(self,species):
        if species not in Pet.allowed:
            raise ValueError(f"u can't have a {species} pet!")
        self.species = species
        
cat = Pet("blue","cat")
dog = Pet("wyatt",'dog')
# dog = Pet("wyatt",'dogdsa') # ValueError: u can't have a dogdsa pet!
# print(cat.name) #blue
# print(cat.species) #cat

# (cat.set_species('rat'))  # cat will be rat
# print(cat.species)        # rat

"""print(id(cat.allowed))
print(id(dog.allowed))
print(id(Pet.allowed))""" # all are points to the same id 


"""
#Ex
class Chicken:
    total_eggs = 0 # class attribute
    def __init__(self,name,species,eggs = 0):
        self.name = name
        self.species = species
        self.eggs = eggs
    def lay_egg(self):
        self.eggs += 1
        Chicken.total_eggs += 1
        return self.eggs

c1 = Chicken("Alice","Partride Silkie")
c2 = Chicken("Amelia","Speckled Sussex")
print(Chicken.total_eggs) # 0 
print(c1.lay_egg()) # 1
print(Chicken.total_eggs) # 1

print(c2.lay_egg()) # 1
print(c2.lay_egg()) # 2
print(Chicken.total_eggs) # 3

"""




