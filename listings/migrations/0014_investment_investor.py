# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-05-03 20:46
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('listings', '0013_auto_20170420_1825'),
    ]

    operations = [
        migrations.AddField(
            model_name='investment',
            name='investor',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
