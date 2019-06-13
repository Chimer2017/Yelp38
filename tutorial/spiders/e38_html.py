import scrapy


class e38Spider(scrapy.Spider):
    name = "e38_html"

    def start_requests(self):
        urls = [
            'https://denver.eater.com/maps/best-restaurants-denver-eater-38',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'e38-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)