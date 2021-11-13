import scrapy


class IcecSpider(scrapy.Spider):
    name = 'icec'
    allowed_domains = ['icec.nefu.edu.cn']
    start_urls = ['https://icec.nefu.edu.cn/index/xwzx.htm']

    def parse(self, response):
        filename = "xwzx.htm"
        open(filename, 'wb+').write(response.body)  # need to be wb+, or treated as str -> fail
