from pyfiglet import figlet_format
from termcolor import colored
print(colored(figlet_format("Dad Joke 3000"),'magenta'))
import requests
url = "https://icanhazdadjoke.com/search"
user_input = input("Let me tell you a joke! Give me a topic: ")
res = requests.get(url,
            headers={"Accept":"application/json"},
            params={'term':user_input})

results = (res.json())
# print(results['results'])


if len(results['results']) != 0:
    print(f"I've got {len(results)} joke/s about {user_input}.Here's one: ") 
    from random import randint
    x = randint(0,len(results['results']) - 1)
    print(results['results'][x]['joke'])
else:
    print(f"Sorry, I don't have any jokes about {user_input}! Please try again.")
