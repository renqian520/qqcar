# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class RedisItem(scrapy.Item):
    url = scrapy.Field()

class MongodbItem(scrapy.Item):
    url = scrapy.Field()
    title = scrapy.Field()
    pubtime = scrapy.Field()
    author = scrapy.Field()
    content = scrapy.Field()
    view = scrapy.Field()
    reply = scrapy.Field()