# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-09-07 08:30
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='grade_level',
        ),
        migrations.DeleteModel(
            name='GradeLevel',
        ),
    ]
