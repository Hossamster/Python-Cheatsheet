#OOP
#Classes can contain methods (functions) and attributes (similar to keys in a dict).



# Encapsulation >> the grouping of public and private attributes and methods into a programmatic class 
            # like designing the deck class, i make cards a private attribute

# Abstraction >> exposing only data in a class interface, hiding private attributes and methods from users

# creating class 
# class User:
#     pass

# user1 = User()
# print(user1) # <__main__.User object at 0x000001F792FAA680>

####################################################################################################################################

### __init__

# class User:
#     def __init__(self):
#         print("A new user has been made")
# user1 = User() # A new user has been made
# user2 = User() # A new user has been made

##################################################################

class User:
    def __init__(self,first,last,age):
        self.f = first
        self.l = last
        self.a = age
user1 = User("Hossam","Kamel",22)
user2 = User("Manar","Hassan",25)
print(f"My name is {user1.f} {user1.l} and i am {user1.a} years old")         # My name is Hossam Kamel and i am 22 years old
print(f"My sister's name is {user2.f} {user2.l} and she has {user2.a} years") # My sister's name is Manar Hassan and she has 25

#creating an object that is an instance of a class is called instantiating a class

#Ex
"""
# Define the Comment class below:
class Comment:
    def __init__(self,username,text,likes = 0):
        self.username = username
        self.text = text
        self.likes = likes
"""