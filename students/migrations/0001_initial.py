# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-09-07 07:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import students.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('blocks', '0001_initial'),
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(default='male', max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='GradeLevel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.CharField(default='grade 11', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lrn', models.CharField(max_length=12, unique=True)),
                ('fname', models.CharField(default='', max_length=60, verbose_name='first name')),
                ('lname', models.CharField(default='', max_length=60, verbose_name='last name')),
                ('mname', models.CharField(blank=True, max_length=60, verbose_name='middle name')),
                ('ename', models.CharField(blank=True, max_length=5, verbose_name='extension name')),
                ('birth_date', models.DateField(help_text='Date format yyyy-mm-dd, e.g 2000-01-20.')),
                ('mother_tongue', models.CharField(default='bisaya', max_length=60)),
                ('IP', models.CharField(default='higaonon', help_text='Ethnic group', max_length=60)),
                ('religion', models.CharField(default='roman catholic', max_length=60)),
                ('address', models.TextField(default='--student address--', help_text='Format: house#/Street/Sitio/Purok, Barangay, Municipality/City, Province')),
                ('image', models.ImageField(blank=True, upload_to=students.models.image_upload_location)),
                ('father_name', models.CharField(default="--father's name of student--", help_text='Format: (Last Name, First Name, Middle Name)', max_length=120, verbose_name="father's name")),
                ('mother_name', models.CharField(default="--mother's name of student--", help_text='Format: (Last Name, First Name, Middle Name)', max_length=120, verbose_name="mother's name")),
                ('guardian_name', models.CharField(blank=True, help_text='Full name of guardian', max_length=160, verbose_name="guardian's name")),
                ('relationship', models.CharField(blank=True, max_length=120)),
                ('contact', models.CharField(blank=True, help_text=' contact number of parents or guardian', max_length=13)),
                ('remarks', models.CharField(blank=True, default='', max_length=60)),
                ('date_registered', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('block', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='blocks.Block')),
                ('course', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='courses.Course')),
                ('gender', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='students.Gender')),
                ('grade_level', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='students.GradeLevel')),
            ],
        ),
        migrations.CreateModel(
            name='StudentStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(default='regular', max_length=120)),
            ],
        ),
    ]