# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-21 13:35
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_manager', '0002_auto_20170521_1334'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sshkeys',
            name='workbench_user',
        ),
        migrations.DeleteModel(
            name='SSHKeys',
        ),
    ]
