import scrapy
from nefuSpider.items import NefuspiderItem

NEXT_PAGE_NUM = 1


class IcecSpider(scrapy.Spider):
    name = "icec_test"
    start_urls = ['https://icec.nefu.edu.cn/index/xwzx/1.htm']

    def parse(self, response):
        for href in response.xpath("//div[@class='newsinfo_box cf']"):
            URL = response.urljoin(href.xpath("div[@class='news_c fr']/h3/a/@href").extract_first())
            if URL.find('type') != -1:
                yield scrapy.Request(URL, callback=self.parse)
            yield scrapy.Request(URL, callback=self.parse_dir_contents)
        global NEXT_PAGE_NUM
        NEXT_PAGE_NUM = NEXT_PAGE_NUM + 1
        if NEXT_PAGE_NUM < 33:
            next_url = 'https://icec.nefu.edu.cn/index/xwzx/%s.htm' % NEXT_PAGE_NUM
            yield scrapy.Request(next_url, callback=self.parse)

    def parse_dir_contents(self, response):
        item = NefuspiderItem()
        item['date'] = response.xpath("//div[@class='detail_zy_title']/p/text()").extract_first()
        item['href'] = response
        item['title'] = response.xpath("//div[@class='detail_zy_title']/h1/text()").extract_first()
        data = response.xpath("//div[@class='detail_zy_c pb30 mb30']")
        item['content'] = data[0].xpath('string(.)').extract()[0]
        yield item
