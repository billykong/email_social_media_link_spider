# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
from scrapy.http import HtmlResponse
from scrapy.exceptions import IgnoreRequest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class PhantomJSMiddleware(object):
    def process_request(self, request, spider):
        PROXY = 'localhost:9150'
        # service_args = [ '--proxy=localhost:9150', '--proxy-type=socks5', ]
        # driver_path = '/Users/billykong/workspace/github/scrapper/webdriver/phantomjs-2.1.1-macosx/bin/phantomjs'
        # driver = webdriver.PhantomJS(executable_path=driver_path, service_args=service_args)
        driver_path = 'webdrivers/chromedriver'
        # driver = webdriver.Chrome(executable_path=driver_path, service_args=service_args)
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--proxy-server=socks5://%s' % PROXY)
        driver = webdriver.Chrome(executable_path=driver_path, chrome_options=chrome_options)


        driver.get(request.url)
        time.sleep(2)
        body = driver.page_source
        return HtmlResponse(driver.current_url, body=body, encoding='utf-8', request=request)

class MusiciansSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
