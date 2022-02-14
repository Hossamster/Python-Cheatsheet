#sorted >> tuple and list 
nums = [4,6,1,30,55,23]
# nums.sort() 
print(sorted(nums))
print(sorted(nums,reverse=True))

nums = (2,1,45,23,99)
print(sorted(nums))

users = [
    {"username": "Hossam", 'tweets': ["I love python", 'I love programming']},
    {"username": "Ahmed123", 'tweets': ["ich bin tut"]},
    {"username": "dodo", 'tweets': [],'ayhaga':'wlnaby'},
    {"username": "Leo", 'tweets': ["dogs are the best"]},
]

# print(sorted(users,key=lambda user:user['username']))
# print("\n")
# print(sorted(users,key=lambda user:len(user['tweets'])))


songs = [
    {"title":"happy birthday","playcount":1},
    {"title":"survive","playcount":6},
    {"title":"Toxic","playcount":31},
    {"title":"YMCA","playcount":94},
]
# print(sorted(songs,key = len))
print(sorted(songs,key = lambda song : (song['playcount'])))
print(sorted(songs,key = lambda song : len(song['title']),reverse=True))
# print(sorted(songs,key = len))

