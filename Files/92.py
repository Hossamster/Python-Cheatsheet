#zip
first_zip = zip([1,2,3],[4,5,6])
print(dict(first_zip)) #{1: 4, 2: 5, 3: 6}
print(first_zip) # zip object
first_zip = zip([1,2,3],[4,5,6])
print(list(first_zip)) #[(1, 4), (2, 5), (3, 6)]

num1 = [1,2,3,4,5]
num2 = [6,7,8,9,10]
z = zip(num1,num2)
print(list(z)) #[(1, 6), (2, 7), (3, 8), (4, 9), (5, 10)]

z = zip(num1,num2)
print(dict(z)) #{1: 6, 2: 7, 3: 8, 4: 9, 5: 10}

words = ['hi','lol','haha',':)']
z = zip(num1,num2,words)
print(list(z)) #[(1, 6, 'hi'),(2, 7, 'lol'),(3, 8, 'haha'),(4, 9, ':)')]

five_by_two = [(0,1),(1,2),(2,3),(3,4),(4,5)]
z = zip(*five_by_two)
print(list(z))

########
midterms = [80,91,78]
finals = [98,89,53]
students = ['dan','ang','kate']

# final_grades = [max(pair) for pair in zip(midterms,finals)] #[98, 91, 78]
final_grades = {pair[0]:max(pair[1],pair[2]) for pair in zip(students,midterms,finals)}
print(final_grades)
#same
scores = zip(
    students,
    map(
        lambda x:max(x), 
        zip(midterms,finals)
    )
)
print(dict(scores))