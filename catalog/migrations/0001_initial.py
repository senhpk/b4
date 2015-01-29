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
                ('img', models.ImageField(null=True, upload_to=b'upload_images', blank=True)),
                ('parent', models.ForeignKey(related_name='category_set', blank=True, to='catalog.Category', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('img', models.ImageField(null=True, upload_to=b'upload_images', blank=True)),
                ('info', tinymce.models.HTMLField()),
                ('description', tinymce.models.HTMLField()),
                ('category', models.ForeignKey(related_name='product_set', to='catalog.Category')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('value', models.CharField(max_length=255)),
                ('product', models.ForeignKey(related_name='property_set', to='catalog.Product')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tab',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('img', models.ImageField(null=True, upload_to=b'upload_images', blank=True)),
                ('description', tinymce.models.HTMLField()),
                ('product', models.ForeignKey(related_name='tab_set', to='catalog.Product')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
