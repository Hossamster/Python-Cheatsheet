""" File IO """

f = open("ayhaga.txt",'r') # r >> reading

print (f)

# print(f.read()) #? I Love u

# print(f.read()) #? Empty ?!
#? Python reads files by using a cursor

f.seek(0) #! return the cusror to the beginning of the file

# print(f.read())

f.seek(0)

#? readline to read line by line
print(f.readline())
print(f.readline())
print(f.readline())


f.seek(0)
print(f.read())


f.seek(0)
print(f.readlines()) # ['I Love u \n', 'ah walahi\n', 'mat3rafsh ?\n']

(f.close())
print(f.closed)
