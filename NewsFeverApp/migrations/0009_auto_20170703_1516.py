# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-03 15:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NewsFeverApp', '0008_auto_20170703_0808'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='a_id',
            field=models.CharField(max_length=10, primary_key=True, serialize=False),
        ),
    ]
