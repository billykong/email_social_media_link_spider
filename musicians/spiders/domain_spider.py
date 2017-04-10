# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class DomainSpider(CrawlSpider):
    #log.start(logfile='log.txt', loglevel=log.CRITICAL)
  name="single_domain"
  allowed_domains = ["cdbaby.com"]
  start_urls = ["https://www.cdbaby.com/"]
  rules = [
    scrapy.spiders.Rule(LinkExtractor(allow=()), callback="parse_page", follow=True)
  ]

  def parse_page(self, response):
    print(response.url)
    # for url in response.xpath('//a/@href').extract():
    #   yield scrapy.Request(url, callback=self.parse)
