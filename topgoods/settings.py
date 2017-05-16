# -*- coding: utf-8 -*-

# Scrapy settings for topgoods project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'topgoods'

SPIDER_MODULES = ['topgoods.spiders']
NEWSPIDER_MODULE = 'topgoods.spiders'

DBKWARGS = {"host":"localhost",
            "port":3306,
            "user":"root",
            "password":"123456",
            "database":"test",}

DOWNLOADER_MIDDLEWARES = {
        'scrapy.contrib.downloadermiddleware.httpproxy.HttpProxyMiddleware':301,
    }

ITEM_PIPELINES = {'topgoods.pipelines.TopgoodsPipeline':300,
                 'scrapy.pipelines.images.ImagesPipeline':1}

# ITEM_PIPELINES = {'scrapy.pipelines.images.ImagesPipeline': 1,
#                   'topgoods.pipelines.TopgoodsPipeline':300}

IMAGES_URLS_FIELD = 'file_urls'
IMAGES_STORE = r'.'
# IMAGES_THUMBS = {
    # 'small': (50, 50),
    # 'big': (270, 270),
# }

LOG_FILE = "scrapy.log"
