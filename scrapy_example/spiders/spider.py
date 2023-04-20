import scrapy

class MySpider(scrapy.Spider):
    name = 'my_spider'

    start_urls = [
        'https://www.example.com',
    ]

    def getTitle(self, response):
        title = response.css('title::text').get()
        return title

    def getLink(self, response):
        link = response.css('a::attr(href)').get()
        return link

    def getAllLinks(self, response):
        links = response.css('a::attr(href)').getall()
        for link in links:
            print(f'Enlace: {link}')

    def parse(self, response):
        print(self.getTitle(response))
        print(self.getLink(response))
        self.getAllLinks(response)
