# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-06-19 21:02
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('investors', '0004_auto_20170619_1333'),
    ]

    operations = [
        migrations.AddField(
            model_name='banktransfer',
            name='investor',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
