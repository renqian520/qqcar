# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


import redis
import pymongo
from scrapy.exceptions import DropItem
import qqcar.settings as settings
from qqcar.items import MongodbItem


class RedisPipeline(object):
    def __init__(self):
        self.redis_db = redis.Redis(host=settings.REDIS_HOST,port=settings.REDIS_PORT,db=settings.REDIS_DB)
        self.redis_dc = settings.MY_REDIS

    def process_item(self, item, spider):
        if self.redis_db.exists(item['url']):
            raise DropItem('%s is exists!' %(item['url']))
        else:
            self.redis_db.lpush(self.redis_dc,item['url'])
        return item


class MongodbPipeline(object):
    def __init__(self):
        self.conn = pymongo.MongoClient('mongodb://{}:{}'.format(settings.MONGODB_HOST, settings.MONGODB_PORT))
        self.db = self.conn[settings.MONGODB_DB]
        self.dc_qq = self.db[settings.MONGODB_DC_qq]
    def process_item(self, item, spider):
        if isinstance(item, MongodbItem):
            if self.site_item_exist(item):
                self.dc_qq.insert(dict(item))
            else:
                raise DropItem('%s,%s is exist!' % (item['content'],item['data_id']))
            return item


    def site_item_exist(self,item):
        if self.dc_qq.find_one({'content':item['content'],'data_id':item['data_id']}):
            return False
        else:
            return True