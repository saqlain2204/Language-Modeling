import scrapy

class WikiSpider(scrapy.Spider):
    name = 'michigan'
    start_urls = ['https://www.mtu.edu/health-informatics/what-is/']

    def parse(self, response):
        for paragraph in response.css('p'):
            yield {
                'text': paragraph.extract(),
            }
        next_page = response.css('sup a::(href)').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)
    
