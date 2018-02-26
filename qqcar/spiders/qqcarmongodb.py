# -*- coding: utf-8 -*-
from scrapy_redis.spiders import RedisSpider
from qqcar.items import MongodbItem
import re


class Myspider(RedisSpider):
    name = 'mongodburl'
    custom_settings = {
        'ITEM_PIPELINES':{
            'qqcar.pipelines.MongodbPipeline':300,
        }
    }
    redis_key = 'qq_spider:start_urls'

    #新闻
    def parse(self,response):
        item = MongodbItem()
        item['url'] = response.url
        item['content'] = self.get_content(response)
        item['title'] = self.get_title(response)
        item['pubtime'] = self.get_pubtime(response)
        item['author'] = self.get_author(response)
        item['view'] = '0'
        item['reply'] = '0'
        yield item


    # 新闻函数
    def get_title(self,response):
        try:
            title = re.compile('<h1>(.*?)</h1>', re.S).findall(response.text)
            for i in title:
                if len(i):
                    title = str(re.sub('<.*?>|\\n|&nbsp;|\xa0|\r|\u3000', '', str(i))).strip().replace(' ', '')
                    title = str(re.sub('<.*?>|\\n|&nbsp;|\xa0|\r|\u3000', '', str(title))).strip().replace(' ', '')
                else:
                    title = 'NULL'
                return title
            if len(title) == 0:
                return 'NULL'
        except:
            pass
    def get_pubtime(self,response):
        try:
            pubtime = response.xpath('//span[@class="a_time"]/text()').extract()
            if pubtime:
                pubtime = str(pubtime[0]).strip()
            else:
                pubtime = 'NULL'
            return pubtime
        except:
            pass
    def get_author(self,response):
        try:
            author = response.xpath('//div[@class="qq_editor"]/text()').extract()
            if author:
                author = str(author[0]).strip().replace('责任编辑：','')
            else:
                author = 'NULL'
            return author
        except:
            pass
    def get_content(self,response):
        try:
            li = []
            contents = re.compile('<P style="TEXT-INDENT: 2em">(.*?)</P>',re.S).findall(response.text)
            for i in contents:
                if len(i):
                    content = str(re.sub('<.*?>|\\n|{1，7}|&nbsp;|\xa0|\r|\u3000', '', str(i))).strip().replace(' ', '')
                    content = str(re.sub('<.*?>|\\n|{1，7}|&nbsp;|\xa0|\r|\u3000', '', str(content))).strip().replace(' ', '')
                    li.append(content)
            content = ''.join(li)
            if len(contents)==0:
                return 'NULL'
            return content
        except:
            pass


