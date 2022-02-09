# Dictionary methods (clear,copy,formkey,get)
instructor = {
    "name" : "Hossam",
    "Owns cat" :True,
    "number of cats":3,
    }
print(instructor)

#clear all keys and values
instructor.clear()
print(instructor)

#copy dictionary
c = {"name" : "Hamada","age" : 22,"Owns cat" :False}
d = c.copy()
print(d)
print(c == d)

#fromkeys to create key-values (to generate default values)
new_user = {}.fromkeys(['name','age','score','value'],'unknown')
print(new_user)

#get.. retrieves a key in an object and return none.
#instead of keyerror if the key does not exist
d = {'a':1,"b":1,"c":3}
print(d['a'])  
print(d.get('a'))
print(d['b'])
print(d.get('b'))
# print(d['no_key']) # key error >>>>>>>>><<<<<<<<<<
print(d.get('no_key'))

print(c.get('name'))
cal = "name"
print(c[cal])

