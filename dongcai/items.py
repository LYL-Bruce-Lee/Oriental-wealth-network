# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TenxunItem(scrapy.Item):
    # define the fields for your item here like:
    pub_time = scrapy.Field()
    title = scrapy.Field()
    agency = scrapy.Field()
    link = scrapy.Field()
    # name = scrapy.Field()
    pass
