import requests
url = "https://icanhazdadjoke.com/search"
user_input = input("Let me tell you a joke! Give me a topic: ")
res = requests.get(url,
            headers={"Accept":"application/json"},
            params={'term':user_input})
results = (res.json())
print(results['results'])
from random import randint
x = randint(0,len(results['results']))
print(len(results['results']))
print(x)