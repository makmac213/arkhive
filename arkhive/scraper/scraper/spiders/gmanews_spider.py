import time
from time import strftime
from urlparse import urlparse

# scrapy
import scrapy
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule

# scraper
from scraper.items import NewsItem

# arkhive
from news.models import News


class GmaSpider(CrawlSpider):
    """
    scrapy crawl gma_spider -o gmanews.json
    """

    name = 'gma_spider'
    allowed_domains = [
            'gmanetwork.com',
        ]
    start_urls = [
            'http://www.gmanetwork.com/news/',
        ]
    rules = (
            Rule(SgmlLinkExtractor(allow=('',)),
            process_links="link_filter",
            callback="parse_items",
            follow=True),
        )

    def parse_items(self, response):
        title = response.xpath('//div[@class="story"]/div[@class="title"]\
                                /h1/text()').extract()
        if len(title):
            item = None            
            link = response.url
            #if not News.objects.filter(link=link).count():
            title = title[0]
            created = response.xpath('//div[@class="story"]/div\
                        /span[@class="timestamp"]/text()').extract()[0]
            created = created[:-2]
            created = time.strptime(created, "%B %d, %Y %I:%M")
            content = response.xpath('//div[@class="story"]\
                        /div[@class="main"]/div[@class="text_body"]').extract()
            tags = response.xpath('//div[@class="story"]\
                        /div[@class="main"]/div[@class="tags"]\
                        /a[@class="tag"]/text()').extract()

            item = NewsItem()
            item['link'] = link
            item['title'] = title
            item['created'] = strftime('%Y-%m-%d', created)
            item['content'] = content
            item['tags'] = list(set(tags))
            item.save()

            return item

    def link_filter(self, links):
        ret = []
        for link in links:
            parsed_url = urlparse(link.url)
            if not News.objects.filter(link=parsed_url).count():
                ret.append(link)
        return ret