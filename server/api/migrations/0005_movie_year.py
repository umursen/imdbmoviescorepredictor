# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-04-11 22:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20170411_2221'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='year',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Year'),
        ),
    ]