# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-21 09:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('build_manager', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='travisinstance',
            name='enabled',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='travisinstance',
            name='last_build_status',
            field=models.CharField(choices=[('S', 'Success'), ('C', 'Cancelled'), ('F', 'Failed')], max_length=1, null=True),
        ),
    ]
