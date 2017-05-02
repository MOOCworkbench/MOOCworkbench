# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-02 14:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DataSchemaField',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name of row')),
                ('datatype', models.CharField(choices=[('string', 'String'), ('number', 'Number'), ('date', 'Date'), ('time', 'Time'), ('datetime', 'DateTime'), ('year', 'Year'), ('yearmonth', 'Year Month'), ('boolean', 'Boolean'), ('object', 'Object'), ('geopoint', 'GeoPoint'), ('array', 'Array'), ('duration', 'Duration'), ('any', 'Any')], max_length=100)),
                ('primary_key', models.BooleanField(default=False, verbose_name='Field is a primary key')),
                ('required', models.BooleanField(default=False, verbose_name='Field is required')),
                ('title', models.CharField(blank=True, max_length=100, verbose_name='Title of field')),
                ('description', models.TextField(blank=True, verbose_name='Description of the contents of the field')),
                ('unique', models.BooleanField(default=False, verbose_name='Values in this row have to be unique')),
                ('format', models.CharField(blank=True, max_length=100, verbose_name='Define a format (only for Date/Time/DateTime)')),
                ('minimum', models.CharField(blank=True, max_length=100, verbose_name='(optional) Define a minimum value (only for Number/Date/Time/DateTime) ')),
                ('maximum', models.CharField(blank=True, max_length=100, verbose_name='(optional) Define a maximum value')),
            ],
        ),
    ]