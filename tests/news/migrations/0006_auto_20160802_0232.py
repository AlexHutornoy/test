# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-01 23:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_auto_20160802_0122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='source',
            field=models.CharField(choices=[('habrahabr', 'habrahabr.ru'), ('maduza', 'maduza.io'), ('lenta', 'lenta.ru')], default='habrahabr', max_length=50),
        ),
    ]