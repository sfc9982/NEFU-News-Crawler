import scrapy
from nefuSpider.items import MainSiteNewsItem

NEXT_PAGE_NUM = 1


class NewsSpider(scrapy.Spider):
    name = "news"
    start_urls = [
        'http://news.nefu.edu.cn/dlyw/463.htm']
        #https://news.nefu.edu.cn/supersearch.jsp?wbtreeid=1001&currentnum=1&_vt=&_vn=6YKu566x&_vk=&_vm=&_va=&_vs=&_vc=&_vb=&_ve=&searchScope=1&type=-1

    def parse(self, response):
        for each in response.xpath("//div[@class='txt']"):
            item = MainSiteNewsItem()
            title = each.xpath("h4/a/text()").extract_first()
            time = each.xpath("//div[@class='time']/span/text()").extract_first()
            link = response.urljoin(each.xpath("h4/a/@href").extract_first())
            #print(date)
            item['title'] = time + " " + title
            item['link'] = link
            # item['time'] = time
            # print('-------------')
            print(item)
            yield item
        global NEXT_PAGE_NUM
        NEXT_PAGE_NUM = NEXT_PAGE_NUM + 1
        if NEXT_PAGE_NUM <= 463 + 1:
            if NEXT_PAGE_NUM == 463+1:
                next_url = 'http://news.nefu.edu.cn/dlyw.htm'
            else:
                next_url = 'http://news.nefu.edu.cn/dlyw/%s.htm' % NEXT_PAGE_NUM
            yield scrapy.Request(next_url, callback=self.parse)
