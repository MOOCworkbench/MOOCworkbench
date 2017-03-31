# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-28 14:29
from __future__ import unicode_literals

from django.db import migrations
import django.db.models.manager
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('ExperimentsManager', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='chosenexperimentsteps',
            managers=[
                ('active_step', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AddField(
            model_name='experiment',
            name='modified',
            field=model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified'),
        ),
        migrations.AddField(
            model_name='script',
            name='modified',
            field=model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified'),
        ),
        migrations.AlterField(
            model_name='experiment',
            name='created',
            field=model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created'),
        ),
        migrations.AlterField(
            model_name='script',
            name='created',
            field=model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created'),
        ),
    ]