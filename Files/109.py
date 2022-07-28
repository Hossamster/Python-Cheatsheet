# instance methods 
class User:
    def __init__(self,first,last,age):
        self.f = first
        self.l = last
        self.a = age
    def full_name(self):
        return f"{self.f} {self.l}"
    def initials(self):
        return f"{self.f[0]}.{self.l[0]}"
    def likes(self,things):
        return f"{self.f} likes {things} things"
    def is_senior(self):
        return self.a >= 65
    def birthday(self):
        self.a += 1
        return f"Happy {self.a}th {self.f}"

user1 = User("Joe","Smith",68)
user2 = User("Blanca","Lopez",32)

# print(user1.full_name()) # Joe Smith
# print(user2.full_name()) # Blanca Lopez

# print(user1.initials()) # J.S
# print(user2.initials()) # B.L

# print(user1.likes(5)) # Joe likes 5 things
# print(user1.likes("chips")) # Joe likes chips things

# print(user1.is_senior()) # true
# print(user2.is_senior()) # false

# print(user1.birthday()) # Happy 69th Joe

class BankAccount:
    def __init__(self,owner,balance_attribute = 0.0):
        self.owner = owner
        self.balance = balance_attribute
    def deposit(self,add):
        self.balance += add
        return self.balance
    def withdraw(self,sub):
        self.balance -= sub
        return self.balance

acct = BankAccount("Hossam")
print(acct.owner)
print(acct.balance)
print(acct.deposit(10))
print(acct.withdraw(7))
print(acct.balance)
