import scrapy

class WikiSpider(scrapy.Spider):
    name = 'nhsrci'
    start_urls = ['https://nhsrcindia.org/health-informatics']

    def parse(self, response):
        for paragraph in response.css('p'):
            yield {
                'text': paragraph.extract(),
            }
        next_page = response.css('sup a::(href)').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)
    
