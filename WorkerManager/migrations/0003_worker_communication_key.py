# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-06 07:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WorkerManager', '0002_auto_20160905_0752'),
    ]

    operations = [
        migrations.AddField(
            model_name='worker',
            name='communication_key',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
    ]