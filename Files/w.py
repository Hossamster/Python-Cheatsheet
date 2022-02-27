class PlayerCharacter:
    membership = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

# TODO: How to instantiate object from class method
    @classmethod
    def adding(cls, num1, num2):
        # return num1 + num2
        # TODO:
        return cls("Hamada", num1 + num2) # This will instantiate the old instance (hossam) and overwrite its data

    def say_hello(self):
        print("helloooooooooooooooooo")

# hossam = PlayerCharacter() >> error as no arguments

hossam = PlayerCharacter("Hossam", 22) # instance of PlayerCharacter class

# print(hossam) # <__main__.PlayerCharacter object at 0x000002824A4FBBE0>

print(hossam.name)  # Hossam
print(hossam.age) # 22

hossam = PlayerCharacter.adding(23,5)
print(hossam.name)# Hamada
print(hossam.age) # 28

hossam.say_hello() # helloooooooooooooooooo

hossam.say_hello = "hi"
print(hossam.say_hello)
            
            
# class User():
#     def sign_in(self):
#         print('logged in')

# class Wizard(User):
#     def __init__(self,name,power):
#         self.name = name
#         self.power = power
    
#     def attack(self):
#         print(f"attacking with power of {self.power}")

# class Archer(User):
#     def __init__(self,name,num_arrows):
#         self.name = name
#         self.num_arrows = num_arrows
    
#     def check_arrows(self):
#         print(f'attacking with arrows: arrows left - {self.num_arrows}')
#     def run(self):
#         print('ran really fast')

# class HybridBorg(Wizard,Archer):
#     def __init__(self, name, power,arrows):
#         Archer.__init__(self,name,arrows)
#         Wizard.__init__(self,name,power)
 
# hb1 = HybridBorg("borgie",50,67)
# (hb1.run())
# (hb1.check_arrows())
# hb1.attack()
# hb1.sign_in()



# MRO >> Method Resolution Order
# class A:
#     num = 10

# class B(A):
#     pass
# class C(A):
#     num = 1
# class D(B,C):
#     pass

# print(D.mro()) 
