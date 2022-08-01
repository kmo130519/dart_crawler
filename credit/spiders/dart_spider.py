import scrapy


class DartSpider(scrapy.Spider):
    name = "dart"

    def start_requests(self):
        urls = [
            "https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20220406002679"
        ]

        for url in urls:
            yield scrapy.Request(url = url, callback = self.parse)

    def parse(self, response):
        # css or xpath
        movie_sels = response.css('ul.lst_detail_t1 > li > dl')
        item = {}
        for movie_sel in movie_sels:
            item['title'] = movie_sel.css('.tit > a::text').get()
            item['age_limit'] = movie_sel.css('.tit > span::text').get()
            item['rating'] = movie_sel.css('.star_t1 > a > span.num::text').get()
            item['rating_count'] = movie_sel.css('.star_t1 > a > span.num2 > em::text').get()
            yield item