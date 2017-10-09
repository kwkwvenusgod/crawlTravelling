# -*- coding: utf-8 -*-
import scrapy
from selenium import webdriver


class CrawlmafengwoSpider(scrapy.Spider):

    name = 'crawlmafengwo'
    # allowed_domains = ['https://www.mafengwo.cn/sales/0-0-0-0-0-0-0-0.html?group=4']
    start_urls = ['http://https://www.mafengwo.cn/sales/0-0-0-0-0-0-0-0.html?group=4/']

    def __init__(self):
        self.driver = webdriver.Firefox()
        self.download_delay = 0.25
        self.driver.implicitly_wait(60)

    def parse(self, response):
        days_filter = response.xpath('//div[@class="filter-bd"]/dl[2]/dd/ul/li').extract()


        pass
