# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-01 09:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0004_auto_20170427_1415'),
    ]

    operations = [
        migrations.AddField(
            model_name='internalpackage',
            name='published',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterUniqueTogether(
            name='packageversion',
            unique_together=set([('package', 'version_nr')]),
        ),
    ]