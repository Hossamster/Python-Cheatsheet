#tuple >> ordered elements
#immutable >> means that it can not be changed
t = (1,2,3,4)
print(type(t))
print(t)
# t[0] = 9 # type error as tuple can not changed 
#tuples are faster than list
# it makes code safer from bugs and problems popping up 
#valid keys in dictionary

k = ('a','b','c','d')
print(k[0])
print(k[1])
print(k[2])

locations = {
    (30.2343,54.54):"Tokyo office",
    (65.665,88.443):"Egypt office",
    (99.332,324.992):"UAE office"
}
print(locations[(99.332,324.992)])



"""
you can not use list as a key in dictionary 

"""
# loc = {[323.32,324.555]:"Lybya office"} #type error
