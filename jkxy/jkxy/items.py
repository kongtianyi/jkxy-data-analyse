# -*- coding: utf-8 -*-

from scrapy import Item
from scrapy import Field


class JkxyItem(Item):
    course_name = Field()  # 课程名
    course_url = Field()  # 课程链接
    course_page_url = Field()  # 课程位置页数url
    course_info = Field()  # 课程简介
    level = Field()  # 等级
    course_num = Field()  # 课时数
    course_time = Field()  # 总时长
    students = Field()  # 已学人数
    permission = Field()  # 观看权限
    category = Field()  # 类别
    push_time = Field()  # 发表时间
    teacher = Field()  # 布道师名
    teacher_url = Field()  # 布道师主页，以备后用
    teacher_title = Field()  # 布道师头衔
    course_back = Field()  # 课程背景
    core = Field()  # 核心内容
    software = Field()  # 软件环境
    provide_data = Field()  # 是否提供资料
    suit_people = Field()  # 适合人群
    tags = Field()  # 标签
    # sub_course_info = Field()  # 子课程信息
    get_time = Field()  # 获取时间
