import scrapy


class IcecSpider(scrapy.Spider):
    name = 'icec'
    allowed_domains = ['icec.nefu.edu.cn']
    start_urls = ['https://icec.nefu.edu.cn/index/xwzx.htm']

    def parse(self, response):
        filename = "xwzx.htm"
        open(filename, 'w').write(response.body)
