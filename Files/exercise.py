class User():
    def __init__(self,email):
        self.email = email

    def sign_in(self):
        print('logged in')

 

# class Archer(User):
#     def __init__(self,name,num_arrows):
#         self.name = name
#         self.num_arrows = num_arrows
    
#     def another_attack(self):
#         print(f'attacking with arrows: arrows left - {self.num_arrows}')


# archer1 = Archer("Hassan",34)
# archer1.sign_in()
# archer1.another_attack()

#
# print(isinstance(wizard1,Wizard)) #true
# print(isinstance(wizard1,User))   #true
# print(isinstance(wizard1,object)) #true

wizard1 = Wizard("Ahmed",25,"abc@g.com")
print(wizard1.email)
# wizard1.sign_in()
# wizard1.attack()