# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-02 17:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NewsFeverApp', '0005_auto_20170702_1706'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='a_name',
            field=models.CharField(default='Unknown', max_length=50, null=True),
        ),
    ]
