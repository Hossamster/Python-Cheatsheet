#List methods index,count,sort,reverse,join
#index >> returns the index of the specified item in the list
numbers = [5,6,7,8,9,10]
print(numbers.index(6)) # 1

new = [5,5,6,7,5,8,8,9,10]
print(new.index(5)) #0
print(new.index(5,1)) #find the index of 5 from the index have 1... #1
print(new.index(5,2)) #4
print(new.index(8,6,8)) #start from index 6 to index 8

names = ["Hossam","Ahmed","Arya","Abbas"]
print(names.index("Ahmed",1))

#count >> return the number of times x appears in the list
print(new.count(5))

#reverse >> reverse the elements of the list
first_list = [1,2,4,5]
first_list.reverse()
print(first_list)

#sort >>msort the items of the list(in-place)
another_list = [6,4,1,2,5]
another_list.sort()
print(another_list)

#join
words = ['coding','is','fun']
print(' '.join(words)) #coding is fun

name = ['Mr','Hossam']
print('.'.join(name))