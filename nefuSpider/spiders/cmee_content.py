import scrapy
from nefuSpider.items import NefuspiderItem

NEXT_PAGE_NUM = 1


class IcecSpider(scrapy.Spider):
    name = "cmee"
    start_urls = ['https://cmee.nefu.edu.cn/index/xyxw/1.htm']

    def parse(self, response):
        for href in response.xpath("//ul[@class='clearfixed']/*"):
            url = response.urljoin(href.xpath("a/@href").extract_first())
            yield scrapy.Request(url, callback=self.parse_dir_contents)
        global NEXT_PAGE_NUM
        NEXT_PAGE_NUM = NEXT_PAGE_NUM + 1
        if NEXT_PAGE_NUM <= 63 + 1:
            if NEXT_PAGE_NUM == 63 + 1:
                next_url = 'https://cmee.nefu.edu.cn/index/xwzx.htm'
            else:
                next_url = 'https://cmee.nefu.edu.cn/index/xyxw/%s.htm' % NEXT_PAGE_NUM
            yield scrapy.Request(next_url, callback=self.parse)

    def parse_dir_contents(self, response):
        item = NefuspiderItem()
        item['title'] = response.xpath("//form/h1/text()").extract_first()
        # print(item['title'])
        item['date'] = response.xpath("//p[@class='time-right']/span/text()").extract_first()
        # item['href'] = response
        data = response.xpath("//div[@class='v_news_content']")
        item['content'] = data[0].xpath('string(.)').extract()[0]
        yield item
