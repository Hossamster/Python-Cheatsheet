#accessing dictionary
instructor = {
    "name" : "Hossam",
    "Owns cat" :True,
    "number of cats":3,
    'fav language':'python',
    44 :"my favourite number"
    }

print(instructor['name'])
print(instructor["number of cats"])
print(instructor[44])

[print(key) for key,val in instructor.items() if val == "python"]


# artist = {
#     "first": "Neil",
#     "last": "Young",
# }
# full_name = f"{artist['first']} {artist['last']}"
# full_name = artist['first]+ " "+artist['last']
# full_name = "{} {}".format(artist['first'],artist['last'])
# print(full_name)