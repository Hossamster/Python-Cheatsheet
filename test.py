numbers = {"first":1,'second':2,"third":3}
squared = {key:num**2 for key,num in numbers.items()}
print(squared)

nsqr = {num:num**2 for num in [1,2,3,4,5,6]}
print(nsqr)

str1 = "ABC"
str2 = "123"
combo = {str1[i]:str2[i] for i in range(0,len(str1))}
print(combo)

num_list = [1,2,3,4]
k = {num:('even' if num % 2 == 0 else 'odd') for num in num_list}
print(k)

list1 = ["CA","NJ","RI"]
list2 = ["California","New Jersey","Rhode Island"]
answer = {list1[i]:list2[i] for i in range(0,len(list1))}
print(answer)

person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]
answer = {k:v for k,v in person}
print(answer)

person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]
answer = dict(person)
print(answer)

person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]
answer = {list[0]:list[1] for list in person}
print(answer)

# make sure your solution is assigned to the answer variable so the tests can work!
answer = {char:0 for char in "aeiou"}
#answer = dict.fromkeys("aeiou", 0)
print(answer)
