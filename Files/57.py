#accessing all values >> use.values()
#accessing all keys >> use.keys()
#accessing both (keys and values) >> use.items()
instructor = {
    "name" : "Hossam",
    "Owns cat" :True,
    "number of cats":3,
    'fav language':'python',
    44 :"my favourite number"
    }
for val in instructor.values():
    print(val)

for key in instructor.keys():
    print(key)

for key,value in instructor.items():
    print(key,value)

