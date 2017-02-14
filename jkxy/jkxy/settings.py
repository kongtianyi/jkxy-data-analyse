# -*- coding: utf-8 -*-


BOT_NAME = 'jkxy'

SPIDER_MODULES = ['jkxy.spiders']
NEWSPIDER_MODULE = 'jkxy.spiders'

MONGO_HOST = "localhost"
MONGO_PORT = 27017
MONGO_DB = "spider"
MONGO_COLL = "jkxy0214"

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 3

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'jkxy.pipelines.JkxyPipeline': 300,
}

