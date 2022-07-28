""" Beatiful Soup """
# Beautiful soup doesn't download HTML , we will use requests to download the html
#? parsing is defined as the processing of a piece of python program and converting these codes into machine language
#! Navigation is an important concept as it lets you flow through the different sections of a website.

# using find >> returns one matching tag
# using find_all >> returns a list of all matching tags
from bs4 import BeautifulSoup
html = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>First HTML Page</title>
</head>
<body>
  <div id="first">
    <h3 data-example="yes">hi</h3>
    <p>more text.</p>
  </div>
  <ol>
    <li class="special">This list item is special.</li>
    <li class="special">This list item is also special.</li>
    <li>This list item is not special.</li>
  </ol>
  <div data-example="yes">bye</div>
</body>
</html>
"""
#               html >> elpage ely ana 3ayz a3mel 3aleha el sho8l
soup = BeautifulSoup(html,'html.parser') # html.parser >> el parser beta3 html 3ashan a3raf a3mel processing w kda

# print(soup)
# print(soup.find("div"))
print('#'*100)
# print(soup.find_all("div"))
# print(soup.find(id='first'))
# print(soup.find_all(class_="special"))
# print(soup.find(attrs = {"data-example":"yes"}))


# select - returns a list of elements matching a CSS selector
""" 
Select by id of foo: #foo 
Select by class of bar: .bar
Select children: div > p 
Select descendents: div p
"""
# print(soup.select('#first'))
# print(soup.select('.special'))
# print(soup.select('[data-example]'))    



#? get_text - access the inner text in an element
#? name - tag name
#! attrs - dictionary of attributes
#! You can also access attribute values using brackets!

k = (soup.select('.special'))[0]
# print(k.get_text())
for i in soup.select('.special'):
    print(i.get_text())

for i in soup.select('.special'):
    print(i.name)
    print(i.attrs)
