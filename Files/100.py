# pip install colorama
# to import/init the colorama module
# pip install termcolor

# import termcolor
# print(dir(termcolor))
# print(help(termcolor))

from termcolor import colored
# colored(word,color,on_color, attrs=[]) >> note: attrs must be a list
print(colored("Hossam", color='magenta',
      on_color="on_white", attrs=['underline', 'bold']))
