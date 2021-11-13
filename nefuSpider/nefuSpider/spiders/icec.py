import scrapy


class IcecSpider(scrapy.Spider):
    name = 'icec'
    allowed_domains = ['https://icec.nefu.edu.cn/']
    start_urls = ['http://https://icec.nefu.edu.cn//']

    def parse(self, response):
        pass
