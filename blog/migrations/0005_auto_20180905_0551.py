# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_article_en_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='ename',
            field=models.CharField(default=83, max_length=30, verbose_name=b'\xe8\x8b\xb1\xe6\x96\x87\xe5\x88\x86\xe7\xb1\xbb\xe5\x90\x8d\xe7\xa7\xb0'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=30, verbose_name=b'\xe4\xb8\xad\xe6\x96\x87\xe5\x88\x86\xe7\xb1\xbb\xe5\x90\x8d\xe7\xa7\xb0'),
        ),
    ]
