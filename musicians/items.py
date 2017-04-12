# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class EmailItem(scrapy.Item):
    # define the fields for your item here like:
    email = scrapy.Field()
    url = scrapy.Field()
    mailto = scrapy.Field()
    subject = scrapy.Field()

class SocialMediaLinkItem(scrapy.Item):
    desc = scrapy.Field()
    url = scrapy.Field()
