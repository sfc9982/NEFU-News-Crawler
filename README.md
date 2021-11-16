# NEFU-News-Crawler
东北林业大学新闻爬虫

快速抓取ICEC信息院的相关新闻

## Commands

### Fetch News Title

`scrapy crawl icec -o titles.json`

内容

`scrapy crawl icec_content -o icec.json`

机电学院

`scrapy crawl cmee_content -o cmee.json`

新闻主站（支持关键字）

`scrapy crawl news -o main.json`
