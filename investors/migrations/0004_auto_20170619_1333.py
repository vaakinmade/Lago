# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-06-19 12:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('investors', '0003_auto_20170602_2205'),
    ]

    operations = [
        migrations.CreateModel(
            name='BankTransfer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('reference_code', models.CharField(max_length=50)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('status', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='wallet',
            name='transaction',
            field=models.CharField(choices=[('CR', 'Credit'), ('DR', 'Debit')], default='', max_length=2),
        ),
    ]