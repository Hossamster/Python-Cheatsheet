class SuperList(list): #list is the parent class and superlist is subclass
    def __len__(self):
        return 1000

s1 = SuperList()
print(s1.__len__())

(s1.append(5))
print(s1[0])
# print(s1[1]) #index error

print(issubclass(SuperList,list)) #True 
print(issubclass(list,object))    #True