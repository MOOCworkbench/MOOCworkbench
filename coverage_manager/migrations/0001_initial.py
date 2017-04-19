# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-19 08:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('build_manager', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CodeCoverage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('badge_url', models.URLField(null=True)),
                ('enabled', models.BooleanField(default=True)),
                ('travis_instance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='build_manager.TravisInstance')),
            ],
        ),
    ]
