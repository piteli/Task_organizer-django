# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-07-23 15:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=200)),
                ('dateCreated', models.DateField()),
                ('dateUpdated', models.DateField()),
            ],
        ),
    ]