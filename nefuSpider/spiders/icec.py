import scrapy
from nefuSpider.items import NefuspiderItem


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

        for each in response.xpath("//li[@id]"):
            print('---------------')
            print(each)
            # 将我们得到的数据封装到一个 `ItcastItem` 对象
            item = NefuspiderItem()
            # extract()方法返回的都是unicode字符串
            name = each.xpath("a/@title").extract()
            title = each.xpath("a/text()").extract()
            # para = each.xpath("p/text()").extract()
            para = 'biubiubiu'

            print(name, title, para)

            # xpath返回的是包含一个元素的列表
            item['name'] = name[0]
            item['title'] = title[0]
            item['para'] = para[0]

            items.append(item)

        # 直接返回最后数据
        return items

    def parse_dir_contents(self, response):
        item = NefuspiderItem()

        item['date'] = response.xpath("//div[@class='detail_zy_title']/p/text()").extract_first()
        item['href'] = response
        item['title'] = response.xpath("//div[@class='detail_zy_title']/h1/text()").extract_first()
        data = response.xpath("//div[@class='detail_zy_c pb30 mb30']")
        item['content'] = data[0].xpath('string(.)').extract()[0]
        return item
