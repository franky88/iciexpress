# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-09-28 08:36
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('subjects', '0002_auto_20170915_1923'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subject',
            name='curriculum',
        ),
    ]
