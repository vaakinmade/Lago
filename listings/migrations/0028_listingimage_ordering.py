# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-06-11 11:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0027_auto_20170610_1706'),
    ]

    operations = [
        migrations.AddField(
            model_name='listingimage',
            name='ordering',
            field=models.CharField(choices=[(6, 6)], default='', max_length=2),
        ),
    ]
