# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-06-22 11:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0031_remove_listing_floor_plan'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='floor_plan',
            field=models.ImageField(default='pic_folder/None/no-img.jpg', upload_to='images/lagopoly'),
        ),
    ]