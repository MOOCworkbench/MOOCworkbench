# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-19 18:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('experiments_manager', '0005_experiment_unique_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='experiment',
            name='public',
            field=models.BooleanField(default=False),
        ),
    ]
