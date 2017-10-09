# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-09-28 08:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subjects', '0003_remove_subject_curriculum'),
        ('curriculums', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='curriculum',
            name='subjects',
            field=models.ManyToManyField(to='subjects.Subject'),
        ),
    ]
