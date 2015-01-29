# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tab',
            name='description',
            field=tinymce.models.HTMLField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tab',
            name='name',
            field=models.CharField(max_length=255, null=True, blank=True),
            preserve_default=True,
        ),
    ]
