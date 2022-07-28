from random import choice
from pyfiglet import figlet_format
import requests
from bs4 import BeautifulSoup
from csv import reader,writer,DictWriter,DictReader
from time import sleep
def open_file(filename):
    with open(filename) as file:
        csv_reader = DictReader(file)
        csv_reader = list(csv_reader)
        return csv_reader

base_url = "https://quotes.toscrape.com/"
url='/page/1/'
def start_game(QUOTES):
    quote = choice(QUOTES)
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
    repeat = ''
    while repeat.lower() not in ['yes','y','no','n']:
        repeat = input("Would u like to play again?")
    if repeat.lower() in ['yes','y']:
        return start_game()
    else:
        return "Okay GoodBye"
    
quotes = (open_file('quotes.csv'))
print(start_game(quotes))