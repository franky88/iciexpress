# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-09-12 03:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
        ('classchedules', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='classschedule',
            name='block',
        ),
        migrations.AddField(
            model_name='classschedule',
            name='course',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='courses.Course'),
        ),
    ]