# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-04-20 17:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0011_auto_20170420_1757'),
    ]

    operations = [
        migrations.CreateModel(
            name='Financials',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('letting_management', models.DecimalField(decimal_places=2, max_digits=10)),
                ('insurance', models.DecimalField(decimal_places=2, max_digits=10)),
                ('maintenance', models.DecimalField(decimal_places=2, max_digits=10)),
                ('corporation_tax', models.DecimalField(decimal_places=2, max_digits=10)),
                ('void_allowance', models.DecimalField(decimal_places=2, max_digits=10)),
                ('listing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='listings.Listing')),
            ],
        ),
        migrations.AlterField(
            model_name='valuation',
            name='capital_growth',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=5),
        ),
    ]
