import scrapy
from nefuSpider.items import NefuspiderItem

NEXT_PAGE_NUM = 1


class IcecSpider(scrapy.Spider):
    name = "people"
    start_urls = ['https://news.nefu.edu.cn/xyrw/1.htm']

    def parse(self, response):
        for href in response.xpath("//div[@class='txt']"):
            url = response.urljoin(href.xpath("h3/a/@href").extract_first())
            if url.find('type') != -1:
                yield scrapy.Request(url, callback=self.parse)
            yield scrapy.Request(url, callback=self.parse_dir_contents)
        global NEXT_PAGE_NUM
        NEXT_PAGE_NUM = NEXT_PAGE_NUM + 1
        if NEXT_PAGE_NUM <= 32 + 1:
            if NEXT_PAGE_NUM == 32 + 1:
                next_url = 'https://news.nefu.edu.cn/xyrw.htm'
            else:
                next_url = 'https://news.nefu.edu.cn/xyrw/%s.htm' % NEXT_PAGE_NUM
            yield scrapy.Request(next_url, callback=self.parse)

    def parse_dir_contents(self, response):
        item = NefuspiderItem()
        item['title'] = response.xpath("//div[@class='m-text m-text-b']/h1/text()").extract_first()
        item['date'] = response.xpath("//div[@class='l']/span/text()").extract_first()
        print('----------------------')
        print(item['date'])

        # item['href'] = response
        data = response.xpath("//div[@class='v_news_content']")
        item['content'] = data[0].xpath('string(.)').extract()[0]
        yield item
