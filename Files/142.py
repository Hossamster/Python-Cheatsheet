""" File modes """
# r >> read
# w >> write
# a >> append 

# with open("ayhaga.txt",'a') as file:
#     file.write('\nHellllllllozzzzzzzz')

# r+ >> read and write (writing based on cursor)

with open ("ayhaga.txt",'r+') as file:
    file.write(":)")
    file.seek(19)
    # file.write()

