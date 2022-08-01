import scrapy
import time

class DartSpider(scrapy.Spider):
    name = "dart"

    def start_requests(self):
        urls = [
            "https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20220406002679/report/viewer.do?rcpNo=20220406002679&dcmNo=8568716&eleId=1&offset=1052&length=4515&dtd=dart3.xsd"
        ]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        time.sleep(3)
        title = response.xpath('/html/body/p.cover-title/a/text()').get()
        print(title)