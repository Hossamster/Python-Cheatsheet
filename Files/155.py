import requests
from bs4 import BeautifulSoup
from csv import reader,writer,DictWriter
from time import sleep
base_url = "https://quotes.toscrape.com/"
url='/page/1/'
all_quotes = []
while url:
    response = requests.get(f"{base_url}{url}")
    soup = BeautifulSoup(response.text,"html.parser")
    quotes = soup.find_all(class_='quote')
    authors = soup.find_all(class_='author')
    print(f'now scraping {base_url}{url}')
    for quote in quotes:
        all_quotes.append(
            {
                "text":quote.find(class_='text').get_text(),
                'author':quote.find(class_='author').get_text(),
                'bio-link':quote.find('a')['href']
                })

    next_btn = soup.find(class_='next')
    url = (next_btn.find('a')['href']) if next_btn else None
    # sleep(1)

from random import choice
quote = choice(all_quotes)
guess = ''
count = 4
print(quote['author'])
print('#'*100)

print(f"Here is a quote {quote['text']}")
while guess.lower() != quote['author'].lower() and count > 0:
    guess = input(f'can u tell me who said this? , u have a {count} remaining chances ')
    count -= 1
    if guess.lower() == quote['author'].lower() :
        print("u get it bravoooooooooo!")
        break
    if count == 3:
        res = requests.get(f"{base_url}{quote['bio-link']}")
        soup = BeautifulSoup(res.text,'html.parser')
        birthday = soup.find(class_='author-born-date').get_text()
        birthplace = soup.find(class_='author-born-location').get_text()
        print(f"here is a hint, the author was born on {birthday} in {birthplace}")
    elif count == 2:
        print(f"here is a hint, the author's first name starts with: {quote['author'][0]}")
    elif count == 1:
        last_name = quote['author'].split(' ')[1][0]
        print(f"here is a hint, the author's last name starts with: {last_name}")
    else:
        print(f"sorry u ran out of guesses, tha author's name is {quote['author']}")



        