# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-06-18 19:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_auto_20160610_1743'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsitem',
            name='slug',
            field=models.SlugField(blank=True, max_length=255),
        ),
    ]