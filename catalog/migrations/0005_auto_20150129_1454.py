# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_auto_20150118_0258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='img',
            field=models.ImageField(upload_to=b'upload_images'),
            preserve_default=True,
        ),
    ]
