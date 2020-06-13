# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup



class AsktalSpider(scrapy.Spider):
    name = 'asktal3'
    allowed_domains = ['www.ask-tal.co.il']
    start_urls = ['http://www.ask-tal.co.il/']

    def parse(self, response):
        #soup = BeautifulSoup(response.body, 'html.parser')
        filename = 'ask-tal3.html'
        with open(filename, 'wb') as f:
            f.write(response.body)



