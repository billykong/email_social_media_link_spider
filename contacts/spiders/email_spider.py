# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from bs4 import BeautifulSoup
from contacts.items import EmailItem, SocialMediaLinkItem
import re
from urllib import parse
import logging

class EmailSpider(CrawlSpider):
  def __init__(self, start_url=None, *args, **kwargs):
    super(EmailSpider, self).__init__(*args, **kwargs)
    self.start_urls = ['%s' % start_url]
    start_domain=start_url.replace("https://","").replace("http://","").replace("www.","").split('/')[0]
    self.allowed_domains = [start_domain]

  name="email_spider"
  rules = [
    scrapy.spiders.Rule(LinkExtractor(allow=()), callback="parse_page", follow=True)
  ]

  def parse_page(self, response):
    soup = BeautifulSoup(response.text, 'lxml')
    mailtos = [a["href"] for a in soup.select('a[href^=mailto:]')]
    items = []
    for mailto in mailtos:
      item = EmailItem()
      item["url"] = response.url
      item["mailto"] = mailto
      item["email"] = re.search('mailto:(.*)', mailto).group(1).split('?')[0]
      if re.search('subject=(.*)', mailto) is not None:
        item["subject"] = parse.unquote(re.search('subject=(.*)', mailto).group(1))
        logging.info('................Pasred Item................')
        logging.info('Page: ' + response.url)
        logging.info(item)
      items.append(item)

    socialMediaList = self.settings.get('SOCIAL_MEDIA_LIST')
    sociaLinks = [a["href"] for a in soup.select('a[href]')]
    for link in sociaLinks:
      parsed_uri = parse.urlparse(link)
      domain = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri)
      for keyword in socialMediaList:
        if keyword in domain:
          socialItem = SocialMediaLinkItem()
          socialItem["desc"] = keyword
          socialItem["media_url"] = link
          socialItem["site_url"] = response.url
          items.append(socialItem)
          break
    return items






