import scrapy

class WikiSpider(scrapy.Spider):
    name = 'wiki'
    start_urls = ['https://en.wikipedia.org/wiki/Health_informatics']

    def parse(self, response):
        for paragraph in response.css('p'):
            yield {
                'text': paragraph.extract(),
            }
        next_page = response.css('a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)
            