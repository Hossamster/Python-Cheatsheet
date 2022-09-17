import sqlite3
import requests 
from bs4 import BeautifulSoup
# request url
# initialize bs 
# extract data we want
# save data to database

    
def scrape_book(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text,'html.parser')
    books = soup.find_all('article') 
    all_books = []
    for book in books:
        book_data = (get_title(book),get_price(book),get_rating(book))
        all_books.append(book_data)
    save_books(all_books)
    

def get_title(book):
    return (book.find('h3').find('a')['title'])    


def get_price(book):
    price = book.select(".price_color")[0].get_text()
    return (float(price.replace('Â','').replace('£','')))

def get_rating(book):
    ratings = {'One': 1, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5}
    paragraph = book.select('.star-rating')[0]
    word = paragraph.get_attribute_list('class')[-1]
    return ratings[word]

def save_books(all_books):
    conn = sqlite3.connect('books.db')
    c = conn.cursor()

    query1 = "CREATE TABLE books (title TEXT, price REAL, rating INTEGER )"
    c.execute(query1)

    query2 = "INSERT INTO books VALUES (?,?,?)"
    c.executemany(query2,all_books)

    conn.commit()
    conn.close()
    
scrape_book("https://books.toscrape.com/catalogue/category/books/history_32/index.html")
