# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-05-17 00:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20170516_2002'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='digest',
            field=models.TextField(default='1', max_length=50, verbose_name='\u6458\u8981'),
        ),
    ]