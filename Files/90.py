<<<<<<< HEAD
#Min and max
print(max('c', 'd', 'a'))  # d
nums = [40, 32, 6, 5, 10]
print(max(nums))  # 40

print(max((1, 2, 3, 4)))  # 4

print(min('c', 'd', 'a'))  # a
nums = [40, 32, 6, 5, 10]
print(min(nums))  # 5

print(min((1, 2, 3, 4)))  # 1

names = ['Arya', 'Samson', 'Dora', "Tim", "Ollivander"]
print(min(names))  # alphabaticly >> Arya
print(max(names))  # alphabaticly >> Tim

print(min(len(name) for name in names))
print(max(len(name) for name in names))

songs = [
    {"title": "happy birthday", "playcount": 1},
    {"title": "survive", "playcount": 6},
    {"title": "Toxic", "playcount": 31},
    {"title": "YMCA", "playcount": 94},
]

print(min(songs, key=lambda x: x['playcount']))
print(max(songs, key=lambda x: x['playcount']))
print(max(songs, key=lambda x: x['playcount'])['title'])

###########
#Ex
# def extremes(my):
#     return (min (my),max(my))
# print(extremes([1,2,3,4,5]))
# print(extremes((99,25,30,-7)))
# print(extremes("alcatraz"))
=======
#Min and max
>>>>>>> main
