# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-09-15 11:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curriculums', '0001_initial'),
        ('subjects', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subject',
            name='curriculum',
        ),
        migrations.AddField(
            model_name='subject',
            name='curriculum',
            field=models.ManyToManyField(to='curriculums.Curriculum'),
        ),
    ]
