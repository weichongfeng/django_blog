# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-12-17 06:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20191213_1703'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='content',
            new_name='content_html',
        ),
    ]
