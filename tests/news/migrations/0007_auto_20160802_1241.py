# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-02 09:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0006_auto_20160802_0232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='source',
            field=models.CharField(choices=[('habrahabr.ru', 'habrahabr.ru'), ('maduza.io', 'maduza.io'), ('lenta.ru', 'lenta.ru')], default='habrahabr.ru', max_length=50),
        ),
    ]
