import requests
from csv import writer,DictWriter
from bs4 import BeautifulSoup
from time import sleep
base_url = "https://quotes.toscrape.com/"
url='/page/1/'
url = "http://quotes.toscrape.com/author/Albert-Einstein/"
all_quotes = []
# while url:
#     response = requests.get(f"{base_url}{url}")
#     soup = BeautifulSoup(response.text,'html.parser')
#     quotes = soup.find_all(class_='quote')
#     authors = soup.find_all(class_='author')
#     print(f'now scraping {base_url}{url}')
#     for quote in quotes:
#         all_quotes.append(
#             {
#                 'text':quote.find(class_='text').get_text(),
#                 'author':quote.find(class_='author').get_text(),
#                 'bio-link':quote.find('a')['href']
#             }
#         )
#     next_btn = soup.find(class_='next')
#     url = next_btn.find('a')['href'] if next_btn else None


response = requests.get(url)
soup = BeautifulSoup(response.text,'html.parser')
description = soup.find(class_='author-description').get_text()
lsts = description.split(',')
# print(lsts)
for i in range(4,len(lsts)-2):
    print(lsts[i])
