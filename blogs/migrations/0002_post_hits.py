# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-05-23 13:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='hits',
            field=models.IntegerField(default=0),
        ),
    ]
