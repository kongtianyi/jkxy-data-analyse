## 简介：

* 对极客学院官网进行数据收集
* 对数据进行简单分析

## 依赖库

* scrapy 1.3.0
* pymongo
* numpy
* pandas
* matplotlib

## 文件介绍

* `jkxy`文件夹下是Scrapy工程，将数据存入本地MongoDB
* `jkxy.csv`是2017年2月4日收集的数据，从MongoDB中导出，导出方式是使用mongoexport工具，命令如下：
  ```
  D:\ProgrammingSoftware\MongoDB\Server\3.4\bin>mongoexport.exe --type=csv -f _id,tags,software,course_num,course_name,course_back,students,teacher,course_url,course_time,get_time,course_info,permission,teacher_url,push_time,category,provide_data,course_page_url,core,teacher_title,suit_people,level -d spider -c jkxy -o ./jkxy.csv
  ```
  为了在excel中不乱码，我把编码方式用notepad++改成了gbk。
* `freshmongo.py`中是一些对MongoDB内数据进行数据清洗的逻辑
* `coursetime_students_analyse.py`是课程时长与学员数的关系的分析脚本
* `coursetimeavg_students_analyse.py`是课程小节平均时长与学员数的分析脚本

## 数据说明

爬虫收集了以下数据：
* course_name          => 课程名
* course_url               => 课程链接
* course_page_url     => 课程位置页数url
* course_info             => 课程简介
* level                        => 等级
* course_num            => 课时数
* course_time            => 总时长
* students                  => 已学人数
* permission              => 观看权限(我提供的数据这个字段是无效的，但代码已经修正)
* category                 => 类别
* push_time               => 发表时间
* teacher                   => 布道师名
* teacher_url             => 布道师主页，以备后用
* teacher_title           => 布道师头衔
* course_back          =>  课程背景
* core                       => 核心内容
* software                => 软件环境
* provide_data         => 是否提供资料
* suit_people            => 适合人群
* tags                       => 标签
* sub_course_info => 子课程信息
* get_time                => 获取时间

## 声明

在数据收集过程中遵循robot协议 ，并设置了爬取延迟，每3秒对网站进行一次访问，尊重极客学院，尊重网站维护人员。
