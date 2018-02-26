# -*- coding: utf-8 -*-
import scrapy
from qqcar.items import RedisItem
import random
import time
import re
import datetime



class Qqcarspider(scrapy.Spider):
    name = 'qqcarspider'
    custom_settings = {
        'ITEM_PIPELINES':{
            'qqcar.pipelines.RedisPipeline':300,
        }
    }

    start_urls = ['http://auto.qq.com/articleList/rolls/',
                  # 杭州
                   'http://hangzhou.auto.qq.com/xcxx2014/list.htm',
                   'http://cgi.data.auto.qq.com/php/index.php?mod=carnews&act=citynewslist&city=395&serial=NaN&type=2&sort=3&page=1&pagesize=20&callback=price_data',

                  # 北京
                  'http://beijing.auto.qq.com',
                  'http://cgi.data.auto.qq.com/php/index.php?mod=carnews&act=citynewslist&city=54&serial=NaN&type=2&sort=3&page=1&pagesize=20&callback=price_data',

                  # 上海
                  'http://shanghai.auto.qq.com',
                  'http://cgi.data.auto.qq.com/php/index.php?mod=carnews&act=citynewslist&city=321&serial=NaN&type=2&sort=3&page=1&pagesize=20&callback=price_data',

                  # 重庆
                  'http://chongqing.auto.qq.com',
                  'http://cgi.data.auto.qq.com/php/index.php?mod=carnews&act=citynewslist&city=55&serial=NaN&type=2&sort=3&page=1&pagesize=20&callback=price_data',

                  # 广州
                  'http://guangzhou.auto.qq.com',
                  'http://cgi.data.auto.qq.com/php/index.php?mod=carnews&act=citynewslist&city=68&serial=NaN&type=2&sort=3&page=1&pagesize=20&callback=price_data',

                  # 深圳
                  'http://shenzhen.auto.qq.com',
                  'http://cgi.data.auto.qq.com/php/index.php?mod=carnews&act=citynewslist&city=78&serial=NaN&type=2&sort=3&page=1&pagesize=20&callback=price_data',

                  # 武汉
                  'http://wuhan.auto.qq.com',
                  'http://cgi.data.auto.qq.com/php/index.php?mod=carnews&act=citynewslist&city=173&serial=NaN&type=2&sort=3&page=1&pagesize=20&callback=price_data',

                  # 成都
                  'http://chengdu.auto.qq.com',
                  'http://cgi.data.auto.qq.com/php/index.php?mod=carnews&act=citynewslist&city=302&serial=NaN&type=2&sort=3&page=1&pagesize=20&callback=price_data',
                  ]

    USER_AGENTS = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/603.2.4 (KHTML, like Gecko) Version/10.1.1 Safari/603.2.4",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0",
        "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:54.0) Gecko/20100101 Firefox/54.0",
        "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:54.0) Gecko/20100101 Firefox/54.0",
        "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:54.0) Gecko/20100101 Firefox/54.0",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.109 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/603.2.5 (KHTML, like Gecko) Version/10.1.1 Safari/603.2.5",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.104 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36 Edge/15.15063",
        "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.3; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0",
        "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36",
        "Mozilla/5.0 (iPad; CPU OS 10_3_2 like Mac OS X) AppleWebKit/603.2.4 (KHTML, like Gecko) Version/10.0 Mobile/14F89 Safari/602.1",
        "Mozilla/5.0 (Windows NT 6.1; rv:54.0) Gecko/20100101 Firefox/54.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:53.0) Gecko/20100101 Firefox/53.0",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:53.0) Gecko/20100101 Firefox/53.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:54.0) Gecko/20100101 Firefox/54.0",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.109 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.109 Safari/537.36",
        "Mozilla/5.0 (X11; Linux x86_64; rv:54.0) Gecko/20100101 Firefox/54.0",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.104 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36",
        "Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0",
        "Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.1 Safari/603.1.30",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:54.0) Gecko/20100101 Firefox/54.0",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.86 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
        "Mozilla/5.0 (Windows NT 5.1; rv:52.0) Gecko/20100101 Firefox/52.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.109 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.86 Safari/537.36",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/58.0.3029.110 Chrome/58.0.3029.110 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/603.2.5 (KHTML, like Gecko) Version/10.1.1 Safari/603.2.5",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.104 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.104 Safari/537.36",
        "Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36",
        "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:53.0) Gecko/20100101 Firefox/53.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.86 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.86 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.86 Safari/537.36 OPR/46.0.2597.32",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/59.0.3071.109 Chrome/59.0.3071.109 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:53.0) Gecko/20100101 Firefox/53.0",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 OPR/45.0.2552.898",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36 OPR/46.0.2597.39",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:54.0) Gecko/20100101 Firefox/54.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/601.7.7 (KHTML, like Gecko) Version/9.1.2 Safari/601.7.7",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/602.4.8 (KHTML, like Gecko) Version/10.0.3 Safari/602.4.8",
        "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; Touch; rv:11.0) like Gecko",
        "Mozilla/5.0 (Windows NT 6.1; rv:52.0) Gecko/20100101 Firefox/52.0",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36"
        ]
    def parse(self, response):
        time.sleep(random.uniform(1,4))
        try:
            if 'http://auto.qq.com/articleList/rolls/' in response.url:
                header = {
                    'Accept': '*/*',
                    'Accept-Encoding': 'gzip, deflate, br',
                    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
                    'Connection': 'Keep-Alive',
                    'Host':'roll.news.qq.com',
                    'Referer': response.url,
                    'User-Agent': random.choice(self.USER_AGENTS)
                }
                #抓取一个月至今数据
                for i in range(2):
                    DayAgo = (datetime.datetime.now() - datetime.timedelta(days=i))
                    #年-月-日 格式
                    yyyy_mm_dd = DayAgo.strftime('%Y-%m-%d')
                    #抓取每天的前10页
                    for i in range(1, 11):
                        url = 'http://roll.news.qq.com/interface/cpcroll.php?callback=rollback&site=auto&mode=1&cata=&date={}&page={}&_={}'.format(
                            str(yyyy_mm_dd), str(i), str(int(time.time() * 1000)))
                        yield scrapy.Request(url,callback=self.parse_url,headers=header,dont_filter=True)

            if 'hangzhou' in response.url:
                for box in response.xpath('//p/a'):
                    item = RedisItem()
                    item['url'] = 'http://hangzhou.auto.qq.com' + box.xpath('.//@href').extract()[0]
                    yield item
            for city in ('beijing', 'shanghai', 'chongqing', 'guangzhou', 'shenzhen', 'wuhan', 'chengdu'):
                if city in response.url:
                    for box in response.xpath('//div[@class="newTxt"]/h3'):
                        item = RedisItem()
                        item['url'] = str(response.url) + str(box.xpath('.//a/@href').extract()[0])
                        yield item
            #杭州行情页
            if 'city=395' in response.url:
                urls = re.compile('"FUrl":"(.*?)","').findall(str(response.text).replace('\\',''))
                for url in urls:
                    item = RedisItem()
                    item['url'] = url
                    yield item
                #抓取每个地区前10页
                for i in range(2,11):
                    next_url = 'http://cgi.data.auto.qq.com/php/index.php?mod=carnews&act=citynewslist&city=395&serial=NaN&type=2&sort=3&page={}&pagesize=20&callback=price_data'.format(str(i))
                    yield scrapy.Request(next_url,callback=self.parse)

            # 北京行情页
            if 'city=54' in response.url:
                urls = re.compile('"FUrl":"(.*?)","').findall(str(response.text).replace('\\',''))
                for url in urls:
                    item = RedisItem()
                    item['url'] = url
                    yield item
                    # 抓取每个地区前10页
                for i in range(2, 11):
                    next_url = 'http://cgi.data.auto.qq.com/php/index.php?mod=carnews&act=citynewslist&city=54&serial=NaN&type=2&sort=3&page={}&pagesize=20&callback=price_data'.format(str(i))
                    yield scrapy.Request(next_url,callback=self.parse)

            # 上海行情页
            if 'city=321' in response.url:
                urls = re.compile('"FUrl":"(.*?)","').findall(str(response.text).replace('\\', ''))
                for url in urls:
                    item = RedisItem()
                    item['url'] = url
                    yield item
                    # 抓取每个地区前10页
                for i in range(2, 11):
                    next_url = 'http://cgi.data.auto.qq.com/php/index.php?mod=carnews&act=citynewslist&city=321&serial=NaN&type=2&sort=3&page={}&pagesize=20&callback=price_data'.format(
                        str(i))
                    yield scrapy.Request(next_url, callback=self.parse)

            # 重庆行情页
            if 'city=55' in response.url:
                urls = re.compile('"FUrl":"(.*?)","').findall(str(response.text).replace('\\', ''))
                for url in urls:
                    item = RedisItem()
                    item['url'] = url
                    yield item
                    # 抓取每个地区前10页
                for i in range(2, 11):
                    next_url = 'http://cgi.data.auto.qq.com/php/index.php?mod=carnews&act=citynewslist&city=55&serial=NaN&type=2&sort=3&page={}&pagesize=20&callback=price_data'.format(
                        str(i))
                    yield scrapy.Request(next_url, callback=self.parse)

            # 广州行情页
            if 'city=68' in response.url:
                urls = re.compile('"FUrl":"(.*?)","').findall(str(response.text).replace('\\', ''))
                for url in urls:
                    item = RedisItem()
                    item['url'] = url
                    yield item
                    # 抓取每个地区前10页
                for i in range(2, 11):
                    next_url = 'http://cgi.data.auto.qq.com/php/index.php?mod=carnews&act=citynewslist&city=68&serial=NaN&type=2&sort=3&page={}&pagesize=20&callback=price_data'.format(
                        str(i))
                    yield scrapy.Request(next_url, callback=self.parse)

            # 深圳行情页
            if 'city=78' in response.url:
                urls = re.compile('"FUrl":"(.*?)","').findall(str(response.text).replace('\\', ''))
                for url in urls:
                    item = RedisItem()
                    item['url'] = url
                    yield item
                    # 抓取每个地区前10页
                for i in range(2, 11):
                    next_url = 'http://cgi.data.auto.qq.com/php/index.php?mod=carnews&act=citynewslist&city=78&serial=NaN&type=2&sort=3&page={}&pagesize=20&callback=price_data'.format(
                        str(i))
                    yield scrapy.Request(next_url, callback=self.parse)

            # 武汉行情页
            if 'city=173' in response.url:
                urls = re.compile('"FUrl":"(.*?)","').findall(str(response.text).replace('\\', ''))
                for url in urls:
                    item = RedisItem()
                    item['url'] = url
                    yield item
                    # 抓取每个地区前10页
                for i in range(2, 11):
                    next_url = 'http://cgi.data.auto.qq.com/php/index.php?mod=carnews&act=citynewslist&city=173&serial=NaN&type=2&sort=3&page={}&pagesize=20&callback=price_data'.format(
                        str(i))
                    yield scrapy.Request(next_url, callback=self.parse)

            # 成都行情页
            if 'city=302' in response.url:
                urls = re.compile('"FUrl":"(.*?)","').findall(str(response.text).replace('\\', ''))
                for url in urls:
                    item = RedisItem()
                    item['url'] = url
                    yield item
                    # 抓取每个地区前10页
                for i in range(2, 11):
                    next_url = 'http://cgi.data.auto.qq.com/php/index.php?mod=carnews&act=citynewslist&city=302&serial=NaN&type=2&sort=3&page={}&pagesize=20&callback=price_data'.format(
                        str(i))
                    yield scrapy.Request(next_url, callback=self.parse)
        except:
            pass



    def parse_url(self,response):
        urls = re.compile('"url":"(.*?)","').findall(str(response.text).replace('\\',''))
        for url in urls:
            item = RedisItem()
            item['url'] = url
            if url:
                yield item







