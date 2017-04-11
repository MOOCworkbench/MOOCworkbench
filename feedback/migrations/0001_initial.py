# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-11 08:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user_manager', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('like', models.BooleanField(verbose_name='Overall, was your experience positive?')),
                ('feedback_like', models.TextField(null=True, verbose_name='What did you like about your experience?')),
                ('feedback_dislike', models.TextField(null=True, verbose_name="What didn't you like about your experience?")),
                ('other_comments', models.TextField(null=True, verbose_name='Do you have any other comments?')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('start_point', models.TextField()),
                ('end_point', models.TextField(null=True)),
                ('for_model', models.CharField(max_length=255, null=True)),
                ('active', models.BooleanField(default=True)),
                ('dependent_on', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='feedback.Task')),
            ],
        ),
        migrations.CreateModel(
            name='UserTask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('active', models.BooleanField(default=False)),
                ('completed', models.BooleanField(default=False)),
                ('left_feedback', models.BooleanField(default=False)),
                ('for_task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='feedback.Task')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_manager.WorkbenchUser')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='feedback',
            name='for_task',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='feedback.Task'),
        ),
    ]
