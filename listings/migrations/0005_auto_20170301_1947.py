# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-03-01 19:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0004_auto_20170228_0838'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listing',
            old_name='city',
            new_name='town',
        ),
        migrations.AddField(
            model_name='listing',
            name='unit_block',
            field=models.CharField(default='', max_length=225),
        ),
    ]