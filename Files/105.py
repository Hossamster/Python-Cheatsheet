import requests
url = 'https://www.icanhazdadjoke.com/search'
res = requests.get(url,
            headers={"Accept":"application/json"},
            params={"term":"love",'limit':2})
data = res.json()
# print(data)
print(data['results'])