# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-06-19 21:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('investors', '0009_banktransfer_investor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='banktransfer',
            name='investor',
        ),
    ]
