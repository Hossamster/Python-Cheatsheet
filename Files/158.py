""" Scrapy framework """
import scrapy 
class Bookspider(scrapy.Spider):
    name = 'bookspider'
    start_urls = ['http://books.toscrape.com']

    def parse(self,response):
        for article in response.css('article.product_pod') :# its like >> soup.select('.')
            yield {'price': article.css(".price_color::text").get("price_color")}

# scrapy runspider -o books.csv 158.py

# After HTML & CSS............