# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-06-22 11:44
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0030_auto_20170615_2045'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listing',
            name='floor_plan',
        ),
    ]
