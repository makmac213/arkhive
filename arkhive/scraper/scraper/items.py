# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

from scrapy.contrib.djangoitem import DjangoItem

# arkhive
from news.models import News


class NewsItem(DjangoItem):
    django_model = News

