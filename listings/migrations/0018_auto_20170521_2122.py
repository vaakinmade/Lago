# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-05-21 20:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0017_statement'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='statement',
            name='investor',
        ),
        migrations.DeleteModel(
            name='Statement',
        ),
    ]
