import scrapy
from nefuSpider.items import NefuspiderItem

NEXT_PAGE_NUM = 1


class IcecSpider(scrapy.Spider):
    name = "icec"
    start_urls = ['https://icec.nefu.edu.cn/index/xwzx/1.htm']

    def parse(self, response):
        for href in response.xpath("//li[@id]"):
            url = response.urljoin(href.xpath("a/@href").extract_first())
            if url.find('type') != -1:
                yield scrapy.Request(url, callback=self.parse)
            yield scrapy.Request(url, callback=self.parse_dir_contents)
        global NEXT_PAGE_NUM
        NEXT_PAGE_NUM = NEXT_PAGE_NUM + 1
        if NEXT_PAGE_NUM <= 32 + 1:
            if NEXT_PAGE_NUM == 32 + 1:
                next_url = 'https://icec.nefu.edu.cn/index/xwzx.htm'
            else:
                next_url = 'https://icec.nefu.edu.cn/index/xwzx/%s.htm' % NEXT_PAGE_NUM
            yield scrapy.Request(next_url, callback=self.parse)

    def parse_dir_contents(self, response):
        item = NefuspiderItem()
        item['title'] = response.xpath("//div[@class='sub_cont']/form/h2/text()").extract_first()
        item['date'] = response.xpath("//div[@class='sub_cont']/form/div[@class='wzxxys']/text()").extract_first()
        # item['href'] = response
        data = response.xpath("//div[@class='sub_about']")
        item['content'] = data[0].xpath('string(.)').extract()[0]
        yield item
