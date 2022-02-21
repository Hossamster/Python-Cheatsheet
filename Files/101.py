# pip install pyfiglet
from pyfiglet import figlet_format
from termcolor import colored
# print(help(figlet_format))
# print(help(colored))
valid_colors = ('red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white')
word = input("What is the word: ")
color = input('what is the color: ')
if color not in valid_colors:
    color = 'red'
ascii_art = (figlet_format(word))
print(colored(ascii_art, color))
