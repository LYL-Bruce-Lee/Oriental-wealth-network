# -*- coding: utf-8 -*-
import scrapy
from Dongfang.items import DongfangItem
import re
import json
import base64


class HgyjSpider(scrapy.Spider):
    name = 'hgyj'
    allowed_domains = ['eastmoney.com']
    page = 1
    base_page = 'date=2&jgmc=&page=' 
    base_url = 'http://data.eastmoney.com/report/hgyj.html#'
    start_urls = ['http://data.eastmoney.com/report/hgyj.html#ZGF0ZT0yJmpnbWM9JnBhZ2U9MQ==']

    def parse(self, response):
        
        resp = response.text
        pattern = re.compile(r'clyb\.firstInit\((.*?)\);')
        content = pattern.findall(resp)
        # print(content)

        data_list = json.loads(content[0])['data']

        for data in data_list:
            item = DongfangItem()
            # '2017/10/15 10:38:33,APPHkyqBwHLfReport,80000180,渤海证券,2,流动性分析周报：定向降准有创新 中性偏紧未改变'
            detail = data.split(',')
            item['pub_time'] = detail[0].split(' ')[0]
            item['title'] = detail[-1]
            item['agency'] = detail[3]
            # http://data.eastmoney.com/report/20171015/hg,APPHkyqBx26KReport.html
            item['link'] = 'http://data.eastmoney.com/report/' + detail[0].split(' ')[0].replace('/', '') + '/hg,' + detail[1] + '.html'

            yield item

        # 爬取半年内的报告 在75页之内
        if self.page <= 75:
            self.page += 1
            next_page = base64.b64encode((self.base_page + str(self.page)).encode())
            next_url = self.base_url + next_page.decode()
            print(next_url)

            yield scrapy.Request(next_url, callback=self.parse, dont_filter=True)


