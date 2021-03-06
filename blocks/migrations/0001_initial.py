# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-09-12 08:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('instructor', '0001_initial'),
        ('classchedules', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Block',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('block_name', models.CharField(max_length=60, unique=True)),
                ('timestamp', models.DateField(auto_now_add=True)),
                ('updated', models.DateField(auto_now=True)),
                ('class_schedule', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='classchedules.ClassSchedule')),
            ],
        ),
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.CharField(default='', max_length=2)),
            ],
        ),
        migrations.AddField(
            model_name='block',
            name='grade_level',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blocks.Level'),
        ),
        migrations.AddField(
            model_name='block',
            name='instructor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='instructor.Instructor'),
        ),
    ]
