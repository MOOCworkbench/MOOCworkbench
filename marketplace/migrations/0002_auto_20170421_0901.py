# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-21 09:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='internalpackage',
            old_name='repo',
            new_name='git_repo',
        ),
    ]
