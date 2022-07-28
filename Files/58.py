#check existence of something (key or value) in dictionary
instructor = {
    "name" : "Hossam",
    "Owns cat" :True,
    "number of cats":3,
    'fav language':'python',
    44 :"my favourite number"
    }

#Does a dictionary have a key
print("name" in instructor.keys())
print("Hossam" in instructor.keys())

#Does a dictionary have a value
print("Hossam" in instructor.values())
print("python" in instructor.values())
