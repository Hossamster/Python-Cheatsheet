#dictionary comprenhension
numbers = {"first":1,'second':2,'third':3}
squared = {key:val **2 for key,val in numbers.items()}
print(squared) #{'first': 1, 'second': 4, 'third': 9}

numbers = {num:num **2 for num in [1,2,3,4,5,6]}
print(numbers) #{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36}

str1 = "ABC"
str2 = '123'
combo = {str1[i]:str2[i] for i in range(0,len(str1))}
print(combo)

#conditional logic 
num_list = [1,2,3,4]
k = {num:("even" if num % 2 == 0 else "odd") for num in num_list}
print(k)

list1 = ["CA", "NJ", "RI"]
list2 = ["California", "New Jersey", "Rhode Island"]

# make sure your solution is assigned to the answer variable so the tests can work!
answer = {list1[i]:list2[i] for i in range(0,len(list2))}
print(answer)
