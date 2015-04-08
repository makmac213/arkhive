from django.conf import settings
from django.contrib.auth.models import User
#from django.contrib.sites.models import Site
from django.db import models

# django_mongodb_engine
from django_mongodb_engine.contrib import MongoDBManager

class News(models.Model):
    title = models.CharField(max_length=255)
    link = models.URLField()
    content = models.TextField()
    created = models.DateTimeField(null=True, blank=True)
    tags = models.CharField(max_length=255, null=True, blank=True)
    scraped_date = models.DateTimeField(auto_now_add=True)

    objects = MongoDBManager()

    class Meta:
        db_table = 'news_news'
        ordering = ['-created']

    def save(self, *args, **kwargs):
        super(News, self).save(using=settings.DB_NONREL)


class Category(models.Model):
    parent = models.ForeignKey('self', null=True, blank=True)
    name = models.CharField(max_length=255)

    class Meta:
        db_table = 'news_categories'

    def save(self, *args, **kwargs):
        super(Category, self).save(using=settings.DB_REL)


class Tag(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        db_table = 'news_tags'

    def save(self, *args, **kwargs):
        super(Tag, self).save(using=settings.DB_REL)


class SpinnedNews(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    content = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name='spinned_by')
    modified = models.DateTimeField(auto_now=True)
    last_modified_by = models.ForeignKey(User, 
                            related_name='latest_spinner')
    tags = models.ManyToManyField(Tag, null=True, blank=True)
    categories = models.ManyToManyField(Category, null=True, blank=True)

    #sites = models.ManyToManyField(Site, null=True, blank=True)

    class Meta:
        db_table = 'news_spinned_news'
        ordering = ['-created']

    def save(self, *args, **kwargs):
        super(SpinnedNews, self).save(using=settings.DB_REL)

