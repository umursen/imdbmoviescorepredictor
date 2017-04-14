# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-04-11 22:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20170330_0204'),
    ]

    operations = [
        migrations.CreateModel(
            name='Year',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField(default=0, unique=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='movie',
            name='year',
        ),
    ]