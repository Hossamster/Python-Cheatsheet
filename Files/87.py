# filter
nums = [1, 2, 3, 4]
evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)  # [2, 4]

# Can we make it with map ?
odd = list(map(lambda x: x % 2 != 0, nums))
print(odd)  # [True, False, True, False]

names = ['austin', 'penny', 'anthony', 'angel', 'billy']
a_names = list(filter(lambda x: x[0] == 'a', names))
print(a_names)

users = [
    {"username": "Hossam", 'tweets': ["I love python", 'I love programming']},
    {"username": "Ahmed123", 'tweets': ["ich bin tut"]},
    {"username": "dodo", 'tweets': []},
    {"username": "Leo", 'tweets': ["dogs are the best"]},
]

# inactive_users = filter(lambda u: len(u['tweets']) == 0,users)
inactive_users = filter(lambda u: not u['tweets'], users)
print(list(inactive_users))

# combining filter and map
names = ["Tam", "Hossam", 'Dodo']
v_names = map(lambda name: f"Your instructor is {name}", filter(
    lambda v: len(v) < 5, names))
print(list(v_names))

# let's do it again
another = list(map(lambda user: user["username"], filter(
    lambda x: not x['tweets'], users)))
print(another)

####
# Ex


def remove_negatives(num):
    return list(filter(lambda n: n > 0, num))


print(remove_negatives([-1, 3, 4, -99]))
