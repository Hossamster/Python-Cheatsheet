
'''
print_users() # None
# prints to the console:
# Colt Steele
'''

def print_users():
    from csv import DictReader,reader
    with open('ayhaga.csv') as file:
        data = reader(file)
        data = list(data)
        data = iter(data)
        next(data)
        for i in data:
            print("{} {}".format(i[0],i[1]))
# print_users()
    

'''
find_user("Colt", "Steele") # 1
find_user("Alan", "Turing") # 3
find_user("Not", "Here") # 'Not Here not found.'
'''

def find_user(first=1,last=2):
    from csv import DictReader,reader
    with open('ayhaga.csv') as file:
        data = list(reader(file))
        for i in data:
            if first == i[0] and last == i[1]: 
                return(data.index(i))
        return("Not Here not found.")


# print(find_user("Colt","Steele"))
# print(find_user("Grace","Hopper"))
# print(find_user("Grace","Hoppere"))
lst = list(range(1,4))
count = 1
for i in lst:
    print(count,i)
    count += 1