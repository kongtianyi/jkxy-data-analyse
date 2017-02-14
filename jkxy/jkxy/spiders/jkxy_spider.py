# -*- coding: utf-8 -*-
from scrapy import Request
from scrapy import Spider
from jkxy.items import JkxyItem  # pycharm在此处会因自身原因说找不到，那是因为jkxy包含在了jkxy_data_analyse文件中，无妨
import time
import re


class JkxySpiderSpider(Spider):
    name = "jkxy_spider"
    allowed_domains = ["www.jikexueyuan.com"]
    start_urls = ['http://www.jikexueyuan.com/course/']

    def start_requests(self):
        for i in range(1, 96):
            yield Request(url=self.start_urls[0]+"?pageNum="+str(i), callback=self.parse)

    def parse(self, response):
        '''
        在课程列表页提取各个课程的有效信息
        '''
        courses = response.xpath('//ul[@class="cf"]/li')
        for course in courses:
            item = JkxyItem()
            infor = course.xpath('div[@class="lesson-infor"]')
            item["course_name"] = infor.xpath('h2/a/text()').extract()[0].replace('\t', '').replace('\n', '')
            item["course_url"] = infor.xpath('h2/a/@href').extract()[0].replace('\t', '').replace('\n', '')
            item["course_page_url"] = response.url
            item["course_info"] = infor.xpath('p/text()').extract()[0].replace('\t', '').replace('\n', '')
            item["level"] = infor.xpath('div/div[1]/dl/dd[2]/em/text()').extract()[0].replace('\t', '').replace('\n', '')
            num_time = infor.xpath('div/div[1]/dl/dd/em').re('[0-9]+')
            item["course_num"] = num_time[0]
            item["course_time"] = num_time[1]
            item["students"] = infor.xpath('div/div[1]/em').re('[0-9]+')[0]
            try:
                item["permission"] = course.xpath('div[@class="lessonimg-box"]/i[1]/@class').extract()[0].replace('\t', '').replace('\n', '')
            except:
                item["permission"] = "public"
            categorys = infor.xpath('div/div[2]/div/a')
            category = ""
            for cell in categorys:
                category = category + cell.xpath('img/@title').extract()[0] + "/"
            item["category"] = category[:-1].replace('\t', '').replace('\n', '')
            yield Request(url=item["course_url"], callback=self.course_page, meta={"item": item})

    def course_page(self, response):
        '''
        提取课程页内的有效信息
        '''
        item = response.meta["item"]
        lesson_teacher = response.xpath('//div[@class="lesson-teacher"]')
        bc_box = lesson_teacher.xpath('div[@class="bc-box"]')
        less_tag_spans = lesson_teacher.xpath('div[@class="less-tag"]/span')
        item["push_time"] = bc_box.xpath('div[@class="timebox"]/span[2]/text()').extract()[0].replace('\t', '').replace('\n', '')
        item["teacher"] = bc_box.xpath('div[@class="teacher-infor cf"]/div[@class="infor-text"]/strong/a/text()').extract()[0].replace('\t', '').replace('\n', '')
        item["teacher_url"] = bc_box.xpath('div[@class="teacher-infor cf"]/div[@class="infor-text"]/strong/a/@href').extract()[0].replace('\t', '').replace('\n', '')
        try:
            item["teacher_title"] = bc_box.xpath('div[@class="teacher-infor cf"]/div[@class="infor-text"]/p/text()').extract()[0].replace('\t', '').replace('\n', '')
        except:
            item["teacher_title"] = None
        infor_content = bc_box.xpath('div[@class="infor-content"]').extract()[0].replace('\t', '').replace('\n', '')
        infors = infor_content.replace('课程背景：', '课程背景^').replace('核心内容：', '核心内容^').replace('软件环境：',
                                        '软件环境^').replace('开发环境：','开发环境^').replace('是否提供资料：',
                                        '是否提供资料^').replace('是否提供源码：', '是否提供源码^').replace('课程等级：',
                                        '课程等级^').replace('适合人群：','适合人群^').replace('适应群体：',
                                        '适应群体^').replace('适应人群：','适应人群^')
        infors = re.sub('<.*?>', '', infors).split('^')
        # 这个地方因为网页结构不规范，只能有所取舍
        try:
            item["course_back"] = infors[1][:-4].replace('\t', '').replace('\n', '')
        except:
            item["course_back"] = None
        try:
            item["core"] = infors[2][:-4].replace('\t', '').replace('\n', '')
        except:
            item["core"] = None
        try:
            item["software"] = infors[3][:-6].replace('\t', '').replace('\n', '')
        except:
            item["software"] = None
        try:
            item["provide_data"] = infors[4][:-4].replace('\t', '').replace('\n', '')
        except:
            item["provide_data"] = None
        try:
            if infor_content.find('课程等级') == -1:
                item["suit_people"] = infors[5][:-4].replace('\t', '').replace('\n', '')
            else:
                item["suit_people"] = infors[6][:-4].replace('\t', '').replace('\n', '')
        except:
            item["suit_people"] = None
        tags = ""
        for span in less_tag_spans:
            tags = tags + span.xpath('a/text()').extract()[0] + '/'
        item['tags'] = tags[:-1].replace('\t', '').replace('\n', '')
        item['get_time'] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        yield item






