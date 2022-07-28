#HTTP introduction
# DNS Lookup
# Computer makes a REQUEST to a server
# Server processes the REQUEST
# Server issues a RESPONSE
# Request/Response cycle

"""
GET

Useful for retrieving data
Data passed in query string
Should have no "side-effects"
Can be cached
Can be bookmarked
"""

"""
POST

Useful for writing data
Data passed in request body
Can have "side-effects"
Not cached
Can't be bookmarked
"""

"""
API - Application Programming Interface
Allows you to get data from another application without needing to understand how the application works
Can often send data back in different formats
Examples of companies with APIs: GitHub, Spotify, Google
"""

"""
Request headers
Accept - Acceptable content-types for response (e.g. html, json, xml)
Cache-Control - Specify caching behavior
User-Agent - Information about the software used to make the request
"""

"""
Response headers
Access-Control-Allow-Origin - specify domains that can make requests
Allowed - HTTP verbs that are allowed in requests
"""

# requests module
# pip install requests

import requests
url = "https://www.icanhazdadjoke.com"
res = requests.get(url)
# print(res)           # <Response [200]>
# print(res.ok)        # True or false
# print(res.headers) # metadata that came back
# print(res.text)    # view-source

# print(f"request to {url} came back with status code {res.status_code}") # lw tmam hayb2a 200 , lw fy problem hayb2a 404
# res = requests.get(url,headers={"Accept":"text/plain"})
# print(res.text)

res = requests.get(url,headers={"Accept":"application/json"})
data = res.json() # dict
print(data) # {'id': 'prWDIBdiGlb', 'joke': 'I just wrote a book on reverse psychology. Do not read it!', 'status': 200}
print(data['joke']) # our joke
print(f"status:{data['status']}") #200