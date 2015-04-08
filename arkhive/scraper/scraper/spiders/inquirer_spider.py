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

# django
from django.utils.html import strip_tags


class GmaSpider(CrawlSpider):
    """
    scrapy crawl inquirer_spider -o gmanews.json
    """

    name = 'inquirer_spider'
    allowed_domains = [
            'inquirer.net',
            'newsinfo.inquirer.net',
            'sports.inquirer.net',
            'lifestyle.inquirer.net',
            'entertainment.inquirer.net',
            'business.inquirer.net',
            'technology.inquirer.net',
            'globalnation.inquirer.net',
        ]
    start_urls = [
            'http://www.inquirer.net',
        ]
    rules = (
            Rule(SgmlLinkExtractor(allow=('',)),
            process_links="link_filter",
            callback="parse_items",
            follow=True),
        )

    def parse_items(self, response):
        title = response.xpath('//div[@class="al-headline"]/\
                                div[@class="container"]/h1').extract()
        if len(title):
            item = None            
            link = response.url
            
            title = strip_tags(title[0])

            # parse date
            created = response.xpath('//h4[@class="byline"]').extract()[0]
            created = created.split('>')[-2].strip()[:-4]
            ord_str = None
            if 'st,' in created:
                ord_str = 'st'
            elif 'nd,' in created:
                ord_str = 'nd'
            elif 'rd,' in created:
                ord_str = 'rd'
            elif 'th,' in created:
                ord_str = 'th'
            created_format = '%H:%M %p | %A, %B %d' + ord_str +', %Y'
            created = time.strptime(created, created_format)

            #content = response.xpath('/html/body/div[6]/div[8]/div/div[2]/div[2]').extract()
            content = response.xpath('//div[@class="main-article"]').extract()

            #tags = response.xpath('//div[@class="story"]\
            #            /div[@class="main"]/div[@class="tags"]\
            #            /a[@class="tag"]/text()').extract()

            item = NewsItem()
            item['link'] = link
            item['title'] = title
            item['created'] = strftime('%Y-%m-%d', created)
            item['content'] = content
            #item['tags'] = list(set(tags))
            item.save()

            return item

    def link_filter(self, links):
        ret = []
        for link in links:
            parsed_url = urlparse(link.url)
            if not News.objects.filter(link=parsed_url).count():
                ret.append(link)
        return ret


    def process_title(response):
        pass