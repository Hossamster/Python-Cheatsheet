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
    sleep(1)


with open('ayhaga.csv','w',newline='',encoding='utf8') as file:
    headers = ['text','author','bio-link']
    csv_writer = DictWriter(file, fieldnames=headers)
    csv_writer.writeheader()
    for quote in all_quotes:
        csv_writer.writerow(quote)