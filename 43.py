#List methods append insert extend
data = [1,2,3]

#append >> add an item to the end of the list
data.append(4)
print (data) # 1 2 3 4

# data.append(7,9) #error, only one :( 
# data.append([5,6,7]) #[1, 2, 3, 4, [5, 6, 7]]
# print (data)

#The solution will be in extend :D 
#extend >> add to the end of a list all values passed to extend
data.extend([5,6,7])
print(data)

#what if we want to add somewhere else,in the middle or at the begining
#insert ?? inserta an item at a given position
another = [456,123,458,221]
another.insert(2,'hi')
print(another)
# another.insert(-1,'look')
# print(another)
another.insert(len(another),'Last')
print(another)