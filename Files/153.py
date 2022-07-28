import requests
from bs4 import BeautifulSoup
from csv import reader,writer,DictReader,DictWriter
url = "https://www.rithmschool.com/blog"
response = requests.get(url)
soup  = BeautifulSoup(response.text,'html.parser')
articles = soup.find_all('article')
with open ('blog_data_csv.csv','w',newline='') as file:
    csv_writer = writer(file)
    csv_writer.writerow(['title','line','date'])

    for i in articles:
        a_tag = i.find('a')
        title = a_tag.get_text()
        url = a_tag['href']
        date = i.find('time')['datetime']
        csv_writer.writerow([title, url, date]) 
