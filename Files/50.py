# List Cpmprenhension
nums = [1, 2, 3]
doubled = [x*2 for x in nums]
print(doubled)

name = 'hossam'
up = [c.upper() for c in name]
print(up)  # ['H', 'O', 'S', 'S', 'A', 'M']

friends = ['mohamed', 'matt', 'micheal']
upp = [friend[0].upper() + friend[1:] for friend in friends]
print(upp)  # ['Mohamed', 'Matt', 'Micheal']

print([num*10 for num in range(1, 6)])  # [10, 20, 30, 40, 50]

print([bool(val) for val in [0, [], '']])  # [False, False, False]

numbers = [1, 2, 3, 4, 5]
string_list = [str(num) for num in numbers]
print(string_list)  # ['1', '2', '3', '4', '5']
