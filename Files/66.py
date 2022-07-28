# Looping and methods in tuple
names = ("Hossam","Ahmed","Malek","Hamza")

for i in names:
    print(i)

i = len(names) - 1
while i >= 0 :
    print(names[i])
    i = i - 1

# count method
x = (1,2,3,3,3,4,4,1)

print(x.count(3)) #3
print(x.count(1)) #2

# index method 
print(x.index(4)) #5

print(x.index(1,3)) #7

print(x.index(3,3)) #3


# nested tuples
lol = (1,2,3,(4,5),6,7)
print(lol[1:4])


