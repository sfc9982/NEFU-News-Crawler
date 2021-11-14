import scrapy
from nefuSpider.nefuSpider.items import NefuspiderItem


class IcecSpider(scrapy.Spider):
    name = 'icec'
    allowed_domains = ['icec.nefu.edu.cn']
    start_urls = ['https://icec.nefu.edu.cn/index/xwzx.htm']

    def parse(self, response):
        # filename = "xwzx.htm"
        # open(filename, 'wb+').write(response.body)  # need to be wb+, or treated as str -> fail
        # context = response.xpath('//*[@id]/a/@title')
        # title_present = context.extract_first()
        # print(title_present)
        # 存放新闻信息的集合
        items = []

        for each in response.xpath("//*[@id]/a/@title"):
            # 将我们得到的数据封装到一个 `ItcastItem` 对象
            item = NefuspiderItem()
            # extract()方法返回的都是unicode字符串
            name = each.xpath("h3/text()").extract()
            title = each.xpath("h4/text()").extract()
            para = each.xpath("p/text()").extract()

            # xpath返回的是包含一个元素的列表
            item['name'] = name[0]
            item['title'] = title[0]
            item['para'] = para[0]

            items.append(item)

        # 直接返回最后数据
        return items
        # pass
