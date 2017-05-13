# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-05-04 16:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_movie_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='actor',
            name='_id',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='director',
            name='_id',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='writer',
            name='_id',
            field=models.IntegerField(default=0),
        ),
    ]
