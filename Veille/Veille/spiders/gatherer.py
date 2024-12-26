import scrapy

class GathererSpider(scrapy.Spider):
    name = 'gatherer'
    start_urls = ['https://thehiddenwiki.org/','https://thehidden2.wiki/',]

    def parse(self, response):
        for article in response.css('a'):
            yield {
                'url': article.css('a::attr(href)').get(),
                'description': response.css('a::text').get(),
            }
