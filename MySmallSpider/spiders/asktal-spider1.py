# -*- coding: utf-8 -*-
import scrapy


class AsktalSpider(scrapy.Spider):
    name = 'asktal1'
    allowed_domains = ['www.ask-tal.co.il']
    start_urls = ['http://www.ask-tal.co.il/']

    def parse(self, response):
        pass
