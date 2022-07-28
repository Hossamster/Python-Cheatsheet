""" Writing to files  """
# u still have to use the open function

# it will overwrite the existing text file
with open("ayhaga.txt",'w') as file: # w >> writing
    file.write("Hello World! from writing file ")

# with open("new_text_file.txt",'w') as file: # w >>
#     file.write("New file created\n" * 10)


print(data)