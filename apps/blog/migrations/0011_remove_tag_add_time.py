# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-05-17 22:44
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_tag'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='add_time',
        ),
    ]
