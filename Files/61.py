# pop to remove the key-value 
d = dict(a=1,b=2,c=3)
# d.pop() >>> type error
d.pop("a")
print(d)

instructor = {
    "name" : "Hossam",
    "Owns cat" :True,
    "number of cats":3,
    'fav language':'python',
    44 :"my favourite number"
    }

instructor.pop("number of cats")
print(instructor)

#popitem removes the last one
# d.popitem('b') >>> error
d.popitem()
print(d)

#update keys and values with another set of key-value pairs

instructor.update({"Married":False})
print(instructor)

instructor['name'] = "Hamada"
print(instructor)


