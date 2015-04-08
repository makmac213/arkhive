# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('link', models.URLField()),
                ('content', models.TextField()),
                ('created', models.DateTimeField(null=True, blank=True)),
                ('tags', models.CharField(max_length=255, null=True, blank=True)),
                ('scraped_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'news_news',
            },
            bases=(models.Model,),
        ),
    ]
