#clear >> clear everything in the list
lis = [1,2,3,4]
lis.clear()
print(lis)

#pop >> remove the item at the given position in the list 
first = [22,66,898,656]
first.pop(1) 
print(first) # 22 898 656

#remove the first item from the list whose value is x
lol = [1,2,3,4,4,4]
lol.remove(2)
print(lol) #[1, 3, 4, 4, 4]
lol.remove(4)
print(lol) #[1, 2, 3, 4, 4]

names = ["Manar","blue","Hossam","arya"]
names.remove("blue")
print(names)