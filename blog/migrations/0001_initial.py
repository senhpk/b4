# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('datetime', models.DateField(verbose_name='\u0414\u0430\u0442\u0430 \u043f\u0443\u0431\u043b\u0438\u043a\u0430\u0446\u0438\u0438')),
                ('short_content', models.TextField(max_length=500)),
                ('content', tinymce.models.HTMLField()),
                ('image', models.ImageField(null=True, upload_to=b'upload_images', blank=True)),
                ('category', models.ManyToManyField(related_name='post_set', to='blog.Category')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
