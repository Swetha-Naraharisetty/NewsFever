# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-02 16:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NewsFeverApp', '0002_auto_20170702_1309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
