# NEFU-News-Crawler
## Description

支持抓取下述各站点的内容列表，并导出为json/csv格式，并对每个网页抓取图片快照。

| 网站名称                                 | 网址                                    |
| ---------------------------------------- | --------------------------------------- |
| 东北林业大学新闻站综合新闻               | https://news.nefu.edu.cn/dlyw.htm       |
| 东北林业大学新闻站人物专栏               | https://news.nefu.edu.cn/xyrw.htm       |
| 东北林业大学信息与计算机工程学院新闻中心 | https://icec.nefu.edu.cn/index/xwzx.htm |
| 东北林业大学机电工程学院                 | https://cmee.nefu.edu.cn/index/xyxw.htm |



## Usage

### 信息学院

`scrapy crawl icec -o titles.json`

### 内容

`scrapy crawl icec_content -o titles.json`

### 机电学院

`scrapy crawl cmee_content -o titles.json`

### 东林新闻主站

综合新闻抓取新增了日期前缀，方便查阅日期和后续的图片快照抓取。

`scrapy crawl news -o titles.json`

### 东林新闻站人物栏目

`scrapy crawl people -o titles.json`

### 网页图片快照抓取

首先将抓取内容导出为csv文件，然后使用`screen.py`，在其中改好`chromedriver`路径、网页数据(csv)文件地址以及图片的保存路径，即可进行批量快照保存。
