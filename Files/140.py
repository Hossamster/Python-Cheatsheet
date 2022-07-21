""" With Statement """
with open("ayhaga.txt",'r') as file: 
    data = file.read()

print(file) # object 
print(file.closed) #? True
print(data)
# print(file.read()) #! Error >> closed file

#######################

# Behind the scenes
f = open("ayhaga.txt")
print(f) # <_io.TextIOWrapper name='ayhaga.txt' mode='r' encoding='cp1252'><_io.TextIOWrapper name='ayhaga.txt' mode='r' encoding='cp1252'>

#? when with starts, it calls the enter method
print(f.__enter__()) # <_io.TextIOWrapper name='ayhaga.txt' mode='r' encoding='cp1252'>
#? when with ends, it calls the exit method and close the file
(f.__exit__())
print(f.closed) 

