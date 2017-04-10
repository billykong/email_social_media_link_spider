# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from bs4 import BeautifulSoup
from musicians.items import MusiciansItem, SocialMediaLinkItem
import re
from urllib import parse

class EmailSpider(CrawlSpider):
  def __init__(self, start_url=None, *args, **kwargs):
    super(EmailSpider, self).__init__(*args, **kwargs)
    self.start_urls = ['%s' % start_url]
    domain_url=start_url.replace("https://","").replace("http://","").replace("www.","").split('/')[0]
    self.allowed_domains = [domain_url]

  name="email_spider"
  rules = [
    scrapy.spiders.Rule(LinkExtractor(allow=()), callback="parse_page", follow=True)
  ]

  def parse_page(self, response):
    print("SCRAPING: " + response.url)
    self.parse_email(response)
    self.parse_social_media_links(response)

  def parse_email(self, response):
    soup = BeautifulSoup(response.text, 'lxml')
    mailtos = [a["href"] for a in soup.select('a[href^=mailto:]')]
    print(mailtos)
    items = []
    for mailto in mailtos:
      item = MusiciansItem()
      item["url"] = response.url
      item["mailto"] = mailto
      item["email"] = re.search('mailto:(.*)', mailto).group(1).split('?')[0]
      if re.search('subject=(.*)', mailto) is not None:
        item["subject"] = parse.unquote(re.search('subject=(.*)', mailto).group(1))
      items.append(item)
    return items

  def parse_social_media_links(self, response):
    # twitter
    # facebook
    # linkedin
    # ............
    # github
    # google+
    # myspace
    # reddit
    # tumblr
    soup = BeautifulSoup(response.text, 'lxml')
    links = [a["href"] for a in soup.select('a[href]')]
    items = []
    for link in links:
      item = SocialMediaLinkItem()
      if "twitter" in link:
        item["desc"] = "twitter"
        item["url"] = link
        items.append(item)
        print(link)
      elif "facebook" in link:
        item["desc"] = "facebook"
        item["url"] = link
        items.append(item)
        print(link)
      elif "linkedin" in link:
        item["desc"] = "linkedin"
        item["url"] = link
        items.append(item)
        print(link)
    print(items)
    return items







