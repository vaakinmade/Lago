# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-04-20 12:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0008_auto_20170420_1307'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='valuation',
            name='value',
        ),
        migrations.AddField(
            model_name='valuation',
            name='listing_value',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='valuation',
            name='rental_income',
            field=models.IntegerField(default=0),
        ),
    ]
