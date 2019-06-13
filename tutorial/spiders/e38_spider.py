import scrapy


class QuotesSpider(scrapy.Spider):
    name = "e38" #identifies the spider, has to be unique

    def start_requests(self):
        urls = [
            'https://denver.eater.com/maps/best-restaurants-denver-eater-38',

        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        namesRaw = response.css('div.c-mapstack__card-hed h1::text')
        names = []
        addRaw = response.css('div.c-mapstack__address::text')
        adds = []
        webRaw = response.css('div.c-mapstack__phone-url a::attr(href)')
        webs = []

        for i in range(1,len(namesRaw),2):
            names.append(namesRaw[i])
            webs.append(webRaw[i])
            adds.append(addRaw[i-1])
        print("Hello World")
        print(names[1].get())
        print(webs[1].get())
        print(adds[1].get())
        for i in range(len(names)):
            yield {
                'name': names[i].get(),
                'address': adds[i].get(),
                'website': webs[i].get(),
            }






        # for card in response.css('section.c-mapstack__card'):
        #     yield {
        #         'name': card.css('div.c-mapstack__card-hed h1::text').get(),
        #         'address': card.css('div.c-mapstack__address::text').get(),
        #         'website': card.css('div.c-mapstack__phone-url a::attr(href)').get(),
        #     }





        
        # next_page = response.css('li.next a::attr(href)')
        # if next_page is not None:
        #     # next_page = response.urljoin(next_page)
        #     # yield scrapy.Request(next_page,callback=self.parse)
        #     yield response.follow(next_page,callback=self.parse)
            
        
            

        
        # page = response.url.split("/")[-2]
        # filename = 'quotes-%s.html' % page
        # with open(filename, 'wb') as f:
        #     f.write(response.body)
        # self.log('Saved file %s' % filename)