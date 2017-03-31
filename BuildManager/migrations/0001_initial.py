# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-31 13:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ExperimentsManager', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TravisCiConfig',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('python_version', models.CharField(default='3.6', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='TravisInstance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_build_status', models.CharField(choices=[('F', 'Failed'), ('S', 'Success'), ('C', 'Cancelled')], max_length=1, null=True)),
                ('enabled', models.BooleanField(default=True)),
                ('config', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BuildManager.TravisCiConfig')),
                ('experiment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ExperimentsManager.Experiment')),
            ],
        ),
    ]
