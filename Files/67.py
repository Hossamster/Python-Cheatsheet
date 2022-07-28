#sets to keep track of a collection of elements
#formal mathematical sets ... no order .. no duplicate values .. can not access by index
#creating
s = set({1,2,3,4,5,6})
# or
s = {1,2,3,4,4} #no duplicate value counted!
print(type(s))
print(s)

#access way
print(4 in s) # the only way
# print(s[0]) type error

#access all values in a set
for i in s:
    print(i)

cities = ['cairo','alex','luxor','aswan','cairo','damiata','alex']
print(set(cities))
print(list(set(cities)))

print(len(set(cities))) # unique cities

