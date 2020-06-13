import scrapy


class QuotesSpider(scrapy.Spider):
    name = "asktal2"

    def start_requests(self):
        urls = [
            'http://www.ask-tal.co.il',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        filename = 'ask-tal2.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)