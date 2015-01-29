# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_auto_20150118_0221'),
    ]

    operations = [
        migrations.CreateModel(
            name='TabImg',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255, null=True, blank=True)),
                ('img', models.ImageField(upload_to=b'upload_images')),
                ('product', models.ForeignKey(related_name='tab_img_set', to='catalog.Product')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TabText',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255, null=True, blank=True)),
                ('description', tinymce.models.HTMLField(null=True, blank=True)),
                ('product', models.ForeignKey(related_name='tab_text_set', to='catalog.Product')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='tab',
            name='product',
        ),
        migrations.DeleteModel(
            name='Tab',
        ),
    ]
