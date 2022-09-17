# import requests
# url = "https://icanhazdadjoke.com/search"

# res = requests.get(url,headers = {'Accept':'text/plain'})
# res = requests.get(url,headers = {'Accept':'application/json'})

# print(res.ok)
# print(res.headers)
# print(res.text)
# print(type(res.text))
# data = res.json()
# print(data)
# print(data['joke'])
# print(f"status:{data['status']}")
# print(type(data))
# print(res.status_code)


# params = {'term':'wife','limit':2}
# res = requests.get(url,params = params,headers={'Accept':'Application/json'})
# k = res.json()

# for joke in k.get('results'):
#     print(joke['joke'])
#     print('\n')


from pyfiglet import figlet_format
from termcolor import colored
from random import randint
import requests
print(colored(figlet_format('Hossam Jokes'),color = 'magenta'))
input = str(input('Give me a topic to tell u a joke: '))
url = "https://icanhazdadjoke.com/search"
response = requests.get(url,params = {'term':input},headers = {'Accept':'application/json'})
length = (len(response.json()['results']))


r = (randint(0,len(response.json()['results'])-1))
print(r)

if length < 1:
    print('No jokes for this topic')
else: 
    ans = (response.json()['results'][r]['joke'])
    print(f"I've got {length} about {input}. Here it is: ")
    print(ans)



