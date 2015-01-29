# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('content', tinymce.models.HTMLField()),
                ('img', models.ImageField(null=True, upload_to=b'upload_images', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
