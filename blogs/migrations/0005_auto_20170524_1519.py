# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-05-24 14:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0004_auto_20170524_0041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default='pic_folder/None/no-img.jpg', upload_to='images/lagopoly/%Y%m%d'),
        ),
    ]
