# -*- coding: utf-8 -*-
import scrapy
import pdb

class DoisongphapluatSpider(scrapy.Spider):
    name = 'doisongphapluat'
    allowed_domains = ['doisongphapluat.com']
    start_urls = ['https://www.doisongphapluat.com/phong-toa-them-2-phuong-voi-hon-85000-dan-thuoc-thanh-pho-thu-duc-a507405.html']

    def parse(self, response):
        # pdb.set_trace()
        item = dict()
        item['title'] = response.xpath('//h1[@class=\"title mb-4 font-weight-bold\"]/text()').get()
        item['abstract'] = response.css('h2.sapo ::text').get()
        item['relative_url'] = response.xpath('//ul[@class=\"related-links box-most-visited\"]//a/@href').get()
           
        yield item 