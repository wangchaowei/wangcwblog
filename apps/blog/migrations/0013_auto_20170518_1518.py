# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-05-18 15:18
from __future__ import unicode_literals

import DjangoUeditor.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_auto_20170518_1006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='digest',
            field=DjangoUeditor.models.UEditorField(default='', verbose_name='\u6458\u8981'),
        ),
    ]
