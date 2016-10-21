# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-10-16 17:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0003_auto_20161016_1519'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='parent',
        ),
        migrations.AddField(
            model_name='top',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='list.Category'),
        ),
    ]