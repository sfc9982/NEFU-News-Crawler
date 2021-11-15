import scrapy
from nefuSpider.items import MainSiteNewsItem

NEXT_PAGE_NUM = 1


class NewsSpider(scrapy.Spider):
    name = "news"
    start_urls = [
        'https://news.nefu.edu.cn/supersearch.jsp?wbtreeid=1001&currentnum=1&_vt=&_vn=6YKu566x&_vk=&_vm=&_va=&_vs'
        '=&_vc=&_vb=&_ve=&searchScope=1&type=-1']

    def parse(self, response):
        items = []
        for each in response.xpath("//div[@class='txt']"):
            item = MainSiteNewsItem()
            title = each.xpath("h4/a/text()").extract_first()
            link = response.urljoin(each.xpath("h4/a/@href").extract_first())
            item['title'] = title
            item['link'] = link
            print('-------------')
            print(item)
            items.append(item)
        global NEXT_PAGE_NUM
        NEXT_PAGE_NUM = NEXT_PAGE_NUM + 1
        if NEXT_PAGE_NUM <= 5:
            next_url = 'https://news.nefu.edu.cn/supersearch.jsp?wbtreeid=1001&currentnum=%s&_vt=&_vn=6YKu566x&_vk' \
                       '=&_vm=&_va=&_vs=&_vc=&_vb=&_ve=&searchScope=1&type=-1' % NEXT_PAGE_NUM
            scrapy.Request(next_url, callback=self.parse)
        return items
