# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-05-24 23:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0005_auto_20170524_1519'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default='pic_folder/None/no-img.jpg', upload_to='images/lagopoly'),
        ),
    ]
