# -*- coding: utf-8 -*-
import scrapy


class MovSpider(scrapy.Spider):
    name = 'mov'
    allowed_domains = ['douban.com']
    offset = 0
    start_urls = ['https://movie.douban.com/subject/26683723/comments?limit=20&start=0']

    def parse(self, response):
        comment_list = response.xpath("//div[@class='comment-item']")
        # print(len(comment_list))
        for comment in comment_list:
            name = comment.xpath(".//span[@class='comment-info']/a/text()").extract_first()
            time = comment.xpath(".//span[@class='comment-time']").extract_first()
            num = comment.xpath(".//span[@class='votes']/text()").extract_first()
            content = comment.xpath(".//p/text()").extract_first()
            score = comment.xpath(".//span[@class='comment-info']/span[2]/@title").extract_first()

            print(time)
        pass
