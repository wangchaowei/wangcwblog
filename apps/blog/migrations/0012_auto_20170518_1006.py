# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-05-18 10:06
from __future__ import unicode_literals

import DjangoUeditor.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_remove_tag_add_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='text',
            field=DjangoUeditor.models.UEditorField(default='', verbose_name='\u6587\u7ae0\u5185\u5bb9'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='text',
            field=DjangoUeditor.models.UEditorField(default='', verbose_name='\u8bc4\u8bba\u5185\u5bb9'),
        ),
    ]
