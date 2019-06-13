import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes" #identifies the spider, has to be unique

    def start_requests(self):
        urls = [
            'http://quotes.toscrape.com/page/1/',
            'http://quotes.toscrape.com/page/2/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text')[0].get(),
                'author': quote.css('small.author::text')[0].get(),
                'tags': quote.css('div.tag a.tag::text').getall(),
            }
        next_page = response.css('li.next a::attr(href)')
        if next_page is not None:
            # next_page = response.urljoin(next_page)
            # yield scrapy.Request(next_page,callback=self.parse)
            yield response.follow(next_page,callback=self.parse)
            
        
            

        
        # page = response.url.split("/")[-2]
        # filename = 'quotes-%s.html' % page
        # with open(filename, 'wb') as f:
        #     f.write(response.body)
        # self.log('Saved file %s' % filename)