# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-03 16:30
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('NewsFeverApp', '0012_auto_20170703_1621'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sourcecategorymap',
            old_name='s_category',
            new_name='category',
        ),
        migrations.RenameField(
            model_name='sourcecategorymap',
            old_name='s_source',
            new_name='source',
        ),
    ]