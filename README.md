# qqcar
腾讯汽车+热门地区新闻爬虫（Scrapy、Redis）

基于Python+scrapy+redis+mongodb的分布式爬虫实现框架

scrapy runspider qqcarredisurl.py 主要功能是抓取种子url，保存到redis

scrapy runspider qqcarmongodb.py 主要是从redis里面读url，解析数据保存到mongodb （拓展到其他机器,修改REDIS_HOST = "主机ip"，都是从redis里面读url,MONGODB_HOST = "存储服务器ip"）

middlewares.ProxyMiddleware 使用阿布云代理服务器轮换请求IP

主要爬取腾讯汽车全网新闻以及热门地区（杭州、北京、上海、重庆、广州、深圳、武汉、成都）行情资讯数据。

                                                       腾讯汽车新闻信息mongodb图示
![腾讯汽车新闻信息](https://github.com/renqian520/qqcar/blob/master/%E8%85%BE%E8%AE%AF%E6%B1%BD%E8%BD%A6%E6%96%B0%E9%97%BB%E4%BF%A1%E6%81%AF.jpg)
