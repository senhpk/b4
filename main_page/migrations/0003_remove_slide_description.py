# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0002_slide_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='slide',
            name='description',
        ),
    ]
