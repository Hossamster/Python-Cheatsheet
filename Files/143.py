import os

# print(os.getcwd())

# print(os.path.abspath(__file__))

# print(os.path.dirname(os.path.abspath(__file__)))

# os.chdir(os.path.dirname(os.path.abspath(__file__)))

# print(os.getcwd())

# file = open(r"C:\Users\Hossam\Desktop\jndsaj.txt",'r+')
# file.write('Hello from Hossam\n')
# print(file.read())

# file.write('Helloxxxx')
# file.write('Helloxxxx')


# file.close()

# mylst = ['Hossam\n','Hassan\n','Kamel\n']
# file.writelines(mylst)
# file.truncate()
# file.close()
# print(file.closed)


# myfile = open(r"C:\Users\Hossam\Desktop\jndsaj.txt",'a')
# myfile.write("appending\n")
# myfile.write("love\n")
# myfile.write("love\n")
# myfile.close()

# myfile = open(r"C:\Users\Hossam\Desktop\jndsaj.txt",'a')
# myfile.write("Hiiiiiiii\n")
# myfile.close()

# myfile = open(r"C:\Users\Hossam\Desktop\jndsaj.txt",'w')
# myfile.write("newfile\n")
# myfile.truncate(4)
# print(myfile.tell()) 
# myfile.close()

# myfile = open(r"C:\Users\Hossam\Desktop\jndsaj.txt",'a')
# myfile.write("Hiiiiiiii\n")
# print(myfile.tell()) 








'''
copy('story.txt', 'story_copy.txt') # None
# expect the contents of story.txt and story_copy.txt to be the same
'''


def copy(text1, text2):
    with open(text1, 'r') as file1:
        data1 = file1.read()
    with open(text2, 'w') as file2:
        data2 = file2.write(data1)
    # print(data1)
    # print(data2)

# copy('ayhaga.txt','new_text_file.txt')


'''
copy_and_reverse('story.txt', 'story_reversed.txt') # None
# expect the contents of story_reversed.txt to be the reverse of the contents of story.txt
'''


def copy_and_reverse(file, revfile):
    with open(file, 'r') as file:
        file = file.read()

    data = file[::-1]

    with open(revfile, 'w') as revfile:
        revfile = revfile.write(data)


# copy_and_reverse('ayhaga.txt','new_text_file.txt')


'''
statistics('story.txt') 
# {'lines': 172, 'words': 2145, 'characters': 11227}
'''


def statistics(file):
    with open(file, mode='r', encoding="utf8") as file:
        data = file.read()
    return {'lines': len(data.split('\n')), 'words': len(data.split(" ")), 'characters': len(data)}


# print(statistics('new_text_file.txt'))



'''
find_and_replace('story.txt', 'Alice', 'Colt') 
# story.txt now contains the first chapter of my new book,
# Colt's Adventures in Wonderland
'''

def find_and_replace(file,searchword,repword):  
    with open(file, mode = 'r+') as file:
        data = file.read()
        new_txt = data.replace(searchword,repword)
        # file.seek(0)
        file.write(new_txt)
        file.truncate()
    


# find_and_replace('ayaha.txt', 'hossam', 'Joe')

""" 
? truncate deletes everything in the file after the current cursor position. 

? It is needed because "Colt" is shorter than "Alice" 
? and we are overwriting character by character from the beginning, 
? so the new text will be shorter than the original by one character for replaced "Alice". 

"""