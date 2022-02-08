#slicing >> make new lists using slices of the old list!
#some_list[start:end:step]
first_list = [1,2,3,4]
print(first_list[1:]) # [2, 3, 4]
print(first_list[2:]) # [3, 4]


print(first_list[-1:]) # [4]
print(first_list[-2:]) # [3, 4]

#second parameter: end
print(first_list[:2]) # [1,2]... doesn't include index 2
print(first_list[:4]) # [1,2,3,4]
print(first_list[1:3]) # [2,3]

print(first_list[:-1]) # [1,2,3]
print(first_list[1:-1]) #[2,3]

#third parameter: step
print(first_list[1::2]) #[2,4]
print(first_list[::2]) #[1,3]

#with negative numbers, reverse the order
print(first_list[1::-1]) #[2,1]
print(first_list[:1:-1]) #[4,3]
print(first_list[2::-1]) #[3,2,1]


##################       tricks with slices

#reversing lists / strings
string = "This is fun!"
print(string[::-1])

#modifying portions of lists
numbers = [1,2,3,4,5]
numbers[1:3] = ['a','b','c']
print(numbers)

print(numbers[::-1])