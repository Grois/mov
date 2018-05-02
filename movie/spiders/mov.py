# -*- coding: utf-8 -*-
import scrapy
from movie.items import *


class MovSpider(scrapy.Spider):
    name = 'mov'
    allowed_domains = ['douban.com']
    base_url = 'https://movie.douban.com/subject/26683723/comments?start=0&limit='
    offset = 0
    start_urls = ['https://movie.douban.com/subject/26683723/comments?limit=20&start=0']

    def parse(self, response):
        if self.offset == 0:
            pass
        comment_list = response.xpath("//div[@class='comment-item']")
        # print(len(comment_list))
        for comment in comment_list:
            item = MovieItem()

            name = comment.xpath(".//span[@class='comment-info']/a/text()").extract_first()
            time = comment.xpath(".//span[@class='comment-info']/span[3]/@title").extract_first()
            num = comment.xpath(".//span[@class='votes']/text()").extract_first()
            content = comment.xpath(".//p/text()").extract_first()
            score = comment.xpath(".//span[@class='comment-info']/span[2]/@title").extract_first()

            item['name'] = name
            item['time'] = time
            item['num'] = num
            item['content'] = content
            item['score'] = score

            yield item
            if self.offset < 45000:
                self.offset += 20
                url = self.base_url + str(self.offset)
                yield scrapy.Request(url, callback=self.parse)
        pass
