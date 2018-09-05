# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20180904_2145'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='en_title',
            field=models.CharField(default=datetime.datetime(2018, 9, 5, 5, 0, 48, 325606, tzinfo=utc), max_length=140, verbose_name=b'\xe8\x8b\xb1\xe6\x96\x87\xe6\xa0\x87\xe9\xa2\x98'),
            preserve_default=False,
        ),
    ]
