import scrapy
import time

class DartSpider(scrapy.Spider):
    name = "dart"

    def start_requests(self):
        urls = [
            "https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20220406002679"
        ]

        for url in urls:
            yield scrapy.Request(url = url, callback = self.parse)

    def parse(self, response):
        time.sleep(3)
        title = response.css('html > body > p.cover-title > a::text').get()
        print(title)
