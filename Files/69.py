#set comprehension >> useful when converting other data types to a set
print({x**2 for x in range(10)}) # set
print({x:x**2 for x in range(10)}) #dictionary
print({char.upper() for char in "hello"})
